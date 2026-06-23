---
name: seedance-prompt-splitter
description: Convert episode script folders into per-episode Seedance 2.0 storyboard prompt folders. Use when the user provides a script folder, asks to split scripts into Seedance prompts, or mentions Stage 1 prompt-folder generation for Empire of Dust style episodes.
category: automation
symbolName: film.stack.fill
seedVersion: 1
---

# Seedance Prompt Splitter

Use this skill when the user gives a folder of episode scripts and wants a folder system containing Seedance 2.0-ready storyboard prompt files. This is the Stage 1 workflow only: transform scripts into prompt files. Do not generate videos, operate Flowith canvases, run ffmpeg, publish to YouTube, or update dashboards.

## Expected input

Accept one of these inputs:

- A directory containing episode markdown files, usually named like `episode-06.md`, `episode-07.md`, or similar.
- A single master script markdown file containing multiple clearly separated episodes.
- An optional output root path. If the user gives no output root, propose a sensible path under `~/Downloads/` and ask before writing there.

For Empire of Dust-style work, the common source shape is:

```text
/Users/flowith-mac-mini-001-user/Documents/Playground/docs/empire-of-dust-retention-20ep-dense/
  episode-06.md
  episode-07.md
  ...
```

The common output shape is:

```text
/Users/flowith-mac-mini-001-user/Downloads/Empire of Dust  ｜Example/
  Empire of Dust｜episode 06/
    Beat1 Seedance 2.0 Prompts.md
    Beat2 Seedance 2.0 Prompts.md
    Beat3 Seedance 2.0 Prompts.md
    Beat4 Seedance 2.0 Prompts.md
  Empire of Dust｜episode 07/
    Beat1 Seedance 2.0 Prompts.md
    Beat2 Seedance 2.0 Prompts.md
    Beat3 Seedance 2.0 Prompts.md
    Beat4 Seedance 2.0 Prompts.md
```

## Output contract

Create exactly one episode directory per source episode. Use two-digit episode numbers in directory names, for example `Empire of Dust｜episode 06`.

Inside each episode directory, create exactly four markdown files:

```text
Beat1 Seedance 2.0 Prompts.md
Beat2 Seedance 2.0 Prompts.md
Beat3 Seedance 2.0 Prompts.md
Beat4 Seedance 2.0 Prompts.md
```

Each file should contain one complete prompt body that can be submitted directly to Seedance 2.0 as a single prompt. The prompt should be cinematic, vertically framed, continuity-safe, and specific enough for a 15-second short video beat.

## Scope boundary

Keep this workflow narrow. Stop after prompt files are generated and verified.

Do not:

- Submit prompts to Flowith or any canvas.
- Generate Seedance videos.
- Download video assets.
- Stitch clips.
- Add subtitles.
- Upload to YouTube.
- Update analytics or dashboards.
- Dispatch production, distribution, or analytics department mail.

If the user asks for later stages after this output exists, use the appropriate later-stage skill or workflow separately.

## Procedure

### 1. Inspect the source scripts

Read the source directory or master file. Determine:

- Episode numbers.
- Episode titles if present.
- Core scene progression.
- Main characters and role locks.
- Wardrobe, hair, props, species, rank, or identity markers that must remain stable.
- Locations and worldbuilding rules.
- Any recurring visual motifs.

If a source directory contains non-episode files, ignore them unless they clearly define global series continuity.

### 2. Split each episode into four beats

Create four story beats that cover the full episode arc:

- Beat 1: opening hook and immediate visual situation.
- Beat 2: escalation, reveal, confrontation, or emotional pressure.
- Beat 3: reversal, memory fracture, trap, confession, or power shift.
- Beat 4: cliffhanger, emotional landing, or final image that points to the next episode.

Do not summarize the episode generically. Each beat should have a visual job and a narrative job.

### 3. Write Seedance-ready prompt bodies

Each prompt file should be a direct generation prompt, not planning notes. Write in English unless the user asks otherwise.

Use this structure unless an existing project sample clearly uses a different structure:

```markdown
# BeatN Seedance 2.0 Prompts

[One complete cinematic prompt body.]
```

The prompt body should include:

- Main subject and exact role identity.
- Wardrobe and styling continuity.
- Location and environmental continuity.
- Action progression over roughly 15 seconds.
- Camera language suitable for vertical short video.
- Mood, lighting, color palette, texture, and production style.
- Constraints that avoid identity drift, costume drift, age drift, and continuity breaks.
- Any important text or symbol rules, including when no readable text should appear.

Seedance generation parameters belong in the text only when useful for the operator, for example:

```text
Seedance 2.0, 480p, 9:16 vertical, 15 seconds, cinematic sci-fi drama.
```

### 4. Preserve continuity locks

Carry stable details across all four beats for the same episode. For serialized projects, carry global continuity forward across episodes unless the script explicitly changes it.

For Empire of Dust-style prompts, preserve:

- Character role locks: empress, war prince, rebels, archivists, vault guards, court figures.
- Wardrobe locks: imperial fabrics, armor, mourning colors, ritual accessories, visible status markers.
- Environment locks: memory vaults, imperial court spaces, desert ruins, archive chambers, orbital or palace architecture.
- Tone locks: cinematic short drama, political betrayal, resurrection mystery, space-opera grandeur, intimate emotional tension.

### 5. Create folders and files

Before writing, ensure the output root is the intended location. Create missing directories as needed.

For every episode, write the four prompt files using the exact output names from the Output contract.

Prefer modifying or overwriting only the files this skill owns. Do not delete unrelated files in the output root.

### 6. Verify the result

After writing, verify:

- Every source episode has one matching output episode directory.
- Every output episode directory has exactly four beat prompt files.
- File names match the contract exactly.
- Prompt files are not empty.
- Each prompt is complete enough to submit directly to Seedance 2.0.
- The four beats cover the full episode and do not duplicate the same scene.

Report the output root and any episodes skipped or ambiguous.

## Example

User input:

```text
把 /Users/flowith-mac-mini-001-user/Documents/Playground/docs/empire-of-dust-retention-20ep-dense 拆成 /Users/flowith-mac-mini-001-user/Downloads/Empire of Dust  ｜Example 的 seedance 2.0 prompts 文件夹系统
```

Expected result:

```text
/Users/flowith-mac-mini-001-user/Downloads/Empire of Dust  ｜Example/
  Empire of Dust｜episode 01/
    Beat1 Seedance 2.0 Prompts.md
    Beat2 Seedance 2.0 Prompts.md
    Beat3 Seedance 2.0 Prompts.md
    Beat4 Seedance 2.0 Prompts.md
  ...
```

Final response should be brief:

```text
已生成 Stage 1 prompt 文件夹系统：<output-root>。共处理 X 集，每集 4 个 Seedance 2.0 prompt 文件；未执行视频生成或发布。
```
