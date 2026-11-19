# Prose and Markdown

Deltas for documentation text. Evidence: 20 READMEs, docs commits, onyx-client, adguard, vault, applications; 2021-2026. Concision, tone, dashes and emoji: see PRIN-01 to PRIN-13.

## DOC-01 · prefer · common · observed

- Rule: Describe a thing in one clause; in a list of fragments use no trailing period, in a list of full sentences use periods, and do not mix inside one list.
- Good: `- \`NAME\`: the lowercase description`
- Source: env var lists and config blocks (no period), applications component list (periods).
- Check: judgment

## DOC-02 · must · common · observed

- Rule: Write headings in Title Case without trailing punctuation, one H1, no skipped levels; number only the steps of an ordered how-to.
- Good: `## Continuous Integration and Automations`
- Source: headings of the Tier 1 READMEs from 2023 on use Title Case without trailing punctuation; sentence-case headings occur only in AI-assisted docs from 2026.
- Check: judgment (markdownlint `MD001` and `MD025` cover levels; markdownlint is configured in 5 repos, 3 of them evidence-eligible)

## DOC-03 · must · common · observed

- Rule: Link on first mention as `[Name](url)`, wrap bare URLs in `<...>`, link internal files with a backticked relative path (a link whose label is a backticked path is fine), and use anchors for in-page jumps.
- Good: link `[Renovate](url)` once, wrap `<https://example.org/docs>`, and point to ``docs/setup.md`` in backticks.
- Bad: a bare `https://example.org/docs` mid-sentence, or a second link to the same name.
- Source: Tier 1 READMEs link on first mention; bare URLs are wrapped in angle brackets in the adguard and onyx-homeassistant READMEs since 2023.
- Check: judgment

## DOC-04 · must · common · observed

- Rule: Give every fenced block a language: `bash` for commands, `yaml`, `go`, `python`, `txt` for output, `text` for trees.
- Good: a fence opened with `bash` for `mise install` and `txt` for its output.
- Bad: a fence with no language, or `shell`.
- Source: all READMEs; adguard uses `shell`, treated as drift.
- Check: judgment (markdownlint `MD040` helps where configured, in 5 repos)

## DOC-05 · must · common · observed

- Rule: Use `-` for bullets, two-space nested indent and `- [x]` / `- [ ]` for status inventories.
- Good: `- [x] vault` with a nested `- [ ] backup` indented two spaces.
- Bad: `* vault` with four-space nesting.
- Source: all READMEs; applications component list.
- Check: judgment

## DOC-06 · must · common · stated

- Rule: Write Markdown prose as one paragraph per line, without hard wraps; code comments follow the formatter's line length.
- Why: the owner's hand-written READMEs are unwrapped and the owner rejoined wrapped text (`dcb1737`, 2025), but 2026 AI-origin sections wrap at 80 to 120.
- Good: one paragraph on one line, however long it runs.
- Bad: the same paragraph broken at 80 columns.
- Source: stated 2026-11-18, wrapping. Evidence: 2023 READMEs and most of the onyx-client README are unwrapped, though some 2021-era onyx-client lines wrap at 120; Go doc comments wrap at 120 (golines), onyx docstrings at about 80; Typst uses sentence-per-line via typstyle, its own exception.
- Check: judgment

## DOC-08 · must · common · stated

- Rule: In alerts, end no line with trailing spaces; put each line on its own `>` line.
- Good: `> [!WARNING]` then `> Deleting the volume loses all data.` then `> Back it up first.`
- Bad: a line ending in two trailing spaces for a hard break.
- Source: stated 2026-11-18, no trailing spaces in alerts.
- Check: judgment (markdownlint `MD009` helps where configured)

## DOC-09 · lean · common · observed

- Rule: Bold only the decision-bearing phrase of a sentence, and use it rarely.
- Why: 2021-2024 text used more bold; 2025-26 IaC READMEs use almost none.
- Source: onyx, adguard; `358cbda` (2024).
- Check: judgment

## DOC-10 · prefer · common · stated

