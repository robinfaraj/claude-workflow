---
name: product-ux-standard
description: The product and UX bar for any app UI the founders build (Tinkers, Postel and the rest) — the details pass to run on every feature (can it be instant, can the user leave, how they learn it is done, what real thing fills the wait, lineage, every state, AI cost), how loading, first-run/import, refresh, empty and error states must behave, how copy reads, and the review loop before showing UI. Use whenever building, changing or reviewing any app screen, flow, state or component: new pages, loading or skeleton states, waits after connecting/importing, empty states, error handling, retries, offline, notices/banners, analytics/dashboards, onboarding, toasts, or when the user asks for "world class", "Linear-level", "really well done" UI/UX. Load it before writing UI code, not after.
---

# Product & UX standard

The bar: what Linear's product and design team would ship. Calm, dense, honest, fast. The user is the founder; they notice everything and hate AI slop, vibe-coded UI, process narration and homework buttons. Decide product and UX details yourself using this file; don't hand them micro-decisions.

## 0. The details pass (every feature, without being asked)

The user expects these small things thought through on every feature, across sessions; they should never have to ask (2026-10-25: "this is what makes a product truly great… make this the standard"). Run this pass when planning, and again before showing anything. Design an answer to each question, or say in one line why it doesn't apply.

1. **Can it be instant?** Look for work redone on every visit (re-scoring, re-fetching, steps run one after another that could overlap), work that could start earlier (on connect, in the nightly job) and results worth remembering. Fix the engineering before designing a wait.
2. **Can the user leave?** Anything over ~10s runs on the server (a Trigger.dev task), never in the tab. Leaving, reloading, a second tab or coming back halfway never loses the work or starts it twice (one run per workspace, idempotent).
3. **How do they find out it's done?** When they're elsewhere in the app: a count on the nav item, a quiet toast with Open, "(n)" in the tab title. No modal or email for routine work.
4. **What real thing can fill the wait?** Show the actual material being worked on as it really progresses: the posts being read and their verdicts, the source a draft comes from, the user's own name, avatar and topics. Never jokes, tips, fake bars or checklists.
5. **Where did this come from?** Every generated thing shows its source and why ("from @maya, 14× her usual views").
6. **Every state, designed.** First run, returning with data, in progress, partly done, done, nothing found, limit hit, error, offline, slow network, phone, reduced motion, dark mode, and a user who isn't the founder (small account, another niche, another language).
7. **What does it cost?** For anything touching AI calls, state the per-use cost change before building; prefer changes that cut repeated AI work.
8. **One moment that earns delight.** A single crafted transition where something real happens (the draft fading into its slot, a queue row turning into its posting time). Craft, not decoration.
9. **What's next?** After the main result, the next step is one click (Schedule, Open, Undo), and every message says what happens now.

Call these out in the plan or artifact ("Details covered: …") so the user can see they were considered.

Everything here is backed by research done on 2026-10-25 (sources at the end). Don't redo that research for routine work; do targeted research only for a genuinely new kind of surface, and add what you learn to this file.

## 1. Honesty over theatre

- Never fake progress: no invented percentages, no bars that crawl to 99%, no artificial delays, no step checklists narrating internal work ("Fetching… Analyzing… Almost there"). Showing work only helps when the work is real and the result is good (Buell & Norton); otherwise it backfires.
- The real fix for a slow wait is usually engineering: start the work earlier (on connect, on submit), stream partial results, cache, precompute. Ask "can this be instant?" before designing a wait.
- Absent ≠ zero. Never show 0 for data that doesn't exist (a platform without views, a post not read yet). Use "—", leave the tile out, or say why in one line.

## 2. Response-time rules (NN/g)

| Wait | What to show |
|---|---|
| < 200ms | Nothing. No spinner, no skeleton (flicker reads as broken). |
| 200ms – 2s | Keep the previous content; dim it (~60% opacity) after ~200ms and keep the dim at least ~400ms once shown (Vercel: show-delay + minimum visible time, no flicker). Pending state on the control that triggered it. Never blank the page. |
| 2 – 10s | Layout-shaped placeholder (static, no shimmer) + one specific status line ("Reading @handle's last 30 days on X…"). |
| > 10s | Same line gains an honest expectation and lets them go: "This can take a minute. You can leave; it'll be here when you're back." The work must continue server-side. |
| Minutes / queued / rate-limited | Say so with a time if known ("X is limiting requests. Resuming around 14:32."). Notify quietly when done (sidebar dot), not with a modal. |

## 3. First run / import (the "just connected" moment)

Never a waiting screen (Duolingo: showing "Session Complete" at once while the upload ran in the background cut perceived latency 60%+ and raised DAU). Render the real page immediately; what hasn't arrived is an empty slot inside the real layout, not a separate loading screen. The rest of the app stays usable; no dead ends.

