#!/bin/bash
# Link every command and role agent into each local Claude Code account, so they
# are typed as /apply-quality-bar and so on, and a `git pull` here updates them
# everywhere. The working agreement (taste.md) is loaded by a SessionStart hook:
# add `cat <this repo>/taste.md` to each account's settings, or install as a plugin.
set -e
REPO="$(cd "$(dirname "$0")" && pwd)"
link_all() { # <source dir> <target dir>
    local SRC="$1" DEST="$2"
    mkdir -p "$DEST"
    for ITEM in "$SRC"/*; do
        [ -e "$ITEM" ] || continue
        NAME=$(basename "$ITEM")
        TARGET="$DEST/$NAME"
        if [ -e "$TARGET" ] && [ ! -L "$TARGET" ]; then
            echo "skip $TARGET (a real file is already there)"
            continue
        fi
        ln -sfn "$ITEM" "$TARGET"
    done
}
for CONFIG in "$HOME"/.claude "$HOME"/.claude-*; do
    [ -d "$CONFIG" ] && [ -f "$CONFIG/.claude.json" -o -f "$CONFIG/settings.json" ] || continue
    # An account whose folder is itself a link already shares another account's.
    [ -L "$CONFIG/skills" ] || link_all "$REPO/skills" "$CONFIG/skills"
    [ -L "$CONFIG/agents" ] || link_all "$REPO/agents" "$CONFIG/agents"
    echo "linked into $CONFIG"
done
