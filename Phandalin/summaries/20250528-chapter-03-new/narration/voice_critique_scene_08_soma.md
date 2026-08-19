# Voice Critique — Soma, scene 08: The Hall of Greed

**Narration:** `session_doc_scene_08_the_hall_of_greed.scrubbed.md`
**Input shape:** per-scene (directory run; scrubbed variant preferred where it exists)

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `Phandalin/voice/_genre.md` @ `6e67c59f94b4` | run record (`.knobs.json`, post-#276); 61 lines, ~7.5K chars |
| Rulebook vs run record | **match** — current file digest equals render-time digest (verified with the pipeline's own `sha256(text.strip())[:12]`) | sha comparison |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4.1K |
| Voice spec | `voice/soma_new_pipeline.md` | rule (c): unique key `soma_new_pipeline` for first name `soma` |
| Per-char examples | `examples/soma.md` | stem equals first name; single file, no concatenation |
| Global examples | none | all four example files route per-character |
| Party doc | `docs/party.md` | roster **3/4** PCs carry `Player:` lines — Brewbarry's block lacks one (campaigns#144 silent-partial hazard) |
| voice_lint | ran on `session_doc_scene_08_the_hall_of_greed.scrubbed.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

No flags.

## Notes

- Scan A2: both quote-final dashes are genuine — line 21's completion device is rendered explicitly ("Vukradin finishes") and line 37's matches a raw `(truncated)` cut-in.
- The anachronism replacement from the scrub pass (the temple-frieze motif, lines 63/69) reads clean in place; reminder that the "demon statue cupping a glowing gem" Abbathor motif is on-the-fly canon from that pass.

## Reclassified table speech

- `"I actually do. Let's clear it out. I have it — look at my character."`
- `"A natural 20."`
- `"No middle numbers, just ones or 20s."`
- `"on it."`
- `"I do not."`
- `"Did I find anything in the rubble?"`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

No flags. The closing pair — Abbathor keeping what is his, "He is not even tired. More's the pity." — lands the scene in Soma's register exactly. Nothing needs touching.
