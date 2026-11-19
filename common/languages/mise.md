# mise

Deltas against `../principles/` (PRIN-39 holds the pinning rule). Evidence: `mise.toml` and `mise.lock` in 31 repos, mostly migrated on 2026-10-25 (29 migration commits).

## MISE-01 · must · mise · stated

- Rule: In every repo, pin each tool exactly in `mise.toml` and commit a lockfile (PRIN-39).
- Why: exact pins and a lockfile in every repo are the owner's standard.
- Good: `[tools]` with `go = "1.25.3"`, `lockfile = true` under `[settings]` and a committed `mise.lock`.
- Bad: `[tools]` with `go = "latest"` and no `lockfile`.
- Source: stated 2026-11-18, mise pins. Evidence: `mise.toml` and `mise.lock` in 31 repos.
- Check: judgment (mise runs the file but does not check the pins)

## MISE-02 · prefer · mise · observed

- Rule: Put runtime setup in `[env]` (for example a venv with `create = true`), explain a non-obvious override in a one-line comment, and define tasks as `[tasks.<name>]` with a `description` and a `run` list.
- Source: HA and DNS repos, vault (`FNOX_PROFILE`); recording-transcriber lint task (low weight).
- Check: judgment

## MISE-03 · lean · mise · observed

- Rule: Read secrets through fnox (`fnox.toml` with a provider, a description per secret and `if_missing = "error"`), not from a committed `local.env`; the file header states the CI and local flow and the run command.
- Why: recent (2026-11) and mixed with AI.
- Source: vault, github-infrastructure, DNS repos, infrastructure (`b53f536`, `27e519a`). See PRIN-26.
- Check: judgment

## MISE-04 · prefer · mise · observed

- Rule: Start `mise.toml` with `min_version`, then `[settings]` with `lockfile = true` and `lockfile_platforms = ["macos-arm64", "linux-x64", "linux-arm64"]`, then `[tools]`.
- Good: `min_version = "2026.10.0"`, then `[settings]` with the lockfile settings, then `[tools]` with `go = "1.25.3"`.
- Source: identical header across the 2026-10-25 sweep (29 migration commits, 21 trailered at 0.75, the rest untrailered at 0.5; one source), subject `chore: migrate to mise`. Tools pinned: go, golangci-lint, pulumi, python, sops, jq, shellcheck, kustomize, kubeconform, yq, talosctl, flux2, vault, fnox.
- Check: judgment (mise runs the file but does not check its layout)

## Note on Linters

PRIN-42 names markdownlint, ruff, shellcheck and yamllint. Ruff, golangci-lint and yamllint are configured in the owner's main repos; shellcheck runs as a pre-commit hook in several; markdownlint config exists in a few repos.
