---
name: wrap
description: Check whether a session can be closed safely and tie up loose ends. Use when the user types /wrap, or asks "can I close this session now?", "anything else open?", "all done?", "tickets updated?", "everything on main?", or "is it all live?".
---

# Can this session be closed?

Check each item for real; do not answer from memory of the conversation.

1. **Code.** `git status` and `git stash list` in every checkout and worktree this session touched. Uncommitted or unpushed work? Commit and push it on its branch, or list it.
2. **Pull requests.** Every PR this session opened: merged, waiting on checks, or waiting on a person? Give links.
3. **Live.** For what was meant to ship: did the deploy or build finish, and does the live thing work? Check it, do not assume.
4. **Running things.** Background tasks, dev servers, watchers, scheduled wakeups, other agents this session started. Stop what is no longer needed; name what must keep running and whether closing this session kills it.
5. **Promises.** Scan the conversation for things you said you would do later, and for requests of the user's that were never finished. Do them now if they are small, otherwise list them.
6. **People.** Anyone who should have been told (Slack, email, ticket comment)? Has it been sent?
7. **Tickets.** Update the tracker as the global rules say. Open follow-ups get a ticket, not a note in this chat.
8. **Clean up.** Remove worktrees you created whose work is merged (never force), and scratch files and servers. Follow the cleanup rules in the global CLAUDE.md.
9. **Memory.** Save anything a future session needs that is not in the code, the tickets or git.

## Answer
Start with one line: **Yes, safe to close** or **Not yet**, and why. Then at most six lines: what is live, what is still open and where it is tracked, what you cleaned up. If something keeps running after the session closes, say where they will hear about it.
