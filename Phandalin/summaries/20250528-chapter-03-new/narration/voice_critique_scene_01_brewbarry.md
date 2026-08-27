# Voice Critique — Brewbarry, scene 01: Ambush at the Blood-Stained Altar

**Narration:** `session_doc_scene_01_ambush_at_the_blood_stained_altar.scrubbed.md`
**Input shape:** per-scene (directory run; scrubbed variant preferred where it exists)

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `Phandalin/voice/_genre.md` @ `6e67c59f94b4` | run record (`.knobs.json`, post-#276); 61 lines, ~7.5K chars |
| Rulebook vs run record | **match** — current file digest equals render-time digest (verified with the pipeline's own `sha256(text.strip())[:12]`) | sha comparison |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4.1K |
| Voice spec | `voice/brewbarry_new_pipeline.md` | rule (c): unique key `brewbarry_new_pipeline` for first name `brewbarry` |
| Per-char examples | `examples/brewbarry.md` | stem equals first name; single file, no concatenation |
| Global examples | none | all four example files route per-character |
| Party doc | `docs/party.md` | roster **3/4** PCs carry `Player:` lines — Brewbarry's block lacks one (campaigns#144 silent-partial hazard) |
| voice_lint | ran on `session_doc_scene_01_ambush_at_the_blood_stained_altar.scrubbed.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

No flags.

## Notes

- Scan A2: both quote-final interruption dashes (lines 49, 55) are inherited from the smoothed extraction layer (raw layer has zero). Line 55's is genuine — Vukradin completes Soma's sentence on the tape. Line 49's is a same-speaker GM cue-split whose tape completion ("minus two on its initiative") was mechanical residue; the narration turns the cut into a dramatic beat ("It does not wait."). Fiction-effective, tape-divergent — adjudicated keep.

## Reclassified table speech

none

## Verdict

No flags. The scene holds Brewbarry's register throughout — body-first, short declaratives; "the size of an ox with no ox in it" and the two-piles ending are exactly his. Nothing needs touching.
