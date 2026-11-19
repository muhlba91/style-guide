---
name: style-review
description: Review a diff, file, commit message, PR text or document against the owner's personal style and report findings with rule IDs. Use when asked to check, audit or review work for the owner's style.
---

# Review Against the Owner's Style

Guide root: the nearest parent of this folder (resolve it with `realpath`) that holds `AGENTS.md`. If there is none, stop and say that the skill must be linked from a checkout of the style guide (`make install`). Paths below are relative to it.

## Steps

1. Determine the scope: a diff, files, commit messages, PR text. Read the target repository's own rules first (`AGENTS.md`, `CLAUDE.md`, linter configs at its root). Follow the precedence in `AGENTS.md`. Judge an excerpt only for what it contains.
2. Read `common/digest/core.md`, then the digests that `common/digest/README.md` lists for the artifacts.
3. Run the repository's linters in check mode only: no fixers, no file changes. Skip a linter the repository does not configure. Do not report what a tool already reports.
4. Check the artifacts against the rules. Cite the rule ID for every finding. Judge only what the scope contains. Before reporting a finding you are unsure about, read the full rule: its Why and Source may explain an exception.
5. Check for the AI-era artifacts under "Avoid" in the digests.
6. For more than 5 files or 300 changed lines, split by artifact type, one subagent per type. Give each the guide root, `common/digest/core.md`, its digests and the Severity and Output sections below. Merge the findings and drop duplicates.

## Severity

| Rule strength | Finding |
| --- | --- |
| `must` | violation |
| `prefer` | suggestion |
| `lean` | note, only in a thorough review, counted separately |
| status `open` | note with the OQ id, never a violation |
| `must` with `open` | forbidden combination: report it as a guide defect, treat the hit as a note |
| digest unclear | read the full rule; if the digest is wrong, report "digest defect" with the rule ID, apart from the findings |

## Output

Write the report in the reply, and write a file only when asked. Start with one line: scope and counts per severity. Then a table:

| Rule | Severity | Location | Finding | Fix |
| --- | --- | --- | --- | --- |

- One row per finding, with `path:line` as location and a concrete fix.
- Group repeated findings of one rule into one row with all locations.
- After the table: inconsistencies with the surrounding code that no rule covers, one line each.
- Report nothing when nothing is wrong. Do not praise.

## Boundaries

- Read-only. Fix only when asked, then follow `style-write`.
- No finding without a rule ID or a clear inconsistency with the surrounding code.
- If the owner rejects a finding, pass it to `style-update` as evidence.
