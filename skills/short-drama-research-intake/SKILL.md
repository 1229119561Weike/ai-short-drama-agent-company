---
name: short-drama-research-intake
description: Convert stored short-drama research signals into safe creative fuel for the short-drama meta system, production, packaging, or analytics. Use when the user asks to use research assets, turn research into creative input, prepare fuel from short-drama-research, or prevent research contamination.
category: analysis
symbolName: doc.text.magnifyingglass
seedVersion: 1
---

# Short Drama Research Intake

Use this skill to transform structured research assets into safe, consumer-specific creative fuel. It is the firewall between research and creation.

The goal is not to summarize everything in the research database. The goal is to choose relevant signals, remove source-specific contamination, keep copy-risk visible, and produce a small fuel packet that another skill or department can use without accidentally copying a real work.

## Default paths

Use the workspace root from `NEO_WORKSPACE_ROOT` when available. Otherwise use the current workspace root.

Research database root:

`$NEO_WORKSPACE_ROOT/storage/files/short-drama-research`

Primary inputs:

- `signals/*.jsonl`
- `hooks/hook-bank.jsonl`
- `formats/narrative-formats.jsonl`
- `case-studies/*.md`
- `do-not-copy/*.jsonl`
- `taxonomies/*.json`

Primary outputs:

- `fuel/for-meta-os/*.json`
- `fuel/for-production/*.json`
- `fuel/for-packaging/*.json`
- `fuel/for-analytics/*.json`

Do not read `raw/` by default. Raw evidence is for audit and validation, not direct creative generation. Read `raw/` only when the user explicitly asks for evidence inspection or validation.

## Trigger situations

Invoke this skill when the user asks to:

- use short-drama research in a new story project
- convert research signals into creative fuel
- prepare inputs for the short-drama meta skill
- help production use research without copying
- package research into hooks, formats, or analytics hypotheses
- check whether research assets are safe to use

Do not invoke it for live web research. That belongs to the research department/browser workflow. This skill consumes stored assets.

## Consumer targets

Pick one target before writing output.

### `meta-os`

For concept and script development.

Output:

- usable hooks
- episode engines
- relationship dynamics
- social emotions
- season escalation suggestions
- explicit copy boundaries
- verification warnings

### `production`

For video generation and post-production planning.

Output:

- visual texture directions
- production-safe setting constraints
- consistency implications
- what not to imitate from source material

### `packaging`

For title, cover, description, comment-bait, and platform promise.

Output:

- title angles
- cover text patterns
- first-frame promise
- comment divide
- expectation/payoff warnings

### `analytics`

For data review and experiment tracking.

Output:

- signal IDs used
- hypotheses to test
- expected metrics movement
- review windows
- keep / expand / pause / test-next framing

## Selection rules

1. Filter by user request: platform, region, genre, target, tone, format, or project.
2. Prefer `verified` and `partially_verified` signals.
3. Allow `unverified` only if the output labels them as `creative_hypothesis`.
4. Always load matching `do-not-copy` notes when using a signal group.
5. Use mechanisms, audience tensions, and structural patterns. Do not reuse protected names, scenes, dialogue, shot sequences, or source-specific visual signatures.
6. Keep the packet small. A useful fuel packet is usually 3-7 mechanisms, not a giant dump.

## Output format

Write concise Markdown for user review. If asked to persist, also write JSON under the relevant `fuel/` directory.

```markdown
## Research Fuel Packet

- target:
- request:
- source boundary:
- verification level:

### Selected Signals

1. signal_id:
   - why selected:
   - safe mechanism:
   - copy-risk boundary:

### Creative Fuel

- hooks:
- episode engines:
- character dynamics:
- social emotions:
- visual/production texture:
- packaging angles:

### Do Not Copy

- ...

### Recommended Next Use

- for meta-os:
- for production:
- for packaging:
- for analytics:
```

## JSON fuel shape

When persisting, use:

```json
{
  "fuel_id": "YYYY-MM-DD-target-slug",
  "created_at": "YYYY-MM-DD",
  "target": "meta-os | production | packaging | analytics",
  "request": {
    "platform": "",
    "region": "",
    "genre": "",
    "theme": ""
  },
  "source_signal_ids": [],
  "verification_level": "creative_hypothesis | partially_verified | verified",
  "copy_safety": {
    "copy_risk": "low | medium | high",
    "do_not_copy": [],
    "allowed_use": []
  },
  "usable_mechanisms": [],
  "not_for_use": [],
  "recommended_next_step": ""
}
```

## Contamination checks

Before returning output, check:

- Does any line include a real source's exact dialogue, unique character, unique institution, or signature twist? If yes, remove or abstract it.
- Does the packet imply unverified data is true platform performance? If yes, relabel as hypothesis.
- Is the target clear? If not, ask the user to choose meta-os, production, packaging, or analytics.
- Could a downstream writing skill accidentally treat raw research as script? If yes, add a stronger `Do Not Copy` section.

## Example

User: “Use the YouTube North America sci-fi research for meta-os.”

Expected fuel:

- target: `meta-os`
- verification level: `creative_hypothesis`
- selected signals: AI family replacement, disaster credit score, alien identity audit
- safe mechanisms: intimate tech replacement, public resource denial, civic identity audit
- do not copy: existing AI companion franchises, dystopian scoring systems, alien-refugee IP
- next use: develop an original 20-episode near-future community sci-fi project
