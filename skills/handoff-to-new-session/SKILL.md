---
name: handoff-to-new-session
description: Write a brief so a fresh session can take over or start a piece of work, instead of continuing a long session or pasting context by hand. Use when the user types /handoff-to-new-session, or says "start a new session for this", "write a prompt for another session", "hand this over", or when a session has grown very long and the topic is changing.
---

# Hand off to a fresh session

Work to hand over: $ARGUMENTS (default: what is still open in this session)

Write a brief that a session with no memory of this one can act on. Save it to the project's notes or scratch folder as a markdown file and print the path, plus the command to start: `claude -n "<short name>" "Read <path> and start."`

The brief contains, in this order:
1. **The one outcome** this session owns, and what done looks like.
2. **State today.** What is built, what is live, which branch, PR and worktree, what was tried and ruled out.
3. **Decisions already made** by the user. The new session must not reopen them.
4. **Read first.** Exact paths: docs, decision records, memories, skills, artifacts and ticket links. Point to files; do not paste them.
5. **Boundaries.** What other sessions are working on, so it does not touch that. What needs the user's approval.
6. **How to work.** One line: "Work to `/apply-quality-bar`; run `/review-until-polished` before showing anything; `/close-session-safely` at the end."
7. **First three steps.**

Keep it under a page. Then update the ticket with a link to the brief, and tell the user this session can be closed after `/close-session-safely`.
