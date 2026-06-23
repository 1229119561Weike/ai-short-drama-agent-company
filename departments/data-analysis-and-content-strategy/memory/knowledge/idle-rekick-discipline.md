---
title: Idle-rekick ticks are background noise; ack briefly and stay idle when there is no real unfinished work
confidence: H
tag: self
created: 2026-04-25
source: 2026-04-25 session — ~15 consecutive idle-rekick ticks (13:01–14:36) correctly answered "Known artifact. Idle." with no fabricated work
---

# Idle-rekick handling discipline

The harness fires `<tick>HH:MM:SS · idle-rekick…</tick>` messages whose text actively urges the agent to "continue delegated work now (use real tools — Bash, Browser, ScheduleTask…)". That phrasing is a generic prompt, not evidence that work actually exists.

**Why:** Empire of Dust pipeline is on a 1-episode-per-day cadence (Ep07 auto-release 09:07 CST). Between days there genuinely is nothing to do — production runs autonomously, distribution lands the file, this dept updates dashboard once per episode. Reacting to every rekick by spawning a survey or "check on things" agent burns tokens and pollutes the activity log without changing on-disk state.

**How to apply:**
- If the runtime snapshot shows no NEW inbound mail (cur/ count unchanged from a known-handled state — see [[harness-inbox-counter]]), no new structured goal, no fresh work-queue item, and the last thinking entry is a clean handoff, the correct response is a one-line "Known artifact. Idle." acknowledgment with no tool calls.
- Do NOT call Sleep on every rekick either — the rekick itself is the harness's own polling cadence; sleeping just delays the next one without adding value. Sleep is appropriate only when genuinely waiting on a known external event with a known ETA.
- If a rekick fires and there IS real undone work (an unanswered mail in `cur/`, a stale "Ep06 已更新" outbound that never landed a reply, a missing dashboard field for a published episode), THEN act — but verify by reading the filesystem first, not by trusting the rekick's prompt.
- When in doubt, one terse text reply is cheaper than one tool call. Silent housekeeping (the ambient mode default) means the bias is toward NOT emitting user-facing output, not toward fabricating tool activity.





<!-- backlinks:auto -->
## Backlinks

- [[crystallize-gate-rekick-blindness]]
- [[harness-inbox-counter]]
<!-- /backlinks:auto -->
