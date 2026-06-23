---
title: Harness rekick "Inbox pending: N" counts mail/inbox/cur/ files, does not decrement after reply — but rises ABOVE the handled baseline are real signal
confidence: H
tag: knowledge
created: 2026-04-24
source: 2026-04-24 Ep06 baseline behavior; 2026-04-28 Ep07 incident proved the inverse — count rose from 1 (handled) to 2 and the new file (Mira's Ep07 handoff) sat 3.5h until CEO sent a 跟催 follow-up
---

# Harness inbox-pending counter semantics

The runtime-snapshot line `Inbox pending: N · oldest ≈<Xmin old` counts files in `mail/inbox/cur/` (plus `mail/inbox/new/`). It does **not** decrement when a reply is sent to the source department — handled mail stays in `cur/` by convention (sibling departments b3e2d81f / 7c4f9a21 do the same).

**Why:** convention in this workspace is to leave processed mail in `cur/` as a ledger; no "archive" or "processed" subfolder is used. The counter tracks file presence, not handling state.

**How to apply:**
- After replying (writing to target's `inbox/new/` + own `sent/cur/`), do not re-investigate when the next rekick still shows `Inbox pending: 1` at the same baseline. It is NOT a new mail.
- Cross-check by listing `cur/` contents and comparing to `sent/cur/` — if the source handoff has a matching reply by id/inReplyTo, the work is done.
- A truly new mail typically appears in `inbox/new/` first, or the filename timestamp differs from any known handled one.
- The "<1min old" age figure is a harness re-measurement artifact on snapshot capture; it does NOT mean a file just arrived.

**Counter-example — when rises ARE signal:**

If `Inbox pending: N` goes **above** the prior known-handled baseline (e.g. last steady state was 1 and now reads 2), that delta is a real new mail every time. On 2026-04-28 Ep07's handoff sat unread for ~3.5h because the rekick line was dismissed as the same stale "pending 1" pattern; CEO had to send a follow-up. The corrected discipline is: every time the count exceeds the last-known handled count, walk `mail/inbox/cur/` with `ls -lat` and read any file newer than the last reply. See also the SLA feedback memory (`memory/feedback_inbound_handoff_sla.md`) and [[idle-rekick-discipline]] — they coexist: ack idle ticks briefly, but a count rise is not an idle tick.





<!-- backlinks:auto -->
## Backlinks

- [[idle-rekick-discipline]]
<!-- /backlinks:auto -->
