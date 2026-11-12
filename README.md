# claude-workflow

A working method for Claude Code, as commands. Each one replaces something that used to be typed out by hand every time.

| Command | What it does |
|---|---|
| `/bar <task>` | Sets the quality bar and the way of working: decide like an owner, ground truth first, show before building, never show unpolished work. |
| `/explore <feature>` | Research (own product, competitors, Mobbin), then three real variants in an artifact. No code yet. |
| `/peak` | Review rounds on the running thing: three kinds of user, edge cases, a design lead's eye, clarity, copy, code. Fix, repeat, up to four rounds. |
| `/ship` | Merge, deploy, check the live result. Only runs when typed. |
| `/wrap` | "Can I close this session?" Checks code, PRs, deploys, running tasks, promises, tickets, and cleans up. |
| `/handoff` | Writes a one-page brief so a fresh session can take over. |
| `/night <goal>` | Unattended run: plan and blockers up front, then a morning report. |
| `/audit <area>` | Codebase review from evidence, ending in checks and types, not more rules. |
| `/tune` | Reads recent prompt history and proposes improvements to these commands. Only runs when typed. |

## Install

**Your own machines** (short names like `/bar`, updated by `git pull`):

```bash
git clone https://github.com/robinfaraj/claude-workflow ~/projects/claude-workflow
~/projects/claude-workflow/install.sh
```

**As a plugin** (commands are then `/flow:bar`, `/flow:peak`, …):

```
/plugin marketplace add robinfaraj/claude-workflow
/plugin install flow@claude-workflow
```

## Improving it

Run `/tune` every week or two. It looks at what was typed right after each command ran (that is what the command missed), at phrases still typed by hand, and at corrections, then proposes at most five edits. Accepted edits are committed here with a changelog line.

Commands are short on purpose: under about 400 words each. A line that did not change behaviour gets deleted, not explained further.
