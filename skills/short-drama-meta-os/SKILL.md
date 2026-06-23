---
name: short-drama-meta-os
description: Develop any user theme into an original blockbuster short-drama project package with a 20-episode season, 4x15s beat structure, Seedance 2.0 prompt-folder plan, and social distribution CSV draft. Use when the user asks to create a new short drama, 爆款短剧, 元skill output, 20集短剧, Seedance prompts from a theme, or a new project with Empire-of-Dust-compatible file structure.
category: development
symbolName: sparkles.tv
seedVersion: 2
---

# Short Drama Meta OS

Use this skill to turn a user theme into a production-ready short-drama project package. It is a creative development skill, not a production or publishing skill.

It should create the same kind of structured production assets that made Empire of Dust operational: 20 episodes, each about 1 minute, each divided into four 15-second beats, with Seedance 2.0 prompt files and social publishing metadata. Empire of Dust is only a reference for folder shape, CSV schema, beat duration, and production handoff discipline; never use it as a reference for creative voice, title grammar, prompt vocabulary, story motifs, tag style, or social-copy cadence. This skill does not generate videos, upload to YouTube, or update dashboards.

## Boundaries

Use this skill for project development:

- theme to season bible
- theme to 20-episode ladder
- episode cards
- 4 x 15s beat sheets
- Seedance 2.0 prompt-folder content
- publishing CSV draft
- greenlight scorecard
- consistency locks

Do not use this skill for:

- Matrix/Seedance video generation
- subtitle burn-in
- final MP4 assembly
- YouTube upload
- playlist selection
- dashboard updates
- live platform research

Those belong to production, distribution, analytics, and research workflows.

## Inputs

Minimum input:

- user theme

Optional inputs:

- platform
- region
- language
- target audience
- tone: serious, manhua, satirical comedy, 3D animation, battle, blockbuster spectacle
- research fuel path from `storage/files/short-drama-research/fuel/for-meta-os/`
- constraints: non-human characters, media-generation reference image needs, budget look, cultural setting

If the user gives only a theme, choose sensible defaults and proceed with a test package. Do not over-question.

## Creative distance from reference projects

Use reference projects as operational templates, not creative sources.

When a user asks for an Empire-compatible or Empire-style output, interpret that as:

- same folder/file organization
- same CSV column schema
- same 20 episodes x 4 beats x 15 seconds production unit
- same level of production readiness and consistency control

Do not copy or drift toward Empire of Dust's creative identity:

- no default Empire title grammar such as repeated `She/They + dramatic verb + cosmic object | Series Ep N`
- no default `Then...` second-line description cadence across rows
- no default Empire tag pack, hashtag pack, thumbnail rhythm, imperial/cosmic/rewrite/throne vocabulary, or solemn sci-fi-fantasy trailer voice
- no default `premium cinematic` phrasing unless the new project's genre bible specifically chooses that register
- no transplanting character archetypes, visual motifs, rule systems, or cliffhanger syntax from a reference project

Before writing package artifacts, create a project-specific voice bible:

- `title_syntax_palette`: 4-6 title forms that fit this project and are not copied from the reference
- `social_copy_voice`: how descriptions should sound for this platform and audience
- `tag_voice`: niche, genre, emotional, culture, and format terms unique to this project
- `prompt_vocabulary_palette`: visual adjectives, camera verbs, pacing words, environment words, and negative-prompt risks derived from the new genre
- `visual_grammar`: recurring shapes, color logic, prop logic, movement logic, and shot rhythm
- `forbidden_reference_habits`: phrases and structures to avoid because they resemble the reference too much

Run a style divergence pass before writing files. If more than a few rows or prompts could be mistaken for the reference project with names swapped, rewrite them before output.

## Production density parity

Creative distance must never reduce production usefulness. When transforming away from a reference project's voice, preserve or increase the density of operational detail:

- keep the same number of beats, rows, fields, locks, prompts, and handoff artifacts requested by the user
- keep each Seedance prompt production-ready, not merely illustrative
- include enough character, environment, action, camera, dialogue, continuity, and avoid-list detail for downstream generation
- replace reference-project vocabulary with project-native vocabulary; do not delete detail to avoid resemblance
- if a reference prompt is long and operationally specific, the new prompt should be comparably specific in its own genre language
- if shortening is necessary for a platform or model limit, state the constraint explicitly and preserve the highest-impact production controls

## Research fuel use

Read only safe transformed fuel from:

`storage/files/short-drama-research/fuel/for-meta-os/`

Also read copy-risk notes from:

`storage/files/short-drama-research/do-not-copy/`

Do not read `storage/files/short-drama-research/raw/` unless the user explicitly asks to inspect raw evidence.

When using unverified fuel, label it as `creative_hypothesis`, not market fact.

## Creative principles

Write for high-retention short drama:

- First 1-2 seconds must show a legible abnormal event, social pain, danger, or impossible image.
- Every episode serves one main viewer question.
- Every 15-second beat should advance plot, shift emotion, and create the next question.
- Every episode ends with an irreversible action or a concrete new threat, not a vague mood.
- Dialogue should create action, pressure, status reversal, or a quotable comment trigger.
- Worldbuilding must be visible as consequences: who loses power, who gets hurt, what machine/rule responds.
- Fuse novelty with classic human themes: desire, shame, betrayal, love, survival, justice, identity, sacrifice, power.
- Use local culture and social emotions as texture, not stereotypes.

## Genre strengths

Support these modes explicitly:

