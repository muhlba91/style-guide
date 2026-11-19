# Runbook and How-To

Evidence: IaC READMEs (human, 2023 origin), adguard and onyx-client how-to sections (human), BOOTSTRAP.md and restore.md (AI-assisted, accepted unchanged). Concision applies (PRIN-01).

## RB-01 · must · common · stated

- Rule: Make every command copy-pasteable: runnable as written, with nothing to edit except marked placeholders.
- Good: `pulumi up` in its own fenced `bash` block.
- Bad: a command embedded in a sentence or split across prose.
- Source: stated 2026-11-18, runbook commands. Observed, not stated: one fenced `bash` block per operation, as in all 5 IaC READMEs (one lead-in sentence, one block).
- Check: judgment

## RB-02 · must · common · stated

- Rule: Say what each command does and what the outcome is, in the lead-in or a trailing comment, in the same place as the command.
- Good: `seed-secrets.sh --check   # lists missing secrets`
- Bad: a block of commands with no statement of effect.
- Source: stated 2026-11-18, runbook outcomes. Evidence: BOOTSTRAP.md and restore.md steps name the outcome ("until ready, then check the app"); [ai], accepted.
- Check: judgment

## RB-03 · must · common · stated

- Rule: Structure the runbook clearly and leave out fuzz; no background essays.
- Good: prerequisites, steps in execution order, then undo or destroy.
- Source: stated 2026-11-18, runbook structure. Observed, not stated: the order above, as in the README order Requirements, Creating, Destroying.
- Check: judgment

## RB-04 · must · common · observed

- Rule: Title an operation by its outcome, not the tool.
- Good: `## Creating the Infrastructure`
- Bad: `## Pulumi`
- Source: 5 IaC READMEs; after the fnox migration the command changed in place (`f9a0852`).
- Check: judgment

## RB-05 · prefer · common · observed

- Rule: In a multi-step block put a short lowercase comment above each command saying what it does; mark an alternative with `# or`.
- Source: adguard deployment steps (2023-2025, human), onyx-client testing.
- Check: judgment

## RB-06 · prefer · common · observed

- Rule: Put a hard prerequisite directly after the command it blocks, as a bold `**Attention**:` line or an alert.
- Good: `**Attention**: set ALLOW_REPOSITORY_DELETION before destroying.`
- Source: github-infrastructure README.
- Check: judgment

## RB-07 · prefer · common · stated

- Rule: Mark numbered-list items `1.`; use a numbered list only for ordered procedures, one action per item, and `-` bullets otherwise.
- Why: the owner's old lists used `1)`, AI-era files use `1.`, the Markdown standard. A separate `BOOTSTRAP.md` linked from the README exists in 2 repos from one day, so it stays optional.
- Source: stated 2026-11-18, list marker. Observed details: ordered-only use, one action per item. Evidence: onyx-client testing (2021-2023), BOOTSTRAP.md and restore.md (2026, AI).
- Check: judgment
