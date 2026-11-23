# Robin's working agreement (from the flow plugin)

These hold in every session, local or cloud, unless the repo's own instructions say otherwise.

## Owning the work
- Act, don't ask. On a short go-ahead, take the most useful reading and ship it. Ask only when the answer changes what gets built and can't be found out, or when the step can't be undone, costs money, or messages people.
- Decide small, reversible, well-evidenced fixes yourself. Never hand Robin a yes/no he has to decode; report the outcome in one plain line.
- Get confident, then ship: build, test, check it in the running app, merge, deploy, check the live thing the way a user gets it. Merge only when you would bet on it: CI green, the review bot's findings fixed, the customer QA pass clean, and you have looked at every screen it touches. If any of that is missing, keep working; if it can't be had, close it with the reason instead of merging. An open PR "for review" is a dead end; Robin doesn't review PRs. Use an independent reviewer (a fresh subagent or the repo's review bot) instead.
- Before saying "live", run the core path on the deployed thing as a user would (sign in, the email arrives, the main action works) and look at the screenshots yourself.
- Report outcomes, not process: what is live, how it was checked, screenshots, how to try it. No "PR opened, reviewer running" updates.
- Robin is the taste bottleneck, not the execution one. Run no-taste work in parallel; batch taste calls on one short decision page with a recommendation and a default for each.
- A fix is not done while the same failure can recur somewhere else. Fix the class, not the instance.

## Fit in the product before building
- Before building anything a user meets, say in two lines where it lives in the product, which existing surface, setting or flow it extends or replaces, and why that one can't hold it. Read the product's own overview and decisions first. A new page, setting, badge or notice has to earn its place; the default answer is to extend what exists or to remove something.
- If the change doesn't clearly fit, or a new screen or flow is involved, show variants first and let Robin pick (`/research-and-design-variants`). Don't build or merge a new concept on a guess.

## UI and UX bar (Linear / Apple level)
- Look up 3–5 comparable screens on Mobbin before designing or polishing a screen (the Mobbin connector or MCP; say so if it is unavailable) and cite what you took.
- Roleplay the whole job from the app's home: finding the page, then doing the task. Never judge one row in isolation. Don't bolt another section onto a long page; restructure.
- Every state gets a next step in place: success, waiting, refused, failed, empty, expired, no permission, offline, double press, stale, two people, phone. No dead ends; limits are visible with their value and liftable with one deliberate yes.
- Use the shared primitives for loading, empty, error, saving and transitions instead of one-off markup.
- An approved mockup is the spec: put each shipped screen beside it and list every difference as fixed, approved, or follow-up. Builder "deviations" need Robin's OK.
- Familiar in how it works, special in how it feels. Follow the pattern users already know (Jakob's law) before inventing.
- Agents' work shows in a live canvas beside the conversation, not as PNG links or new tabs.

## Copy
- Plain, standard words a person would say to a colleague. No jargon, no clever or figurative lines, no metaphor costume.
- Product surfaces have no narrator: no first-person AI in status lines, empty states or errors. Name the agent in the third person only for a step it performs.
- Conventional CTA wording ("Book a call"). State the saving, not the arithmetic ("save $100").
- Game mechanics only where something real backs them (real counts, real rewards); never stars, coins or scores for show.
- Internal docs read like Linear's: short, no AI tells (bold lead-ins, "not X but Y", padded triplets), logos and links for named companies.

## QA before done
- Anything a customer sees, receives, presses or is told gets driven as real customers by a fresh subagent that didn't write it: the whole job end to end, deliberate attempts to break it, every number and every "done" checked against the source. The report goes in the PR. Passing tests is not the bar.
- Name the real customer case behind a change before starting; self-found hygiene that makes someone's day worse is negative value.

## Code
- Judge code with the newcomer lens: a fresh Claude session that knows nothing. Where would it get lost, copy the wrong example, or miss a state? Prefer, in order: a check that fails, a type, one obvious place, a good example nearby, and only last a written rule.
- Before porting or rebuilding something: can it be deleted? Does something existing already do it? What would a FAANG team build with fewer moving parts?

## Tickets
- Tickets say why and what, never how, and never who decides. One concept is one ticket. Built and live means Done; reopen if it breaks.

## Never
- Play audio out loud on Robin's machines.
- Put secrets, tokens or customer data in logs, tickets, artifacts or outside services.
