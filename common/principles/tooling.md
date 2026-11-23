# Tooling and Pinning

## PRIN-39 · must · common · stated

- Rule: Manage tool versions with mise: pin every tool exactly in `mise.toml` and commit `mise.lock`, in every repo.
- Good: `mise.toml` pins `python = "3.14.1"`, `mise.lock` is committed, and the README says to run `mise trust` and `mise install`.
- Bad: `python = "3.14"` with no lockfile.
- Source: stated 2026-11-18, exact pins and a lockfile in every repo. Observed details: the README tells contributors to run `mise trust` and `mise install`. Evidence: 31 repos have `mise.toml` and `mise.lock`; 29 migration commits on 2026-10-25, 21 with AI trailers (0.75) and 8 without (0.5).
- Check: judgment (`mise.lock` helps; mise does not check the layout)

## PRIN-40 · must · common · observed

- Rule: Pin every dependency, image, chart, action and tool to an exact version; never `latest`, except runner labels such as `ubuntu-latest`. Pin by digest only for an unstable tag.
- Good: `image: nginx:1.27.2` and `uses: actions/checkout@<full sha> # v4.2.2`.
- Bad: `image: nginx:latest`.
- Source: images and charts (all values files), Actions by SHA since 2024-10, Python constraint `>=3.14,<3.15`; exceptions are legacy (2023 workflows, three falco plugin tags).
- Check: judgment (renovate keeps pins current)

## PRIN-41 · must · common · observed

- Rule: Let Renovate propose version updates; do not bump pinned versions by hand unless a bump needs a code change.
- Good: merge the Renovate PR `chore(deps): update nginx to v1.27.3`.
- Bad: edit the pinned `1.27.2` to `1.27.3` by hand with no code change.
- Source: all repos use the shared preset (`renovate-config`); `chore(deps)` commits.
- Check: judgment (renovate proposes the updates)

## PRIN-42 · must · common · stated

- Rule: Lint every file type in the repo with the linters that make sense for it (code, Markdown, shell, workflows with actionlint per CI-11); a file type alone does not justify a linter (YAML-04 for yamllint); the gates pass before work is done.
- Why: stated in the owner's working notes (ruff, markdownlint, shellcheck, yamllint); narrowed 2026-11-23 because a linter that adds no signal only adds maintenance.
- Good: the gates `ruff check`, `markdownlint`, `shellcheck` and `actionlint` all pass before the change is called done; no `yamllint` in a repo whose only YAML is workflows and tool configs.
- Bad: ruff passes while the new `deploy.sh` and `README.md` were never linted; or yamllint added only because the repo has a `renovate.json` and workflows.
- Source: stated 2026-11-15, lint every file type; stated 2026-11-23, only the linters that make sense for the repo. Evidence: Observed: golangci-lint and ruff in the Go and Python repos; yamllint in several repos; shellcheck in 10 or more pre-commit configs plus CI; markdownlint configured in 5 repos, 3 of them evidence-eligible.
- Check: judgment (pre-commit and CI run the configured linters; they do not enforce which linters fit)

## PRIN-43 · prefer · common · observed

- Rule: Fix the code instead of loosening the linter; keep one shared lint config per language across repos.
- Source: Go configs differ by 4 to 9 lines across 5 repos; `nolint` commits add reasons, not config relaxations (adguard `124fa1b`).
- Check: judgment

## PRIN-44 · must · common · observed

- Rule: Suppress a finding only with a narrow, named suppression and a written reason; remove it when the cause is gone.
- Good: `//nolint:mnd // 0o600 is the correct permission for private keys`
- Bad: `//nolint`
- Source: about 16 nolints in shared-library, 10 to 12 in four other Go repos, all with reasons; hadolint ignores carry reasons.
- Check: tool:golangci-lint (`nolintlint`, Go only)

## PRIN-45 · prefer · common · observed

- Rule: Expose the same task names in every repo: `lint`, `fix`, `test`, `coverage` (Makefile or mise tasks).
- Source: 8 Makefiles define lint, fix, test and coverage (adguard lacks fix and coverage); mise tasks exist only in the excluded recording-transcriber, low weight.
- Check: judgment

## PRIN-50 · must · common · stated

- Rule: Pin the linters in `mise.toml` so one `mise install` provides them, except yamllint, which comes from a local install and is never listed in `mise.toml` (YAML-04).
- Good: `shellcheck = "0.11.0"` and `actionlint = "1.7.12"` in `[tools]` of `mise.toml`.
- Bad: shellcheck installed by hand or through the system package manager; `yamllint` in `mise.toml`.
- Source: stated 2026-11-15, ruff, markdownlint, shellcheck and yamllint pinned in mise; stated 2026-11-23, yamllint removed from mise (its mise build breaks repos on Python 3.15) and used from a local install. Evidence: the mise sweep of 2026-10-25 (21 of 29 commits trailered at 0.75, the rest 0.5); ruff, markdownlint and shellcheck appear in mise configs; actionlint is new (stated).
- Check: judgment
