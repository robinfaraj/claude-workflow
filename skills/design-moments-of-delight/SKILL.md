---
name: design-moments-of-delight
description: Find the moments in a screen or flow that deserve craft and delight, and build them - success and confirmation screens, waits and loading, first run, empty states, transitions, micro-interactions, the product's own characters. Use when the user types /design-moments-of-delight, or asks for "customer delight", "wow", "make it feel insanely good", "every detail matters", "animations, transitions, micro-interactions", "how it feels", or says a screen is "plain", "lazy", "low effort" or "boring". Also use when building any success, confirmation, connection, onboarding, loading or empty state.
---

# Moments of delight

Where: $ARGUMENTS (default: the screens built or changed in this session)

A plain screen that works is not finished. The task as written is the floor. Time spent here is part of the job, not extra; do not skip it to report sooner.

## 1. Find the moments
Walk the flow and list every place the user feels something. These are where craft pays; most of the rest should stay quiet.
- **They just did something that took effort or trust**: connected an account, paid, finished setup, published, invited a teammate. The most wasted screen in software is the plain "Success" page.
- **They are waiting**: loading, generating, importing, syncing. A wait is stage time.
- **They see it for the first time**: first run, first result, first empty state.
- **They hit a milestone**: first sale, 10th post, a streak, a record.
- **Something moves**: a page changes, a panel opens, an item is added, removed or reordered.
- **Something went wrong**: an error handled with grace is remembered longer than a success.

## 2. Start from the house's best work
Before inventing, find the two or three best moments this product already has (its motion tokens, characters or mascots, signature animations, the page everyone shows off) and read how they are built. New moments use the same vocabulary, so the product feels like one hand made it. If the project has characters, they are the first tool to reach for: let them react, work, celebrate, wait with the user.

Then look outside: how do the best products handle this exact moment (Mobbin flows if connected; and name real ones you know in detail). Take the mechanism, not the look.

## 3. Design each moment
For each moment on the list, pick from these moves. Say which you chose and why it fits this moment.
- **Show the real thing, not a stand-in.** While waiting, show the actual work arriving: the first products pulled from the store, the rows filling in, the draft being written. After connecting, show what was found ("214 products, 3 collections, your best seller is…"), not "Connected".
- **Make the result feel earned.** The state changes in front of them: the line draws, the number counts up to its value, the check lands, the card settles into its place in the list.
- **Continuity.** Things move from where they were to where they go. The button becomes the panel; the thumbnail becomes the page. Nothing pops in or blinks out.
- **Physical response.** Press, hover, drag and drop answer within 100 ms, with weight: a slight give on press, a spring on release, a snap on drop. On mobile, a matching haptic.
- **Stagger and rhythm.** Lists and groups arrive in order, 20 to 40 ms apart, never all at once and never slowly.
- **A character moment.** The product's character does something small and specific to this situation. Once.
- **The found detail.** Something nobody asked for and most will not notice at first: an icon that reflects the real time of day, a greeting that knows what happened yesterday, an empty state drawn for this exact screen, a keyboard shortcut that feels like a secret.
- **Sound and haptics**, only where the platform expects them, and never on by surprise.
- **Next step in the same breath.** The success moment hands over the one obvious next action while the feeling lasts.

## 4. Restraint, or it becomes annoying
- It never makes the user wait. Animation runs alongside the work, never in front of it. Anything on the way to a task is under 300 ms; only a celebration may run longer, and it never blocks input.
- Big moments happen once. The tenth time, the same event is quiet.
- One hero per screen. If everything moves, nothing matters.
- Frequent actions get the least motion; rare, earned ones get the most.
- Reduced-motion users get the finished state, with nothing lost.
- 60 fps on a mid-range phone, or it is cut. Transform and opacity only; no layout thrash.
- It matches the product's tone. Playful where the product is playful; in a money or error context, calm and exact.

## 5. Judge it in motion
A screenshot cannot show feel. Run it and record it (screen recording, or frames captured through the interaction), at normal speed and on a throttled network so the wait is real. Watch it three times. Cut what is tiresome on the third watch. Check it under reduced motion and on a small screen.

## Report
For each moment: what it was, what it is now, the move used, and a recording or frame strip. Then **Ideas I did not build**: the bolder ones, with what they would cost, so the user can say yes.
