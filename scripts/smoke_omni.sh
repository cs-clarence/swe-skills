#!/usr/bin/env bash
# Install the projection into a scratch workspace with omni and check every skill resolves.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
ws="$(mktemp -d)"
trap 'rm -rf "$ws"' EXIT
mkdir "$ws/src"
git -C "$root" ls-files -z | (cd "$root" && xargs -0 cp --parents -t "$ws/src")
cd "$ws"
git init -q
cat > workspace.omni.yaml <<YAML
projects: []
projections:
  - source: local
    id: swe-skills
    path: src
YAML
omni projection sync
omni projection status
for d in "$root"/skills/*/; do
  n="$(basename "$d")"
  [ -f ".agents/skills/$n/SKILL.md" ] || { echo "missing installed skill: $n"; exit 1; }
done
echo "ok: omni installed all skills"
