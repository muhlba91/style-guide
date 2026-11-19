---
name: style-audit
description: Audit the style guide itself for structure, duplication, contradictions, stale evidence, privacy leaks and coverage, and test it on held-out work. Use after large changes, on a schedule, or when the guide's quality is in doubt.
---

# Audit the Style Guide

Guide root: the nearest parent of this folder (resolve it with `realpath`) that holds `AGENTS.md`. If there is none, stop and say that the skill must be linked from a checkout of the style guide (`make install`). Paths below are relative to it.

## Modes

- **Quick**: structure and privacy on touched files. Run `make check` and read the touched rules.
- **Full**: everything below, by a subagent with a stronger model than the author.

## Checks

1. **Structure**: run `make check`. It covers rule format, unique and retired IDs, required fields, OQ references, `must` with `open`, tool names, family against file, index ranges, Good lines on `must`, digests, skill links, em dashes, emoji, emails, home paths, gendered pronouns and token budgets.
2. **Duplication**: the same rule in two files, or a language rule that belongs in the principles.
3. **Contradiction**: rules that disagree with each other, with `AGENTS.md` or with the stated preferences.
4. **Checkability**: a rule an agent cannot apply without seeing the original repos: vague wording, no Good or Bad example. Also a rule that names a third party's annotation key or field that the owner does not require and a review would not miss, or any API version: a maintenance cost, reword it.
5. **Evidence**: `must` without an owner statement or two independent repos. Sources that rest on AI-era material, excluded repos or email alone. Linter configs that do not exist in the owner's repos.
6. **Open items**: `open` rules without a current OQ entry, OQ entries already answered.
7. **Self-style**: the guide follows its own rules.
8. **Privacy**: no personal data, private content, email details, secrets or verbatim quotes beyond a short subject line.
9. **Coverage**: artifact types and languages in the owner's repos without rules, rules without current evidence.
10. **Skills**: paths and steps in the four skills match the files. The precedence in `AGENTS.md` and the severity table of `style-review` agree with the rule format and strength definitions in `AGENTS.md`.
11. **Digests**: a rule whose scope, exception or precedence sits only in Why or Source loses it in the digest. Review a sample once from the digests and once from the full rules, and compare.

## Held-Out Test

1. Pick 5 to 10 recent artifacts that are not evidence for any rule: commits by the owner, new files, README edits.
2. Run `style-review` on them with a subagent that did not write the rules.
3. Compare the findings with what the owner did. A hit on the owner's own text is a false positive. Count them per rule.
4. Reverse test: take AI-written text from the owner's repos that the "Avoid" lists name, and check that the review catches it.
5. Report per rule: false positives, misses, rules never triggered.

## Output

Write the report to `work/audits/<YYYY-MM-DD>[-b].md` (gitignored; add a suffix when one exists for the day): findings by check, severity (blocker, fix, nit), a proposed change per finding. Hand every proposed change to `style-update`. Edit no rule during an audit. Never commit or push.
