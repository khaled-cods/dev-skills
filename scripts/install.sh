#!/usr/bin/env bash
# Copy every skill into your personal Claude Code skills folder.
# Usage: ./scripts/install.sh            (all skills)
#        ./scripts/install.sh code-review debug-systematically   (only these)
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
dest="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$dest"
if [ "$#" -gt 0 ]; then names=("$@"); else names=($(ls "$here/skills")); fi
for n in "${names[@]}"; do
  if [ ! -d "$here/skills/$n" ]; then echo "unknown skill: $n" >&2; exit 1; fi
  rm -rf "$dest/$n"
  cp -r "$here/skills/$n" "$dest/$n"
  echo "installed $n -> $dest/$n"
done
echo "Done. Restart Claude Code (or open a new session) to load them."
