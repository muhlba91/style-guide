#!/usr/bin/env python3
"""Structure and content checks of the rule files, the skills and the privacy of the repository (`make rules`)."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULE_DIRS = ("common/principles", "common/languages", "common/writing")
FAMILIES = {
    "PRIN", "GO", "PY", "SH", "K8S", "CI", "RENOV", "MISE", "NIX", "TYPST",
    "DOC", "README", "RB", "COMMIT", "PR", "MAIL", "PULUMI", "YAML", "CONF", "MAKE",
}  # fmt: skip
HEADER = re.compile(r"^## ([A-Z][A-Z0-9]*)-(\d{2}) · (must|prefer|lean) · ([a-z-]+) · (stated|observed|open)\s*$")
RULE_LIKE = re.compile(r"^#{2,3} [A-Z][A-Z0-9]*-\d")
FIELD = re.compile(r"^- (Rule|Why|Good|Bad|Source|Check):\s*(.*)$")
FIELD_ORDER = ("Rule", "Why", "Good", "Bad", "Source", "Check")
CHECK_VALUE = re.compile(r"^(judgment|tool:[\w.-]+)(\s|,|$)")
OQ_REF = re.compile(r"OQ-\d+")
EM_DASH = "—"
EMOJI = re.compile("[\U0001f300-\U0001faff☀-➿⭐✅❌]")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PRONOUN = re.compile(r"\b(he|she|his|him|himself|herself)\b", re.I)
HOME_PATH = re.compile(r"/Users/[A-Za-z0-9._-]+/")
REQUIRED = ("Rule", "Source", "Check")
TOOL_NAME = re.compile(r"tool:([\w.-]+)")
STATED_SOURCE = re.compile(r"^stated \d{4}-\d{2}-\d{2}")
RULE_ID = re.compile(r"[A-Z][A-Z0-9]*-\d{2}")
INDEX_ROW = re.compile(r"^\| \[([\w.-]+\.md)\]\([^)]*\) \| ([^|]+) \|")
INDEX_RANGE = re.compile(r"([A-Z][A-Z0-9]*)-(\d{2})(?: to (?:[A-Z][A-Z0-9]*-)?(\d{2}))?")

# Tools that a `Check: tool:<name>` may name. Derived 2026-11 by listing which tools are
# configured in the owner's repos (pre-commit, mise, Makefile, pyproject, .golangci, renovate configs):
# conform (37 repos), golangci-lint (8), shellcheck (10 or more), yamllint (5),
# markdownlint (5, 3 of them evidence-eligible), hadolint (2), kubeconform (2), renovate (17, includes config validation),
# ruff (5), typstyle (2), gitleaks (16), pre-commit, mise, pytest-cov (5), mutmut (2), nixfmt (2).
ALLOWED_TOOLS = {
    "conform", "golangci-lint", "shellcheck", "yamllint", "markdownlint", "hadolint", "kubeconform",
    "renovate", "ruff", "typstyle", "gitleaks", "pre-commit", "mise", "pytest-cov", "mutmut", "nixfmt",
}  # fmt: skip

# Families allowed per rule file (file name only).
FILE_FAMILIES = {
    "principles": {"PRIN"},
    "go.md": {"GO"}, "pulumi.md": {"PULUMI"}, "python.md": {"PY"}, "shell.md": {"SH"},
    "yaml-kubernetes.md": {"K8S"}, "yaml.md": {"YAML"}, "makefile.md": {"MAKE"}, "config-other.md": {"CONF"}, "github-actions.md": {"CI"}, "renovate.md": {"RENOV"},
    "mise.md": {"MISE"}, "nix.md": {"NIX"}, "typst.md": {"TYPST"},
    "prose.md": {"DOC"}, "repo-readme.md": {"README"}, "runbook.md": {"RB"},
    "commit.md": {"COMMIT"}, "pr-issue.md": {"PR"}, "email.md": {"MAIL"},
}  # fmt: skip


TOKEN_CHARS = 3.6  # rough characters per token for English Markdown
FILE_BUDGETS = {  # tokens; quality wins over token savings, so raise a budget when a skill needs the text
    "common/skills/style-write/SKILL.md": 500,
    "common/skills/style-review/SKILL.md": 800,
    "common/skills/style-update/SKILL.md": 900,
    "common/skills/style-audit/SKILL.md": 1000,
    "AGENTS.md": 1200,
}


def check_budgets(root=None):
    """Return an error for every skill or entry file above its token budget."""
    root = root or ROOT
    errors = []
    for name, budget in FILE_BUDGETS.items():
        path = root / name
        if path.is_file():
            size = round(len(path.read_text(encoding="utf-8")) / TOKEN_CHARS)
            if size > budget:
                errors.append(f"{name}: about {size} tokens, budget {budget}")
    return errors


def load_retired(text):
    """Return the retired rule IDs of common/retired.txt (first column of every non-comment line)."""
    return {line.split()[0] for line in text.splitlines() if line.strip() and not line.startswith("#")}


def check_retired(seen, retired):
    """Return an error for every retired ID that a rule file uses again."""
    return [f"{seen[rule_id]}: {rule_id} is retired and must not be reused" for rule_id in sorted(retired & set(seen))]


def parse_rules(text):
    """Return a list of (header match, fields dict, block text) for every rule header in the text."""
    rules, current = [], None
    for line in text.splitlines():
        if re.match(r"^#{1,6} ", line):
            if current:
                rules.append(current)
            match = HEADER.match(line)
            current = (match, {}, []) if match else None
            if not match and RULE_LIKE.match(line):
                rules.append((None, {"header": line}, []))
            continue
        if current:
            field = FIELD.match(line)
            if field:
                current[1][field.group(1)] = field.group(2).strip()
            current[2].append(line)
    if current:
        rules.append(current)
    return rules


def allowed_families(name):
    """Return the families a rule file may hold, or None when the file is not in FILE_FAMILIES."""
    path = Path(str(name))
    if path.parent.name == "principles":
        return FILE_FAMILIES["principles"]
    return FILE_FAMILIES.get(path.name)


def check_rule_text(name, text, oq_ids, seen, warnings=None, cites=None):
    """Return errors for the rules in text. Append non-fatal findings to warnings, OQ citations to cites."""
    errors = []
    warnings = warnings if warnings is not None else []
    cites = cites if cites is not None else {}
    for match, fields, block in parse_rules(text):
        if match is None:
            errors.append(f"{name}: malformed rule header: {fields.get('header', '')}")
            continue
        rule_id = f"{match.group(1)}-{match.group(2)}"
        where = f"{name}: {rule_id}"
        if match.group(1) not in FAMILIES:
            errors.append(f"{where}: unknown family")
        families = allowed_families(name)
        if families is not None and match.group(1) in FAMILIES and match.group(1) not in families:
            errors.append(f"{where}: family {match.group(1)} does not belong in this file")
        if rule_id in seen:
            errors.append(f"{where}: duplicate id (also in {seen[rule_id]})")
        seen[rule_id] = name
        labels = [m.group(1) for m in map(FIELD.match, block) if m]
        order = [FIELD_ORDER.index(label) for label in labels]
        if order != sorted(order):
            errors.append(f"{where}: fields out of order (expected {', '.join(FIELD_ORDER)})")
        for field in REQUIRED:
            if not fields.get(field):
                errors.append(f"{where}: missing field {field}")
        if fields.get("Check") and not CHECK_VALUE.match(fields["Check"]):
            errors.append(f"{where}: Check must start with 'judgment' or 'tool:<name>'")
        errors += [
            f"{where}: tool:{tool} is not configured in the owner's repos (ALLOWED_TOOLS)"
            for tool in TOOL_NAME.findall(fields.get("Check", ""))
            if tool not in ALLOWED_TOOLS
        ]
        if match.group(3) == "must" and match.group(5) == "open":
            errors.append(f"{where}: must and open together are forbidden; use prefer with open")
        if match.group(5) == "stated" and not STATED_SOURCE.match(fields.get("Source", "")):
            # warning only: many existing stated rules lack the date, which is not recoverable from the evidence
            warnings.append(f"{where}: stated Source should start with 'stated YYYY-MM-DD'")
        if match.group(3) == "must" and not fields.get("Good"):
            warnings.append(f"{where}: must without a Good line")
        cites[rule_id] = set(OQ_REF.findall("\n".join(block)))
        if match.group(5) == "open":
            refs = OQ_REF.findall("\n".join(block))
            if not refs:
                errors.append(f"{where}: status open without an OQ reference")
            errors += [f"{where}: {ref} not defined in OPEN-QUESTIONS.md" for ref in refs if ref not in oq_ids]
        if match.group(3) == "must" and match.group(5) == "observed" and len(fields.get("Source", "")) < 20:
            errors.append(f"{where}: must/observed needs a concrete Source")
    return errors


def check_privacy(name, text):
    errors = []
    if EM_DASH in text:
        errors.append(f"{name}: contains an em dash")
    if EMOJI.search(text):
        errors.append(f"{name}: contains an emoji")
    if EMAIL.search(text):
        errors.append(f"{name}: contains an email address")
    if PRONOUN.search(text):
        errors.append(f"{name}: uses a gendered pronoun, write \"the owner\"")
    if HOME_PATH.search(text):
        errors.append(f"{name}: contains an absolute home path")
    return errors


def check_skill(skill_dir):
    errors = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir.name}: SKILL.md missing"]
    head = skill_file.read_text(encoding="utf-8").split("---")
    front = head[1] if len(head) > 2 and head[0].strip() == "" else ""
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    if not name or name.group(1).strip() != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name must equal the folder name")
    if not re.search(r"^description:\s*\S", front, re.M):
        errors.append(f"{skill_dir.name}: frontmatter description missing")
    link = ROOT / ".agents" / "skills" / skill_dir.name
    if not link.is_symlink() or not link.resolve() == skill_dir.resolve():
        errors.append(f"{skill_dir.name}: .agents/skills link missing or wrong (run make skills)")
    return errors


def expand_ids(cell):
    """Expand an index cell such as 'PRIN-39 to 45, PRIN-50' into a set of IDs."""
    ids = set()
    for family, start, end in INDEX_RANGE.findall(cell):
        for number in range(int(start), int(end or start) + 1):
            ids.add(f"{family}-{number:02d}")
    return ids


def index_errors(label, readme_text, ids_by_file):
    """Compare the IDs in each index row with the IDs the file holds."""
    errors = []
    for line in readme_text.splitlines():
        row = INDEX_ROW.match(line)
        if not row or row.group(1) not in ids_by_file:
            continue
        listed, actual = expand_ids(row.group(2)), ids_by_file[row.group(1)]
        if listed != actual:
            missing = ", ".join(sorted(actual - listed)) or "none"
            extra = ", ".join(sorted(listed - actual)) or "none"
            errors.append(
                f"{label}: index for {row.group(1)} differs from the file (not listed: {missing}; not in file: {extra})"
            )
    return errors


def oq_warnings(oq_text, cites):
    """Compare each OQ entry's Affects line with the rules that cite it (both directions)."""
    warnings, listed = [], {}
    current = None
    for line in oq_text.splitlines():
        heading = re.match(r"^### (OQ-\d+)", line)
        if heading:
            current = heading.group(1)
            listed.setdefault(current, set())
        elif current and line.startswith("- Affects:"):
            listed[current] |= set(RULE_ID.findall(line))
    citing = {}
    for rule_id, refs in cites.items():
        for ref in refs:
            citing.setdefault(ref, set()).add(rule_id)
    for oq, rules in sorted(listed.items()):
        for rule_id in sorted(rules - citing.get(oq, set())):
            warnings.append(f"{oq}: Affects lists {rule_id}, which does not cite it")
        for rule_id in sorted(citing.get(oq, set()) - rules):
            warnings.append(f"{oq}: {rule_id} cites it but is not in Affects")
    return warnings


