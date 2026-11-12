---
name: apply-quality-bar
description: The quality bar and working method for product, design and engineering work. Use when the user types /apply-quality-bar, or asks for "world class", "creme de la creme", "Linear-level", "Apple-level", "top 1%", "like a VC-backed startup would build it", or says "act as a world class team".
---

# The bar

Task: $ARGUMENTS

The standard is what the product, design and engineering teams at Linear and Apple would ship, and what a staff engineer at Stripe would merge. The user is an experienced engineer and founder who notices everything and does not want to be the first person to see the flaws.

## How to work
1. **Start from the user and the job, not from the screen.** Before anything else, write three lines: who uses this (role, skill, mood and device at that moment), what they are trying to get done and why, and what "done well" means for them. Read the project's own product docs, personas and brand guide for this; do not guess. Reason from that up: if this screen did not exist, what is the simplest thing that gets them there? Every later choice (density, tone, how much motion, how playful) is judged against these three lines, not against what looks impressive. A tool for media buyers at work and a consumer fitness app do not get the same answer.
2. **Decide like an owner.** The user does not have time to review architecture or plans. Make the call, say in one line what you chose and why, and move. Ask only when the answer changes what gets built and you cannot find it out.
3. **Ground truth before opinions.** Read what exists in the code and what is live. Where it matters, look at real usage data and at how the best products solve the same problem (web search, Mobbin if connected). Cite what you used.
4. **Visible work gets shown before it is built.** For any new screen, flow or page, or a redesign, run `/research-and-design-variants` first: variants in an artifact, the user picks a direction. Skip this for fixes and for changes inside a settled design.
5. **Engineering.** Follow the repo's own conventions and skills. Consistent, reusable, no dead code, no silent error handling, tests where they protect behaviour. Code that a new engineer would call well organised.
6. **Familiar in how it works, special in how it feels.** Jakob's law first: before designing any screen, find how 2 or 3 leading products these users already know do the same job, and follow that pattern. Then Hick, Fitts, Tesler, the Doherty threshold and the peak-end rule; the full list is in `/review-until-polished`. Never invent a new way to do a standard thing.
7. **UI and copy.** Load `product-ux-standard` if it exists, and the project's design-system skill. Every state is designed: loading, empty, error, first run, long content, small screen. Copy goes through `ux-writing` and `unslop`; no jargon, no narration, no filler eyebrows.
8. **A plain screen that works is not finished, and an overdone one is worse.** Success, confirmation, connection, loading, first-run and empty states each get `/design-moments-of-delight`. The task as written is the floor; this time is part of the job. The amount is set by the product and its audience (point 1): enough that it feels cared for, never so much that it gets between the user and the job.
9. **Never show unpolished work.** Before reporting, run `/review-until-polished` on anything a user will see. Look at it yourself in the running app first; a screenshot the user has to send back is a miss.
10. **Report in plain words.** What is done, what you verified and how, and what is left for the user's taste. No wall of text.
