# Voice Critique — Soma, scene 02: Battle with the Ochre Jellies

**Narration:** `session_doc_scene_02_battle_with_the_ochre_jellies.scrubbed.md`
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
| voice_lint | ran on `session_doc_scene_02_battle_with_the_ochre_jellies.scrubbed.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

No flags.

## Notes

- "zero hit points" (line 29) survives in narration prose. The genre rulebook explicitly licenses hit points in prose ("Drop hit points, distances, spell names directly into prose"), and the GM saw this exact line during the scrub pass (candidate 2.3 context) and protected it. Not a finding — recorded so nobody "fixes" it later.
- Scan A2: all three quote-final dashes (lines 67, 75, 85) check out against the raw tape — a completion device, a real interruption by Vukradin, and a real GM cut-in respectively.
- "I have seen fishermen do this, standing in a boat with a hole in it" (line 17) was checked against the behavioral-taxonomy ban and passed: it names a concrete remembered image from Soma's coastal life, which is exactly the "name what the narrator actually saw" fix the ban prescribes.

## Reclassified table speech

- `"Nice. Natural one. Well done, Gary."`
- `"Vukradin will use a cantrip. Hits. Starry Wisp. Four damage."`
- `"Yeah, and 10 — five. So you do 10 damage to the one with seven."`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

No flags. Combat alternates the procedural and the felt per the rulebook, and the death-save paragraph ("the body argues with it… the argument goes my way") renders the mechanic somatically without naming it. Nothing needs touching.