1. Start the job the moment the user connects (queue it from the connect endpoint; a page-load fallback re-requests it idempotently). Never make a first-time user wait for a cron.
2. Show the user's own identity immediately (avatar, @handle from OAuth).
3. One status line that changes only on real events: reading → "Found 42 posts. Adding up views…" → gone. At most three states.
4. Fill in real results as they land (poll every ~2s while importing, capped). Placeholders keep the final layout so nothing jumps.
5. When numbers arrive they simply land. No count-ups, confetti or reveal animation (Duolingo saves celebration for real milestones; Superhuman keeps animation minimal). The first view must read well for small or weak accounts too, without apologising.
6. Measure it: track "connected → first number seen" and recovery after errors, not raw latency (Duolingo tracked conversion through the wait, not milliseconds).
7. Return visits should show the last numbers instantly (persisted client cache) while fresh ones load.

## 4. Refresh / switching (range, filter, tab)

- Keep previous data on screen (`placeholderData: keepPreviousData`); dim after 300ms; cancel superseded requests. No skeletons, no spinners over content.
- Long-lived data: stale-while-revalidate. A failed background refresh keeps the old data plus a quiet inline note: "Couldn't refresh · showing numbers from 10:42 · Retry".

## 5. Errors

"Try again" alone is not an error state. In order:

