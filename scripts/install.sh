#!/usr/bin/env bash
# Links every skill of this repository into the skill folders of the agents on this machine.
# Targets default to ~/.claude/skills and ~/.agents/skills; override with STYLE_GUIDE_SKILL_DIRS (space separated).
# Links into this repository and dangling links are replaced; anything else at the target is left alone and reported.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
read -r -a targets <<<"${STYLE_GUIDE_SKILL_DIRS:-${HOME}/.claude/skills ${HOME}/.agents/skills}"

for target in "${targets[@]}"; do
  mkdir -p "${target}"
  for skill in "${root}"/common/skills/*/; do
    name="$(basename "${skill}")"
    link="${target}/${name}"
    current="$(readlink "${link}" 2>/dev/null || true)"
    if [[ ! -e "${link}" ]] || [[ "${current}" == "${root}/"* ]]; then
      ln -sfn "${root}/common/skills/${name}" "${link}"
      echo "linked ${link}"
    else
      echo "skipped ${link}: exists and does not point into this repository"
    fi
  done
done
