# ISSUE — Manshoon's Phantasmal Killer damage: two opposite GM rulings, same day

> ## ✅ RESOLVED 2026-08-27 — **the damage stands. Manshoon took 13 psychic.**
>
> There was never a conflict between two GM rulings. **The audit was wrong, twice,
> for the same reason: it cited RAW without checking which PHB this table runs.**
>
> **PHB 2024 (XPHB), p.304** — *"On a successful save, the target takes half as much
> damage, and the spell ends."* Half of 26 is **13**.
> **PHB 2014, p.265** is materially different — a failed save *frightens* with no
> immediate damage, and a made save deals nothing. That is the text both the stage-1
> pass and stage-2 finding #2 applied.
>
> The GM confirmed 2026-08-27 that the table runs **2024**. Daz was reading 2024 on
> tape, unambiguously: *"he'll have disadvantage on ability checks and attack rolls
> for the duration"* (2014 says *frightened*) and *"if he's successful… he gets half
> the damage."* He rolled 1+9+10+6 = 26; half is 13, the exact figure called.
>
> **So the stage-0 ruling was not an override of RAW — it WAS RAW.**
> `consistency_report_stage0_gmassist.sources.yaml:56` mislabels it as an override.
> The GM never reversed themselves; the audit reversed a correct ruling twice.
>
> **Applied:** 13 psychic damage restored across 9 sites in 3 files, plus two
> consequences the no-damage reading had hidden — the made save **ends the spell**,
> so Manshoon carries **no disadvantage** and **Daz's concentration is free**.
> Residue left deliberately in `scene_extractions/logs/2026-08-27_100935_scene_extract_batched.md`:
> that is a run log and correcting it would falsify the record of what the pass produced.
>
> **The lesson:** never cite RAW without naming the edition. The 5etools MCP was down,
> but the data was on disk at `~/src/5etools-src/data/spells/{spells-phb,spells-xphb}.json`
> and settled it in one read. Tracked as an open skill change in the stage-2 `sources.yaml`.
>
> The account below is preserved as filed, and is wrong where it treats the two
> positions as equally weighted. One correction is marked inline.

---

**Filed:** 2026-08-27
**Resolved:** 2026-08-27
**Severity:** High — this is Manshoon's hit points at the moment Chapter 66
opens. The party's opening round is built on it, and the record currently
asserts one answer while the rulings log asserts the other.
**Scope:** `summaries/20260824/session_2026_08_24_session_2026_08_24.md` (4 sites),
`summaries/20260824/session_summary.md` (4 sites),
`summaries/20260824/scene_extractions/05_…manshoon.md`
**Authoritative sources used to verify:**
`GMT20260825-005740_Recording.transcript.cleaned.vtt` (≈01:32:17),
`summaries/20260824/consistency_report_stage0_gmassist.sources.yaml`

---

## Summary

On 2026-08-27 the GM ruled, in writing, that the damage **was** taken. Later the
same day, twice, the GM approved corrections asserting that it **was not**. The
files on disk carry the second answer. Nobody has been shown both at once.

## The two rulings

**Ruling A — stage 0, recorded at `consistency_report_stage0_gmassist.sources.yaml:56`:**

> post-review, 2026-08-27: "the phantasmal killer damage was taken." Manshoon
> made the save (17) AND took 13 psychic damage. Overrides the RAW reading of
> Phantasmal Killer, under which a successful save deals nothing — the GM
> outranks the PHB at their own table. Matches Daz's own call on tape at
> 01:32:17: "he still took 4… er, 13 points of psychic damage."

Line 124 of the same file states this "CLOSES the open item and REVERSES this
run's initial inference (save-made therefore no damage)." It was applied to four
places in the stage-0 recap.

**Ruling B — stage 1 (2026-08-27) and reaffirmed at stage 2 (18:42 UTC):**

The stage-1 pass found the GM's retraction on tape, immediately after granting
the damage:

> "Okay, so he takes 13 points of psychic damage. Alright, **oop, sorry, that's
> not… no, he should not have taken…**"

and reversed Ruling A, propagating "no damage stands" to stage 0, stage 1 and
later the scene extractions. Stage-2 finding #2 then flagged an internal
contradiction in the same document and the GM approved the fix, which reinforced
"took nothing."

## Why this is not settled

**Neither the stage-1 card nor the stage-2 card told the GM that Ruling A
existed.** Both presented the question as a document-internal inconsistency to be
resolved against the tape and against RAW. So the approvals are not a considered
reversal of an explicit GM ruling — they are answers to a narrower question than
the one that actually matters.

The stage-2 pass only surfaced Ruling A *after* the cards were built, while
reading `sources.yaml` to match the report format. The skill's inventory step
reads `consistency_report_stage*.md` but not the `.sources.yaml` companion,
which is where the rulings log lives.

## The evidence, both directions

**For "took nothing":**
- The GM audibly withdrew it one breath after granting it.
- ~~RAW: Phantasmal Killer deals no damage on a successful save. There is no
  half-damage clause; Daz's "he still took 13" applied a rule the spell lacks.~~
  ⛔ **This bullet is false and is the whole error.** It is the PHB **2014** text.
  Under **PHB 2024**, a successful save deals **half damage** — and Daz's "he still
  took 13" was quoting the rule correctly, not inventing one.
- Every artifact on disk now says so, in eight places — because this audit put it
  there.

**For "13 taken":**
- The GM's own written words, after the session, with the tape available.
- The GM outranks RAW at their own table, and the note says so explicitly.
- "oop, sorry, that's not…" is an unfinished sentence. It is *read* as a
  retraction of the damage; it could as easily have been a retraction of
  something about the save, the disadvantage rider, or the spell's duration.

## What is needed

A single GM ruling, made with both of the above in view. Then:

- **If "took nothing" stands:** nothing to change. Add a line to
  `consistency_report_stage0_gmassist.sources.yaml` marking Ruling A superseded,
  so the next run does not resurrect this.
- **If "13 taken" stands:** revert eight sites across three files — the scene-05
  bullet, and in both `session_summary.md` and the stage-0 recap the combat
  bullet, the Manshoon NPC entry ("He is undamaged going into next session") and
  the Phantasmal Killer spell entry ("no damage stands, which is RAW for a made
  save").

Do not let the pipeline run forward until this is answered — `distill` and
`campaign_state` will bake whichever version is on disk into the grounding docs.

## Related

- Stage-2 report: `summaries/20260824/consistency_report_stage2_scene_extractions.md`
  §2 and **Open item**
- Stage-0 rulings log: `consistency_report_stage0_gmassist.sources.yaml:56, 124`
- Review artifact: https://claude.ai/code/artifact/d57b8740-0bc4-47fc-85c0-1902599d315a
