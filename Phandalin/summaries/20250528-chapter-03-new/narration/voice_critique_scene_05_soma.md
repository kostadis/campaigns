# Voice Critique — Soma, scene 05: Exploring the Stone Bedrooms

**Narration:** `session_doc_scene_05_exploring_the_stone_bedrooms.md`
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
| voice_lint | ran on `session_doc_scene_05_exploring_the_stone_bedrooms.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

No flags.

## Notes

- "my joints are filing their usual complaints" (line 11) is the one Soma-scene instance of the accounting register that is native to Vukradin — see the doc-level convergence note in the summary. One word; spot-edit only if you want the registers fully separated ("my joints lodging their usual complaints" keeps the joke without the ledger verb).
- Scan A2: all four quote-final dashes check out — the "bed frames—"/"don't have" completion matches the raw cue split, and the note-vs-running exchange renders Soma's own pivot, confirmed by "I voted for this" at line 67.

## Reclassified table speech

- `"cleric,"`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

No flags. "My bale contains a bard who treats news like a bucket brigade of one" is the scene in one sentence. Spot-edit at most.
