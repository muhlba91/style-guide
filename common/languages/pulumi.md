# Pulumi (Go Programs and Library)

Only what the Go findings show: github-infrastructure, vault, mail-services, home-cluster infrastructure (Go since 2026-02, earlier TypeScript), assignment-infrastructure (grep only), shared-library.

Not covered: stack YAML and `Pulumi.<stack>.yaml` contents, Pulumi ESC, secret providers, provider-specific resource choices, the earlier TypeScript programs, `pulumi up` operations (see `../writing/runbook.md`). The excluded repo `pulumi-proxmoxve` was not used.

## PULUMI-01 · must · pulumi · observed

- Rule: Structure a program as a thin `main.go` plus `pkg/{lib,model,util}`: `lib` creates resources, `model` holds config structs, `util` holds helpers; test doubles live in `test/mocks`.
- Good: `main.go` only loads config and calls `lib.Create(ctx, cfg)`; structs sit in `pkg/model`.
- Bad: a 400-line `main.go` that declares resources and config structs.
- Source: 6 of 6 Pulumi repos, 2023-2026; home-cluster moved into the same layout in 2026-02.
- Check: judgment

## PULUMI-02 · must · pulumi · stated

- Rule: In Pulumi programs, log the failure with the area prefix, then return the error unchanged; do not wrap with `%w` at each level. Libraries, including shared-library, wrap new errors (GO-12).
- Why: flat orchestration code with greppable origin. About 156 log calls against 3 to 12 `Errorf` per repo.
- Good: `log.Err(err).Msgf("[google][project] error creating project: %s", name)` then `return err`
- Source: stated 2026-11-18, error handling by project type. Evidence: github-infrastructure, vault, home-cluster; human.
- Check: judgment

## PULUMI-03 · must · pulumi · observed

- Rule: Name error variables after the call with a short operation prefix and `Err` (`sErr`, `iErr`, `ghErr`); reuse plain `err` only for the first error in a function.
- Why: avoids shadowing in long flat functions (`govet` strict shadow).
- Good: `sErr := secret.Create(...)` then `iErr := ingress.Create(...)`.
- Bad: `err := secret.Create(...)` then `err := ingress.Create(...)` in the same function.
- Source: 5 of 5 Pulumi repos, 2023-26; a variant `errVault` exists in home-cluster.
- Check: tool:golangci-lint (`govet` shadow)

## PULUMI-04 · prefer · pulumi · observed

- Rule: In Pulumi programs (libraries wrap errors per GO-12 instead), prefix log messages as `[area][sub-area]` and word them "error `<doing>` ..." or "failed to `<do>` ...".
- Source: zerolog calls in 4 repos; home-cluster `07895dc` deepened prefixes (2026).
- Check: judgment

## PULUMI-05 · must · pulumi · stated

- Rule: Load stack configuration once in a `config` package into typed model structs with `cfg.RequireObject`, or with `cfg.GetObject` only when the whole config key is optional and a missing key means all defaults; make optional fields pointers and read them with `defaults.GetOrDefault(ptr, fallback)`.
- Good: `var c model.Vault; cfg.RequireObject("vault", &c)` and `defaults.GetOrDefault(c.Replicas, 3)`; `cfg.GetObject("server", &c)` when the whole `server` key may be absent.
- Bad: `cfg.Get("replicas")` parsed with `strconv.Atoi` inside a resource function.
- Source: stated 2026-11-19, optional config read with `cfg.GetObject`. Evidence: github-infrastructure, vault, mail-services, home-cluster; shared-library helper.
- Check: judgment

## PULUMI-06 · prefer · pulumi · stated

- Rule: In the reusable library, create resources with `Create(ctx, opts)` or `Create(ctx, name, opts)` (24 of 43 take `name`): context first, options struct last; export the options struct, document every field, make optional fields pointers or documented defaults, and add extras through `PulumiOptions []pulumi.ResourceOption`. Repo-internal helpers keep positional arguments.
- Why: 24 of 43 library `Create` functions also take `name string`.
- Source: stated 2026-11-18, options struct scope. Evidence: shared-library throughout, `llms.txt` states the pattern; 2026-11 library code takes `name`.
- Check: judgment

## PULUMI-07 · prefer · pulumi · observed

- Rule: Test resources with `pulumi.RunErr` and `pulumi.WithMocks`, assert resource counts by type token or resource outputs, and keep mocks in `test/mocks`.
- Source: shared-library accesskey and file tests; the only tested Pulumi code.
- Check: judgment

## PULUMI-08 · lean · pulumi · observed

- Rule: Gate destructive operator toggles behind an environment variable that defaults to false.
- Good: `ALLOW_REPOSITORY_DELETION` unset means no deletion.
- Source: github-infrastructure.
- Check: judgment
