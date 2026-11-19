# Change Hygiene

## PRIN-46 · prefer · common · observed

- Rule: Make one focused change per commit; join at most two related changes.
- Why: subjects become changelog lines; see COMMIT-13 for the `;` form.
- Source: 5216 commits; runs of identical experiment commits in the personal cluster repo are counter-evidence.
- Check: judgment

## PRIN-47 · prefer · common · observed

- Rule: Change code, version pins, manifests and docs together when they depend on each other.
- Good: bump the library version in `pyproject.toml`, `manifest.json` and the README table in one commit.
- Source: onyx-homeassistant-integration and onyx-client pairs (2026); tool expectations kept with tests.
- Check: judgment

## PRIN-48 · must · common · stated

- Rule: After a large change, audit code and docs in a separate review pass before calling it done.
- Why: stated in the owner's working notes.
- Good: after a 40-file refactor, a second review pass over code and docs runs and its findings are fixed before reporting done.
- Bad: report done right after the last edit, with no separate review.
- Source: stated 2026-11-15, audit after large changes.
- Check: judgment

## PRIN-49 · must · common · observed

- Rule: Gate commits with pre-commit hooks and repeat the gates in CI.
- Why: the same core hooks (conform, gitleaks, detect-private-key, whitespace, EOF) run in all 37 configs.
- Good: conform at `commit-msg`, whitespace and EOF fixers, secret detection, linters.
- Source: `.pre-commit-config.yaml` and `.conform.yaml` in 37 configs; the hook set varies beyond the core.
- Check: tool:pre-commit
