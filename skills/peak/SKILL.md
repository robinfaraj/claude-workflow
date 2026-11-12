---
name: peak
description: Run review rounds on finished work until nothing is left to fix, the way a demanding founder does QA. Use when the user types /peak, or asks "is this world class?", "roleplay as different users", "think about edge cases", "do iterations", "review rounds", "polish it", or before showing them any user-facing work.
---

# Review until it is peak

Target: $ARGUMENTS (default: what was built or changed in this session)

You are doing the QA the user would otherwise do with screenshots. Review the real thing, running, not the code. Take screenshots of every screen and state you judge. If you cannot run it, say so first; do not pretend.

## One round
Go through each lens, write down every finding, then fix them all.

1. **Users.** Walk the flow as three people who really use this product: a first-timer who knows nothing, a busy regular on a phone, and a sceptic deciding whether to pay or churn. For each: where do they hesitate, what do they misread, what do they need that is missing?
2. **Edge cases.** Empty, loading, error, offline, slow network, very long text, zero and huge numbers, no permission, first run, returning after a week, narrow (375px) and wide (1440px) screens, dark mode if the app has it.
3. **Design lead at Linear or Apple.** Hierarchy, spacing rhythm, alignment, type scale, contrast, motion, consistency with the rest of the app. What looks cheap, random or generated? What would they refuse to ship? Check against `product-ux-standard` and the project's design system if present.
4. **Clarity.** Does a stranger understand what this is and what to do in the first second? Is anything there that does not earn its place?
5. **Copy.** Run `ux-writing` and `unslop` over every string. No jargon, no vague references, no "short sentence. Another short sentence." rhythm.
6. **Engineer.** Read the diff as a reviewer: correctness, the repo's conventions, error handling, anything fragile. Run the project's checks.

## Loop
After fixing, run another round on the result with fresh screenshots. Stop when a round finds nothing that a user would notice, or after 4 rounds. Do not stop at the first round because it "looks good".

## Report
Short: rounds run, what changed (grouped, not a log), before and after screenshots of the biggest improvements, and a separate list called **Your call** with the matters of taste you could not settle. Be honest about what is still weak.
