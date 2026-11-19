# Naming

## PRIN-20 · prefer · common · observed

- Rule: Name things by domain meaning, not by mechanism or type.
- Good: `rotation.Create`, `OnyxShutter`, `external-secret-mealie-db.yaml`.
- Bad: `handler2`, `utils_misc`, `data.yaml`.
- Source: Go packages by provider or domain, Python classes with a product prefix, Kubernetes file names; all repos.
- Check: judgment

## PRIN-21 · prefer · common · observed

- Rule: Use the upstream or API term for a concept instead of a local synonym.
- Good: rename `read_only` to `readonly` to match the API.
- Source: onyx-client v12 renames (2026, [ai?]); Home Assistant naming; provider resource names in Pulumi code. Weight 0.5.
- Check: judgment

## PRIN-22 · prefer · common · observed

- Rule: One concept per file or module, named after the concept; group files by kind.
- Good: `exception/invalid_command.py`, `modules/firewall.nix`, `lib/google/project.go`.
- Source: Python library since 2021, Go Pulumi repos 2023-2026, Nix repos 2026.
- Check: judgment

## PRIN-23 · prefer · common · observed

- Rule: Replace magic numbers with a named constant that carries the unit or reason.
- Good: `maxRepositoryLength = 100`
- Bad: `if len(name) > 100`
- Source: Go (`mnd` enforced), Python `const.py`, Kubernetes limits from measured values; all years. Go makes it `must` (GO-26).
- Check: tool:golangci-lint (Go only)
