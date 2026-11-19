---
name: style-update
description: Change the style guide from feedback or new evidence. Use when the owner corrects a rule, rejects or confirms a review finding, answers an open question, or when new repos or text should refine the rules.
---

# Update the Style Guide

Guide root: the nearest parent of this folder (resolve it with `realpath`) that holds `AGENTS.md`. If there is none, stop and say that the skill must be linked from a checkout of the style guide (`make install`). Paths below are relative to it.

The owner decides. Draft every change, show it, apply it only after approval.

## Inputs

| Input | Typical result |
| --- | --- |
| Correction by the owner | rule changed or added, status `stated` |
| Review finding accepted or rejected | strength raised or lowered, rule narrowed, evidence added |
| Answer to an `OPEN-QUESTIONS.md` entry | rule set to the answer, status `stated`, entry removed |
| New repo, commit range or text | new evidence, possibly a new `lean` rule |

## Steps

1. Classify the input and find the affected rule: search IDs and wording in `common/`. Avoid new rules that duplicate existing ones.
2. Place the change: a rule that holds in several languages belongs in `common/principles/`, a language file holds only deltas.
3. Draft the change as a diff in the rule format (`AGENTS.md`). Set the status: `stated` for the owner's own words, `observed` for evidence, `open` with a new OQ entry when the owner must decide.
4. A new rule takes the next free number of its family: the highest number in the rule files and in `common/retired.txt`, plus one. List every deleted or merged ID in `common/retired.txt` (`ID replaced-by`); the checker fails if a retired ID reappears.
5. Set the strength:
   - An owner statement sets any strength with status `stated`, including a correction that loosens a rule. Source: `stated YYYY-MM-DD, <topic>`.
   - Use `prefer` with `open`, never `must` with `open`.
   - Raise `lean` to `prefer`, or `prefer` to `must`, only with two independent sources or an owner statement.
   - Lower a strength when counter-evidence or rejected findings accumulate. State why in Source.
6. Show the diff and the reason in a few lines. Wait for approval.
7. Apply the change in three parts:
   - Update `OPEN-QUESTIONS.md`, the index of the touched folder, `common/retired.txt` and `CHANGELOG.md` (one dated line per change with the rule ID).
   - Put every scope and exception in the Rule sentence: digests drop Why and Source.
   - Run `make digest`.
8. Run `style-audit` in quick mode on the touched files. It runs `make check`. For a large change (`AGENTS.md`, Working Rules) run full mode with a stronger model.

## Boundaries

- Record no private content, email details or secrets. Paraphrase.
- Name a third party's annotation key or field in a rule only when the owner requires it and a review would miss it; name no API versions.
- Never raise a rule on AI-era evidence alone. Tiers and weights: `AGENTS.md`, Working Rules.
- Never commit or push unless asked.
