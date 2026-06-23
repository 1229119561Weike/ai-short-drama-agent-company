---
title: Crystallize activity gate counts idle-rekick ticks as user messages, so empty rounds keep firing during idle clusters
confidence: H
tag: knowledge
created: 2026-04-26
source: 2026-04-25 → 2026-04-26 — 5th consecutive crystallize round triggered by idle-rekick clusters with gate scores 40–60 ("23 user msgs since 4.0h ago (score=46)" this round); commit log entries 7506893 / 633afb3 / f1a91eb / 7a62a5e all reflect the same empty-round outcome
---

# Crystallize gate is blind to idle-rekick ticks

The MaintenanceScheduler activity gate that decides whether to spawn a crystallize subprocess counts every harness-injected `<tick>HH:MM:SS · idle-rekick…</tick>` message as a user message. During an idle cluster (typical: 10–25 ticks at ~10-min spacing over a 4-hour window), the gate score easily exceeds the run threshold even though zero genuinely user-driven activity occurred.

**Why:** the gate's input is the raw user-channel message count from the canonical session — it has no allow-list / source-tag filter for harness-generated ticks. Only a settings.json hook (or a gate-side filter change) can fix this; it cannot be fixed from inside crystallize itself. Memory cards do not change scheduler behavior.

**How to apply:**
- Detect this pattern fast in §1 Survey: if the session excerpt is dominated by `<tick>…idle-rekick…</tick>` lines each followed by a one-line agent ack ("Known artifact. Idle." or equivalent per [[idle-rekick-discipline]]), and `thinking.jsonl` has no new entries since the last snapshot, this is the gate-blindness pattern.
- Proceed normally through §1 / §1.5: confirm no new view is forming, no aging aspires need decay, no orphaned wikilinks. Expect both to come up empty.
- Skip §2 (no new cards), skip §2.5d (no scratchpad pruning during active monitoring), skip §4 entirely (idle-rekicks carry zero personal-context observations).
- Run §3 only if a card was actually touched this round; otherwise the index is already current.
- Always run §5 with `--allow-empty` and `CARDS_TOUCHED=0`. The snapshot commit message should briefly note the pattern (e.g. "idle-rekick Nth recurrence — gate blindness, no work") so the next round can see at a glance that this is a known, expected empty round.
- Do **not** invent decoy cards or rewrite existing ones to make the round "feel productive" — empty rounds are auditable and legitimate per the workflow doc.
