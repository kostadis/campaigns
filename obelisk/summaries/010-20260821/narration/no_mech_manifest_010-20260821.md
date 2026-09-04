# no-mech manifest — Chapter 10 (010-20260821)

Run 2026-09-04. Skill: `/no-mech`. Applied to `scene_extractions_smoothed/`
**after** `/remove-recap` and **before** `sd_plan` / `sd_narrate`.

`scene_extractions/` and the VTT are untouched — `apply_cut.py` refuses to write
outside a `*_smoothed/` directory.

## Scan (Phase 1)

`scan_quotes.py … --party-config config/party.yaml`

The pattern flags were again a low floor: **4 of 47** on scene 06, a scene the
reading pass found to be 47/47 mechanical (~9% recall). The triage's
"REVIEW CLOSELY — no NPC speaker labels" fired on scenes 03, 06 and 08; only two
of those three were mechanical. Scene 03 is a full two-hander in which all of
Daran Edermath's lines carry the `GM` label, exactly the one-directional
limitation the skill documents.

## Rulings (Phase 2) and application (Phase 3)

| Scene | Quotes | Mode | Cut | Left | GM ruling |
|---|---|---|---|---|---|
| 02 Planning at the Miner's Exchange | 0 | — | — | 0 | already cut in the prior run under the same precedent |
| 03 Consulting Daran Edermath | 91 | spans | 6 | 85 | **bonus cluster only** |
| 04 Preparations at Stonehill Inn | 40 | spans | 2 | 38 | cut the call and the number, keep the result |
| 05 A Bounty for Cragmaw Castle | 70 | spans | 3 | 67 | cut the call and the number, keep the result |
| 06 Journey Along the Triboar Trail | 47 | **all** | 47 | 0 | cut the whole section |
| 07 Arrival at the Old Owl Well | 146 | spans | 8 | 138 | cut the call and the number, keep the result |
| 08 Scouting Wyvern Tor | 28 | spans | 21 | 7 | cut 21, keep the seven |

**Total: 87 quotes cut.**

### Scene 03 — the ruling that went against the proposal

Two clusters were proposed; the GM ruled **the bonus cluster only**. The +1
Investigation/Survival award and its bookkeeping came out (6 quotes). The
Netheril meta-argument — the GM denying Daran ever said it, Zenvon's notes
proving otherwise, and the GM's *"Thank you — I think that's why we have the
notes"* — was **kept**, because it is the payoff to Daran's ten-minute lecture.
Recorded here because it is the one place this run's cut is narrower than the
classifier alone would have made it.

The GM-to-player prompt at line 148 (*"you could, for example, ask him about
Halia"*) was **not** in either ruled cluster and was left in rather than
silently folded into the cut. Open item if it reaches the prose.

### Scene 06 — whole-section cut

All 47 quotes are the GM and Zenvon operating the virtual tabletop
(*"Thirty miles. You said thirty miles a day, right?"*, *"Do you see that blue
line?"*, *"You moved yourself back. I'll move you back here."*, *"No, I was just
measuring the distance."*) plus out-of-character exposition delivered to the
player as a lecture. Applies the standing ch10 scene-02 precedent.

Narrated from summary bullets alone. Those bullets already carry the caravan
wreck, the north-south trade route, Neverwinter's frontier and the Spellplague,
so no fact was lost with the quotes.

### Scene 08 — the seven kept

Veyra's *"I don't think you know where you're going, buddy"* and *"well done"*;
the GM's *"Do you want to tell her anything, or just look at her knowingly?"*;
Zenvon's silent stare; the natural-20 find; and the smoke-and-ridge read-aloud.
Cut: DC negotiation, both Perception calls and totals, VTT map placement,
wall-clock (*"it's almost 7.40"*) and session scheduling (*"we'll continue next
week"*).

**Drafting error, corrected before applying.** The options as put to the GM were
inconsistent about the natural-20 line — option A named seven kept quotes but
said "cut 22", while option B's only content was "also cut the natural-20 line".
The GM declined B, so the line was **kept** and the cut is 21, not 22. Flagged to
the GM in the same breath rather than resolved silently.

## Orphans

`apply_cut.py` reported **no orphaned acknowledgements** on any of the six files.
Every cut was dry-run first; no line number was rejected, so no file had drifted
since the scan.

## Downstream

- `plan.md` regenerated (7 sections; scene 01 gone, 02–08 renumbered 1–7).
- Scene 5's narrator hand-corrected from Maela to Zenvon: `sd_plan` had put Maela
  on sections 5 and 6 back to back and left Zenvon — the only player-run PC — with
  one scene of seven. GM-ruled. Final rotation Zenvon 2 / Pip 2 / Veyra 2 / Maela 1.
- All stale `session_doc_scene_*.md` deleted before re-narrating; all seven scenes
  re-narrated (`gpt-5.6-sol`, medium effort).

## Phase 4 — seam check after re-narration

Two defects found walking the seams, both the failure mode the skill documents,
both fixed before shipping:

| Seam | Defect | Fix |
|---|---|---|
| 01 → 02 | Scene 02 opened with `“It waits.”` — scene 01's closing sentence rendered **as quoted dialogue**, so Zenvon's narration appeared to be spoken aloud in Pip's hearing | echo line deleted; scene 02 now opens *"Zenvon did not intend to make it wait much longer"*, which reads as a clean continuation of scene 01's *"It waits."* |
| 05 → 06 | Scene 06 opened with *"Then I kept walking."* — a **verbatim duplicate** of scene 05's closer, which would assemble as the same line twice in a row | echo line deleted |

The other four seams were clean.

## Residue check

One mechanical term reached the prose, in scene 01 — the scene narrated from
summary bullets alone: *"The quest log made it look cleaner than it was."*
`quest log` is **already ruled residue** in `notes/scrub_register_policy.md`, so
the standing ruling was applied rather than re-asking. Replaced (not deleted, per
`/scrub`) with *"The list I had copied out…"*, which is in Zenvon's established
note-taking register.

**Open item, upstream:** the source is not a quote but the summary bullet at
`session_summary.md:63` and `:239`, which says "a newly assembled quest log".
The bullet was **not** edited — that is an enhance-layer scope decision, not this
skill's. It will re-seed the same term on any future narration of this scene.

## Correction: the hatch did NOT disappear

The skill predicts that with mechanics removed upstream there is nothing left for
`sd_narrate` to reclassify, so the `<!-- table-speech reclassified: … -->` hatch
may vanish. **That did not happen here.** Four of seven scenes still carry one
(02, 03, 04, 07), and scene 07's hatch reclassifies five of the seven quotes the
GM explicitly ruled KEPT — including Veyra's *"well done"* and the
*"look at her knowingly"* prompt.

So the narrator is still treating GM-voiced character beats as table speech even
after the mechanics are gone. That is a finding about `sd_narrate`, not about the
cut, and it is left open here rather than papered over. **No hatch was
hand-written.** The two scenes with no hatch (01, 05) are the two whose quote
sections were cut in full — there, the prediction held.

## What it bought

Scene 05 (Triboar Trail), narrated from summary bullets alone after a 47/47 cut,
is the clearest case. Every fact from the GM's out-of-character lecture survives
— the High Road running north-south, Neverwinter as the practical frontier, the
Spellplague, "wizards who should have known better" — but re-rendered in Zenvon's
voice as a scout reading a road, instead of quoted as a lecture delivered to a
player over a map. The scene also recovered the party's night watch and the
darkvision split, which the roll-by-roll input had flattened.

As the skill says: the argument is **room**, not correctness.
