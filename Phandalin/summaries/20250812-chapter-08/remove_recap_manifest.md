# remove-recap manifest — 20250812 (Chapter 8, Tower of Storms)

**Run:** 2026-09-04
**Ruling: NO CUT.** Chapter 8 contains no recap. Nothing was removed from any layer.

Recorded because a null result that is not written down gets re-litigated, and
because this chapter is an instructive *negative* case: it has the shape a recap
detector reaches for, and it is not one.

---

## Why the detector returned nothing usable

`find_recap.py` scored zero scenes, but not because it looked and found a clean
opening — it never ran its heuristics:

```
01_silence_at_the_tower_of_storms.md   -- no '## Voiced moments' section
... (all 6 scenes, same message)
```

Phandalin's extractions use `## Scene summary` + `## Verbatim moments`. The
script keys on `## Voiced moments`, which is another campaign's schema. **The
0/6 is a parse failure, not an audit**, and reporting it as "no recap detected"
would have been a false clean bill. Everything below was established by hand.

## The three surfaces, checked individually

| # | Surface | State |
|---|---|---|
| 1 | scene 01 in `## Scenes` | **live play.** Every bullet is chapter-8 action, beginning with Vukradin casting Silence. |
| 2 | `## Summary` prose in `session-summary.md` | **clean.** Opens *"The party arrived at the rocky plateau of the Tower of Storms"* — this session's own first beat. |
| 3 | enhanced-summary file | **does not exist.** No `narration/enhanced_sections.md`. The surface that would have carried a recap into every scene prompt is absent entirely. |

Transcript sweep for recap markers (`last time`, `left off`, `recap`,
`previously`, `what happened before`) returned **one** hit across the whole
session — `"I think I cheated last time we played"` at 00:57:29, a table joke
fifty minutes into play. There is no opening recap on the tape. The first four
minutes are dead air, then camera glare, a dog, and Baldur's Gate 3.

## The thing that looks like a recap and is not

Scene 01's `## Verbatim moments` opens with three short blocks:

> **GM** — *recalling where the interrupted battle left off*
> "The harpy sang." / "That's what happened."
>
> **Soma** — *recalling the song's effect*
> "And a couple people got charmed."
>
> **GM** — *clarifying that a single harpy had been singing*
> "Oh, no, it's only one." / "Just put Harpy one." / "Sorry."

**This is a mid-combat resume, not a chapter retelling, and it must stay.**
Chapter 7's own record ends on the harpies' luring song *"leaving them
vulnerable as the session ended on a cliffhanger"* — the two sessions are one
continuous encounter, split by the clock. The charmed condition re-established
in those eight words is the precondition for the session's first action
(Vukradin's Silence removing it), so removing them would leave scene 01 opening
on a spell that dispels a condition the document never established.

The third block is also a **GM correction** — three harpies were circling but
only one was singing. That is the Phase 2 rescue class: a clarification
delivered while re-establishing state, not present in the previous chapter.
Cutting the "recap" blind would have taken it.

## Distinguishing rule this run establishes

> A **chapter recap** retells a *completed* previous session for orientation.
> A **combat resume** re-establishes *live state* in an encounter that never
> ended. The first is duplication; the second is a load-bearing precondition.
>
> The tell is the previous chapter's ending, not the current chapter's opening:
> a chapter that ended on a cliffhanger cannot be recapped, only resumed.

## Cost avoided

The chapter is fully rendered — `plan.md`, six narration scenes, two
`.scrubbed.md`, plus the complete `narration_dgx/` experiment. Per the skill's
cost table, a cut here would have renumbered every scene and required a full
re-narration of both renders. That cost was correctly not paid.

## Carry-forward

- `find_recap.py` cannot read Phandalin extractions (schema mismatch, above).
  Every future `/remove-recap` in this campaign will silently return 0/N until
  the script learns `## Verbatim moments` or the campaign adopts the other
  heading. **Until then, the by-hand three-surface check is the check.**
