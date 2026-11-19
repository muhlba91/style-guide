# Makefile

Evidence: 11 Makefiles in 11 repos, all Go projects or Pulumi programs: shared-library, vault, github-infrastructure, mail-services, home-cluster infrastructure, assignment-infrastructure, adguard provider, watermeter, game-director, plus two outside the tiers (telegraf plugin 2022, a Pulumi provider fork whose Makefile derives from an upstream template). The onyx repos have none. No Makefile commit carries an AI trailer. Five Makefiles are the same file with one import path changed, so the true sample is smaller than the count. The teaching-toolkit Makefile (AI-generated) is cited only as labeled supporting evidence. Rules that restate the Go target set live in `go.md` (GO-06) and `../principles/tooling.md` (PRIN-45).

## MAKE-01 · prefer · makefile · stated

- Rule: In new or substantially rewritten Makefiles, keep the Makefile a thin wrapper: one target per task, named as in PRIN-45, with an aggregate `check` that runs lint and test. Observed: each target runs tools directly; add `build` and `clean` for binaries.
- Why: the same commands work in every repo and CI.
- Good: `lint:` runs `golangci-lint run -c .golangci.yml` and `go vet ./...`; `fix:` runs `golangci-lint fmt -c .golangci.yml`.
- Source: stated 2026-11-18, Makefile shape for new Makefiles. Observed details: tools run directly, `build` and `clean`. Evidence: 10 of 11 have `lint` and `test`; 8 have `fix` and `coverage`; 4 have `build` and `clean`; the aggregate `check` comes from the reviewed teaching-toolkit Makefile.
- Check: judgment

## MAKE-02 · prefer · makefile · stated

- Rule: In new or substantially rewritten Makefiles, declare all targets in one `.PHONY:` line. Observed: put it at the top, after the variables.
- Why: a stray file named `test` or `lint` cannot shadow the task, and one line is easy to keep complete.
- Good: `.PHONY: help check lint test fix coverage`.
- Source: stated 2026-11-18, Makefile shape for new Makefiles. Observed details: position after the variables. Evidence: existing Go Makefiles declare one `.PHONY` per target (10 of 11); new ones follow the reviewed teaching-toolkit style.
- Check: judgment

## MAKE-03 · prefer · makefile · stated

- Rule: In new or substantially rewritten Makefiles, define targets with a single colon (`lint:`).
- Why: the double colon in the existing Go and Pulumi Makefiles (10 of 11) is likely inherited from a template and no reason is documented.
- Source: stated 2026-11-18, Makefile shape for new Makefiles. Evidence: an older Makefile (2022) uses a single colon.
- Check: judgment

## MAKE-04 · lean · makefile · observed

- Rule: Put variables first with `:=`. Use `?=` only for values the caller may override.
- Why: constants stay fixed; overrides are explicit.
- Good: `TESTPARALLELISM := 8` and `ARTIFACT_NAME := tool`, but `GOOS ?= $(shell go env GOOS)`.
- Source: `TESTPARALLELISM`, `WORKING_DIR` (`$(shell pwd)`) and `ARTIFACT_NAME` in 9 Makefiles; `?=` appears only in telegraf (`GOOS`, `GOARCH`) and the fork (`TESTTAGS`). Teaching-toolkit (AI, supporting only) uses `?=` for every tool name.
- Check: judgment

## MAKE-05 · prefer · makefile · observed

- Rule: Do not call `mise` from the Makefile. Pin tools in `mise.toml` and call them by name.
- Why: one place pins versions; `make` works in a shell where mise is active and in CI after `mise-action`.
- Good: `golangci-lint run -c .golangci.yml`, not `mise exec -- golangci-lint run`.
- Source: 0 of 11 Makefiles mention mise; all 9 Go repos pin `golangci-lint` in `mise.toml` and say in the README to run `mise install` then `make ...`; mise tasks exist only in the excluded recording-transcriber (low weight).
- Check: judgment

## MAKE-06 · prefer · makefile · observed

- Rule: Make the `test` target the exact command CI runs. CI calls `make test` and keeps lint in a separate job with the same config.
- Why: a green local `make test` predicts the CI job.
- Good: the workflow installs tools with `jdx/mise-action`, then runs `make test`; `lint` mirrors the golangci-lint action (`-c .golangci.yml`) plus `go vet ./...`.
- Source: `make test` in the verify or pr workflow of 6 of 6 workflows checked (shared-library, vault, github-infrastructure, adguard, watermeter, game-director); lint runs through `golangci-lint-action`, not `make lint`; `fix`, `coverage` and `clean` never run in CI.
- Check: judgment

## MAKE-07 · lean · makefile · observed

- Rule: Copy the target set of the newest sibling repo's Makefile, not its syntax: apply MAKE-02, MAKE-03 and MAKE-08, and change only the artifact name and the test package path.
- Why: identical task behavior across repos, no per-repo design; the sibling's double colons and per-target `.PHONY` are legacy.
- Source: 5 Makefiles (shared-library, vault, github-infrastructure, mail-services, home-cluster infrastructure) differ only in the Go import path of `make test`; assignment-infrastructure adds `yamllint .` to `lint`. Created 2025-10 to 2026-02 in "initial version" or "migrate to go" commits, so one copy event, not independent evidence.
- Check: judgment

## MAKE-08 · prefer · makefile · stated

- Rule: In new or substantially rewritten Makefiles, add a `help` target that lists every target with its `##` description, and set `.DEFAULT_GOAL := help`.
- Why: the existing Go Makefiles have none (0 of 11) and list commands in the README; new Makefiles are self-describing.
- Good: `lint:  ## run golangci-lint`
- Source: stated 2026-11-18, Makefile shape for new Makefiles. Evidence: the teaching-toolkit Makefile (Tier 1.5, supporting) uses `.DEFAULT_GOAL := help`, `##` help text and an aggregate `check`; the owner reviewed it (2026-10).
- Check: judgment

## MAKE-09 · lean · makefile · observed

- Rule: Indent recipes with tabs and write one plain command per line. Add `@` only to guards and echo.
- Why: recipe output shows what ran; chains and line continuations hide it.
- Good: `go build -o $(WORKING_DIR)/bin/$(ARTIFACT_NAME) ./cmd/tool` then `chmod +x ...` on the next line.
- Source: all recipe lines in the 9 Go Makefiles are tab-indented; shell logic is limited to usage guards (`@test -n "$(SRC)" || (echo "usage: ..." && exit 1)` in watermeter, 2026, likely AI-assisted) and multi-line `if` blocks in the template-derived fork. `coverage` runs `open`, which assumes macOS.
- Check: judgment

## Not Covered

- release-please configuration.
- CODEOWNERS.
- Jupyter notebooks.
