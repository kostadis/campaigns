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
