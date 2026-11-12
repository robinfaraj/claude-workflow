#!/bin/bash
# Link every command into each local Claude Code account, so they are typed
# as /bar, /peak and so on, and a `git pull` here updates them everywhere.
set -e
REPO="$(cd "$(dirname "$0")" && pwd)"
for CONFIG in "$HOME"/.claude "$HOME"/.claude-*; do
    [ -d "$CONFIG" ] && [ -f "$CONFIG/.claude.json" -o -f "$CONFIG/settings.json" ] || continue
    mkdir -p "$CONFIG/skills"
    # An account whose skills folder is itself a link already shares another account's.
    [ -L "$CONFIG/skills" ] && continue
    for SKILL in "$REPO"/skills/*/; do
        NAME=$(basename "$SKILL")
        TARGET="$CONFIG/skills/$NAME"
        if [ -e "$TARGET" ] && [ ! -L "$TARGET" ]; then
            echo "skip $TARGET (a real folder is already there)"
            continue
        fi
        ln -sfn "${SKILL%/}" "$TARGET"
    done
    echo "linked into $CONFIG/skills"
done
