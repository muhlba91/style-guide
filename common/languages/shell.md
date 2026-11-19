# Shell

Deltas against `../principles/`. Evidence: provisioning assets in vault and mail-services (about 25 files, human, 2024-2026), HA lifecycle scripts (2023 human, 2026 AI-assisted), applications scripts. The shellcheck hook is configured in 10 or more repos (pre-commit and CI), but not on `.j2` templates; there is no `.shellcheckrc` or `.editorconfig` in the owner's main repos.

## SH-01 · prefer · shell · observed

- Rule: Use `#!/bin/sh` and POSIX constructs for provisioning snippets on a bare VM or minimal container; use `#!/usr/bin/env bash` only when you need arrays, `[[ ]]` or functions.
- Bad: bash arrays under `#!/bin/sh`.
- Source: vault and mail-services assets; HA lifecycle scripts use bash. Counter: `node-red-init.sh` uses `[[ ]]` under `sh`.
- Check: tool:shellcheck (dialect mismatch; the hook runs in 10 or more repos)

## SH-02 · must · shell · stated

- Rule: In new scripts, start bash with `set -euo pipefail` and `sh` snippets with `set -eu`; existing scripts stay unless touched. Observed: mark accepted failures with `|| true` and bracket intentionally failing sections with `set +e` and `set -e`.
- Why: existing provisioning `sh` snippets have no `set -e`.
- Good: `set -euo pipefail` on line 2 of a bash script, then `grep -q ready "${log}" || true` for an accepted failure.
- Bad: a bash script with no `set -e` that carries on after a failed `cd`.
- Source: stated 2026-11-18, shell safety. Observed details: `|| true` and the `set +e` brackets. Evidence: HA lifecycle scripts from 2023, mailcow and ntfy restore sections.
- Check: judgment

## SH-03 · prefer · shell · observed

- Rule: Label sections with `### name ###` in provisioning snippets (one per tool, lowercase) and `#region name` / `#endregion` in longer bash scripts.
- Source: all vault and mail-services assets; HA scripts since 2023-06. 2 repo families, human.
- Check: judgment

## SH-04 · lean · shell · observed

- Rule: Shell: add one short lowercase comment above a block of commands that form a step, none above a line the command explains (PRIN-14).
- Good: `# restore from backup, if exists` above a three-command block.
- Source: all asset scripts, human 2024-2026.
- Check: judgment

## SH-05 · lean · shell · observed

- Rule: In multi-step scripts prefix each echo with a `[module]` tag and write `ERROR:` or `WARNING:` after it; send errors to stderr.
- Source: HA `prepare.sh`, `configuration.sh`, `backup_restore.sh` since 2023 (human); the log-prefix form in the 2026 `util.sh` is AI-assisted.
- Check: judgment

## SH-06 · must · shell · stated

- Rule: Pass shellcheck in all scripts, including `assets/**/*.sh`, and add no `.shellcheckrc`. Observed: quote every expansion as `"${var}"`.
- Why: older unquoted scripts are legacy; shellcheck does not run on `.j2` templates yet.
- Good: `cp "${src}" "${dst}"`.
- Bad: `cp $src $dst`.
- Source: stated 2026-11-18, shell safety. Observed details: `"${var}"` braces. Evidence: HA `8262b6a` (2023, unquoted) versus all quoted after the shellcheck gate (2026-08).
- Check: tool:shellcheck

## SH-07 · lean · shell · observed

- Rule: Name positional arguments in uppercase at the top with defaults (`SOURCE_PATH=${2:-.}`); declare function locals lowercase with `local` and assign command substitutions on a separate line.
- Source: 4 of 4 HA scripts.
- Check: tool:shellcheck (`SC2155`)

## SH-08 · prefer · shell · observed

- Rule: Record the installed version in `/opt/<app>.version` and skip or restore only when it differs or is missing.
- Source: mailcow, ntfy, traefik `install.sh` (human, 2024-2026). See PRIN-28.
- Check: judgment

## SH-09 · prefer · shell · stated

- Rule: Name new Go template files (scripts, compose files) `.tpl`; rename existing `.j2` files when you refactor them and leave the rest.
- Why: the files are Go templates but end in `.j2`.
- Source: stated 2026-11-18, template suffix. Evidence: vault 20+ and mail-services 15+ assets.
- Check: judgment

## SH-10 · must · shell · observed

- Rule: In scripts embedded in Flux manifests write shell variables as `$${VAR}` and Flux substitutions as `${VAR}`.
- Good: `echo "$${HOST} uses ${CLUSTER_NAME}"` in a ConfigMap script (shell `HOST`, Flux `CLUSTER_NAME`).
- Bad: `echo "${HOST}"` for a shell variable, which Flux replaces with an empty string.
- Source: home-cluster applications `configmap-scripts.yaml`; the only repo with that mechanism.
- Check: judgment

## SH-11 · lean · shell · observed

- Rule: Keep real logic in versioned script files; embedded ConfigMap scripts are thin wrappers that install dependencies and call the script.
- Source: HA `configmap-scripts.yaml` 2025-07 to 2026-08.
- Check: judgment

## SH-12 · prefer · shell · observed

- Rule: Parameterize scripts and compose files with Go-template placeholders (`{{ .name }}`, spaces inside braces, camelCase keys) and keep a `prepare`, `install`, `postinstall` triple per component.
- Source: vault 20+ and mail-services 15+ assets; split from SH-09 because the owner statement covers only the suffix.
- Check: judgment

## Avoid (AI-Era Artifacts)

- `Args:` / `Returns:` / `Notes:` docblocks per function (HA `util.sh`, 2026-08; the owner's 2023 scripts have none). If a sourced helper file needs one, keep it to one line.
- Box-drawing banners and emoji status output (`validate-manifests.sh`).
- `set -euo pipefail` under `#!/bin/sh` (`immich-init`), which is not POSIX.
