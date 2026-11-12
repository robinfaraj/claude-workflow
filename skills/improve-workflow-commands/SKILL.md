---
name: improve-workflow-commands
description: Improve the workflow commands in this plugin from how the user has worked recently. Use when the user types /improve-workflow-commands, or asks to "improve the workflow", "update the commands from my recent sessions", or "what do I keep repeating".
disable-model-invocation: true
---

# Tune the workflow

Period: $ARGUMENTS (default: the last 14 days)

The commands live in the `claude-workflow` repo (find it with `readlink ~/.claude/skills/apply-quality-bar`). They should keep matching how the user really works.

1. **Collect.** Run `python3 <repo>/skills/tune/scripts/recent.py --days 14`. It reads the prompt history of every local Claude Code account and prints: how often each command was used, the prompts typed in the turns right after a command ran, repeated phrases, repeated short prompts, and correction prompts.
2. **Find what the commands missed.**
   - What the user typed right after `/review-until-polished`, `/research-and-design-variants`, `/merge-deploy-verify`, `/close-session-safely` and the others is what the command should have done by itself. Screenshots with complaints after `/review-until-polished` are the strongest signal.
   - Phrases still typed by hand many times that a command should cover.
   - A repeated multi-step request no command covers yet: a candidate for a new one.
   - Commands not used at all: wrong name, wrong trigger phrases, or not needed.
3. **Read the sessions** behind the three strongest signals (the script prints session ids; transcripts are in the account's `projects/` folder) so the change is based on what happened, not on one line.
4. **Propose** at most five edits, each as: evidence (count and one quote), the exact change, and what it should stop the user from typing. Prefer changing a line to adding a paragraph; delete instructions that had no effect. Keep every command under about 400 words.
5. **Apply** the ones the user accepts, add a line to `CHANGELOG.md`, bump the version in `.claude-plugin/plugin.json`, commit and push.

Never put customer names, secrets or pasted private content from the history into the repo.
