# Tests

## PRIN-35 · prefer · common · observed

- Rule: Place tests so they mirror the source tree and name each test after the behavior it checks.
- Good: `tests/data/test_numeric_value.py` for `onyx_client/data/numeric_value.py`; `TestCreate_CustomDays`.
- Source: onyx-client 2021-2026; Go shared-library 97 test files next to sources.
- Check: judgment

## PRIN-37 · prefer · common · stated

- Rule: Test libraries and gate their coverage in CI, with the threshold in the project config; do not require tests for infrastructure programs or services.
- Why: shared-library is tested thoroughly (97 test files), github-infrastructure has 2 test files, game-director and watermeter have none.
- Source: stated 2026-11-18, tests beyond libraries. Observed details: three Python repos fail below 95% since 2023 (`fail_under = 95`); Go shared-library reports coverage to coveralls without blocking. Evidence: Go repos read, 2023-2026.
- Check: judgment (pytest-cov `fail_under` enforces it in Python; Go `make coverage` has no threshold)

## PRIN-38 · lean · common · observed

- Rule: Use real, anonymized captured data as fixtures, and keep time-dependent tests independent of the system clock.
- Source: onyx-client `d9a4e5e` (2023, human); flaky-test fix in 2026 [ai].
- Check: judgment
