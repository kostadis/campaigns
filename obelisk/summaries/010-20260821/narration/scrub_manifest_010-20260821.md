# Scrub manifest — 010-20260821 (Chapter 10, "The Wizard of the Old Owl Well")

Run date: 2026-09-04. Narration produced by `sd_narrate` (backend `codex-cli`,
model `gpt-5.6-sol`, reasoning effort `medium`) over `scene_extractions_smoothed/`.

Scanner (`find_residue.py`) returned **0 candidates across all 8 scenes**. Every
finding below came from the Phase 1b reading pass. "0 candidates" and "no
residue" are different statements, and this run is the difference.

## GM-authored divergences

These spans deliberately differ from the tape. A fidelity check WILL flag them.
Do not "fix" them back.

| Scene | Line | Tape / narration as generated | Scrubbed | Class |
|---|---|---|---|---|
| 01 | 61 | `“Medic!”` | `“Hold on — I have you.”` | narrator-authored anachronism |
| 03 | 111 | `“But, you know, that's [unclear] — but let me just tell you something.”` | `“But, you know — let me just tell you something.”` | transcript artifact |
| 07 | 151 | `…with those rough-ins…` | `…with those marauders…` | uncarded ASR garble (`cf-vs-03`) |
| 07 | 197 | `…bugbears Monday, Tuesday, Wednesday…` | `…bugbears Firstday, Secondday, Thirdday…` | real-world calendar with a Faerûn canonical equivalent |

Notes on two of these:

- **`“Medic!”` is not on the tape at all.** The heal is on tape; the shout was
  invented by the narrator. That is why it was scrubbed under a register policy
  that otherwise keeps the players' own anachronisms — the policy licenses the
  table, not the narrator.
- **`rough-ins` → `marauders` is a rewrite, not a recovery.** `ruffians` was the
  likelier reconstruction and was explicitly declined in favour of Hamun's own
  word for them, used two lines earlier. This closes one of the four `cf-vs-03`
  garbles **at the narration layer only** — `scene_extractions_smoothed/07…md`
  still carries `rough-ins` with its uncarded-garble annotation.

## New canon (`provenance: on_the_fly`)

- **Firstday / Secondday / Thirdday** — Forgotten Realms canonical tenday day
  names, introduced to this campaign by GM ruling on 2026-09-04. **The campaign
  had no calendar before this**: `notes/everyone_is_a_suspect.md:352` records
  "No campaign doc records one, so this doc carries no Tenday stamps." This run
  sets the precedent; a calendar doc does not yet exist.
- No new proper nouns, items, institutions or personas were invented. No
  marginal-note / sage-gloss device was used this run.

## GM rulings on what is NOT residue

None of this is scannable — `find_residue.py` matches numbers, fixed table-speak
phrases and player names, and cannot match vocabulary at all. Without this record
the next run re-proposes every item.

- **Register: ren-faire — EXCEPT where a canonical Faerûn word exists.** Modern
  idiom from the players is in-canon and stays verbatim. Where Faerûn has its own
  established word for the thing, that word wins.
- **Kept, explicitly in-canon:** `“God's plan”` (03:21), `“chunk of change”`
  (05), `“keep your eyes peeled”` (04), Pip's `“professional road security”`
  register (03 — it is in `voice/pip_voice.md`).
- **`“Generous to what?”` (04:73) — KEPT, ruled in-canon.** An uncarded ASR
  garble from `cf-vs-03` that accidentally produced a working mishearing beat;
  Toblen repeats himself and Zenvon answers `“Paying attention. Okay.”`
  This instance of `cf-vs-03` is now closed as *kept*, not outstanding.

## Notes

- **Scenes 04, 05, 06, 08 were reviewed and produced no `.scrubbed.md`.** That is
  correct, not an omission — `assemble.py` prefers `.scrubbed.md` per scene and
  falls back to the raw `.md`, so the mixed directory assembles correctly.
- **Scene 02 is NOT processed and was deliberately not scrubbed.** See below.
- **`--party-md` loaded 0 player names.** `load_player_names` matches a literal
  `Player: ` prefix; `docs/party.md` writes `**Player:** Nikhil Reddy`, so the
  `**` defeats it. `player_name` detection was blind for this entire run and the
  reading pass covered that class instead. Tooling gap, not a campaign problem.
- **No scanner false positives were persisted to `ignore` this run** (there were
  no scanner candidates at all). Pre-existing ignores are unchanged.

## RESOLVED — scene 02 re-narrated from summary only

`sd_narrate` writes a `<!-- table-speech reclassified: … -->` comment recording
spans it judged out-of-fiction and dropped. It wrote **none** for scenes 01, 02
and 03 (04-08 all have one). In scene 02 the consequence was severe: 45 quoted
lines against 28 lines of narration, and all of them the table operating the
virtual tabletop, rendered as in-fiction dialogue in Zenvon's voice.

**GM ruling (2026-09-04): none of that scene's 107 captured quotes is roleplay.**
All are mechanical, and the scene is to be narrated as the party standing over a
map working out where to go next.

Applied as:

1. The entire `## Voiced moments` section of
   `scene_extractions_smoothed/02_planning_at_the_miner_s_exchange.md` was cut,
   with an italic note recording what was cut and why. This extends `/voice-smooth`'s
   tooling/logistics class (ruling `vs-08`) from a single beat to a whole scene.
   The verbatim record is untouched in `scene_extractions/` and the VTT.
2. `sd_narrate --scene 2` re-run against the edited smoothed layer.

Result: **0 quoted lines** (was 45), narrated from the scene-summary bullets.
No `.scrubbed.md` was needed — a fresh `find_residue.py` scan returns 0 and the
reading pass found nothing. A hatch was never fabricated at any point.

**Side effect, worth knowing before assembly.** The narrator sometimes opens a
scene by repeating the previous scene's closing line. Regenerating scene 02
dropped the 01->02 echo, so exactly one such echo now remains in the document:
scene 03 ends and scene 04 opens on the identical sentence, *"I managed not to
laugh until his back was turned."* Assembled, that sentence appears twice in a
row. It is the only remaining instance and it predates this run.
