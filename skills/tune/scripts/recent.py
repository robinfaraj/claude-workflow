#!/usr/bin/env python3
"""Summarise recent Claude Code prompts across every local account, for /tune."""
import argparse, collections, datetime, glob, json, os, re

CMDS = ["bar", "explore", "peak", "night", "wrap", "ship", "handoff", "audit", "tune"]
ap = argparse.ArgumentParser()
ap.add_argument("--days", type=int, default=14)
args = ap.parse_args()
cut = (datetime.datetime.now() - datetime.timedelta(days=args.days)).timestamp() * 1000

rows = []
for f in glob.glob(os.path.expanduser("~/.claude*/history.jsonl")):
    acct = f.split("/")[-2]
    for line in open(f, errors="ignore"):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if r.get("timestamp", 0) >= cut:
            rows.append((r["timestamp"], acct, r.get("sessionId"), os.path.basename(r.get("project", "")), r.get("display", "").strip()))
rows.sort()
print(f"{len(rows)} prompts in the last {args.days} days\n")

used = collections.Counter()
after = collections.defaultdict(list)
by_session = collections.defaultdict(list)
for r in rows:
    by_session[r[2]].append(r)
for sess, rs in by_session.items():
    for i, r in enumerate(rs):
        m = re.match(r"/(?:[\w-]+:)?(\w+)", r[4])
        if m and m.group(1) in CMDS:
            used[m.group(1)] += 1
            for nxt in rs[i + 1 : i + 4]:
                if not nxt[4].startswith("/"):
                    after[m.group(1)].append((sess, nxt[3], nxt[4][:300].replace("\n", " ")))

print("## Command use")
for c in CMDS:
    print(f"  /{c}: {used[c]}")
print("\n## Typed right after a command (what it may have missed)")
for c, items in after.items():
    print(f"\n/{c}")
    for sess, proj, text in items[:25]:
        print(f"  - [{proj} {str(sess)[:8]}] {text}")

texts = [r[4] for r in rows if not r[4].startswith(("/", "!"))]
grams = collections.Counter()
for t in texts:
    w = re.findall(r"[a-zäöüß']+", t.lower())
    seen = set()
    for n in (4, 5):
        for i in range(len(w) - n + 1):
            g = " ".join(w[i : i + n])
            if g not in seen:
                seen.add(g)
                grams[g] += 1
print("\n## Repeated phrases (5+ prompts)")
for g, n in grams.most_common(60):
    if n >= 5:
        print(f"  {n:4d}  {g}")

short = collections.Counter(t.lower() for t in texts if len(t) < 40)
print("\n## Repeated short prompts (3+)")
for t, n in short.most_common(40):
    if n >= 3:
        print(f"  {n:4d}  {t}")

corr = [r for r in rows if re.match(r"(no[ ,.!]|nope|wrong|why (did|do|are|is)|i (said|told)|still|that'?s not|stop|dont |don't )", r[4].lower())]
print(f"\n## Corrections: {len(corr)} (latest 30)")
for r in corr[-30:]:
    print(f"  - [{r[3]} {str(r[2])[:8]}] {r[4][:220]!r}")
