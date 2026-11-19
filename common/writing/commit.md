# Commit Messages

Evidence: 5216 owner commits in 40 repos (2021: 91, 2022: 38, 2023: 881, 2024: 1167, 2025: 1151, 2026: 1888), of which 236 carry an AI trailer (all 2026). Subject statistics cover all of them. Conform config in 37 repos.

## COMMIT-01 · must · common · observed

- Rule: Write the subject as `type(scope)?: description` in Conventional Commits form.
- Why: release-please builds changelog and version from subjects.
- Good: `feat: add config-sync to gatus`
- Bad: `Add config sync to Gatus.`
- Source: 5214 of 5216 comply, all years; conform at commit-msg and in PRs.
- Check: tool:conform

## COMMIT-02 · must · common · stated

- Rule: Use `feat` for any change visible to a user or operator, including enabling, migrating or updating an app in infra repos; `fix` for corrections, `refactor` for restructuring, `perf` for performance, `chore` for maintenance without visible effect, `docs` for docs only, `test` for test-only changes (conform allows it).
- Why: feat is 49% of 2026 commits in the infra repos; `test` and `perf` are rare.
- Good: `feat: enable the mail relay` for a new deployed app; `fix: handle empty response`.
- Bad: `chore: enable the mail relay`, or `doc: update setup`.
- Source: stated 2026-11-18, commit types (merged from the retired COMMIT-03). Observed details: 2025 feat 596 versus fix 356; 2026 feat 928, fix 662, chore 222; `doc:` is a typo; evidence from home-cluster apps, mail, vault, github-infrastructure.
- Check: judgment (conform helps: it checks the type list only)

## COMMIT-04 · prefer · common · observed

