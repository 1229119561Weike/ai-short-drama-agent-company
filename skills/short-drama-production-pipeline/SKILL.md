---
name: short-drama-production-pipeline
description: Turn an approved short-drama-meta-os project package into production execution: validate Seedance 2.0 beat prompts, prepare reference-image needs, coordinate video generation handoff, assembly, subtitles, QA, and distribution handoff. Use when the user asks to produce a short drama episode/season from meta-os outputs, start production, generate beat videos, assemble final MP4s, QA prompts/assets, or hand completed short-drama assets to publishing.
category: automation
symbolName: film.stack
seedVersion: 1
---

# Short Drama Production Pipeline

Use this skill after a short-drama concept package has been approved and the user wants to move from development into production execution.

This skill consumes outputs from `short-drama-meta-os`; it does not create the story from scratch. It preserves the project's own creative voice and visual grammar while applying the operational discipline proven by previous short-video pipelines: per-beat prompts, consistent assets, generated clips, assembled vertical MP4, subtitles, QA, and handoff to distribution.

## Trigger situations

Invoke this skill when the user asks to:

- start producing a short drama from a `short-drama-meta-os` package
- produce episode 1, episode N, or a full season
- generate Seedance 2.0 beat videos from existing prompt files
- prepare character/reference image needs for production
- assemble beat clips into final vertical MP4s
- add subtitles or QA completed videos
- hand completed short-drama assets to publishing/distribution
- continue production after the meta package is approved

Do not invoke this skill for theme ideation, season writing, research intake, live platform research, YouTube upload, or dashboard updates.

## Ownership boundaries

### This skill owns

- production readiness checks for approved project packages
- prompt folder validation
- reference-image requirement extraction
- per-beat video generation handoff planning
- generated-clip tracking
- final episode assembly planning
- subtitle and audio-transcript expectations
- production QA checklist
- handoff packet for distribution and analytics

### This skill does not own

- source research collection: research department / browser workflow
- research-to-fuel transformation: `short-drama-research-intake`
- story concept, 20-episode ladder, prompt writing from theme: `short-drama-meta-os`
- actual media generation tool invocation unless the user explicitly asks to generate now; use `media-generation` for that step
- YouTube Studio upload, playlist selection, or publishing: distribution workflow
- performance dashboard updates: analytics/dashboard workflow

## Input contract

Required inputs:

- approved project package path, or a clear project root
- target scope: one beat, one episode, multiple episodes, or season
- prompt files for each target beat, normally `Beat1 Seedance 2.0 Prompts.md` through `Beat4 Seedance 2.0 Prompts.md`

Optional inputs:

- reference image cards or explicit `Reference Image Need` section
- production fuel from `storage/files/short-drama-research/fuel/for-production/`
- platform requirement: YouTube Shorts, TikTok, Douyin, Bilibili
- language/subtitle requirement
- target resolution and codec constraints

If target scope is missing, default to the next unproduced approved episode. If approval status is unclear, stop and ask for user confirmation before generating media.

## Production density and creative distance

Production execution must preserve the creative identity defined by the project package:

- use the project's `Voice And Divergence Bible`, not a reference project's voice
- keep project-native prompt vocabulary, visual grammar, title syntax, and social-copy logic
- treat Empire of Dust or other prior projects as operational references only: folder shape, 4-beat discipline, QA rigor, final-video expectations
- do not rewrite prompts into another franchise's language while preparing them for generation
- do not reduce prompt density while avoiding imitation; replace vocabulary, not detail

## Phase 1: Intake and readiness check

Read the approved package and target episode folder.

Check:

- target episode folder exists
- exactly four beat prompt files exist for a one-minute episode
- each beat prompt includes duration, ratio, character locks, setting locks, action, camera/edit controls, dialogue/subtitles if needed, continuity notes, avoid list
- project voice bible or visual grammar exists
- output CSV row exists for the episode if distribution will follow
- reference image needs are documented for non-human, stylized, creature, robot, mascot, or high-consistency characters

If a beat prompt is short, missing locks, or too generic, return it to `short-drama-meta-os` for prompt expansion instead of generating.

## Phase 2: Reference image planning

If the project needs reference images, create a production reference checklist before video generation.

Typical items:

- protagonist full-body character card
- antagonist / pressure-system card
- recurring side character card
- key prop card
- environment card
- outfit/pose variants when continuity matters

For each item, record:

- asset id
- purpose
- prompt source
- whether it is required before generation or optional later
- file path once created

