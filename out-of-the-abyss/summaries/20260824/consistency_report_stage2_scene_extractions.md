# Consistency Report — Session 2026-08-24 Scene Extractions (Stage 2)

Checked: `scene_extractions/01`–`05`. All fourteen findings are **ruled and
applied**; this document is the propagation checklist for the next run, not a
list of open work. One item is open and it is *not* from this stage — see
**Open item** at the foot.

The stage-2 layer is the one that carries verbatim quotes into narration.
Findings #1, #6 and #7 below existed **only** here: they entered by lifting a
quote from the tape, which stages 0 and 1 never do.

---

## 1. Critical: "Alyss proved right" names a person who does not exist

- **Location**: `01_the_long_descent.md:45–46`
- **Issue**: A quoted recap line opens "Alyss proved right." No Alyss exists in
  the campaign — not in the registry, not in prep, not at stage 0 or 1.
- **Evidence**: The GM was reading `summaries/20260817/session-summary.md:16`
  aloud; the rest of the quote matches that line word for word. The source text
  is "Thorin, suspicious of the GM's repeated questions about exact positions,
  **was proved right**." The ASR compressed the whole subject clause into one
  name. Not A'lai either — `entity_registry.yaml:2224` has `A'lai Aivenmore`,
  who had nothing to do with the stair.
- **Ruling**: approve.
- **Applied**: quote restored to the source text; attribution line annotated
  with the read-aloud provenance. Stage-2 only, nothing upstream to fix.

## 2. Moderate: the same document says Manshoon took 13 psychic damage and that he took none

- **Location**: `05_…manshoon.md:24`; `session_summary.md:107`
- **Issue**: One bullet read "26 psychic damage (later rolled to 13 relevant
  after the save)"; three bullets later the same file recorded the 13 as called
  and withdrawn, "the save held clean and Manshoon took nothing."
- **Evidence**: Both statements in one document. The narrator lifts from the
  bullets, so the first would have reached prose.
- **Ruling**: approve — **then corrected 2026-08-27 after checking the PHB.**
- **Applied**: the internal contradiction was real and is fixed, but the *direction*
  was wrong. This card asserted "there is no half-damage clause," which is true of
  **PHB 2014** and false of **PHB 2024, p.304**: *"On a successful save, the target
  takes half as much damage, and the spell ends."* This table runs 2024, confirmed
  by the GM. **Manshoon takes 13 psychic damage** — half of 26 — and the made save
  ends the spell, so no disadvantage rider and no ongoing concentration for Daz.
  Conformed across 9 sites in 3 files. The stage-0 ruling was right all along; see
  the resolved Open item.

## 3. Moderate: two different anti-magic fields conflated into one

- **Location**: `02_…obsidian_tower.md:20`; `session_summary.md:52`
- **Issue**: The bullet attributed "It also prevented fire from being cast" to
  the *cavern's* anti-magic field.
- **Evidence**: The verbatim block has the GM separating them explicitly — the
  Candlekeep-wide force field "protected teleportation management magic from
  coming in or out to Candlekeep. It also prevented fire from being cast" (past
  tense, already disabled), and only then "this is sort of a general… anti-magic
  area" for the cavern. Load-bearing for next session's duel.
- **Ruling**: approve.
- **Applied**: bullet split in both files; the citadel ward named as separate
  and already disabled.

## 4. Moderate: shaft depth — 1,000 ft or 1,500 ft

- **Location**: `01_the_long_descent.md:26`; `session_summary.md:7, 39, 116, 165`;
  `session_2026_08_24_…md:7, 29, 88, 137`
- **Issue**: Scene 01 contradicted itself — 500 ft to the catch, "another 500
  feet" to the feather-fall zone, then "approximately 1,500 feet below the
  surface." The GM said both figures in one breath: "you drop another thousand
  feet, 500 feet."
- **Evidence**: Prep is on 1,000 — `20260824_worth_two_faces.md:88` has the rest
  of the party "stuck 900 ft up," and line 452 builds the Dawnbringer cold open
  on "a thousand feet is roughly a hundred seconds" of feather fall.
- **Ruling**: discuss → **GM note: "It was 1000 feet. We agreed on the table."**
- **Applied**: 1,000 ft in seven places across three files; the arithmetic now
  closes (500 + 500). Grygum's two spoken "1500 feet" lines left as spoken —
  they are player dialogue, not narration.

## 5. Moderate: the broken owlbear is filed a scene early

- **Location**: `03_…iron_guardian.md:21`; `session_summary.md:69`
- **Issue**: The destroyed statue sat in scene 03's bullets as though seen on the
  way in.
- **Evidence**: The file's own verbatim block heads it *[The Broken Owlbear
  Discovered]* — "Returning inside after the dragon's boon…" It was found after
  scene 04.
- **Ruling**: approve.
- **Applied**: bullet prefixed with the timing in both files.

## 6. Minor: "Albert" is not a character

- **Location**: `03_…iron_guardian.md:142–143`
- **Issue**: "Albert goes, sorry, sorry, I was reading from the answer key."
- **Evidence**: Every other line in the scene calls the speaker the owlbear or
  the guardian. No Albert in the registry or anywhere in the campaign. Left
  alone it reads as a proper noun the narrator keeps using.
- **Ruling**: approve.
- **Applied**: corrected to "The owlbear goes…", attribution line annotated with
  the garble. Stage-2 only.

## 7. Minor: "Great, Thorin. Thorin is fault." — spliced, and not English

- **Location**: `01_the_long_descent.md:75–76`
- **Issue**: Two GM cues merged across Thorin's interjection, which turns a
  self-correction into what reads as sarcasm aimed at Thorin. "is fault" is a
  garble.
- **Evidence**: Transcript order — GM "Great," → Thorin interjects → GM "Thorin.
  Thorin is fault. Sorry, sorry, Zalthir, sorry." The GM had just misnamed the
  faller as Zalthir; the apology is to Zalthir.
- **Ruling**: approve.
- **Applied**: split into two quoted cues; attribution annotated that the words
  behind "is fault" are not recoverable from the tape. **The GM did not supply
  the actual line**, so the garble stands, marked. Stage-2 only.

## 8. Minor: three phrases in scene 04 wear quote marks but were never said

- **Location**: `04_…dragon_s_trial.md:15, 23, 25`; `session_summary.md:77, 85, 87, 141`
- **Issue**: "what did he take", "are we who we say we are", Manshoon "is still
  inside" — none contiguous anywhere in the transcript.
- **Evidence**: Actual lines — Grygum "tell us **what he took** is interesting,
  too"; GM "You can ask if everyone is **who they say they are**"; GM "He goes,
  **he's still inside**."
- **Ruling**: approve.
- **Applied**: all three replaced with the transcript wording, in both files
  (four sites at stage 1, including the dragon's NPC dossier entry).

## 9. Minor: "OK Corral moment" is the extractor's phrase

- **Location**: `05_…manshoon.md:22`; `session_summary.md:105`
- **Issue**: Presented as a GM quote.
- **Evidence**: The GM said "there's kind of like that, you know, okay corral
  sort of…" and later "yeah, okay, chorale moment, right?" — the transcript's
  garble of the same phrase. The clean quoted form appears in neither.
- **Ruling**: discuss → **GM note: "It's an OK corral moment is a reference to
  the movie, we need to flag this to come up with some in-faerun equivalent."**
- **Applied**: false quote replaced with the real one, plus an inline ⚠️ flag in
  both files. Durable copy filed at
  `notes/issues/20260827_ok_corral_needs_faerun_equivalent.md` — the inline flag
  will not survive the next `extract`.

## 10. Minor: "Tip-top" in the bullets, "Rip-top" in the verbatim block

- **Location**: `03_…iron_guardian.md:13, 49–50`
- **Issue**: One file, two spellings of the same four words.
- **Evidence**: The transcript has "Rip-top"; the bullet had normalised it.
- **Ruling**: approve.
- **Applied**: verbatim block normalised to "Tip-top", attribution annotated with
  what the transcript captured. `session_summary.md:61` already read "Tip-top" —
  no change needed there.

## 11. Minor: "Let him try. Let him try." was two utterances

- **Location**: `04_…dragon_s_trial.md:26, 28`; `session_summary.md:88, 90`
- **Issue**: Merged into one breath; and the GM's "Yeah, yeah, she, yeah, she,
  **yeah, she,** yeah, you can" had lost a repetition.
- **Evidence**: Transcript — GM "Let him try." → Zalthir "Oh, snap." → GM "Let him
  try." The file's own verbatim block gets this right; only the bullet merged it.
- **Ruling**: approve.
- **Applied**: both split/restored in both files.

## 12. Minor: Daz ends the session inside the anti-magic band

- **Location**: `05_…manshoon.md:27`; `session_summary.md:110`; `session_2026_08_24_…md:83`
- **Issue**: The position was recorded; the consequence was not.
- **Evidence**: The GM pinned the field — "the anti-magic shell is on the bridge,
  right? It's not in the tower" — and Zalthir put it at 10 ft. The tower has four
  mounted crossbows. The dragon's 30-ft widening is banked, not spent.
- **Ruling**: approve.
- **Applied**: consequence stated in all three files — Daz opens round two unable
  to cast, which is why the plan was crossbows.

## 13–14. Trivial: auto-applied, not put to the GM

- `02_…obsidian_tower.md:165` — malformed emphasis (`— **noting…*`) repaired.
- `03_…iron_guardian.md:88` — "Yeah, ok, I got a 13" restored to the transcript's
  "Yeah, okay, I got a 13."

---

## Open item — RESOLVED 2026-08-27: the damage stands

**Phantasmal Killer: did the 13 psychic damage stand? — YES.**

`consistency_report_stage0_gmassist.sources.yaml:56` records a direct GM ruling
of 2026-08-27: *"the phantasmal killer damage was taken."* Line 124 states it
"CLOSES the open item and REVERSES this run's initial inference (save-made
therefore no damage)."

Every artifact on disk now says the opposite — "no damage stands" — reversed by
the stage-1 pass on the strength of the GM's on-tape retraction ("oop, sorry,
that's not… no, he should not have taken…"), and reaffirmed here by finding #2.

**Resolution.** The GM asked what the PHB actually says, and the answer settled it
against the audit. `5etools-src/data/spells/spells-xphb.json` — **PHB 2024, p.304**:

> The target makes a Wisdom saving throw. On a failed save, the target takes 4d10
> Psychic damage and has **Disadvantage on ability checks and attack rolls** for the
> duration. **On a successful save, the target takes half as much damage**, and the
> spell ends.

The 2014 text (p.265) is materially different — a failed save *frightens* with no
immediate damage, and a made save deals nothing. **Both the stage-1 finding and
finding #2 above applied the 2014 reading to a 2024 table.**

Daz was reading 2024 on tape, unambiguously: "he'll have **disadvantage on ability
checks and attack rolls** for the duration" (2014 says *frightened*), and "if he's
successful… **he gets half the damage**." He rolled 1+9+10+6 = 26; half is 13, the
exact figure called. The GM confirmed the edition 2026-08-27.

So the stage-0 ruling was not a GM override of RAW — **it was RAW**, and
`consistency_report_stage0_gmassist.sources.yaml:56` mislabels it as an override.
Nothing was reversed by the GM; the audit was simply wrong twice, in the same way,
for the same reason.

**Applied:** 13 psychic damage restored across 9 sites in 3 files, together with the
two consequences the no-damage reading had hidden — the made save **ends the spell**,
so Manshoon carries no disadvantage and Daz's concentration is free.

**The lesson, for the skill:** never cite RAW without naming the edition. See
`notes/issues/20260827_phantasmal_killer_damage_ruling_conflict.md` (resolved).

---

## Summary

| # | Severity | Verdict | Propagated to |
|---|---|---|---|
| 1 | Critical | approve | scene 01 only |
| 2 | Moderate | approve → **corrected** | scene 05, stage 1, stage 0 — 13 psychic damage stands (PHB 2024) |
| 3 | Moderate | approve | scene 02, stage 1 |
| 4 | Moderate | discuss → 1,000 ft | scenes 01, stage 1, stage 0 |
| 5 | Moderate | approve | scene 03, stage 1 |
| 6 | Minor | approve | scene 03 only |
| 7 | Minor | approve | scene 01 only |
| 8 | Minor | approve | scene 04, stage 1 |
| 9 | Minor | discuss → flag | scene 05, stage 1, `notes/issues/` |
| 10 | Minor | approve | scene 03 |
| 11 | Minor | approve | scene 04, stage 1 |
| 12 | Minor | approve | scene 05, stage 1, stage 0 |
| 13–14 | Trivial | auto | scenes 02, 03 |