- manhua drama: bold visual symbols, power reversal, high-status humiliation, cliff-heavy pacing
- satirical comedy / brain-off drama: clear absurd premise, fast reversal, joke with social bite, low cognitive load
- 3D animation: strong silhouettes, simple readable action, recurring visual motifs, character-card compatibility
- battle drama: visible stakes, power rules, rank reversal, tactical surprise every beat
- industrial blockbuster: compressed scale through iconic locations, huge stakes, premium visual language, but still short-form legibility

## V0.1 test mode

In v0.1, do not immediately create all 20 full prompt folders unless the user explicitly asks. For testability, produce:

1. Full season architecture for 20 episodes
2. Complete episode cards for all 20 episodes
3. Complete 4-beat prompt-file content for episodes 1-2 only
4. CSV rows for episodes 1-2 only
5. Greenlight scorecard for the concept and first two episodes
6. Ask the user to confirm or revise before expanding to all 20 episodes

This keeps the iteration tight and prevents generating a large wrong package.

## Output structure

Use this structure for v0.1 test output:

```markdown
## Short Drama Project Package v0.1

### Source Boundary
- theme:
- research fuel used:
- verification level:
- copy-safety note:

### Market Thesis
- region:
- platform:
- audience:
- emotional promise:

### Series North Star
- working title:
- one-line hook:
- primal desire:
- shame trigger:
- power fantasy:
- key dramatic question:
- moral engine:

### Voice And Divergence Bible
- reference format used:
- reference elements allowed:
- reference elements forbidden:
- title_syntax_palette:
- social_copy_voice:
- tag_voice:
- prompt_vocabulary_palette:
- visual_grammar:
- style_divergence_pass:

### Consistency Bible
- world rule:
- protagonist lock:
- antagonist / pressure system:
- relationship web:
- visual identity:
- recurring props:
- do-not-copy boundaries:

### 20-Episode Season Ladder
| Ep | Title | Main Viewer Question | Irreversible Action | Next Pressure |
|---|---|---|---|---|

### Episode 1 Full 4-Beat Sheet
- Beat 1 (0-15s):
- Beat 2 (15-30s):
- Beat 3 (30-45s):
- Beat 4 (45-60s):

### Episode 2 Full 4-Beat Sheet
...

### Seedance 2.0 Prompt Folder Plan
- project root:
- episode folder naming:
- prompt file naming:

### Episode 1 Prompt Files
#### Beat1 Seedance 2.0 Prompts.md
...

### Episode 2 Prompt Files
...

### Publishing CSV Draft Rows
```csv
episode,title,description_line_1,description_line_2,description_line_3,tags,hashtags,thumbnail_text
```

### Greenlight Scorecard
- hook_clarity:
- primal_desire_strength:
- conflict_visibility:
- relational_legibility:
- world_legibility:
- irreversible_action_strength:
- dialogue_cuttability:
- quoteability:
- cliff_strength:
- visual_identity_strength:
- originality_of_premise:
- format_distance_from_reference:
- voice_distinctiveness:
- research_fuel_transformation:
- production_feasibility:
- titleability:
- comment_bait:

### What To Test With User
- tone:
- hook strength:
- cultural fit:
- prompt format:
- CSV packaging:
```

## Style divergence gates

A package cannot pass greenlight if any of these are below 7:

- `hook_clarity`
- `conflict_visibility`
- `relational_legibility`
- `cliff_strength`
- `originality_of_premise`
- `format_distance_from_reference`
- `voice_distinctiveness`

If `format_distance_from_reference` is low, keep the operational schema but rewrite titles, descriptions, tags, prompt vocabulary, scene-title syntax, and thumbnail language until the project reads like its own franchise.

## Seedance prompt rules

Each beat prompt should be ready to save as a standalone file and feed to Seedance 2.0 later.

Include:

- scene title
- duration: 15s
- aspect ratio: 9:16
- visual style
- character locks
- setting locks
- beat action
- camera direction
- dialogue / subtitle text if needed
- continuity notes
- negative prompt / avoid list

Do not include instructions to generate all beats in one prompt. Each beat is an independent unit.

## Publishing CSV rules

For each episode row include:

- episode
- title
- description_line_1
- description_line_2
- description_line_3
- tags
- hashtags
- thumbnail_text

Description line 3 should be project-specific by default. It may include a brief channel subscription line, but its wording must match the new project's audience, tone, and language rather than reusing a reference project's boilerplate.

Before finalizing CSV rows:

- vary title syntax using the project's `title_syntax_palette`
- avoid repeating the same description-line rhythm across most rows
- write tags from this project's genre, emotion, culture, platform niche, and visual promise
- write hashtags as discovery handles for this project, not a generic reference pack
- make thumbnail text feel like the new show's native hook language
- reject rows that could fit the reference project after only swapping names

## Non-human character reference images

If the theme uses non-human, stylized, creature, robot, alien, animal, or mascot leads, include a `Reference Image Need` section.

State whether media-generation should create:

- protagonist character card
- antagonist / pressure-system card
- recurring side character cards
- props / vehicle / environment cards

Do not call media-generation from this skill unless the user explicitly asks to generate images now. This skill only specifies what should be generated.

## Handoff after approval

After the user approves the v0.1 package, the next stage may:

- expand episodes 3-20 into full prompt files
- write project files under `storage/files/<project-slug>/`
- hand production to a production pipeline skill/department
- hand packaging to distribution
- hand hypotheses to analytics

Do not skip user approval between v0.1 test and full package expansion.
