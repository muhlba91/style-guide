# Pull Requests, Issues and Replies

Evidence: the owner's own PRs and issues in onyx-client, onyx-homeassistant-integration, pulumi-proxmoxve (excluded from other evidence, used here for reply text only), adguard; the owner's issues on third-party repos; about 200 issue comments, 2021-2026. No PR review comments by the owner exist. Replies are friendly and unhurried; the tone follows PRIN-08.

## PR-01 · must · common · observed

- Rule: Make the PR title the commit subject: Conventional Commits, lowercase, imperative, with the `; fix #N` suffix when it applies.
- Why: the title becomes the changelog line. Branch-name titles (`Feat/mutmut`, 5 PRs) are accidents.
- Good: title `feat: add retry option; fix #12`.
- Bad: title `Feat/retry-option`.
- Source: onyx-client, onyx-homeassistant-integration, pulumi-proxmoxve 2023-2026.
- Check: judgment (conform checks commit subjects, not PR titles)

## PR-02 · must · common · observed

- Rule: Leave the PR body empty or one line: a `BREAKING CHANGE:` line, a `fix #N`, or one sentence of why; do not restate the diff.
- Good: body `fix #12`.
- Bad: a body that lists every changed file and restates the diff.
- Source: 11 of 20 PRs empty in onyx-client, 11 of 18 in onyx-homeassistant-integration, 33 of 57 empty or one line in proxmox.
- Check: judgment

## PR-03 · lean · common · observed

- Rule: In a longer PR body open with the change in one lowercase sentence, then a short list of what changed, then blockers as a task list with links.
- Source: a handful of 2021-2024 PRs (proxmox #42, #38, #20, #6; onyx #45, #33); a 2026 AI PR has a similar shape (weight 0.5 unless trailered).
- Check: judgment

## PR-04 · prefer · common · stated

- Rule: Do not add a PR template; keep PR bodies free-form, with the commit subject as title and a body only when needed.
- Why: none of the owner's repos has a template and no checklist boxes appear.
- Source: stated 2026-11-18, PR template. Evidence: `.github` holds CODEOWNERS, FUNDING and workflows only.
- Check: judgment

## PR-05 · lean · common · observed

- Rule: In a PR to a project that is not the owner's, explain the use case in 2 to 3 sentences, say what is minimal and untouched, thank the maintainer in one line, and follow the target's template.
- Source: 2026 external PRs (vyos-rolling, sonar-checkstyle); two others look AI-assisted.
- Check: judgment

## PR-06 · prefer · common · stated

- Rule: Title an issue as a Title Case noun phrase naming the capability or problem, without a Conventional Commits prefix.
- Why: own repos use Title Case (`Local API Access`); third-party trackers force their templates.
- Good: `Local API Access`
- Source: stated 2026-11-18, issue titles. Observed details: quote the error line in a bug title; about 10 own issues 2021-2026.
- Check: judgment

## PR-07 · prefer · common · observed

- Rule: In an issue state the current situation, the wanted solution and the constraint in short paragraphs; use bullets for options, links to docs or code, and `- [x]` tasks; use no template headings.
- Source: 2021 issues used template headings, 2023-2026 dropped them. Epics link sub-issues with task lists.
- Check: judgment

## PR-08 · prefer · common · observed

- Rule: In a bug report to someone else give versions, the exact setup, the observed behavior, what you ruled out, then logs in a code block; start a feature request with the use case and the risk it removes.
- Source: reports on kgateway, octodns, auth-actions, talos, opnsense, hcloud (2026).
- Check: judgment

## PR-09 · must · common · observed

- Rule: Reply to strangers in a friendly, direct tone: thank once, say what is known, say what is needed, give the next step; apologize plainly and once for a real own error or delay.
- Good: "thanks for the report. reproduced on 2.3; can you attach the debug log? then the fix is next."
- Bad: "Hopefully this should fix it!!!"
- Source: Onyx (2021-2026), proxmox, adguard; never exaggerates (`should fix`, `hopefully`).
- Check: judgment

## PR-10 · prefer · common · stated

- Rule: Start every sentence lowercase in replies and issue bodies, the first one included; titles use Title Case. Use standard case in greetings and text to maintainers of other projects; keep code, versions and product names exact.
- Why: about 70% of the owner's reply sentences start lowercase; titles, external PRs and greetings use standard case.
- Source: stated 2026-11-18, reply case. Observed details: the greeting, external-maintainer and exact-name clauses; replies 2021-2026.
- Check: judgment

## PR-11 · must · common · observed

- Rule: Ask for missing facts as a short list, each with a purpose: version, debug logs, a minimal program, output of the failing command; ask the reporter to redact secrets.
- Good: "to narrow this down, please send: the version, the debug log (redact tokens), and the output of the failing command."
- Bad: "Doesn't work for me either, any news?" or "Please provide more info."
- Source: Home Assistant, proxmox, adguard issues.
- Check: judgment

## PR-12 · prefer · common · observed

- Rule: If the cause is upstream, say so with the reason, ask the reporter to try upstream directly, open an issue there and link it, and keep the local issue open until it is fixed.
- Source: about 25 replies in the proxmox provider repo, 2023-2026.
- Check: judgment

## PR-13 · prefer · common · observed

- Rule: Decline in this order: thank, say it is not planned or you are reluctant, give the technical reason in a few lines, offer what you can do (docs, an alternative, accepting a fitting PR); no blame.
- Source: proxmox #17, #26, #723; Home Assistant #72, #494, #8.
- Check: judgment

## PR-14 · prefer · common · observed

- Rule: Announce a fix with the exact version in backticks; for a beta ask the reporter to test it; close after confirmation or with `closing due to being stale`.
- Source: Home Assistant #72, #89 beta loop (2023-12); `12.0.2 will fix ...`.
- Check: judgment

## PR-15 · lean · common · observed

- Rule: Thank a contributor once and briefly; ask for a rebase, CLA or failing checks plainly; if you redo the change, link the commit and close.
- Source: adguard #52, proxmox #164, #1022, Home Assistant #655.
- Check: judgment

## PR-16 · prefer · common · observed

- Rule: Explain behavior as a short numbered flow or a list of options with the favored one and why; link the code line or doc section instead of paraphrasing it.
- Source: Home Assistant #154, #89, #8; proxmox #26, #327; replies run 4 to 12 lines.
- Check: judgment

## PR-18 · must · common · stated

- Rule: Add no attribution to PR text: no "Generated with" line and no AI trailer, whatever the tool's default adds (COMMIT-17).
- Why: the owner reviews and owns what is merged; PR bodies follow the commit rule.
- Good: body `fix #12` and nothing after it.
- Bad: a body ending in a "Generated with ..." line or a `Co-Authored-By:` AI trailer.
- Source: stated 2026-11-18, attribution (no "Generated with" line in commits or PRs).
- Check: judgment
