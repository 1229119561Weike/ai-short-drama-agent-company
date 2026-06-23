# Empire of Dust Episode Artifact Index

This file is the canonical handoff map for Empire of Dust production and publishing evidence. It is designed to help a new operator identify the correct final assets without searching through old candidates, subtitle intermediates, and retry files.

## Canonical interpretation rules

- A final MP4 is canonical only when a final path and media properties are recorded in a QA handoff or department reply.
- Analytics/dashboard updates require publish evidence: URL, video ID, final title, and playlist confirmation.
- `Season complete 20/20` does not mean every historical ledger row has complete CEO-held evidence. The dashboard currently distinguishes season completion from ledger completeness.
- Do not fill missing rows by inference. If a URL/video ID/playlist confirmation is missing, mark that item pending.

## Episode status overview

| Episode | Production artifact | Publish evidence | Dashboard/ledger state | Notes |
|---:|---|---|---|---|
| 01–05 | Prompt folders and historical project assets exist | User-published / historical evidence outside the latest CEO-held chain | Present in historical dashboard context | Treat as historical unless exact URL/video ID is needed. |
| 06–08 | Final MP4s and production intermediates exist in episode folders | Published evidence exists historically | Dashboard has historical rows | Earlier successful pipeline samples. |
| 09–12 | Final MP4 variants exist in production archive | CEO-held publish records incomplete | Ledger record gap | Do not mark analytics complete without URL/video ID/title/playlist evidence. |
| 13 | Published evidence exists historically | Published evidence in dashboard context | Dashboard row exists | Use dashboard/memory if needed. |
| 14 | Production/publish record gap | Publish evidence incomplete | Ledger record gap | Do not infer completion. |
| 15 | Production evidence exists, but publish evidence missing in CEO-held chain | User claimed manual publish, but CEO lacks URL/video ID/final title/playlist confirmation | Analytics pending | Keep gated until evidence exists. |
| 16 | Production complete, publishing previously blocked/no valid publish evidence | Missing URL/video ID/playlist confirmation | Analytics pending | Keep gated until publish evidence exists. |
| 17 | Final MP4 + QA handoff complete | `https://youtube.com/shorts/QM7ngkn8ans` / `QM7ngkn8ans` | Dashboard updated | Valid publish evidence. |
| 18 | Final MP4 + QA handoff complete | `https://youtube.com/shorts/JK6T-3SfAq8` / `JK6T-3SfAq8` | Dashboard updated | Valid publish evidence. |
| 19 | Final MP4 + QA handoff complete | `https://youtube.com/shorts/nWDUYrk3Gkc` / `nWDUYrk3Gkc` | Dashboard updated | Beat3/Beat4 retry-to-success recorded. |
| 20 | Final MP4 + QA handoff complete | `https://youtube.com/shorts/WRN1KO7gE_Y` / `WRN1KO7gE_Y` | Dashboard updated; season 20/20 complete | Finale; performance metrics pending. |

## Canonical recent episode artifacts

### Episode 17

- Final MP4: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 17/Empire of Dust Episode 17 final.mp4`
- Media properties: 1080x1920, audio present, 60.299229s, 35,475,630 bytes
- QA handoff: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 17/Episode 17 Production QA Handoff.md`
- Publish URL: `https://youtube.com/shorts/QM7ngkn8ans`
- Video ID: `QM7ngkn8ans`
- Final title: `The Empire Was Built on a Stolen Lock | Empire of Dust Ep 17`
- Playlist: `Empire of Dust` confirmed
- Evidence messages: production `msg_5ac87899-4768-4dec-be45-e21eadcba0fe`; publish `msg_2feb6a2a-3460-4f3f-b743-4f0b9106f8c9`; dashboard `msg_421a2780-c075-43c4-b7bb-3dd2e4de9474`

### Episode 18

