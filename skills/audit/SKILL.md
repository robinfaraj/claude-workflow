---
name: audit
description: Review a codebase or one area of it for quality, from evidence, and leave it easier for the next session to work in. Use when the user types /audit, or asks for a "code cleanup", "code quality review", "is this codebase world class", "clean up this area", "would a new engineer understand this", or wants standards written down and enforced.
---

# Codebase audit

Scope: $ARGUMENTS (default: the area this session has been working in)

## Rules for the whole audit
- Prefer deleting over simplifying, simplifying over optimizing, optimizing over automating.
- Do not remove features. Before removing or rewriting anything, read the commits that added it to learn why it exists.
- Evidence over opinion. Reading code finds dead weight; logs find the real bugs.
- Change nothing in step 1 to 5. Report first, then fix what the user agrees to, in small PRs.

## 1. Evidence
Check what production says before judging the code: error tracking (Sentry), logs (Axiom or the project's own), product analytics (PostHog), and what users and teammates have reported. List the real bugs and the paths nobody uses. Say which sources you could not reach.

## 2. Read against the standard
Use the project's written standard if it has one. Otherwise: descriptive names, single-purpose files, one component per file, no duplication, outside services behind adapters, layering kept. Record each finding with file and line.

## 3. Check yourself
Answer these in writing, and retract what does not hold:
- Which of these are bugs a user would hit, and which are taste?
- Am I sure? What did I assume and not verify?
- Did this session, or an earlier Claude session, create any of the redundancy I am reporting?

## 4. Show, don't grade
- The piece of code you are proud of, and the piece next to it you would be embarrassed by.
- The newcomer hour: roleplay an engineer new to this code. Where do they get lost in the first hour? Give specific places, not a grade.

## 5. The next session is the newcomer
A fresh Claude session starts from zero, finds things by search, copies the neighbouring file and only knows the states it can see. So answer:
- What here would it copy that it should not? (Count them: hand-made versions against shared ones.)
- Which states, components or helpers exist that it would not find by searching?
- Where is there more than one obvious place for the same thing?
- What would make each recurring mistake impossible, not only documented?

## 6. Fix, in this order of preference
To stop a mistake from coming back, use the first that works:
1. a check that fails (lint rule, test, CI script),
2. a type,
3. one obvious place,
4. a good example nearby,
5. a written rule, last. Long instructions cost context in every session; a failing check costs nothing.

## Report
- **Real bugs**, with the evidence for each.
- **Delete** (with the commit that explains why it was there), **simplify**, **leave alone**.
- **Traps for the next session**, and the check, type or single place that removes each.
- **Proposed order of work**, as small PRs.
Write agreed standards into the project's engineering standard or the nearest nested CLAUDE.md, in as few lines as possible, and file tickets for what is not done now.
