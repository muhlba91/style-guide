---
name: style-write
description: Write or edit code, configuration, documentation, commit messages, PR and issue text or emails in the owner's personal style. Use whenever output should match the owner's voice and conventions.
---

# Write in the Owner's Style

Guide root: the nearest parent of this folder (resolve it with `realpath`) that holds `AGENTS.md`. If there is none, stop and say that the skill must be linked from a checkout of the style guide (`make install`). Paths below are relative to it.

## Steps

1. List the artifact types in the task: code, configuration, README or docs, agent file, runbook, commit, PR or issue, email.
2. Follow the precedence in `AGENTS.md`.
3. Read `common/digest/core.md`, then the digests that `common/digest/README.md` lists for each artifact.
4. Look at the target repository for what the guide leaves open. Copy no pattern that a rule forbids.
5. Write. Keep text crisp, precise and grounded. Add no comment the code already makes clear.
6. Run the repository's linters and formatters and fix findings.
7. Self-check against the `must` rules of the digests read: no filler, repetition, decoration, em dashes, emoji, exaggeration or attribution lines.

## Boundaries

- Invent no style. If no rule covers a point, follow the surrounding code and say nothing.
- Copy no AI-era artifact that a digest lists under "Avoid".
- Put no personal data, secrets or private content into the output because a rule's example had it.
- Commit and push only when asked.