- Final MP4: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 18/Empire of Dust Episode 18 final.mp4`
- Media properties: 1080x1920, audio present, 60.299229s, 35,464,706 bytes
- QA handoff: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 18/Episode 18 Production QA Handoff.md`
- QA handoff SHA256: `a7b7e3900a04b000daf3af0228dde31517d602926285f3c44f27a52315233e32`
- Beat task IDs: Beat1 `cgt-20260511110132-bkgrg`, Beat2 `cgt-20260511111319-7x6bt`, Beat3 `cgt-20260511111928-ltcmm`, Beat4 `cgt-20260511112504-v9k4b`
- Publish URL: `https://youtube.com/shorts/JK6T-3SfAq8`
- Video ID: `JK6T-3SfAq8`
- Final title: `She Heard the Name She Had Before the Empire | Empire of Dust Ep 18`
- Playlist: `Empire of Dust` confirmed
- Status/visibility: published / Public
- Evidence messages: production/publish `msg_fa97f806-87f6-481c-8908-72121c02a4f9`; publish-only `msg_db3d2ca7-d3ec-4f63-8eac-01105c59a879`; dashboard `msg_d397047a-eba6-4dec-b36c-75ea03b5b47e`

### Episode 19

- Final MP4: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 19/Empire of Dust Episode 19 final.mp4`
- Media properties: 1080x1920, audio present, 60.299229s, 56,757,148 bytes
- QA handoff: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 19/Episode 19 Production QA Handoff.md`
- QA handoff SHA256: `d081277ac6a687a19defd563da98a02b089b46288fdb6210598da1344330e7aa`
- Beat task IDs:
  - Beat1 `cgt-20260512180355-rwjtc` succeeded
  - Beat2 `cgt-20260512181140-g89x5` succeeded
  - Beat3 initial `cgt-20260512181625-5cl2r` failed, retry `cgt-20260512185829-2clrl` succeeded
  - Beat4 retry `cgt-20260512190334-k74cv` failed, retry `cgt-20260512190936-mwkrb` succeeded
- Publish URL: `https://youtube.com/shorts/nWDUYrk3Gkc`
- Video ID: `nWDUYrk3Gkc`
- Final title: `She Returned With the Code That Could Replace the Throne | Empire of Dust Ep 19`
- Playlist: `Empire of Dust` confirmed
- Status/visibility: published / Public
- Evidence messages: production `msg_419b9514-f94b-43e8-9c21-4ae875485ab7`; publish `msg_24f34cd4-2569-4a01-8620-3314469301fa`; end-to-end `msg_31b1c4c7-2e50-4ec6-a499-cbbdf2bd1aef`; dashboard `msg_8a829a95-d9e0-48e5-aae2-e8a82c8c8c7e`

### Episode 20 Finale

- Final MP4: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 20/Empire of Dust Episode 20 final.mp4`
- Media properties: 1080x1920, audio present, 60.299229s, 42,366,706 bytes
- QA handoff: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 20/Episode 20 Production QA Handoff.md`
- QA SHA256: `0e931efe2b559ff45d2aabf3d1f7bd2df357d2a481c8d959b182ce5700786985`
- Beat task IDs:
  - Beat1 `cgt-20260513110147-v7sqh`
  - Beat2 `cgt-20260513110712-96twq`
  - Beat3 `cgt-20260513111346-g9wvj`
  - Beat4 `cgt-20260513111943-dxgr8`
- Production note: initial run hit `401 invalid token`, then recovered; Beat1–4 succeeded after recovery.
- Publish URL: `https://youtube.com/shorts/WRN1KO7gE_Y`
- Video ID: `WRN1KO7gE_Y`
- Final title: `She Saved the Empire Without Becoming Its Prison | Empire of Dust Finale`
- Playlist: `Empire of Dust` confirmed
- Status/visibility: published / Public
- Browser evidence: monitor task `bja85re11`, completed at `2026-05-13T04:02:51.039Z`
- Evidence messages: production `msg_2a3f2760-6765-4b3f-8d72-02297598fecf`; publish `msg_84dcbeff-bc8b-4118-9da4-a8123768cee9`; dashboard `msg_18159734-fba9-4234-a8b5-d5cb0e76d731`

## Dashboard and report artifacts

- Dashboard source: `dashboard-overrides.json`
- Dashboard state after Ep20: S01 complete at 20/20, ledger completeness 14/20, metrics pending
- Season wrap-up report path: `storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust 杀青项目报告书.md`

## Maintenance rule

When a future operator adds or repairs evidence, update this index with:

- episode number
- final MP4 path
- media properties
- QA handoff path and hash if available
- beat task IDs and retry/failure chain
- publish URL and video ID
- final title
- playlist confirmation
- dashboard status
- evidence message IDs