- Rule: Put a comma before "and" only where it prevents ambiguity or helps clarity; otherwise omit it.
- Why: the comma appears in the CI section of 10 READMEs since 2023, but the owner does not treat it as a rule.
- Good: `linting and verifying the code`; `tests, docs, and release notes` when clarity gains.
- Source: stated 2026-11-18, serial comma.
- Check: judgment

## DOC-11 · prefer · common · stated

- Rule: Use American spelling.
- Why: conform spellcheck uses locale US in 37 repos, even though "behaviour" and "colour" appear in adguard and toolkit text.
- Source: stated 2026-11-18, spelling. Evidence: `.conform.yaml` in 37 repos; mixed README text.
- Check: judgment (conform spellcheck covers commit messages only)

## DOC-13 · prefer · common · observed

- Rule: Give a surprising behavior's cause in the same sentence after a colon or semicolon, not in a separate paragraph.
- Source: vault README (BGP, NetBird), onyx README v6; weight 0.75 to 1.0.
- Check: judgment

## DOC-14 · prefer · common · observed

- Rule: Document a breaking release with a version-mapping row, a "Migration from A to B" section and a `BREAKING CHANGE:` commit footer.
- Good: mark "deprecated, removed in X" in the row; one bullet per change in the section (old name -> new name).
- Source: onyx-client `36900b6` (2026-11), adguard "Migrations" with one H3 per hop (2024-03, human).
- Check: judgment

## DOC-15 · prefer · common · stated

- Rule: Write agent instructions as short imperative fragments with numeric limits; put one rule per bullet and add a rationale only when the exception matters.
- Why: opsbot `SOUL.md` and `AGENT.md` use numeric limits; the toolkit `CLAUDE.md` (AI-built, inferred) uses prose with rule IDs.
- Good: `Output: results only; no restatement.`
- Source: stated 2026-11-18, agent file style. Observed details: one rule per bullet, rationale only for exceptions. Evidence: opsbot files (4 commits, no trailer), toolkit CLAUDE.md (Tier 1.5).
- Check: judgment

## DOC-16 · lean · common · observed

- Rule: State agent boundaries as a closed list: what the agent may do, what needs a one-off approval, what stays with the owner.
- Source: four private working notes and plans, Tier 1.5 (inferred, AI-assisted); consistent across all four.
- Check: judgment

## DOC-17 · prefer · common · observed

- Rule: Use GitHub alert blockquotes (`[!IMPORTANT]`, `[!WARNING]`, `[!NOTE]`, `[!CAUTION]`) only for caveats that can break things, one per caveat: the first line gives the consequence, the next the remedy.
- Good: `> [!WARNING]` then `> Deleting the volume loses all data.` then `> Back it up first.`
- Bad: a `[!NOTE]` that only restates a feature.
- Source: adguard (2023), onyx-homeassistant-integration (2023-12), docker_helm, vault (6 alerts, 2026), shared-library.
- Check: judgment

## DOC-18 · must · common · stated

- Rule: Put everything the reader is meant to copy (commands to run, prompts, instructions to paste into a config, snippets) in a fenced code block with a language tag (`bash`, `text`, `yaml`), written so it works as pasted; a command or file only named in running text stays inline code, as in README-05's Development opener.
- Why: the reader copies it as is; inline code breaks on quotes and line wraps.
- Good: "Add this to `~/.claude/CLAUDE.md`:" followed by a fenced `text` block with the instruction.
- Bad: an instruction to paste written inside a sentence in quotes.
- Source: stated 2026-11-19, copy-pasteable text. Evidence: runbook commands are already copy-pasteable (RB-01).
- Check: judgment

## Avoid (AI-Era Artifacts)

- Em dashes, emoji, banners (PRIN-11 to PRIN-13).
- Hard-wrapped paragraphs at 80 to 120 columns.
- Sentence-case headings such as "Repository layout".
- Marketing phrases and feature walls ("integrates seamlessly").
- A new README section per change (PRIN-07).
- Typos the owner leaves ("needs to exists", "udpate readme") are not style; fix them when touching the text.
