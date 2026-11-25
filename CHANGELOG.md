# Changelog

## 0.9.0
- `design-critic` agent (ex-Linear senior designer): signs off the approved design before the build and the screenshots before the merge. The gate now runs it beside customer QA.
- `taste.md` is the founders' working agreement, not one person's, so a teammate's sessions read true too ("Needs a founder" instead of a name).
- From two weeks of prompts, what was still typed by hand: keep going without "go on"; read earlier research and artifacts before proposing; a craft check (cheap, generic or vibe-coded fails; delight only where earned); think of every other customer a change touches; short, plain replies that say what is live and what waits on whom; docs change with the change that makes them wrong.
- `/improve-workflow-commands`: fixed the script path and ignore scripted pings in the history.

## 0.8.0
- Role agents: `cpo` (product, Linear and Apple bar, Mobbin first), `cto` (engineering, delete or reuse first, cost, risk, proof) and `customer-qa` (roleplays real customers, breaks it, checks every number, screenshots).
- `taste.md`: the gate is the default. CPO and CTO before any non-trivial build, customer QA after, without being asked.
- `install.sh` links the agents too.

## 0.7.1
- `taste.md`: "Fit in the product before building" (where it lives, what it extends or replaces, variants when it doesn't clearly fit) and what "confident enough to merge" means.

## 0.7.0
- `taste.md`: the working agreement and the UI, copy and QA bar, loaded into every session by a SessionStart hook, so cloud sessions, Claude in Slack and other machines work to the same bar as the main laptop.
- `product-ux-standard` moved in from a single account, so `/apply-quality-bar` finds it everywhere.

## 0.6.0
- Removed `/design-moments-of-delight`: its first real test produced an overdone widget. A list of design moves gets executed as a checklist.
- `/apply-quality-bar`, `/research-and-design-variants` and `/review-until-polished` now run only when typed.

## 0.5.0
- Start from the user and the job (first principles); the level of delight is set by product and audience; overdone counts as a finding.

## 0.4.0
- UX laws as their own review lens, Jakob's law first in the bar and in variant research.

## 0.3.0
- `/design-moments-of-delight`, wired into the quality bar and the review rounds (new Feel lens, judged in motion).

## 0.2.0
- Commands renamed to say what they do, like function names.

## 0.1.0
- First version, written from three weeks of real sessions: `/apply-quality-bar`, `/research-and-design-variants`, `/review-until-polished`, `/work-overnight`, `/close-session-safely`, `/merge-deploy-verify`, `/handoff-to-new-session`.
- `/review-code-quality`, from the code-quality session of 11 Nov.
- `/improve-workflow-commands`, to keep the commands matching how the work is really done.
