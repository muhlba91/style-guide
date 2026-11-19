#!/usr/bin/env bash
# Recreates the relative links .agents/skills/<name> -> ../../common/skills/<name> and .claude/skills -> ../.agents/skills.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${root}"

mkdir -p .agents/skills .claude
find .agents/skills -mindepth 1 -maxdepth 1 -type l -delete

for skill in common/skills/*/; do
  name="$(basename "${skill}")"
  ln -s "../../common/skills/${name}" ".agents/skills/${name}"
  echo "linked ${name}"
done

ln -sfn ../.agents/skills .claude/skills
echo "linked .claude/skills"
