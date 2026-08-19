# Voice Critique — Valphine Sotorra, scene 10: Ambush on the Road

**Narration:** `session_doc_scene_10_ambush_on_the_road.md`
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
| voice_lint | ran on `session_doc_scene_10_ambush_on_the_road.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

### [1] cliché simile in the closing beat

> The four of them hold the hilltop, weapons up, the whole road pulled taut as a bowstring, and I stand at the front of it with my hand crossbow loose in my grip and the first Orcish phrase waiting on my tongue.

**Why:** "taut as a bowstring" is a workshopped fantasy simile — the rulebook's "Generic fantasy reach — specific or nothing" rule — and it is the only generic figure in an otherwise exact scene ("An ambush, in the sense that a door slamming is an argument").
**Suggested rewrite:** "…the whole road narrowed to the breath before a verdict, and I stand at the front of it…" *(grounded in spec — her judgment register; also avoids doubling the literal crossbow later in the same sentence. Scene 10 has no `.scrubbed.md`; the fix belongs in a new one.)*

## Notes

- **Dialogue notes, GM scope calls:** "so the other players can't understand us" (line 53, Vukradin, verbatim) — table-speak on the tape, but from an Eloquence bard "players" reads as diegetic troupe-speak, and the narration around it treats it in-fiction; defensible as-is. "You did some good tanking for us" (line 61) — same gamer-slang family as scene 7's "tank," locked speech.
- "It's gonna take the entire campaign" (line 67) — GM already ruled keep as in-fiction (scrub 10.1); recorded so nobody relitigates it.
- Scan A2: zero quote-final interruption dashes in this scene.

## Reclassified table speech

- `"It's 10:31 — if we're starting a new combat, we should wait until next week."`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

One flag, one simile, one spot edit. "It is simply where fluency comes from. Ownership." is the best single beat any narrator lands in this session.
