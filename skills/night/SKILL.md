---
name: night
description: The user is going to sleep or leaving and wants work to continue unattended. Use when the user types /night, or says "going to sleep", "I'm off to bed", "work on this overnight", "will it be ready in the morning", or "what will you do while I'm asleep".
---

# Overnight run

Goal for the morning: $ARGUMENTS (default: finish what this session is working on)

## Before the user leaves (answer in under ten lines, right away)
1. **Plan.** What you will finish tonight, in order, and what "done" means for each.
2. **Blockers.** Anything that needs them now: a decision, a login, an approval, a 2FA code, a credential. Ask all of it in one go. If there is nothing, say so.
3. **Limits.** What you will not do without them. Default: no production data writes, no spending money, no messages to customers, no force pushes. Merging and deploying follow the project's own rules.
4. **Will it survive.** Check that the machine stays awake: start `caffeinate -dimsu -w $PPID` in the background if it is not already running, and tell them to leave the lid open and the charger in. If the work can run in the cloud instead, say that this is the safer option.

## While they are away
- Do not stop to ask. Decide like an owner (see `/bar`), note each decision in one line for the morning report.
- If you hit a usage limit, the session continues on its own after the reset; leave it.
- If one item is blocked, write down why and move to the next. Never sit idle waiting.
- Run `/peak` on anything user-facing before calling it finished.
- Keep tickets current as the global rules say.

## Morning report (the last thing you write)
- **Done and verified**, with links (PR, preview, live URL, build).
- **Decisions I made**, one line each.
- **Blocked**, with exactly what is needed from them.
- **Look at this first**: the one thing they should check.
Send a push notification when the report is ready, if that tool is available.
