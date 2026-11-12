---
name: ship
description: Merge the current work, deploy it and confirm it is live. Only when the user types /ship or plainly says "merge", "deploy", "merge and deploy", "push to main" or "get it live".
disable-model-invocation: true
---

# Ship

What: $ARGUMENTS (default: the work of this session)

Follow the project's own release rules first (CLAUDE.md, a `submit`, `deploy` or `verify-app` skill). Where the project says nothing, do this:

1. **Ready?** Working tree clean, branch pushed, the project's checks pass (types, lint, tests, build). If a check fails, fix it or stop and say why. Do not ship around a failing check.
2. **Merge.** Open a PR if there is none. Wait for CI. Merge the way the repo does. Never push straight to a protected main, never force push.
3. **Deploy.** If merging deploys on its own, watch that deploy until it finishes. If not, run the project's deploy. Database migrations and other production writes run only if the user approved them in this session.
4. **Verify live.** Open the production URL or build and check the changed thing works: the real page or endpoint, not only a 200 on the home page. For a mobile build, confirm the build number arrived where it should.
5. **Tidy.** Update the ticket, delete the merged branch, remove your worktree.

Report in three lines: what shipped (PR link), where it is live and how you checked, and anything that did not go out. If a step fails, say which one and what state things are in now. Do not say "done" until step 4 has passed.
