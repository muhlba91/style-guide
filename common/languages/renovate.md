# Renovate

Deltas against `../principles/`. Evidence: `renovate-config` (138 commits, 14 the owner's, since 2025-07), consumer `renovate.json` in about 10 repos.

## RENOV-01 · must · renovate · observed

- Rule: Keep consumer `renovate.json` to `$schema`, an `extends` list of `github>muhlba91/renovate-config` presets, an explicit `enabledManagers` allowlist, and extra `packageRules` or `customManagers` only for real exceptions; put reusable rules into a preset.
- Good: `"extends": ["github>example/renovate-config:default", "github>example/renovate-config:group-go"]` and `"enabledManagers": ["gomod", "github-actions"]`.
- Bad: a 40-line `packageRules` block in the consumer that every repo repeats.
- Source: all consumer repos; presets `default`, `automerge`, `group-go`, `group-pulumi` (2026-10-25).
- Check: judgment

## RENOV-02 · prefer · renovate · observed

- Rule: Automerge patch updates everywhere, minor for application and library repos, major only in the tooling repos; never automerge Python minor or major; opt out single packages with a rule.
- Source: applications (patch), github-infrastructure, vault, mail-services (patch and minor), renovate-config (all); `2be95da`, mailcow `automerge: false`.
- Check: judgment

## RENOV-03 · prefer · renovate · observed

- Rule: Label every PR `dependencies` plus `renovate-<type>`; commit types follow COMMIT-04.
- Source: `default.json` `:semanticCommitTypeAll(chore)` and its label rules.
- Check: tool:renovate

## RENOV-04 · prefer · renovate · stated

- Rule: Write Renovate `description` text in lowercase. Observed: give each non-obvious `packageRule` a one-line `description` stating the intent or constraint.
- Why: presets start uppercase and applications lowercase; lowercase is the standard.
- Good: `keep the kgateway chart and CRDs in lockstep`
- Source: stated 2026-11-18, Renovate style. Observed details: one description per non-obvious rule. Evidence: applications 3 of 3 rules; preset files all rules.
- Check: judgment

## RENOV-05 · prefer · renovate · observed

- Rule: Track versions that managers cannot see with a `custom.regex` manager keyed on a `# renovate: datasource=<ds> packageName=<name>` comment above the value.
- Why: extend the docker-compose manager to `*.yml.j2`.
- Source: applications (7 annotated lines in Kubernetes YAML), vault and mail-services.
- Check: judgment (Renovate consumes the comment but does not enforce it)

## RENOV-06 · prefer · renovate · stated

- Rule: Indent consumer `renovate.json` and preset files with 2 spaces.
- Why: consumers use 4 spaces today and presets 2; no `.editorconfig` covers it.
- Source: stated 2026-11-18, Renovate style. Evidence: all consumer repos versus `renovate-config/*.json`.
- Check: judgment
