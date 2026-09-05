# no-mech manifest — 20250812 (Chapter 8, Tower of Storms)

**Run:** 2026-09-04
**Target:** `scene_extractions_smoothed/` (6 scenes, 471 quotes)
**Result:** 5 lines cut across 4 scenes. **Phase 4 re-narration NOT run.**

---

## The headline: this session is a poor candidate, and that is the finding

The skill's reference case (obelisk ch10) had scenes that were *entirely* the
table operating a VTT, with no fiction in them. Chapter 8 is not that. It is a
combat session in which **the mechanics are the events**:

- `"Vukradin with three hit points and silence concentration"` is the dramatic
  peak of the chapter.
- `"Soma, you're down to two"` is the TPK moment.
- The 25-point lightning bolt is the encounter's turn.

Two standing rulings point the same way, and both would have been violated by an
aggressive pass:

| Source | Clause |
|---|---|
| `voice/_genre.md` | *"Tone shifts scene to scene: … **mechanical procedural during combat (hit points, saves, the named spell)**, then back to lyrical interior."* |
| `voice/vukradin_new_pipeline.md` | *"He speaks in clean procedural D&D mechanics when coordinating — hit points, ranges, durations, conditions, save DCs, spell slots. **This is his way of being precise about life-and-death matters.**"* |

So for this campaign — and for Vukradin especially — combat mechanics are
**register and characterization**, not residue. 54 of the 59 pattern-flagged
lines were in canon before review.

`/voice-smooth` had also already removed this session's genuine table-operation
content the day this ran: Roll20 token requests, the bear-token loss, the DHCP
tangent, and the internet outage (~30 blocks, scene 06).

## Scanner: the triage was dead, and it is the Valphine bug

All six scenes returned `likely roleplay — NPC speakers present: Valphine`.

**Valphine is a PC.** The extractions label her `Valphine`; `config/party.yaml`
declares `Valphine Sotorra`; the match is exact. The scanner therefore counts the
party's cleric as an NPC and triages every scene as roleplay on that basis.
`UNKNOWN` and `Gary Young` inflate the same signal.

Six identical triage lines, none of them evidence. This is the **same root cause** as the
`narrator: Valphine` repair in `narration_dgx/plan.md`, recorded in
`voice_smooth.sources.yaml` (`findings.valphine_short_label`).

**Correcting an earlier overstatement:** her *voice spec* is fine. Both renders
carry `narrator: Valphine Sotorra` in scene 04's frontmatter, so the spec
resolved and she was rendered with it — a spec attaches to a scene's narrator,
not to quote-block labels. What `sd_plan` emits is the short label, which makes
`sd_narrate` **refuse to start** (#300) until hand-repaired; that failure is
loud. **This triage bug is the silent one**, and it is the reason the mismatch is
worth fixing upstream rather than patching per-run.

Pattern recall was also low as advertised: 59 flags over 471 quotes, and the
reading pass rejected all but 5 of them.

## What was cut

| Scene | Line | Text | Class |
|---|---|---|---|
| 02 | 30 | `"Public roll. Harpies are 11. That's a hit."` | Roll20 operation |
| 04 | 34 | `"You get bonus hit points or temporary hit points based on your druid level…"` | rules lecture to a player |
| 05 | 179 | `"Let's check the landing and make sure there's nothing on the landing."` | at-the-table, already labelled OOC |
| 06 | 192 | `"…it's not letting me roll it, so 8d6 by hand. 25."` | tool failure |
| 06 | 258 | `"Let me actually double-check the rule, make sure there isn't something I missed on this."` | rules lookup |

Quote counts: 02 66→65, 04 51→50, 05 84→83, 06 113→111. Scenes 01 and 03
unchanged. Every cut scene carries a `*Cut by GM ruling…*` note naming what went
and why. `--dry-run` was run first on all four; **no orphaned acknowledgements
were reported.**

Note on the scene-06 cut of L192: the `25` damage value lives in that line, but it
is restated immediately by Vukradin (`"25 half damage is 12"`), so the number
survives in the fiction. Checked before cutting.

## What was deliberately KEPT

- **Every hit point, save, damage number and condition** in all six scenes.
- **The 18 `bare-ack` flags** (`"Yeah."`, `"Okay."`, `"Yes."`). GM ruled leave-all.
  Cutting one orphans the line it answers — the skill's own named landmine.
- **`"Roll a religion check"`** (05 L112) and the blown-rolls exchange. They set up
  *"Our cleric's not very religious, is she?"*, which is the scene's best joke.
- **Moesko's stat readout** (06 L45/L75 — AC 13, 58 hp, initiative 10). Cutting it
  would have reversed ruling C5 from the voice-smooth pass, which explicitly kept
  the settled values.

## Deviation from the approved ruling — flagged, not silently applied

Scene 06 L369 was approved for cutting **as scheduling**:

> `"Pick up the loot, and we'll figure out what that conch is and everything next week."`

**Not cut.** `apply_cut.py` removes whole quote lines, and *"next week"* is a
two-word clause inside an otherwise in-fiction line that carries the loot pickup
and the conch hook — the setup for the next session. Cutting the line to remove
the clause would have deleted approved in-fiction content.

Left intact. The narrator drops trailing scheduling language on its own, and
`/scrub` can take the clause downstream if it survives. **Open for the GM to
overrule.**

## Phase 4 — NOT run

Re-narration was not performed. Both existing renders (`narration/`,
`narration_dgx/`) were built from the **verbatim** layer and reflect neither this
pass nor the voice-smooth rulings that preceded it. A re-narration would need to
regenerate **all six scenes**, not just the four touched here, and the seam walk
in Phase 4 would then be required.

Consequently there is **no seam damage to report and no measurement of what this
bought** — the honest statement is that the input is better and the output has
not been regenerated to show it.

## Carry-forward

- `OPEN` — re-narrate all six scenes from `scene_extractions_smoothed/`, then walk
  the seams.
- `OPEN` — GM to confirm or overrule leaving scene 06 L369 intact.
- `OPEN` — `Valphine` → `Valphine Sotorra` label mismatch. Breaks `sd_plan`
  narrator output (loudly: `sd_narrate` refuses to start) and this scanner's
  triage (silently). A roster alias is the better fix than relabelling, since
  the extractor will keep emitting the short label.
- `NOTE` — `apply_cut.py`'s smoothed-directory guard tests the **path string**, so
  it refuses a bare filename run from inside the directory. Pass a path that
  includes the `*_smoothed/` component.
- `NOTE` — a cut note that quotes the line it removed will match a later grep for
  that line. Verify against quote lines (`^> `) only, not whole-file text. Same
  shape as `/scrub` re-flagging its own audit comments.
