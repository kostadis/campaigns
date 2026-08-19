# Voice Critique — Valphine Sotorra, scene 06: The Priest's Remains

**Narration:** `session_doc_scene_06_the_priest_s_remains.md`
**Input shape:** per-scene (directory run; scrubbed variant preferred where it exists)

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `Phandalin/voice/_genre.md` @ `6e67c59f94b4` | run record (`.knobs.json`, post-#276); 61 lines, ~7.5K chars |
| Rulebook vs run record | **match** — current file digest equals render-time digest (verified with the pipeline's own `sha256(text.strip())[:12]`) | sha comparison |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4.1K |
| Voice spec | `voice/valphine_new_pipeline.md` | rule (c): unique key `valphine_new_pipeline` for first name `valphine` |
| Per-char examples | `examples/valphine.md` | stem equals first name; single file, no concatenation |
| Global examples | none | all four example files route per-character |
| Party doc | `docs/party.md` | roster **3/4** PCs carry `Player:` lines — Brewbarry's block lacks one (campaigns#144 silent-partial hazard) |
| voice_lint | ran on `session_doc_scene_06_the_priest_s_remains.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

No flags.

## Notes

- **Canon check needed:** "I trained him in interrogation" (line 37, Valphine re: Brewbarry). At Chapter 3 the party is weeks old; no grounding doc supports a training arrangement this early. Unverifiable from here — flagged for a consistency ruling rather than asserted as fabrication.
- **Borderline, judged licensed:** "I compose my face into the mild curiosity of a cleric encountering mortality" (line 41) wears the banned portrait shell ("the X of a Y…"), but the move underneath is not explanatory taxonomy — she is deliberately manufacturing a class-typical appearance as a mask, which is her spec exactly. Recorded so the GM can overrule.
- Scan A2: both quote-final dashes match raw-layer truncations with real completions.

## Reclassified table speech

- `"Surrounded by thieves"`
- `"Just watching your icon zoom off."`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

No flags. The theology paragraph ("Lolth's grammar in a beard") and the theft ("the sting is instructive") are Valphine at full spec. The two notes above are for the GM's judgment, not edits.
