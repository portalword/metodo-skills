#!/usr/bin/env sh
# metodo-skills installer (macOS / Linux)
# Usage:  sh install.sh [target-dir, default ~/.claude] [--no-third-party]
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-$HOME/.claude}"
case "$TARGET" in --no-third-party) TARGET="$HOME/.claude"; SKIP=1;; esac
[ "$2" = "--no-third-party" ] && SKIP=1
mkdir -p "$TARGET/skills" "$TARGET/commands" "$TARGET/agents"

echo "Installing metodo-projeto and design-sistema into $TARGET/skills"
cp -R "$HERE/skills/metodo-projeto" "$HERE/skills/design-sistema" "$TARGET/skills/"
echo "Installing chat commands into $TARGET/commands"
cp "$HERE"/commands/*.md "$TARGET/commands/"
echo "Installing the testador agent into $TARGET/agents"
cp "$HERE"/agents/*.md "$TARGET/agents/"

[ -n "$SKIP" ] && { echo "Done (third-party skills skipped)."; exit 0; }

# Third-party skills are NOT bundled (their licenses). They are downloaded from their official sources.
echo ""
echo "Third-party skills (downloaded from their official sources):"
echo "  design-taste-frontend  https://github.com/Leonxlnx/taste-skill"
echo "  interface-design       https://github.com/Dammyjay93/interface-design"
echo "  transitions-dev/polish https://transitions.dev  (manual download, see their terms)"
printf "Download the first two now? (y/n) "; read OK
case "$OK" in y*|Y*|s*|S*) ;; *) echo "Skipped. The skills still work without them."; exit 0;; esac
command -v npx >/dev/null 2>&1 || { echo "npx (Node.js) not found. Install Node.js, or install them manually from the links above."; exit 0; }
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend
npx skills add https://github.com/Dammyjay93/interface-design --skill interface-design
echo ""
echo "Done. transitions-dev / transitions-polish: get them at https://transitions.dev"
