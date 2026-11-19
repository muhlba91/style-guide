# Go

Deltas against `../principles/`. Evidence: shared-library, github-infrastructure, vault, mail-services, home-cluster infrastructure, adguard provider, game-director, watermeter; 2023-2026. 2023 adguard code is built on an upstream template and is weaker evidence than 2025-26 code. The shared linter config is likewise an adopted upstream template, so it shows adoption, not authorship.

Pulumi programs: see [pulumi.md](pulumi.md).

## GO-01 · must · go · observed

- Rule: Gate every repo on one `.golangci.yml` (v2 schema) through `make lint`, which runs `golangci-lint run -c .golangci.yml` then `go vet ./...`; `make fix` runs `golangci-lint fmt`.
- Why: one strict baseline across the Pulumi and service repos.
- Good: `make lint` runs `golangci-lint run -c .golangci.yml` then `go vet ./...`.
- Bad: a per-repo `make lint` that calls only `go vet ./...`.
- Source: 6 Pulumi and service repos since 2025 carry the same config apart from small differences; the baseline is the adopted upstream golden config with its comments, so it shows adoption, not authorship. The adguard config is an unrelated file. Pre-2025 code (telegraf) does not follow it.
- Check: tool:golangci-lint

## GO-02 · must · go · observed

- Rule: Keep the strict profile and conform to it: complexity caps, `gochecknoglobals`, `gochecknoinits`, `nonamedreturns`, `mnd` (flags bare numbers except in the ignored functions the config lists, such as `time.Date`, `strconv.Parse*`, `os.WriteFile`, `flag.*`), `goconst`, `godot`, `testpackage`, `errorlint`, `errname`, `sloglint`, `depguard` (ban `log` outside main and `math/rand`), formatters `goimports`, `gofumpt`, `golines` at 120 columns.
- Good: `var ErrNoHost = errors.New("no host")` and `const maxRetries = 3` instead of a bare `3`.
- Bad: `func load() (cfg Config, err error)` with a named return.
- Source: shared-library `.golangci.yml` and its copies in the other 2025-26 repos; adopted template (GO-01).
- Check: tool:golangci-lint

## GO-03 · must · go · observed

- Rule: Go: write a suppression as `//nolint:<linter> // <reason>` with a short lowercase reason and no period (PRIN-44).
- Good: `//nolint:gochecknoglobals // set at build time using ldflags`; a TODO line (PRIN-18) carries `//nolint:godox // TODO is required` because `godox` is on.
- Bad: `//nolint`
- Source: about 60 nolints across 6 repos; `nolintlint` requires a name and an explanation.
- Check: tool:golangci-lint (`nolintlint`)

## GO-04 · prefer · go · observed

- Rule: Use initialisms in identifiers (`ID`, `IP`, `URL`) and rename instead of suppressing when the linter is right.
- Source: shared-library `f6e7733`, `19e94a8` (2026, human).
- Check: tool:golangci-lint (`revive`, `staticcheck`)

## GO-05 · prefer · go · observed

- Rule: Allow package-level variables only for build-time values (`Version`, `Gitsha` via ldflags), module-level Pulumi config and default lists, each with a `nolint:gochecknoglobals` reason.
- Source: 6 of 9 repos.
- Check: tool:golangci-lint (`gochecknoglobals`)

## GO-06 · prefer · go · observed

- Rule: Run Go tests with `go test -v -tags=all -parallel $(TESTPARALLELISM) -timeout 2h -covermode atomic -coverprofile=covprofile`; target names follow PRIN-45 and MAKE-01.
- Source: the same test command in 6 Pulumi and service repos since 2025; 8 Makefiles have lint, fix, test and coverage (the adguard Makefile has no `fix` or `coverage`); pre-2025 telegraf differs.
- Check: judgment

## GO-07 · prefer · go · observed

- Rule: Stay on the latest Go minor within weeks of release; use `slices`, `maps`, `min` and range-over-int from the standard library.
- Source: upgrade commits 2025-08, 2026-02, 2026-09 across repos; `intrange`, `copyloopvar`, `exptostd` linters.
- Check: tool:golangci-lint (`intrange`, `copyloopvar`)

## GO-08 · prefer · go · observed

- Rule: Lay out services as `cmd/<binary>`, `internal/` for private code and `pkg/` only for what other modules import; split `internal` by role (`configuration`, `logging`, `store`, `transport`, `health`).
- Source: game-director, watermeter, adguard; 3 of 3.
- Check: judgment

