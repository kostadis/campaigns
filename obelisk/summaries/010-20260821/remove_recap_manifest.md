# remove-recap manifest — Chapter 10 (010-20260821)

Run 2026-09-04. Skill: `/remove-recap`. GM ruling recorded per Phase 3.

## Detection

`find_recap.py summaries/010-20260821/scene_extractions_smoothed`

| | |
|---|---|
| Scene | `01_a_heroic_recap.md` |
| Score | **6/6 — RECAP, strong** |
| Quotes | 45 (GM share 0.91, longest GM-only run 39) |
| Markers | past-tense **188** vs live-play **0** |
| opening_markers | `let me read you what happened`, `last time`, `previously,` |
| scheduling_talk | `three weeks`, `a month` |
| closing_sting | `bum, bum, bum` |
| Boundary | closing sting at line 150; **first live play: none** |

`--all-scenes` audit: all seven other scenes score **0/6**. That separation is
what licensed scoping the skill to the first scene.

## Rescue check (Phase 2)

`recap_unique.py --against summaries/008` — 76,318 words of chapter 8 material.

- **Bullets poorly covered upstream: none.** Every beat in the recap is already
  recorded in chapter 8's documents.
- **Two items the script flagged as "this chapter's bookkeeping" were NOT.**
  Zenvon reaching 3rd level / Arcane Trickster, and the Sildar letter, are both
  chapter 8 events; verified present verbatim at `summaries/008/session-summary.md:6`
  and `:28`. Nothing to rescue.
- **One genuinely new item — rescued.** See below.

### Rescued: the party learns the sword's name

Source: `scene_extractions/01_a_heroic_recap.md:97`, the GM breaking frame while
reading the chapter 8 recap aloud:

> "Aldith Tresendar, though nobody in the party recognized or learned its name.
> **Fine. We now learned its name.**"

This is a chapter 10 knowledge-state change and cannot exist in chapter 8's
document. **GM ruling: record against the item, not in a scene.** Applied to:

| File | Change |
|---|---|
| `docs/entity_registry.yaml` (`Talon`) | note extended: name learned ch10 out of frame; provenance and crypt link still unknown |
| `docs/world_state.md:128` | "the party does not know its name" → learned in Ch. 10; provenance still unknown |
| `docs/world_state.md:174` | "**Talon is unidentified**" → "**Talon is named but unidentified**" |

## What was cut — all three surfaces

| # | Surface | Action |
|---|---|---|
| 1 | `scene_extractions_smoothed/01_a_heroic_recap.md` | deleted (derived layer) |
| 1b | `session_summary.md` `## Scenes` | recap scene block removed |
| 2 | `session_summary.md` `## Summary` | paragraphs 1–3 dropped; chapter now opens at *"With the party still at the Miner's Exchange…"* |
| 3 | `session_2026_08_21_chapter_10_….md` `## Summary` | paragraphs 1–2 dropped; opens at *"With their wounds tended and their minds made up…"* |

Surface 3 is `sd_narrate`'s positional recap argument, so those two paragraphs
were framing context in **every** scene's narration prompt.

Chapter-8 provenance of the dropped prose was verified against
`summaries/008/session-summary.md`: Sildar's 150 gp (`:28`, `:131`),
Garaele's comb (`:30`, `:138–146`), Halia's 100 gp offer (`:32`, `:149–156`).

## Hard invariant honoured

`summaries/010-20260821/scene_extractions/01_a_heroic_recap.md` (19.1K) and every
VTT are **untouched**. The recap was really said; that record stands.

## Renumbering

Scenes 02–08 became plan sections 1–7. `plan.md` regenerated via `sd_plan`; all
stale `narration/session_doc_scene_*.md` deleted before re-narrating.

## Upstream gaps found

None. Chapter 8's record is complete with respect to everything its recap covered.
