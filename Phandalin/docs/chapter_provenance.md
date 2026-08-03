# Chapter provenance

**This bible is not a uniform corpus.** `NeverwinterExpansionismandtheNorth.md`
is the output of roughly five successive narrative-generation approaches
layered over each other across the life of the campaign. Chapters differ in
narrative person, in heading convention, in whether scene order tracks
narrative order, and in whether a session recording exists behind them at all.

Any tool that assumes one structure will produce **plausible, wrong** results
on this bible. That is not a hypothetical — see *Evidence* below.

This file records what each chapter *is*. It deliberately does **not** record
what to do about it: routing decisions change, provenance doesn't.

---

## Evidence

A scene-boundary tool (`scene_map`, CampaignGenerator PR #227) tried to recover
per-scene boundaries by anchoring a derived summary's scene list into chapter
prose. Across chapters 2–30 it reported 147 of 148 scenes anchored — 99%.

The real figure was **129 distinct boundaries from 148 scenes, 87%**. Eighteen
anchors landed on positions already claimed by another scene, silently
collapsing them. The metric counted attempts that returned a value, not
boundaries that existed.

The tool was not broken. It was applied to a corpus whose scenes were written
under several different conventions, some of which have no locatable boundary
to find. PR #227 was closed as obsolete.

---

## Per-chapter table

`1p‰` / `3p‰` are crude proxies — occurrences of `I|my|me` and
`the party|they|their` per 1000 words. They separate first- from third-person
blocks reliably; they cannot distinguish two first-person blocks written by
different generators.

| Ch | Title | Words | 1p‰ | 3p‰ | Person | Headings | Model |
|---:|---|---:|---:|---:|---|---|---|
| 1 | Neverwinter Expansionism and the North | 632 | 0 | 1 | 3rd | none | lore excerpt |
| 2 | Arrival in Phandalin | 5352 | 7 | 7 | mixed | `CC.SS` ×13 | A |
| 3 | To find a shapeshifter | 2985 | 8 | 4 | 1st | `CC.SS` ×6 | A |
| 4 | The Bard, the Kings, and the Carver | 2589 | 51 | 5 | 1st | `CC.SS` ×9 | A |
| 5 | Saving Adabra | 3699 | 50 | 2 | 1st | `CC.SS` ×8 | A |
| 6 | Vukradin, Rank Cheval | 2990 | 40 | 6 | 1st | `CC.SS` ×9 | A |
| 7 | Conflict-free gold, a curious side quest… | 1931 | 38 | 7 | 1st | `CC.SS` ×2 | B |
| 8 | The Tower of Storms | 1302 | 43 | 7 | 1st | `CC.SS` ×3 | B |
| 9 | The Beating Heart of the Storm | 2492 | 54 | 3 | 1st | `CC.SS` ×4 | B |
| 10 | Phandalin: Old Debts and New Suspicions | 3507 | 35 | 10 | 1st | `CC.SS` ×7 | B |
| 11 | The stag, the brambles, the wolves… | 1672 | 52 | 5 | 1st | `CC.SS` ×3 | B |
| 12 | Naturalists and Interventionists | 3508 | 37 | 3 | 1st | `CC.SS` ×4 | B |
| 13 | Confronting Adabra | 2714 | 42 | 6 | 1st | `CC.SS` ×5 | A |
| 14 | The Butterskull Quest | 460 | 6 | 6 | mixed | `CC.SS` ×2 | A |
| 15 | Freeing Big Al, Petunia… | 1913 | 38 | 4 | 1st | `CC.SS` ×3 | A |
| 16 | Deals with Harbin, and Sister Kaella… | 3926 | 73 | 3 | 1st | `CC.SS` ×4 | A |
| 17 | Blood Money, Clean Gold, and Fine Wine | 1394 | 0 | 21 | 3rd | `CC.SS` ×2 | C |
| 18 | Falcon's Hoard and Hidden Truths | 620 | 1 | 14 | 3rd | `CC.SS` ×1 | C |
| 19 | To the Logger's Camp | 1695 | 61 | 1 | 1st | `CC.SS` ×10 | A |
| 20 | The Spiral's Grasp | 1062 | 0 | 49 | 3rd | none | D |
| 21 | When Boars Are More Than Just Boars | 1096 | 0 | 24 | 3rd | none | D |
| 22 | From Retreat to Redemption (and Cheese) | 1267 | 0 | 38 | 3rd | none | D |
| 23 | The Ale, the Ex, and Axeholm | 901 | 0 | 34 | 3rd | none | D |
| 24 | Where Reality Unravels: Breaching Axeholm | 643 | 0 | 20 | 3rd | none | D |
| 25 | From Out-of-Phase Dwarves… | 998 | 0 | 33 | 3rd | none | D |
| 26 | Sisters Against the Machine | 1017 | 0 | 33 | 3rd | none | D |
| 27 | When the Machine Screams | 906 | 0 | 20 | 3rd | none | D |
| 28 | Drones, Dread, and Dangerous Deliveries | 977 | 0 | 29 | 3rd | none | D |
| 29 | A Cheesy Compromise in the Mine | 795 | 0 | 25 | 3rd | none | D |
| 30 | Brewbarry's Bloody Axe and the Beer Blight | 1889 | 0 | 32 | 3rd | `## **Scenes**` + 16 `###` | E |
| 31 | A Grave New Friend and a Glimmering Blade | 1128 | 0 | 12 | 3rd | `## **Scenes**` + 14 `###` | E |
| 32 | Silencing the Siren's Warning | 858 | 0 | 15 | 3rd | `## **Scenes**` + 10 `###` | E |
| 33 | The One Hit Point Principle | 9684 | 43 | 8 | 1st | `## **POV — Scene**` ×9 | F |
| 34 | The Carver is not the Carver | 5438 | 42 | 3 | 1st | `## POV — Scene` ×5 | F |
| 35 | A dragon defeated, a bard tempted… | 5760 | 47 | 4 | 1st | `## POV — Scene` ×6 | F |
| 36 | A Gem of a Problem, A Rat of a Solution | 5094 | 48 | 5 | 1st | `## POV — Scene` ×5 | F |
| 37 | The Intervention | 10997 | 41 | 7 | 1st | `## POV — Scene` ×8 | F |
| 38 | The Charge of the Light Brigade | 8644 | 39 | 7 | 1st | `## POV — Scene` ×8 | F |
| 39 | Through the valley to the top of the hill | 5160 | 33 | 3 | 1st | `## POV — Scene` ×5 | F |
| 40 | Unraveling the Storm God's Secrets | 5481 | 39 | 5 | 1st | `## POV — Scene` ×5 | F |
| 41 | A Storm is Coming | 4982 | 34 | 6 | 1st | `## POV — Scene` ×5 | F |
| 42 | The Aasimar has Landed | 6372 | 38 | 4 | 1st | `## POV — Scene` ×6 | F |
| 43 | The Unfated Routine of Rimardo and Corrin | 6202 | 40 | 9 | 1st | `## POV — Scene` ×6 | F |
| 44 | Victory Lap | 7384 | 48 | 7 | 1st | `## POV — Scene` ×8 | F |
| 45 | Universal Basic Treasure | 7558 | 43 | 6 | 1st | `## POV — Scene` ×6 | F |

## The models

**A — first-person POV prose, sequential** (2–6, 13–16, 19).
Scene order tracks narrative order. Headings are `## CC.SS <POV> <in-world date>`,
hand-authored, globally unique, sequence unbroken.

**B — LLM-generated narrative** (7–12).
Reads first-person and is factually accurate, but **scene order does not
strictly track narrative order**. Not distinguishable from model A by any
mechanical signal — both sit at 35–54‰ first-person. This boundary was
established by GM reading for accuracy and cannot be re-derived from the text.

**C — third person** (17–18). Carries `CC.SS` headings but no POV name.

**D — third-person session summaries** (20–29). No headings of any kind. One
logical scene per chapter; `chunk_by_scenes` returns `None` and callers fall
through to character-count chunking.

**E — scene summaries** (30–32). 40 named scenes across three chapters, but
each list sits under a `## **Scenes**` wrapper. Since `chunk_by_scenes` splits
on `##` and consults `###` only when no `##` exists, the wrapper defeats the
scene titles and the whole chapter collapses to one chunk.

**F — current deterministic model** (33–45). `## <POV> — <Scene Title>`, which
`chunk_by_scenes` recognises as the `h2_speaker` convention and
`annotate_pov` reads for carry-forward speaker banners. This is the target
shape.

## Recording coverage

**Unknown for every chapter.** There is no chapter→session mapping recorded
anywhere:

- No `<!-- chapter: N | session: YYYYMMDD -->` markers in the bible.
  `split_chapters` supports them and would carry them into per-chapter
  frontmatter; this bible has zero.
- No `session:` frontmatter in any file under `docs/chapters/`.

What exists locally: **14 session directories** (`summaries/`,
`summaries/old/`) dated 2026-03-18 → 2026-06-23, holding 20 `.vtt` files across
**13 distinct sessions** (most sessions have both a raw and a `.cleaned`
transcript). **No audio is stored in this tree** — the recordings are in Zoom
cloud.

The exception is `old/20260324/`, which has **no VTT anywhere** yet does have
`vtt_extractions/` and `vtt_roleplay_extractions/` directories. That session
was transcribed at some point and the transcript is no longer in the tree — so
recorded-session count is at least 14, and the local VTT set is already known
to be incomplete.

13 VTTs against 13 chapters in model F (33–45) is suggestive but **unverified**.
Do not act on it as if it were established.

The numbered directories `summaries/1/` … `summaries/39/` are a separate
2026-08-01 batch of LLM-generated summaries with no recording behind them; they
contain fabricated quotes and module-canon backfill and are not evidence of
session coverage.

## Known defects

Minor, recorded so they aren't rediscovered:

- Chapter 8 alone uses the `X's Perspective` suffix in scene headings.
- `Valphine Sotorra` appears in 02.02/02.05/02.08/02.11, plain `Valphine`
  everywhere else — including 02.12, in the same chapter.
- Scenes 17.01, 17.02 and 18.01 carry a date but no POV name.
- Bible chapter titles for 33, 40 and 43 begin with stray punctuation
  (`: `, `— `).
- Chapters 2 (7‰) and 14 (6‰) have first-person density far below their
  model-A neighbours' 35–73‰. Possibly sub-boundaries; possibly just chapter 2
  being dialogue-heavy and chapter 14 being only 460 words.

---

*Chapter numbering shifted once during the 2026-08-02 editing pass — a chapter
was removed from the 20s and everything above it moved down one. Any reference
to a chapter number predating that should be treated as suspect.*