1. Retry silently first (backoff + jitter, ~3 attempts; honor `Retry-After`). The user sees nothing.
2. If older data exists, keep it and add the quiet "Couldn't refresh · showing … from HH:MM" note.
3. Say whose fault and what to do, in one calm sentence, inline where the content was (never a modal):
   - Ours (5xx): "Analytics didn't load. This is on our end, and we've been notified." Only say "notified" when it's true: report it (Sentry, tagged with the same short error ID the server logged). Then: Try again · "Tell us what happened" (opens the in-app feedback form prefilled with the error ID, type Bug) · a copyable "Error ID abc123". The user asked for this pattern: we know, we're on it, and you can reach us.
   - Offline: "You're offline. This page loads when you're back." No button; refetch on `online`.
   - Expired token: one primary button that fixes it ("Reconnect X"). That is not homework; only the user can do it.
   - Third party down / rate-limited: no retry button (clicking won't help): "X hasn't answered since Oct 24. Postel keeps trying; numbers are from then."
   - Partial failure: show everything that loaded; flag only the failed part; label totals that exclude it ("X only").
4. Tone: calm, specific, no "Oops", no exclamation marks. "We" is fine when it's our fault and we're acting on it ("we've been notified"). One message per failure; never explain the same problem twice on a page.
5. Status and error notes are muted text where the content would be (Linear: "don't compete for attention you haven't earned"). Colour only when the user must act (reconnect). An indicator appears only when something is actually wrong, never by default.
6. Every error screen has a way out (Vercel: "no dead ends"); optimistic updates roll back or offer Undo on failure.

## 5b. Motion

Small, fast, purposeful; never decoration. Linear-level smoothness, not celebration.

- Animate only `transform` and `opacity` (no layout properties, never `transition: all`). 150–300ms, ease-out. Interruptible.
- Selection indicators move rather than jump (a single underline that slides to the picked tab).
- Data changes ease: chart bars scale (`scaleY`, origin bottom) to their new heights when switching metric; lines fade in.
- New content fades in once (`fade-in-0 animate-in duration-200`, the app's tailwindcss-animate utilities) when it first lands; refreshes don't re-animate, they only dim.
- Status text fades between states (key the element by its text).
- No count-ups, confetti, bouncing or staggered entrance choreography on routine screens; save celebration for real milestones.
- Every animation and transition has `motion-reduce:animate-none` / `motion-reduce:transition-none`.
- Verify motion with a mid-transition screenshot (~100ms after the trigger), not just the end state.

## 6. Empty states

- One calm line (plus one action only if the user must do something). Shaped like the content it becomes. No illustrations-with-paragraphs, no "Get started" checklists, no repeating "nothing here" three ways.
- If the app can fill it itself (widen a range, import, retry), it does, and doesn't ask.

## 7. Information design (dashboards, analytics, lists)

- Summary before detail; one chart, switched by the numbers above it, beats four charts.
- Every insight carries its evidence and a next step that does the work (opens Ask Postel prefilled, applies a change with Undo). No vanity metrics without an action.
- Say each number once. One caption for what changes compare to ("vs previous 30 days") instead of four phrasings.
- One compact number style everywhere ("8.7K"); full numbers where small differences matter (followers).
- Compare fairly: rank against each account's usual at the same age, not raw totals across platforms.
- Filters that scale: platform tabs (few) over per-account tabs (many); accounts go in a dropdown.

## 8. Copy

- Plain words the user recognizes; active voice; buttons say what happens ("Write a thread", "Reconnect X").
- No process narration, no internal names, no em-dash asides, no "not X but Y", no "Here's the thing". Follow `docs/copy-voice.md` in Postel (e.g. "Ask Postel", not "Jarvis"; "viral", not "breakout").
- Dates over relative time in lists ("Oct 23"); relative only for freshness ("Updated 12 min ago", "3 days ago").

## 9. Visual craft (Postel app shell)

- New shell tokens: shell `#f4f4f2`, panel white, ink primary buttons, violet (`brand`) only for counts, selection and focus; hairlines, not shadows; 13px UI text; `PageHeader` 44px bar with "Title / context" and actions on the right.
- One primary (ink) button per view; secondary actions outline. Touch targets ≥ 40px on phones.
- Charts: accent at ~60% with full on hover, labels that match the tiles, hairline tooltips, axis start/end dates.
- Phone: controls wrap to their own row; no clipped labels; tiles 2×2.
- New UI borrows its shapes from the surface it sits beside; it never invents its own. Before styling, grep the neighbouring components for radius, padding, gap and text size, and copy them. Postel's tiers are: main cards `rounded-[14px]`, card header strip `min-h-10 px-4 py-2 text-xs`, card body `px-4 sm:px-5 pt-4 pb-4`; secondary panels (e.g. "Why this post") `rounded-[10px] px-3.5 py-3 text-xs`, with a 13px medium heading; list rows `rounded-[7px] px-2.5 py-2`; stacked cards `gap-4`. A secondary thing must not look like a second main card. The brand guide's `rounded-lg` is outdated for the new shell.
- A placeholder or wait state that turns into a real card uses that card's exact shell, including controls that change its height (e.g. platform tabs, shown at rest with `inert`). Verify by measuring edges in screenshots of both states: same pixel, or it jumps.

## 10. The review loop (before showing any UI)

1. Build a temporary fixture route that renders every state from fixture data (never committed; a `TEMP-FIXTURE` proxy bypass line, removed before commit).
2. Screenshot every state, desktop and phone, with Playwright via installed Chrome (`channel: "chrome"`); dismiss the cookie banner and hide the Next dev badge.
3. Send the screenshots to an independent reviewer subagent with no builder context, role-playing an Apple/Linear principal designer: P0/P1/P2 per state with exact fixes and a 0–10 score. Fix and re-send to the same reviewer until no P0/P1 remain (target ≥ 8.5).
4. Only then show the user, with an artifact gallery of the final screenshots.

## Sources

- Duolingo, Android app performance (defer non-critical work, no blocking loaders, measure conversion): https://blog.duolingo.com/android-app-performance · streak milestones: https://blog.duolingo.com/streak-milestone-design-animation · Year in Review: https://blog.duolingo.com/year-in-review-behind-the-scenes
- Linear, design refresh ("structure should be felt not seen"): https://linear.app/now/behind-the-latest-design-refresh · sync engine: https://linear.app/now/scaling-the-linear-sync-engine
- Vercel Web Interface Guidelines (show-delay + min visible time, skeletons mirror content, no dead ends, errors guide the exit): https://vercel.com/design/guidelines
- Superhuman, built for speed (<100ms, prefetch, minimal animation): https://blog.superhuman.com/superhuman-is-built-for-speed/
- Figma multiplayer (reconnect reconciles automatically): https://www.figma.com/blog/how-figmas-multiplayer-technology-works/

- Buell & Norton, "The Labor Illusion" (Management Science, 2011): https://pubsonline.informs.org/doi/10.1287/mnsc.1110.1376 · HBS: https://www.hbs.edu/faculty/Pages/item.aspx?num=55804
- NN/g response-time limits: https://www.nngroup.com/videos/3-response-time-limits-interaction-design/ · progress indicators: https://www.nngroup.com/articles/progress-indicators/ · skeleton screens: https://nngroup.com/articles/skeleton-screens/ · error messages: https://www.nngroup.com/articles/error-message-guidelines/
- Viget on skeletons feeling slower: https://viget.com/articles/a-bone-to-pick-with-skeleton-screens
- Harrison et al., progress bar perception: https://www.chrisharrison.net/index.php/Research/ProgressBars
- Apple HIG progress indicators: https://developer.apple.com/design/human-interface-guidelines/progress-indicators
- Shopify Polaris error messages: https://polaris.shopify.com/patterns/error-messages
- Linear offline mode: https://linear.app/docs/offline-mode · Figma offline: https://help.figma.com/hc/en-us/articles/360040328553
- React transitions: https://react.dev/reference/react/useTransition · TanStack placeholder data: https://tanstack.com/query/v5/docs/framework/react/guides/placeholder-query-data
- Stripe error handling: https://docs.stripe.com/error-low-level · Vercel error IDs: https://vercel.com/changelog/vercel-now-supports-customizing-platform-error-pages
- Mobbin reference screens (2026-10-25): import waits (WorkOS "It should take less than a minute" = good; Monarch step checklist over a blurred dashboard = what to avoid), analytics (TikTok Studio switching tiles, X content table, Reddit/Nextdoor first-48h curves; Hootsuite/HubSpot "N/A"/0 = what to avoid).
