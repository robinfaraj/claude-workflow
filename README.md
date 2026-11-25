# claude-workflow

A working method for Claude Code, as commands. Each one replaces something that used to be typed out by hand every time.

| Command | What it does |
|---|---|
| `/apply-quality-bar <task>` | Sets the quality bar and the way of working: decide like an owner, ground truth first, show before building, never show unpolished work. |
| `/research-and-design-variants <feature>` | Research (own product, competitors, Mobbin), then three real variants in an artifact. No code yet. |
| `/review-until-polished` | Review rounds on the running thing: three kinds of user, edge cases, a design lead's eye, clarity, copy, code. Fix, repeat, up to four rounds. |
| `/merge-deploy-verify` | Merge, deploy, check the live result. Only runs when typed. |
| `/close-session-safely` | "Can I close this session?" Checks code, PRs, deploys, running tasks, promises, tickets, and cleans up. |
| `/handoff-to-new-session` | Writes a one-page brief so a fresh session can take over. |
| `/work-overnight <goal>` | Unattended run: plan and blockers up front, then a morning report. |
| `/review-code-quality <area>` | Codebase review from evidence, ending in checks and types, not more rules. |
| `/improve-workflow-commands` | Reads recent prompt history and proposes improvements to these commands. Only runs when typed. |

## Role agents

| Agent | Role |
|---|---|
| `cpo` | Product lead, Linear and Apple bar. Customer, fit, Mobbin, every state. Verdict before building. |
| `cto` | Engineering lead, Vercel and Stripe bar. Delete or reuse first, simplest design, cost, risk, proof. |
| `customer-qa` | Independent tester. Roleplays real customers, breaks it, checks every number, screenshots. |
| `design-critic` | Ex-Linear senior designer. Signs off the design before the build and the screenshots before the merge. |

The working agreement runs the CPO and CTO before any non-trivial build, then customer QA and the design critic after it, without being asked.

## Always on

Installed as a plugin, `taste.md` is loaded at the start of every session by a SessionStart hook: how to own the work, the UI and copy bar, QA before done. It is how a cloud session or Claude in Slack gets the same guidance as a local one. A repo turns it on for every session by listing the marketplace and plugin in its `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "claude-workflow": { "source": { "source": "github", "repo": "robinfaraj/claude-workflow" } }
  },
  "enabledPlugins": { "flow@claude-workflow": true }
}
```

## For a team repo

To give everyone who works in a repo the same baseline, without each person installing anything, copy this into the repo: the agents into `.claude/agents/` and `taste.md` somewhere a project SessionStart hook prints it. Tinkers does this with `scripts/cloud/sync-flow.sh` and `scripts/cloud/session-start.sh`, which skips the print when the person already has this plugin, so nobody reads it twice.

## Install

**Your own machines** (short names like `/apply-quality-bar`, updated by `git pull`):

```bash
git clone https://github.com/robinfaraj/claude-workflow ~/projects/claude-workflow
~/projects/claude-workflow/install.sh
```

**As a plugin** (commands are then `/flow:apply-quality-bar`, `/flow:review-until-polished`, …):

```
/plugin marketplace add robinfaraj/claude-workflow
/plugin install flow@claude-workflow
```

## Improving it

Run `/improve-workflow-commands` every week or two. It looks at what was typed right after each command ran (that is what the command missed), at phrases still typed by hand, and at corrections, then proposes at most five edits. Accepted edits are committed here with a changelog line.

Commands are short on purpose: under about 400 words each. A line that did not change behaviour gets deleted, not explained further.
