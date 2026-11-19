# GitHub Actions

Deltas against `../principles/`. Evidence: workflows in home-cluster applications, github-infrastructure, vault, HA, container repos (8 repos with the same shape), 2023-2026. The untrailered 2026-10 sweep commits carry the owner's subjects; the content is uniform enough to be tool-assisted, so they weigh 0.5 (0.75 only where a commit carries a trailer) and never raise a rule alone.

## CI-01 · must · github-actions · stated

- Rule: Start every workflow with `name:` in Title Case, `on:` and top-level `permissions: contents: read` (a job may add another minimal read scope it needs, such as `pull-requests: read`); give every job `runs-on: ubuntu-latest` (the runner label is the exception to PRIN-40's no-`latest`) and a human `name:`; raise write permissions per job only, except when every job of a workflow needs the same permissions: then set exactly those scopes once at the top level instead of repeating them per job (never `write-all`). Give pipeline, pr and deploy workflows a `concurrency` group `${{ github.workflow }}` with `cancel-in-progress: false` for main and deploy, `${{ github.workflow }}-${{ github.ref }}` with `true` for PRs.
- Why: 99 of 164 workflows have a `concurrency` block; top-level permissions are in 160.
- Good: `name: Pipeline`, `permissions: contents: read` at the top, a `concurrency` group `${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` in `pr.yml`; the `deploy` job adds `id-token: write` for itself. When every job needs `id-token: write`, the workflow sets it once at the top level.
- Bad: no top-level `permissions:`, or `permissions: write-all` on the workflow.
- Source: stated 2026-11-19, top-level permissions when every job needs the same. Evidence: 8 repos; top-level permissions in 160 of 164 workflows; `chore(ci): fix github workflow concurrency` in about 8 repos (2026-10-07). 2023 workflows lacked both blocks.
- Check: judgment

## CI-02 · must · github-actions · observed

- Rule: Pin every third-party action to a full commit SHA with the version as a trailing comment (`# vX.Y.Z`).
- Good: `uses: actions/checkout@0123456789abcdef0123456789abcdef01234567 # v4.2.0`
- Bad: `uses: actions/checkout@v4`
- Source: all workflows since 2024-10 (`c23bb71`); 2023 workflows used tags. See PRIN-40.
- Check: judgment (OpenSSF Scorecard reports unpinned actions)

## CI-03 · must · github-actions · observed

- Rule: Start every job with `step-security/harden-runner` using `egress-policy: audit`, then `actions/checkout`.
- Good: first step `uses: step-security/harden-runner@<sha> # vX.Y.Z` with `egress-policy: audit`, second step `actions/checkout`.
- Bad: a job that starts with `actions/checkout` and has no harden-runner.
- Source: harden-runner in 161 of 164 workflows, added with the scorecard rollout 2024-10.
- Check: judgment

## CI-04 · prefer · github-actions · observed

- Rule: Use one job per gate (`conform`, `lint`, `shellcheck`, `ruff`, `kubeconform`, tests); preview and deploy jobs list the gates in a multi-line `needs:`.
- Why: previews do not depend on `conform`, so a commit message problem does not block them (`aad0f91`, 2026-11).
- Source: applications `pipeline.yml`, `pr.yml`; github-infrastructure `pr.yml`.
- Check: judgment

## CI-05 · prefer · github-actions · observed

- Rule: Install tools with `jdx/mise-action` from `mise.toml`; separate setup actions only restore caches, with a comment saying so.
- Source: `245e01df` (applications) and the 2026-10-25 migration in about 12 repos.
- Check: judgment

## CI-07 · lean · github-actions · observed

- Rule: Release containers and libraries with release-please (`include-v-in-tag: true`, PR title `chore(release): release ${version}`) and build multi-arch (`linux/amd64,linux/arm64`) with buildx.
- Source: pgvecto and node-red repos; 2 repos.
- Check: judgment

## CI-08 · must · github-actions · observed

- Rule: Name workflow files `pipeline.yml`, `pr.yml`, `dependency_review.yml`, `scorecard.yml`, `codeql.yml`, `release.yml`, `verify.yml` with the `.yml` extension.
- Good: `.github/workflows/dependency_review.yml`, `pipeline.yml`.
- Bad: `.github/workflows/dependency-review.yaml`, `ci.yaml`.
- Source: all repos; the underscore in `dependency_review.yml` is consistent.
- Check: judgment

## CI-09 · prefer · github-actions · stated

- Rule: Write a single-command step as a one-line `run:`; use `run: |` for several commands.
- Why: applications uses the block form for one command, github-infrastructure the one-line form.
- Good: `run: yamllint .`
- Source: stated 2026-11-18, `run:` form. Evidence: both repos, 2023-2026.
- Check: judgment

## CI-10 · must · github-actions · observed

- Rule: Run conform on pull requests with `fetch-depth: 0`, in addition to the commit-msg hook (COMMIT-20).
- Good: `uses: actions/checkout@<sha> # vX.Y.Z` with `fetch-depth: 0` before the conform step.
- Bad: the conform step runs on a shallow checkout and cannot see the PR commits.
- Source: github-infrastructure `pr.yml`, 37 repos with `.conform.yaml`.
- Check: judgment (conform helps)
