# Concision

## PRIN-01 · must · common · stated

- Rule: Write the shortest text that is still complete.
- Why: the owner's first requirement for every artifact.
- Good: `Deploy the stack with pulumi up.`
- Bad: `In order to deploy the stack, you will now want to run the following command.`
- Source: stated 2026-11-18, concision. Evidence: matches the terse subjects (median 4 words), one-line PR bodies and README intros across all repos, 2021-2026.
- Check: judgment

## PRIN-02 · must · common · stated

- Rule: Leave out filler and do not write around a point; say it directly.
- Why: stated; the email sample opens with the point in about 80 of 95 texts.
- Good: `The cache is cleared on restart.`
- Bad: `It is worth noting that the cache will generally be cleared whenever a restart occurs.`
- Source: stated 2026-11-18, filler. Evidence: also visible in human READMEs (2023) and replies.
- Check: judgment

## PRIN-03 · prefer · common · observed

- Rule: Put the point or purpose in the first sentence.
- Good: `This repository contains the IaC for X using Pulumi.`
- Bad: a feature wall or marketing paragraph before the purpose.
- Source: 11 of 14 READMEs open with a one-sentence purpose; commit subjects; replies start with the finding.
- Check: judgment

## PRIN-04 · must · common · stated

- Rule: Be precise: give exact values, units, versions, identifiers and paths instead of vague words.
- Good: `timeout: 90 s, three missed pulses`.
- Bad: `a short timeout`.
- Source: stated 2026-11-18, precision. Evidence: CV edit replaced vague bullets with scope and numbers (human, 2026); config docs carry units ("in s", "in %").
- Check: judgment

## PRIN-05 · must · common · stated

- Rule: Do not include text that adds no information: restating a heading, the code, the diff or the previous sentence; API docs of exported or public functions are excepted (GO-18, PY-13).
- Good: a command block without a paragraph that repeats the command in words.
- Bad: `This section describes the installation.` under `## Installation`.
- Source: stated 2026-11-18, text that adds no information. Evidence: PR bodies of 11 of 20 PRs are empty, human commits have no body in 98.6% of cases.
- Check: judgment

## PRIN-06 · prefer · common · observed

- Rule: Delete stale text in the same change that makes it stale (caveats, tool and version lists that duplicate `mise.toml`, commented-out code), except the tool names in the README Development opener (README-05).
- Good: remove the "limitation" row when the feature ships.
- Bad: keep `currently not supported` after the release.
- Source: onyx-homeassistant-integration 2023 removed a warning and rewrote the section; shared-library 2026 dropped the requirements list in favor of mise; human.
- Check: judgment

## PRIN-07 · prefer · common · observed

- Rule: Add a document section only when a reader needs it; do not let a README or doc grow per change.
- Why: 2026 AI-assisted READMEs grew without trimming; the owner removed duplicated lists when the owner edited by hand.
- Good: update the existing table row.
- Bad: add a new section that explains the change history.
- Source: shared-library README rewrite and mise sweep (2026); onyx and vault README growth in AI-era commits is accepted but not the owner's habit. Weight 0.5.
- Check: judgment