If the user asks to generate images now, invoke `media-generation`; otherwise only prepare the checklist.

## Phase 3: Beat video generation handoff

For each beat:

- confirm model target: `Seedance 2.0`
- confirm duration: `15s`
- confirm aspect ratio: `9:16`
- confirm per-beat prompt is standalone
- attach required reference images when available
- preserve negative prompts and continuity locks
- record generation status: `pending`, `generated`, `failed`, `needs_retry`, `approved`

When actually generating media, use `media-generation` and save outputs under the project production folder. Do not silently proceed after failed generation; record the failure and retry only with a concrete adjustment.

Suggested tracking path:

```text
<project-root>/production/<Series Title>｜episode XX/
  Beat1 Seedance 2.0 Prompts.md
  Beat1 generated.mp4
  Beat1 generation-notes.md
  Beat2 Seedance 2.0 Prompts.md
  Beat2 generated.mp4
  ...
```

## Phase 4: Assembly and subtitles

After all four beat clips are approved:

- assemble in beat order: Beat1 -> Beat2 -> Beat3 -> Beat4
- target final format: vertical 1080x1920 MP4 unless user specifies otherwise
- maintain around 60 seconds total for a four-beat episode
- use actual audio/transcript for subtitles when audio exists
- burn subtitles only after transcript timing is checked
- save final as a clear episode file, e.g. `<Series Title> Episode 02 final.mp4`

Do not claim final assembly succeeded until the output file exists and basic media properties are checked.

## Phase 5: Production QA

Run QA before handoff.

Minimum QA checklist:

- final file exists
- resolution is vertical 1080x1920 or agreed target
- duration is close to expected episode length
- audio exists if expected
- subtitles are readable and not cut off
- beat order is correct
- no visible prompt leakage, watermarks, unrelated text, or wrong character identity
- continuity locks are respected across beats
- final frame supports the episode cliffhanger
- no obvious cultural-copy, source-copy, or reference-project imitation issue

If QA fails, classify the issue:

- prompt issue -> return to `short-drama-meta-os` for revision
- generation issue -> regenerate affected beat
- assembly issue -> reassemble
- subtitle issue -> regenerate transcript/subtitle burn
- story/package issue -> ask user before scope-changing rewrite

## Phase 6: Distribution handoff

When production QA passes, prepare a handoff packet for distribution.

Include:

- final MP4 path
- episode number
- series title
- publishing CSV path and row number
- exact title/description/tags/hashtags/thumbnail text from CSV
- subtitle language
- QA result
- any playlist/channel instructions supplied by user

Publishing itself is not this skill's job. Hand the packet to the distribution workflow or department.

## Phase 7: Analytics handoff

After publishing returns a valid result, analytics can use:

- episode number
- final title
- URL/video ID
- publish time
- package hypotheses from meta-os
- production notes affecting retention, e.g. hook, cliffhanger, visual consistency issues

Do not update dashboards before publishing returns a real URL/video ID and final title.

## Department collaboration

Use departments without duplicating their responsibilities:

- CEO Office: coordinates scope, approval gates, and blockers
- 短剧调研部门: gathers live research and stores evidence/signals
- `short-drama-research-intake`: converts stored signals into safe production fuel
- `short-drama-meta-os`: writes or revises story package and prompts
- 内容生产部门: executes media production and QA when department delegation is appropriate
- 内容分发部门: uploads/publishes after production QA
- 数据分析与内容策略部门: reviews performance after valid publish data exists

## Output formats

### Readiness report

```markdown
## Production Readiness Report
- project:
- target scope:
- approved package path:
- prompt folder:
- beat files found:
- missing or weak assets:
- reference image needs:
- ready for generation: yes/no
- blockers:
```

### Episode production tracker

```markdown
## Episode Production Tracker
| Beat | Prompt | Reference assets | Generation status | QA status | Notes |
|---|---|---|---|---|---|
```

### Distribution handoff packet

```markdown
## Distribution Handoff Packet
- series:
- episode:
- final mp4:
- duration:
- resolution:
- audio:
- subtitle status:
- CSV path:
- CSV row:
- title:
- description lines:
- tags:
- hashtags:
- thumbnail text:
- QA result:
```

## Done criteria

For readiness work, done means the user knows whether the target episode can enter generation and exactly what is missing.

For production work, done means each target episode has:

- four generated/approved beat clips
- assembled final vertical MP4
- subtitles if expected
- QA result
- distribution handoff packet

For handoff-only work, done means distribution has enough exact metadata and file paths to publish without rereading creative drafts.
