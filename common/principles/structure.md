# Structure

## PRIN-24 · prefer · common · observed

- Rule: Keep entry points thin: initialize, load config, wire, run; put logic in packages or modules.
- Source: `main.go` of Pulumi programs and services, HA `__init__.py`, `modules/default.nix` as an import list; 2023-2026.
- Check: tool:golangci-lint (`funlen`, `gocognit`, Go only); otherwise judgment

## PRIN-25 · prefer · common · observed

- Rule: Read configuration once, in one place, into a typed structure; keep per-site or per-host facts out of code and templates, as variables or data inputs.
- Good: `${HOME_DOMAIN}` defined once in `cluster-configuration.yaml`.
- Bad: the domain hard-coded in ten manifests.
- Source: Go config packages (`RequireObject`, `env` struct), Flux `postBuild` variables, Nix data flake input, Python `const.py`; all domains, 2023-2026.
- Check: judgment

## PRIN-26 · must · common · observed

- Rule: Never commit a secret in clear; deliver secrets through a secret store, an external secret object or an out-of-band file.
- Why: a leaked secret is not undone by a later commit.
- Good: `kind: ExternalSecret` that references `remoteRef.key: app/db-password`.
- Bad: `password: hunter2` in a values file.
- Source: ExternalSecret everywhere, SOPS for bootstrap only, Nix secrets as files, fnox, pre-commit `detect-private-key` and gitleaks; all repos.
- Check: tool:gitleaks (pre-commit hook, `detect-private-key`)

## PRIN-27 · prefer · common · observed

- Rule: Keep control flow flat: guard clauses and early returns instead of nesting.
- Good: `if data is None: return None`
- Source: Python and Go code in all repos; complexity caps in golangci config.
- Check: tool:golangci-lint (`cyclop`, `gocognit`, Go only)

## PRIN-28 · prefer · common · observed

- Rule: Make scripts and resource definitions safe to run again.
- Good: guard an install with a recorded version; `mkdir -p`.
- Source: mailcow, ntfy and traefik install scripts (2024-2026); Pulumi programs; HA lifecycle scripts (AI-assisted, 2026).
- Check: judgment
