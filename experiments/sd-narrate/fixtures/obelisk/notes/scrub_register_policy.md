# Scrub register policy — obelisk

Standing GM rulings on what is **not** residue, so `/scrub` stops re-proposing
them. Read this at Phase 0, before walking any candidates.

**None of it is scannable.** `find_residue.py` matches numbers, fixed table-speak
phrases and player names; it cannot match vocabulary at all, by design (see the
skill's hard invariant). This file is the only thing that stops the next run
re-asking a settled question — and a settled ruling re-asked is a settled ruling
put back at risk.

Created 2026-09-04 during the Chapter 10 narration scrub.

---

## The register: ren-faire, except where Faerûn has its own word

*(GM ruling, 2026-09-04)*

**Ren-faire.** Modern idiom is in-canon. The players are people playing at
period, the anachronisms are theirs, and they stay verbatim. Do not propose
scrubbing a modern turn of phrase merely for being modern.

**The exception: where a canonical Faerûn word exists for the thing, it wins.**
Not a matter of register — a real-world proper noun for something Faerûn already
names is simply the wrong word. `Monday` → `Firstday`.

**The corollary, and the line that actually did the work this run: the policy
licenses the table, not the narrator.** An anachronism a player said on tape is
covered. One the *narrator* invented is not, because no player chose it and it
was never part of the campaign's voice. Check the smoothed extraction before
proposing — `“Medic!”` was scrubbed on exactly this basis while
`“Monday, Tuesday, Wednesday”` (on tape) was only converted, not cut.

## Calendar

- **Tenday day names are Firstday, Secondday, Thirdday … Tenday.** Adopted
  2026-09-04. The campaign had no calendar before this — `notes/everyone_is_a_suspect.md:352`
  records that no campaign doc sets one. There is still no calendar doc; this is
  the whole of the ruling.
- `“twice on the tenth day”` is kept as spoken.

## Ruled in-canon — never propose these again

| Term | Where | Ruling |
|---|---|---|
| `God's plan` | ch10 sc03 | Keep. Ren-faire. |
| `chunk of change` | ch10 sc05 | Keep. Ren-faire. |
| `keep your eyes peeled` | ch10 sc04 | Keep. Ren-faire. |
| `professional road security` | ch10 sc03 | Keep — it is Pip's established register, in `voice/pip_voice.md`. |
| `“Generous to what?”` | ch10 sc04 | **Keep.** An ASR garble that produced a working mishearing beat; the surrounding lines absorb it in-voice. Closed as *kept*, not outstanding. |

## Classes that ARE residue here

- **Transcript artifacts** — a literal `[unclear]` / `[inaudible]` in finished
  narration is always a candidate.
- **Uncarded ASR garbles** that mean nothing in English (`rough-ins`). Note the
  remedy is a GM choice between recovery and rewrite, and it is not automatic:
  ch10 declined `ruffians` (the likelier recovery) in favour of `marauders`
  (Hamun's own word two lines earlier).
- **Virtual-tabletop and quest-log tooling** narrated as in-fiction dialogue —
  `your pointer`, `quest log`, `question mark`, `you moved us there`,
  `teleport to the quest location`. This is `sd_narrate` failing to reclassify,
  not a register question. Prefer fixing the upstream extraction and re-running
  the scene over hand-excising twenty spans, and **never hand-write a
  `<!-- table-speech reclassified -->` hatch** to cover it.

  **Precedent, ch10 scene 02 (2026-09-04):** where a scene's captured quotes are
  *entirely* mechanical, the ruling is not "scrub the worst spans" but "none of
  this is roleplay" — cut the whole `## Voiced moments` section at the smoothed
  layer with an audit note, and re-run `sd_narrate --scene N` so the scene is
  narrated from its summary bullets alone. That produced a scene with zero
  quoted lines, which was the correct outcome: the party over a map, deciding.
  Check for this shape whenever a scene is planning or logistics rather than
  encounter or conversation.

## Recaps and table mechanics — standing rulings (2026-09-04)

Added during the Chapter 10 `/remove-recap` + `/no-mech` run. None of it is
scannable; this file is the only thing that stops the next run re-asking.

**Recaps are cut by default.** The recording opens with the GM catching the table
up on last time; that belongs to the previous chapter's document, which already
exists. Cut all three surfaces in one pass — the scene, the `## Summary` prose in
`session_summary.md`, and the enhanced-summary file that `sd_narrate` takes as its
recap argument. The scheduling chatter that precedes a recap goes with it.

**Rescue before cutting, always.** A recap can carry canon that cannot exist in
the previous chapter — ch10's recap is where the party learned the sword is named
**Talon**, because the GM read the name aloud and then said "Fine. We now learned
its name." Rescued content goes to the **entity's own record**, not smuggled into
a scene it did not happen in.

**Roll callouts inside roleplay scenes: cut the call and the number, keep the
result.** "Roll an Insight check" and "Fourteen?" go; what the character learns
from it stays. Ruled ch10 sc04/05/07.

**Mechanical rewards and their bookkeeping are cut** — the +1 Investigation
bonus award in ch10 sc03, and the four lines of "make a note of it" that followed.

**But an out-of-character exchange that pays off an in-fiction beat is KEPT.**
Ch10 sc03: the GM denied Daran ever mentioned Netheril, Zenvon's notes proved
otherwise, and the GM conceded — *"Thank you, I think that's why we have the
notes."* That is the payoff to Daran's ten-minute lecture and it stays. The test
is not "is this out of character" but "does cutting it cost a beat".

**Wall-clock and session-scheduling talk is always cut.** "it's almost 7.40",
"we'll continue next week".

**A GM prompt that sets up a character beat is KEPT even though it is mechanically
shaped.** Ch10 sc08: *"Do you want to tell her anything, or just look at her
knowingly?"* produced the best moment in the scene.

## Chapter 11 no-mech rulings (session 011, 2026-09-06)

### Speaker-label signal is dead by campaign convention

Across all seven Chapter 11 scenes, NPC dialogue remains under the `GM` outer
label. The useful identity signal is the italic direction (`as Hamun Kost`, `as
Pip`, and similar), not a distinct NPC speaker label. Future `/no-mech` runs
must never treat `GM` as evidence that a quote is mechanical; classify from the
direction and the full exchange.

### Session-specific scope rulings

- Cut roll calls and numeric roll reports, initiative and damage arithmetic,
  rules lookups and tutorials, character-sheet/VTT operation, level-up and
  spell-selection administration, and session scheduling. Preserve the
  fictional outcome and any character beat that follows.
- Preserve exploration and encounter prompts when they set up an actual choice
  or character response.
- Preserve the pike/bike misunderstanding, praise for the clever illusion plan,
  and the “one glorious point of damage” exchange as table texture.
- Cut the unresolved “second toy” request, the Maela missed-roll exchange,
  “Rolling for attack,” “Almighty God, Master,” and the closing “this was fun”
  exchange. These are exact Chapter 11 rulings, not a blanket rule that all
  player reactions should be cut.
- Keep the Sildar/Ruxithid recollection and the explicit clarification that
  Veyra's blue crystal was not disclosed to Hamun. Though delivered partly as
  table clarification, both protect current-story knowledge boundaries.
