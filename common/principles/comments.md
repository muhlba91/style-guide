# Comments

## PRIN-14 · must · common · stated

- Rule: Write no comment where the code already says it, except API docs of exported or public functions (GO-18, PY-13).
- Good: `dns.Create(ctx, opts)` with no comment.
- Bad: `// create the dns entries` above that call.
- Source: stated 2026-11-18, comments. Evidence: Go orchestration files carry only section labels; Python functions mostly have no comment. All years.
- Check: judgment

## PRIN-15 · must · common · observed

- Rule: Comment only to give a reason, unit, assumption or non-obvious constraint, and put it above the line or constant.
- Why: a CI step comment may also say what feeds what.
- Good: `STREAM_READ_TIMEOUT = 90  # seconds, three missed pulses`
- Bad: `# set the timeout to 90`
- Source: Python, Go, YAML and Nix, all repos 2021-2026; an AI comment was edited from "what" to "why" (onyx-homeassistant-integration `08478d4`); CI step comments in github-infrastructure `pipeline.yml`, `pr.yml` (2026-11); Kubernetes manifests (about 85 comments).
- Check: judgment

## PRIN-16 · prefer · common · observed

- Rule: Start inline comments lowercase and end them without a period; Go doc comments are the exception (GO-17).
- Good: `# restore from backup, if exists`
- Bad: `# Restore from backup, if it exists.`
- Source: shell assets, Python, YAML comments, CI comments; human 2023-2026.
- Check: judgment

## PRIN-17 · prefer · common · observed

- Rule: Do not leave commented-out code or config in source; delete it, except a deliberate switch (a recovery block kept next to the active one) that says so.
- Why: git has the history.
- Source: home-cluster infrastructure `07895dc` removed a 40-line commented block (2026); counter-evidence: `# initdb:` toggles in CNPG manifests.
- Check: judgment

## PRIN-18 · prefer · common · observed

- Rule: A TODO links its issue or upstream bug and states the removal condition.
- Good: `# TODO: remove once <issue url> is fixed`; in Go, `// TODO: remove once <issue url> is fixed //nolint:godox // tracked upstream`
- Bad: `# TODO: fix this`
- Source: about 5 TODOs in 5 Go repos and YAML manifests, nearly all with a link; one applications TODO has none.
- Check: judgment (in Go, `godox` is on: every TODO also needs a `//nolint:godox` on the same line with a reason)

## PRIN-19 · must · common · stated

- Rule: Keep a file header to at most 3 lines; put longer design notes in docs.
- Why: a header gives the purpose and any non-obvious contract; AI-era long headers are not the owner's style.
- Good: `# Which modules do something is decided by dev.* options.`
- Bad: a 20-line header repeating the module list.
- Source: stated 2026-11-18, file header length. Observed details: purpose and contract as content; Nix modules in two repos, one-line headers next to 9-line essays, AI-assisted, weight 0.5.
- Check: judgment
