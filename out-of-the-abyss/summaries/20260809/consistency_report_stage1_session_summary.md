# Consistency Report — Stage 1, `session-summary.md`

**Session:** 2026-08-03 (played), exported 2026-08-09 — Chapter 63
**Run:** `/staged-consistency`, 2026-08-29, artifact mode. Full re-run of all stages.
**Prior passes on this session:** stage-0 check 2026-08-09 (`2a4a15a4`); full staged pass
2026-08-19 (`9fa79061`, 67 findings, 10 rulings, **no report files written** — its rulings
survived only in the commit message, which is why this file exists).

---

## Headline

**`session-summary.md` was the stale layer.** The 08-19 pass corrected `gm-assist.md` and
the scene extractions thoroughly and left stage 1 behind. That is the worst place for it:
`.cg/activity.jsonl` shows `enhance` writing this file at 18:10 and `extract` reading it at
19:01, so scene 03's summary block is generated from these bullets. Re-running the pipeline
would have pushed every error here back down into scene files that were already correct.

---

## Findings

| # | Severity | Finding | Ruling |
|---|---|---|---|
| 1 | Critical | Simulacrum ruling absent at 7 of 10 Manshoon mentions (L34, 106, 112, 114, 155, 184, 205) | **approved** |
| 2 | Critical | L108 `"sticking in the middle of Zalthir"` — ruled → Glabbagool 08-19, logged in the glossary, never applied here | **approved** |
| 3 | Critical | Root cause: the cleaned VTT's `Gabriel → Zalthir` player-scrub eats ASR garbles of Glabbagool (3 hits) | **approved** — filed as `notes/issues/20260829_gabriel_scrub_eats_glabbagool.md` |
| 4 | Moderate | L67 scrape-it-off ruling credited to "The DM"; tape `:787` is **Grygum** | **approved** |
| 5 | Moderate | L25 "before he could escape with the sapphire" — he searched and found nothing | **rejected** — GM keeps it as dramatic framing |
| 6 | Moderate | L88 Street Justice / Sturdy Knot stated backwards | **approved** |
| 7 | Moderate | L91 "his documented build lands at 18–19" is wrong; passive Investigation is 24 | **approved** — closes an 08-19 open item |
| 8 | Moderate | L98 Thorin's guardian ability is **Sentinel** (PHB-2024 207), on his sheet | **approved** — closes the second 08-19 open item |
| 9 | Moderate | L239 dangling sentence quoting a GM slip ("stole the key" — he took the **gem**) | **approved** |
| 10 | Minor | L57 vs L102 — A'lai's shriek rendered two ways in one file | **discuss** → carried to stage 2, settled there as **KEEP** |
| 11 | Minor | L72 "canonically establishes" — wording overturned on 08-09 still standing | **approved** |
| 12 | Minor | L142 Kalan quote welds two cues, drops "Right?" | **approved** |

**Applied without asking (mechanical):** duplicated "and and" (L145); quote tense
`prepare` → `preparing their monographs` (tape `:1431`; L23 already correct); the
"(as transcribed)" hedge dropped from "Hill Strike" — real, **Strike of the Giants
(Hill Strike)**, GotG 19, `Thorin-level-08.md:117`.

**Checked and dismissed:** "a conventional loop" (L214) — the "a" is on the tape in Daz's
prior cue, split by Thorin's interruption. A `verify_quotes.py` false positive.

---

## The two open items from 2026-08-19, both closed

Both were carried forward as "needs a character sheet rather than a ruling". `docs/party/`
holds the sheets and answers both. **Note the sheets are level 08 and the party levelled to
9 during this session** (`cleaned.vtt:83`, `:95`) — every number below reconciles only once
that is applied.

- **Daz's passive Investigation 24.** Sheet gives 23 at 8th level with Investigation +8.
  Proficiency goes +3 → +4 at level 9, making it exactly **24** — which is what Daz says on
  tape (`:2119`). The recap was right; the doubt note was wrong, and its "18–19" figure
  matches nothing on the sheet.
- **Thorin's guardian ability.** `Thorin-level-08.md:114` — **Sentinel** (PHB-2024 207).
  *Guardian*: Opportunity Attack when a creature **within 5 ft** takes the Disengage action.
  *Halt*: Speed 0 on a hit. **Still a GM call:** whether the assassin passed within 5 ft.

Two other numbers reconcile the same way and needed no ruling: Daz's max HP 56 (sheet 50 at
L8; Daz states 56 on tape `:3267`) and Zalthir's 57 (sheet 51 at L8; stated on tape `:1675`).