## GO-09 · prefer · go · observed

- Rule: Name files by action or noun (`create.go`, `validate.go`, `session.go`); use `constants.go` and `error.go` per package, and put `<file>_test.go` next to the file.
- Source: shared-library, github-infrastructure, game-director.
- Check: judgment

## GO-10 · prefer · go · observed

- Rule: Constructors are `NewX(...)` returning the concrete pointer; interfaces are small, defined by the consumer and composed by embedding.
- Source: game-director (13 constructors), watermeter; counter-evidence: adguard 2023 returns an interface.
- Check: tool:golangci-lint (`interfacebloat`, `iface`)

## GO-11 · prefer · go · observed

- Rule: Declare sentinel errors in a `var (...)` block in `error.go`, named `ErrX` (exported) or `errX`, and test with `errors.Is`.
- Source: game-director (5 packages), adguard.
- Check: tool:golangci-lint (`errname`)

## GO-12 · must · go · stated

- Rule: In new or substantially rewritten Go code in libraries (including pulumi/shared-library) and services, wrap errors with `%w` and add context; existing code stays unless touched. Pulumi programs log and return unchanged (PULUMI-02).
- Why: callers can match the cause with `errors.Is`; no special case for the Pulumi library.
- Good: `fmt.Errorf("failed to create the adguard client: %w", err)`
- Bad: `return err` with no context in a new library function.
- Source: stated 2026-11-18, error handling by project type; the owner decided new library code wraps, whatever shared-library does today (0 `%w`, legacy). Evidence: adguard 2023, watermeter 2026, game-director 2026.
- Check: tool:golangci-lint (`errorlint`)

## GO-13 · lean · go · observed

- Rule: Example only, not a rule: vault validates a config struct by collecting all problems with the field path as prefix and returning them joined.
- Source: vault `bgp/validate.go`, 2026, one repo; API design of one program.
- Check: judgment

## GO-14 · prefer · go · observed

- Rule: Services read configuration from environment variables through `caarlos0/env/v11` into one struct with `env` and `envDefault` tags; `Init()` exits on a parse error.
- Source: adguard 2023, game-director 2026, watermeter 2026; 3 of 3. The two newer services are AI-heavy 2026 work, so this stays `prefer` until a non-2026 service confirms it.
- Check: judgment

## GO-15 · prefer · go · observed

- Rule: Document every config struct field with a doc comment that includes unit and default, written as GO-17 requires (starts with the identifier, ends with a period).
- Good: `// TokenTTL is the TTL of a JWT in seconds. Defaults to 1 hour.`
- Source: game-director, github-infrastructure model structs, shared-library options; adguard 2023 has none.
- Check: judgment

## GO-16 · prefer · go · stated

- Rule: Use `log/slog` for new services; Pulumi programs keep zerolog (log prefixes: PULUMI-04).
- Why: `sloglint` and `depguard` require it and game-director migrated from logrus in 2026-07; watermeter and adguard still use logrus.
- Source: stated 2026-11-18, Go logger. Evidence: game-director `c9fd0bf`, 26 files.
- Check: tool:golangci-lint (`sloglint`, `depguard`)

## GO-17 · must · go · stated

- Rule: Give every exported function and type a one-line doc comment so callers know what it does from the rendered docs alone. Observed: start it with the identifier, end it with a period, and do the same for exported constants and fields.
- Why: the goal is that a reader of only the rendered docs and interfaces knows what happens. Inline comments inside a function still follow PRIN-14.
- Good: `// Create adds the record and returns its id.` above `func Create(...)`.
- Bad: `// adds the record` or no comment above an exported `Create`.
- Source: stated 2026-11-18, API documentation. Observed details: identifier first, period, constants and fields. Evidence: documented functions 64/70, 74/74, 37/37, 39/41 in four repos; older hand code (telegraf, proxmox provider, adguard 2023) has undocumented exported identifiers.
- Check: tool:golangci-lint (`godot`, `godoclint`)

## GO-18 · must · go · stated

- Rule: Under the summary line of an exported function, add one `name: description.` line for every parameter, even an obvious one such as `ctx`; this API documentation overrides PRIN-05 and PRIN-14. No `@param`, no headings.
- Why: callers must know from the rendered docs what each argument does.
- Good: `// ctx: The Pulumi context.` and `// timeout: Maximum wait in seconds, defaults to 30.`
- Bad: `// @param timeout the maximum wait`
- Source: stated 2026-11-18, parameter lines. Evidence: about 240 such lines in shared-library and 100 to 250 in four other repos, human, 2025-26.
- Check: judgment

