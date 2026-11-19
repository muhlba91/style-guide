# Nix

Evidence: homelab-router-infrastructure and dev-infrastructure (`nix/` trees, 2026). Most content is AI-assisted and owner-reviewed; trailered commits weigh 0.75, the 22 of 25 untrailered router commits weigh 0.5 and cap at `prefer`; the repos hold no written Nix rules, so the rules here come from the code. Deltas against `../principles/`.

## NIX-01 · must · nix · stated

- Rule: Describe and review Nix at a high level only: layout, option schema, data flow, secrets, pinning and checks; do not prescribe expression-level style beyond the formatter.
- Good: "Each host imports one flat module list; secrets come from sops; inputs are pinned in `flake.lock`."
- Bad: "Replace `optionalAttrs` with `mkIf` and avoid `with pkgs;`."
- Source: stated 2026-11-18, Nix at a high level.
- Check: judgment

## NIX-02 · prefer · nix · observed

- Rule: Put the flake in `nix/` with `modules/` (one file per concern), `modules/options/` (schema), `hardware/` and `tests/`; keep `modules/default.nix` a flat import list with a one-line header.
- Source: identical tree in 2 of 2 repos.
- Check: judgment

## NIX-03 · lean · nix · observed

- Rule: Name modules after the concern in one lowercase noun, kebab-case for compounds, subdirectories for sub-areas.
- Good: `dns.nix`, `auto-reboot.nix`, `transport/netbird.nix`
- Source: 2 of 2 repos.
- Check: judgment

## NIX-04 · prefer · nix · stated

- Rule: Gate features with `<x>.enable` options. Observed: drive every host or site from one typed option namespace (`router.*`, `dev.*`) declared in `modules/options/`, and let modules read only `config.<ns>`.
- Source: stated 2026-11-18, Nix gating. Observed details: the namespace layout. Evidence: both flakes.
- Check: judgment

## NIX-05 · lean · nix · observed

- Rule: Give every option a type and a short description with unit, reason or the meaning of `null`; build repeated shapes with small helpers in a plain-function `types.nix`.
- Source: `options/types.nix`, `options/user.nix`; [ai]-assisted.
- Check: judgment

## NIX-06 · prefer · nix · observed

- Rule: Keep generated site and host data out of module code: a data flake input (`flake = false`) with fixtures as default, overridden by the tooling; tests always run on committed fixtures.
- Source: `sites` input (router), `hosts` input (dev-infra).
- Check: judgment

## NIX-07 · prefer · nix · observed

- Rule: Nix: never put secret values in Nix or the data input; declare only name, owner, mode and reload command and fail activation if a declared file is missing (PRIN-26).
- Why: the Nix store is world-readable.
- Source: `modules/secrets.nix` in both repos.
- Check: judgment

## NIX-08 · prefer · nix · observed

- Rule: Pin inputs to a stable nixpkgs release, set `inputs.nixpkgs.follows` on other inputs, let Renovate propose release bumps, and take single newer packages from an unstable input through an explicit argument (`pkgsUnstable`).
- Source: both flakes; Renovate does not automerge `flake.lock`.
- Check: judgment (renovate helps)

## NIX-09 · prefer · nix · stated

- Rule: Make nixfmt, deadnix and statix blocking checks. Observed: ship flake checks that run offline on fixtures (lint with shellcheck, per-host evaluation, eval tests) and enforce invariants with `assertions`.
- Source: stated 2026-11-18, Nix tooling. Observed details: offline fixtures, evaluation tests, assertions. Evidence: `tests/checks.nix`, CI jobs "Nix Check", "Nix Test".
- Check: judgment (nixfmt, deadnix and statix help)

## NIX-10 · lean · nix · observed

- Rule: Write comments as a short header with the file's contract and inline comments only for a why (race, security, nixpkgs quirk); see PRIN-15, PRIN-19.
- Source: all modules read; headers range from one line to 9 lines; the limit is 3 (PRIN-19).
- Check: judgment

## NIX-11 · lean · nix · observed

- Rule: Let Pulumi generate per-host keys, secrets and `vars.nix`, let Nix consume them as input, share no logic across the boundary, and run Nix through a thin wrapper script.
- Source: dev-infra README and flake comments.
- Check: judgment

## Not Covered

Individual service modules, hardware and test files, expression style. A scope for Nix commit subjects was dropped as too weak.
