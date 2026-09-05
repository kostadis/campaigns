# Scrub manifest — 20250812 (Chapter 8, Tower of Storms)

**Run:** 2026-09-04
**Target:** `summaries/20250812-chapter-08/narration/` — 6 scenes
**Render under review:** `sd_narrate --backend codex-cli --model gpt-5.6-sol --codex-reasoning-effort medium`,
with `--prose-mode --narration-genre-file voice/_genre.md --reflections`.

Scanner returned **2 candidates across 6 scenes**, both false positives. The
reading pass found **2 more**, one of which was the only real residue in the
chapter. Those are different statements and both are recorded below.

---

## GM-authored divergences

Every row is a deliberate departure from the tape, approved by the GM. A fidelity
check will flag these; **do not "fix" them back.**

| Scene | Line | Tape / raw narration | Scrubbed | Class |
|---|---|---|---|---|
| 06 | 153 | `For a moment, our sight of the fight falters. The bear vanishes from the shared view, then returns as the confusion clears.` | *(removed)* | out-of-fiction table event, euphemised |
| 05 | 127 | `"I mean, it smells like napalm."` | `"I mean, it smells like a pitch fire."` | **authorial rewrite of verbatim player speech** (Wade, tape l.6287) |

The scene-05 row is the more serious of the two and is marked as such: it changes
what a player actually said, under the ren-faire register ruling below. It is not
a transcription correction.

The scene-06 row is the same underlying table event the DGX render wrote as
`the DM's internet dies` / `the bear token vanishes off the board`. Codex did not
reproduce that literally — it euphemised it into in-fiction perception. `the shared
view` has no in-world referent, so it was cut rather than kept.

## New canon (`provenance: on_the_fly`)

**None.** Both approved changes are a removal and a plain-language substitution.
`pitch fire` is ordinary descriptive language, **not** a coined proper noun, and
must not be registered as an entity or an alias.

## GM rulings on what is NOT residue

None of this is scannable — `find_residue.py` cannot match vocabulary at all — so
without this section the next run re-proposes every line of it.

| Ruling | Detail | Scope |
|---|---|---|
| **Ren-faire register** | *"ren-faire except where there is pre-existing faerun words — e.g. Tendays instead of week"* | **NEW, campaign-wide.** Appended to `notes/scrub_register_policy.md`. |
| Architectural distances are not residue | `eighty feet above the water`, `fifteen feet over an empty chamber` — physical description, not movement mechanics. Same class as the precedented `three-foot-high retaining wall`. | per-instance, this run |
| Reclassification hatches reviewed and correct | 23 spans across 4 scenes (s01 ×3, s02 ×9, s03 ×1, s06 ×10) | this run |

### On the ren-faire ruling

It was given in response to the napalm question and is broader than that span, so
it was recorded as policy and the napalm span was **re-asked separately** rather
than being resolved by inference. The GM then ruled `replace in-world`.

Applying the new rule to this narration produced **zero additional candidates**:

- no occurrence of `week` anywhere in the six scenes;
- `"30 minutes"` (s04) is a real time unit Faerûn uses normally — tenday replaces
  *week*, not *minute*;
- `no second lightning bolt` (s06) is an ordinal, not a time unit;
- the only other hit sits inside a hatch, i.e. already out of the narration.

**Cross-chapter observation, not acted on:** the campaign's existing narration is
already inconsistent on this — 13 uses of `tenday` against 29 of `week` across
`summaries/*/narration/`. That predates this ruling and is out of scope for this
run, but a sweep is now justified.

## Notes

### Scenes with no `.scrubbed.md`, and why

Scenes **01, 02, 03, 04** had no accepted changes and therefore have no
`.scrubbed.md`. That is correct, not an omission — `collect_scene_files` in
`assemble.py` prefers `.scrubbed.md` per scene and falls back to the raw `.md`, so
the mixed directory assembles correctly. All six scenes are marked `processed`
because all six were reviewed. No `(D)` skips are outstanding.

**Consequence for any downstream pass:** the effective file set is not uniform.
A `/voice-critic` fix or consistency repair touching scenes 05 or 06 must land in
**both** the raw and the `.scrubbed.md`; scenes 01–04 have only the raw.

### Scanner false positives deliberately NOT persisted to `ignore`

`eighty feet` and `fifteen feet` were rejected per-instance and **not** written to
`.scrub_state.json`. Both strings are generic enough that persisting them would
subtract them from every future scan in the campaign and silently blunt the
`foot_count` detector on genuine movement-mechanic residue. The ignore list is
unchanged at 7 entries.

### Tooling gaps hit during this run

1. **`--party-md` loaded 3 of 5 roster members, full names only.**
   `player_names_loaded` reported `David Mendenhall`, `Wade Brown`, `Gary Young`.
   Stéphane Bourdeaud and Kostadis Roussos did not load, because
   `load_player_names` matches a literal `Player: X` prefix that Phandalin's
   `docs/party.md` does not use. Bare first names are invisible to the detector
   regardless — this is what let `Gary's voice cuts across the table` survive the
   scan in the *DGX* render of the same session.

2. **`voice_lint` ignores this campaign's `extra_tics` block** — `note [config]
   unrecognised voice_lint key 'extra_tics' — ignored`. Not a scrub tool, but hit
   during the same review; recorded here because both gaps affect every run in
   this workspace.

### Handed off, NOT fixed here

**Scene 01, line 81 — a wrong character name.**

> It disengages and beats away from the halberd, keeping open air between itself and **Homer**.

The halberd is Brewbarry's; `Homer` is a *different* registry entity (it appears in
`docs/entity_registry.yaml` in a distinct-pair entry with `Elmer`). The name occurs
nowhere in the VTT, nowhere in `scene_extractions/`, and nowhere in `docs/party.md`
— so the narrator substituted an unrelated campaign name for the acting character.

This is a **fidelity defect, not mechanical residue**, so it is out of scope for
`/scrub` and was not touched. It belongs to `/consistency-check`. Flagged here so
it is not lost: it is the single most serious problem in this render, and no scrub
pattern will ever surface it.