## GO-19 · prefer · go · observed

- Rule: In a doc comment, add behavior beyond the name only when not obvious: defaults, naming scheme, clamping, secrecy.
- Good: `// defaults to 30 if <= 0`
- Source: shared-library `rotation.Create`, `WritePulumiStrict`.
- Check: judgment

## GO-20 · prefer · go · observed

- Rule: Inside functions, use short lowercase section labels in orchestration code (`// dns`, `// outputs`) or a reason for a constraint; never narrate the next line.
- Source: vault and github-infrastructure `main.go`; PRIN-14. Older telegraf code (2021 to 2024) narrates, so `prefer`.
- Check: judgment

## GO-21 · lean · go · observed

- Rule: Skip package comments.
- Source: `ST1000` and revive package-comment rules disabled; none found. A disabled check enforces nothing.
- Check: judgment

## GO-22 · prefer · go · observed

- Rule: Test in the external package (`package x_test`) with `testify` (`require` for preconditions, `assert` for values) and name tests `TestFunc` or `TestFunc_Variant`.
- Source: 96 of 97 test files in shared-library; the exception carries a `nolint:testpackage` reason. One repo only.
- Check: tool:golangci-lint (`testpackage`, `testifylint`)

## GO-23 · prefer · go · observed

- Rule: Use table tests with `t.Run` for pure functions, one test per variant for resource creation, and `t.TempDir()` for files.
- Source: shared-library; `t.Parallel` is not used (`paralleltest` disabled).
- Check: tool:golangci-lint (`usetesting`)

## GO-24 · prefer · go · stated

- Rule: Group imports as standard library, third party, local module, using goimports.
- Why: strict in shared-library, looser in infra `main.go` files; `gci` is off.
- Source: stated 2026-11-18, import grouping. Observed details: local prefixes in the goimports config; alias only on conflict, with a short camelCase alias. Evidence: shared-library, github-infrastructure, vault.
- Check: tool:golangci-lint (`goimports` local-prefixes)

## GO-25 · lean · go · observed

- Rule: Document `main` as "main is the entry point of ..."; start, wait for SIGINT or SIGTERM, then shut down in reverse order.
- Source: game-director, adguard, Pulumi `main.go` files.
- Check: judgment

## GO-26 · must · go · observed

- Rule: Go: enforce PRIN-23 with `mnd`, and write file permissions in `0o` octal with a named default.
- Good: `const defaultFileMode = 0o600` passed to `os.WriteFile(path, data, defaultFileMode)`.
- Bad: `os.WriteFile(path, data, 0600)`.
- Source: github-infrastructure `google/defaults.go`, shared-library `file/write.go`.
- Check: tool:golangci-lint (`mnd`)

## GO-27 · prefer · go · observed

- Rule: Keep lists and tuning constants per provider in a `defaults.go` with a one-line doc per item.
- Source: github-infrastructure `lib/{google,scaleway,aws}/defaults.go`, watermeter `constants.go`.
- Check: judgment

## GO-28 · prefer · go · observed

- Rule: Quote values in error messages with `%q` and use `errors.New` for static text.
- Good: `fmt.Errorf("unknown record type %q: %w", kind, err)` and `errors.New("no host")`.
- Source: adguard 2023, watermeter 2026, game-director 2026; split from GO-12 because the owner statement covers only wrapping.
- Check: judgment

## GO-29 · prefer · go · observed

- Rule: Pass slog keys as constants from a `logging` package and errors as `slog.Any("error", err)`; never use the global logger of the standard `log` package.
- Source: game-director `c9fd0bf` (2026-07), enforced by `sloglint` and `depguard`; one service family.
- Check: tool:golangci-lint (`sloglint`, `depguard`)

## Avoid (AI-Era Artifacts)

- Long prose doc comments on every private method and interface method (game-director, watermeter, 2026; lines are all owner-committed but the verbosity differs from 2023 code). Keep the one-line form (GO-17).

## Not Covered

Dockerfiles and goreleaser, GitHub Actions for Go beyond mise setup, full read of any repo, `assignment-infrastructure` code. No clear case of the owner editing AI-written Go code was found.