def check_index(directory):
    readme = ROOT / directory / "README.md"
    if not readme.is_file():
        return [f"{directory}/README.md missing"]
    text = readme.read_text(encoding="utf-8")
    errors = [
        f"{directory}/README.md does not list {path.name}"
        for path in sorted((ROOT / directory).glob("*.md"))
        if path.name != "README.md" and path.name not in text
    ]
    ids_by_file = {}
    for path in sorted((ROOT / directory).glob("*.md")):
        if path.name != "README.md":
            found = {f"{m.group(1)}-{m.group(2)}" for m, _, _ in parse_rules(path.read_text(encoding="utf-8")) if m}
            ids_by_file[path.name] = found
    return errors + index_errors(f"{directory}/README.md", text, ids_by_file)


def markdown_files():
    skip = {ROOT / "LICENSE.md"}
    for path in sorted(ROOT.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if path in skip or relative.parts[0] in {"work", ".git", "node_modules"}:
            continue
        yield path


def main():
    errors = []
    oq_file = ROOT / "OPEN-QUESTIONS.md"
    oq_ids = set(OQ_REF.findall(oq_file.read_text(encoding="utf-8"))) if oq_file.is_file() else set()
    seen, warnings, cites = {}, [], {}
    for directory in RULE_DIRS:
        for path in sorted((ROOT / directory).glob("*.md")):
            if path.name != "README.md":
                errors += check_rule_text(
                    path.relative_to(ROOT),
                    path.read_text(encoding="utf-8"),
                    oq_ids,
                    seen,
                    warnings,
                    cites,
                )
        errors += check_index(directory)
    retired_file = ROOT / "common" / "retired.txt"
    if retired_file.is_file():
        errors += check_retired(seen, load_retired(retired_file.read_text(encoding="utf-8")))
    errors += check_budgets()
    for path in markdown_files():
        errors += check_privacy(path.relative_to(ROOT), path.read_text(encoding="utf-8"))
    for skill_dir in sorted((ROOT / "common" / "skills").glob("*/")):
        errors += check_skill(skill_dir)
    if oq_file.is_file():
        warnings += oq_warnings(oq_file.read_text(encoding="utf-8"), cites)
    for error in errors:
        print(f"ERROR {error}")
    for warning in warnings:
        print(f"WARNING {warning}")
    no_good = sum(1 for w in warnings if w.endswith("must without a Good line"))
    print(
        f"{len(seen)} rules checked, {len(errors)} errors, {len(warnings)} warnings ({no_good} must rules without Good)"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