- Rule: Write dependency commits as `chore(deps): update <thing> to vN`; use `feat(deps)` only when the bump changes what ships (upstream provider, major chart).
- Source: `chore(deps)` 340, `feat(deps)` 94, `fix(deps)` 11; Renovate `:semanticCommitTypeAll(chore)`.
- Check: judgment (Renovate's `:semanticCommitTypeAll(chore)` helps for bot commits)

## COMMIT-05 · must · common · stated

- Rule: Use no scope except `ci`, `deps` and `release`; they are scopes, never types: write `chore(ci): add workflows`, not `ci: add workflows`.
- Why: conform allows only these scopes; other scopes appear 1 to 3 times each.
- Good: `chore(deps): update nginx to v1.27.3`, `chore(ci): add workflows` and `feat: add retry option`.
- Bad: `feat(client): add retry option` and `ci: add workflows`.
- Source: stated 2026-11-18, commit scopes; clarified 2026-11-19 after an evaluation run used `ci:` as a type. Evidence: 17.2% of commits carry a scope, 96.4% of those are `ci` or `deps`.
- Check: tool:conform (scope whitelist)

## COMMIT-06 · must · common · stated

- Rule: Flag a breaking change with a `BREAKING CHANGE: <what breaks>` footer line, not with `!` after the type.
- Why: both forms parse in release-please; the footer is the form the owner uses.
- Good: subject `feat: upgrade to onyx api v6`, footer `BREAKING CHANGE: dropping support for onyx api < v6`.
- Bad: `feat!: upgrade to onyx api v6`
- Source: stated 2026-11-18, breaking marker. Evidence: 54 human commits in 11 repos, 2021-2026 use the footer; `!` appears 5 times (3 AI). With `Release-As` (COMMIT-15) the footer is the only place human commits have a body.
- Check: judgment

## COMMIT-08 · must · common · observed

- Rule: Write the description in lowercase imperative mood without a trailing period; keep literal identifiers in their case.
- Good: `fix: increase trivy operator memory`
- Source: 0 of 5216 start uppercase or end with a period; conform `imperative`, `case: lower`, `invalidLastCharacters: .`.
- Check: tool:conform

## COMMIT-09 · prefer · common · stated

- Rule: Aim for 3 to 6 words in the description; never exceed 100 characters in the header.
- Why: median 4 words and 32 to 37 characters every year, but 8.8% of human subjects and 7 of 20 recent ones are longer, so the word count is a target and 100 is the limit.
- Source: stated 2026-11-18, subject length. Evidence: subjects over 100 characters carry an upstream issue link.
- Check: tool:conform (header length), judgment (word count)

## COMMIT-10 · must · common · stated

- Rule: Set the conform header `length` to 100.
- Why: header limits differ across repos; one ceiling keeps subjects short.
- Good: `.conform.yaml` has `length: 100` under the header rules.
- Bad: `length: 200`.
- Source: stated 2026-11-18, subject length ceiling. Evidence: 37 `.conform.yaml` files: 80 (13), 90 (1), 100 (3), 120 (8), 200 (12).
- Check: tool:conform

## COMMIT-11 · prefer · common · observed

- Rule: Start with a precise verb; use `update` for bumps and `prepare ... to vX` before an unreleased upstream version.
- Good: add, fix, update, enable, migrate, move, remove, upgrade, set, prepare, cleanup, use, increase, disable, rename.
- Source: first-word counts (add 1018, fix 972, update 821, enable 369); "implement", "improve", "support", "bump" are rare.
- Check: judgment (conform helps: it checks the imperative only)

## COMMIT-12 · prefer · common · stated

- Rule: Name the thing changed instead of echoing the type (`fix: fix X`).
- Why: the best-formed subjects are specific, even though 15% of subjects echo the type.
- Good: `fix: add annotations for gatus-sidecar`
- Bad: `fix: fix trivy resources`
- Source: stated 2026-11-18, commit types. Evidence: 781 `fix: fix` subjects.
- Check: judgment

## COMMIT-13 · prefer · common · observed

- Rule: Prefer `;` over `and` to join two separate changes; `and` inside one noun phrase is fine; use at most two clauses.
- Good: `fix: correct golangci-lint findings; update dependencies`
- Source: 124 of 5216 subjects, 2023-2026; `and` still appears in a few recent untrailered subjects.
- Check: judgment

## COMMIT-14 · prefer · common · observed

- Rule: Reference an issue at the end of the subject after a semicolon (`; fix #12`, `; part of #12`); do not use `Closes` footers.
- Source: 31 subjects in 8 repos, 2021-2025, none in 2026; 99% of commits have no reference.
- Check: judgment

## COMMIT-15 · must · common · stated

- Rule: Write no prose body; use footers only (`BREAKING CHANGE`, `Release-As: X.Y.Z`).
- Why: the subject carries the whole message; AI-assisted commits that added bodies are not the standard.
- Good: `feat: drop the v1 endpoint` with footer `BREAKING CHANGE: v1 endpoint removed`.
- Bad: a three-paragraph body explaining the change.
- Source: stated 2026-11-18, commit bodies. Evidence: 72 of 4980 human commits have a body.
- Check: judgment

## COMMIT-17 · must · common · stated

- Rule: Add no attribution to commits or PR text: no `Co-Authored-By` trailer for agents and no "Generated with" line. Add no `Signed-off-by` either (PR-18 covers PR text).
- Why: the owner reviews and owns what is committed; 236 commits of 2026 carry a trailer, which is not the standard.
- Good: `fix: handle empty response` and nothing after the subject.
- Bad: a trailing `Co-Authored-By:` line naming an agent, or `Signed-off-by:`.
- Source: stated 2026-11-18, attribution. Observed details: `Signed-off-by` appears 0 times, conform `dco: false`.
- Check: judgment

## COMMIT-18 · lean · common · observed

- Rule: Keep AI-written subjects to the owner's average length by dropping the qualifier.
- Source: average 43 characters for AI commits versus 35 for human; "apply review findings for ..." pattern (7 in 2026).
- Check: judgment (conform helps: it checks length only)

## COMMIT-19 · prefer · common · observed

- Rule: Let release-please create release commits and notes; pin a manual release with `chore: release X.Y.Z` (no scope; release-please's own commits are `chore(release): release X.Y.Z`) and a `Release-As: X.Y.Z` footer; write no release prose by hand.
- Source: GitHub Releases are all bot-generated from subjects; `Release-As` in container repos 2022-2026. Keep emoji out of anything that reaches a changelog (PRIN-12).
- Check: judgment

## COMMIT-20 · prefer · common · observed

- Rule: Provide a `.conform.yaml` with the policy `commit` and wire it as a commit-msg pre-commit hook.
- Good: imperative, `case: lower`, `invalidLastCharacters: .`, `body.required: false`, `dco: false`, `gpg.required: false`, spellcheck US, `descriptionLength: 100`, types refactor, perf, chore, test, docs, no_type, scopes ci, deps, release.
- Source: 37 configs; conform accepts `feat` and `fix` without listing them (shared-library and cluster applications list neither, and 25 of their last 600 commits are `feat`); 26 are identical apart from header length, 11 differ in scopes (`update`) or order. A template file would fit better.
- Check: tool:conform

## Avoid (AI-Era Artifacts)

- Long subjects that spell out the full behavior.
- Bodies that restate the diff or list files.
- Direct-to-main experiment runs with identical subjects (`update resources (3)` through `(12)`, `play around with homepage` x5); squash or reword when done (PRIN-46).
