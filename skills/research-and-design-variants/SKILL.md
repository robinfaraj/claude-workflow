---
name: research-and-design-variants
description: Research a feature or screen and present design variants in an artifact before anything is built. Use when the user types /research-and-design-variants, or asks to "research how others do this", "use Mobbin", "give me variants", "create a design exploration", "show me options as an artifact", or to settle a design direction or theme.
---

# Explore before building

Subject: $ARGUMENTS

Do not write product code in this step. The output is one artifact the user can react to.

1. **What we have.** Read the current implementation and how it looks today (run it, screenshot it). State what is wrong with it in a few bullets, using the user's own complaints where they gave them.
2. **What users do.** If the project has analytics or support data you can reach, check how the current thing is used. Say so if you cannot.
3. **How the best do it.** Find 5 to 8 strong references: direct competitors and the best products next to the space. Use Mobbin (`search_screens`, `search_flows`, `search_sections`) when connected, and web search. Mobbin credits are limited, so search with intent, not broadly. Note what is table stakes and what is distinctive. Keep the links and screens.
4. **Principles that apply.** Jakob's law decides the structure: say which familiar pattern each variant follows and which products use it. Then name the few other laws that matter here (Hick, Fitts, Tesler, peak-end; list in `/review-until-polished`), each tied to a concrete choice. Do not list laws for show.
5. **Variants.** Build 3 real variants, not three colours of one idea. Each is rendered at true size in the artifact, in the project's design language, with real content, not lorem ipsum. Mobile and desktop where both exist.
6. **Recommendation.** Say which you would ship and why, what you would take from the others, and what it costs to build.

Publish the artifact, give the link, and stop for the user's pick. If they said they are away or asleep, pick your recommendation and continue with `/apply-quality-bar`.
