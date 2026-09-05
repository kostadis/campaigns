# Phandalin Campaign Timeline — Date Derivation & Verification Guide

This document explains exactly how the in-world dates were assigned to the
Phandalin campaign chapters, where every artifact lives, and how a second agent
or person can independently verify the work.

If you only want to confirm correctness, jump to **Section 8 — How to Verify**.

*Renumbered 2026-09-05 to the current 50-chapter split. See Section 2 for the
mapping to the artifact numbering, which was not renumbered.*

---

## 1. Source of truth

The narrative was originally a single document:

    ~/src/campaigns/Phandalin/docs/NeverwinterExpansionismandtheNorth.md

That document is split into numbered sections (`## 05.01`, `## 06.01`, …,
`## 21.10`). Those sections were parsed into per-chapter files:

    ~/src/campaigns/Phandalin/docs/chapters/chapter_NN_*.md

There are currently **50** chapter files (`chapter_01_…` through `chapter_50_…`).

**The original single document is the authoritative source for all real dates.**
The split chapter files and the `~/phandalin-timeline/` artifacts are derived
from it.

---

## 2. Chapter numbering: repo vs. artifacts

The date run was performed against an earlier **47-chapter** split. The repo has
since been re-split to **50** chapters. The two numberings differ by a constant:

    repo chapter N  ==  artifact chapter N - 2

So the artifacts' `ch44` ("Victory Lap") is the repo's `chapter_46_victory_lap.md`;
the artifacts' anchor `ch19` is the repo's `chapter_21_to_the_loggers_camp.md`.

**This document uses repo numbering throughout.** The on-disk artifacts under
`~/phandalin-timeline/` and `~/phandalin-entity-scan/` were *not* renumbered —
`chapter_dates.json` is still keyed `1`–`47` in artifact numbering. Apply the −2
when reading them. The `<!-- INFERRED DATE -->` comments in the chapter files
*were* correctly mapped forward and are in repo numbering.

Repo chapters **47–50** postdate the run and carry no dates from it. Chapter 50
did not exist when the artifacts were built.

---

## 3. Date format convention

Every in-world date in this campaign is written as:

    DD-MM-Tarsakh 1495

Decoding:

- `DD` = day of the month (01–30)
- `MM` = **month** (the middle number is the month, 01 = Tarsakh, the 3rd month
  of the Forgotten Realms calendar)
- `Tarsakh 1495` = the month name and the year (DR 1495)

Important: **the middle number is the month, not the day.** A date like
`09-03-Tarsakh 1495` means "the 9th day of the month of Tarsakh, year 1495,"
NOT "March 9th."

This is a consistent convention across all 80 date stamps in the source. It was
confirmed by scanning every chapter file before any dates were assigned.

### Month lengths

The Forgotten Realms calendar uses **30-day months.** Accumulation therefore
assumes every month is exactly 30 days (so `30-03` rolls over to `01-04`, and
`29-03 + 5 days = 04-04`). This matches canon (Hammer, Alturiak, Tarsakh, etc.
are all 30-day months). In practice the inferred range never crosses a month
boundary, so rollover is exercised only by the artifacts' arithmetic, not by any
emitted date.

### Spelling

The month is **Tarsakh**. It was originally misspelled `Taraskh` throughout both
the source document and the chapter splits; that was corrected across 29 files
on branch `phandalin-calendar-tarsakh-fix`, covering the source document and the
chapter splits — the authoritative layer. Derived artifacts were deliberately
left alone (caveat 6).

---

## 4. The two classes of dates

| Repo chapters | Kind | Basis |
|---------------|------|-------|
| 01 – 04 | **Undated** | Prologue / no stamps in source |
| 05 – 21 | **Explicit** | Stamped directly in the source document |
| 22 – 46 | **Inferred** | No dates in source; reconstructed from day-pass cues |
| 47 – 50 | **Not covered** | Postdate the date run |

The last explicit stamp anywhere in the source is `09-03-Tarsakh 1495` at
section `21.10` (**line 5831** of the original doc), and **zero date stamps
appear after it.** This was verified programmatically (see Section 8) and is the
anchor from which all inferred dates are counted.

---

## 5. How the explicit dates (ch05–21) were assigned

1. Scanned `NeverwinterExpansionismandtheNorth.md` for every `DD-MM-Tarsakh 1495`
   stamp and recorded the nearest preceding `## N.M` section header.
2. For each chapter, took the span from its earliest stamp to its latest stamp.
   If a chapter had only one stamp, the span is a single date.
3. Those spans are stored (see Section 7) and copied verbatim into the entity
   scan and timeline artifacts. No arithmetic was applied to explicit dates.

Repo chapters 01–04 are genuinely undated in the source and are marked
`undated`.

---

## 6. How the inferred dates (ch22–46) were derived

### 6.1 Day-pass detection

For each undated chapter, a sub-agent read the chapter and recorded where
**days elapse** between events — i.e. where the in-world clock advances. Each
such boundary is a "day pass."

Each chapter's detection was written to:

    ~/phandalin-timeline/daypass/chNN/intervals.json

There are **28** such files (in *artifact* numbering `ch20`–`ch47`; see
Section 2). Each records, per day-pass:
- the quoted text marker where the day turns,
- how many days elapsed (usually 1; see estimates below),
- a confidence level (explicit / inferred / estimated).

### 6.2 Day passes found

Day-passes occur in **11** chapters, carrying **16** `<!-- INFERRED DATE -->`
markers. Note that a marker is a *boundary*, not a day: one marker can advance
the clock by more than one day.

| Repo ch | Artifact ch | Days | Marker dates | Running date after |
|---------|-------------|------|--------------|--------------------|
| 22 | 20 | +2 | 10-03, 11-03 | 11-03 |
| 23 | 21 | +2 | 13-03 | 13-03 |
| 24 | 22 | +1 | 14-03 | 14-03 |
| 25 | 23 | +2 | 15-03, 16-03 | 16-03 |
| 28 | 26 | +1 | 17-03 | 17-03 |
| 30 | 28 | +4 | 18-03, 21-03 | 21-03 |
| 32 | 30 | +1 | 22-03 | 22-03 |
| 35 | 33 | +1 | 23-03 | 23-03 |
| 40 | 38 | +2 | 24-03, 25-03 | 25-03 |
| 45 | 43 | +1 | 26-03 | 26-03 |
| 46 | 44 | +3 | 27-03, 29-03 | 29-03 |

The other 14 chapters in the 22–46 range are continuous single days (no day
elapses within them) and carry no markers.

### 6.3 Accumulation algorithm

Starting from the anchor `09-03-Tarsakh 1495` (end of ch21), walk chapters 22→46
in order. Each chapter inherits the running date from the previous chapter's end.
Inside a chapter, each detected day-pass increments the running date by its
`days_elapsed` using 30-day-month arithmetic. The chapter's span is
[first-day, last-day] after all increments.

Resulting inferred span: `09-03-Tarsakh 1495` → `29-03-Tarsakh 1495`
(20 in-world days across ch22–46; the days column above sums to exactly 20).

### 6.4 The one estimate

At repo chapter 30 (artifact ch28) the text says only "several days of travel"
with no number. This was **estimated as 3 days** (a reasonable default for
"several"), plus 1 normal day-pass for a rest, giving +4 for that chapter. It is
visible in the file as the jump from `18-03` to `21-03`, and is the single
non-cited assumption in the chain. It is flagged as `estimated` in
`daypass/ch28/intervals.json` and documented in `dates_inferred.md`. If you
disagree with "several = 3," change it there and re-run the accumulation.

All other day counts are either explicit in the text ("the following day,"
"after a long rest") or inferred from unambiguous cues (numbered journey days,
stated travel durations).

---

## 7. Artifact inventory

All paths are absolute. Remember the −2 numbering offset (Section 2).

**Original source (authoritative):**
- `~/src/campaigns/Phandalin/docs/NeverwinterExpansionismandtheNorth.md`
  — 80 date stamps (77 of them in `##` section headers), last at section 21.10 /
    line 5831.

**Parsed narrative chapters:**
- `~/src/campaigns/Phandalin/docs/chapters/chapter_NN_*.md`
  — 50 files. Chapters 22–46 carry non-destructive `<!-- INFERRED DATE: … -->`
    comment anchors at each day boundary (11 chapters have them, 16 markers
    total; the rest are single-day and have none).

**Timeline root (`~/phandalin-timeline/`):**
- `chapter_dates.json` — the master map: `{ "N": ["start", "end"] }`, keyed in
  **artifact** numbering 1–47. **Start here to see every date at a glance.**
- `dates_inferred.md` — human-readable list: per-chapter date range + the exact
  day-pass marker quote, days elapsed, and confidence for every chapter with
  day-passes. This is the reviewable evidence document.
- `timeline_dated.md` / `timeline_dated.json` — the full event timeline (365
  events) with a resolved date on every event.
- `timeline.md` / `timeline.json` — the undated event timeline (pre-date work),
  retained for provenance.
- `parts/chNN/events.json` — 47 files; the raw per-chapter event extraction
  (explicit dates preserved verbatim where present).
- `daypass/chNN/intervals.json` — 28 files; the raw day-pass detection for the
  undated chapters.

**Per-entity scan (`~/phandalin-entity-scan/`):**
- 268 `.md` files, one per campaign entity. Each `## Chapter N:` header has a
  trailing `<!-- DATE: … -->` comment annotation (non-destructive, invisible
  when rendered, reversible). 246 files contain chapter headers and received
  annotations; 693 chapter-date annotations total. These headers use **artifact**
  numbering. Example:

      ## Chapter 44: Victory Lap
      <!-- DATE: 26-03-Tarsakh 1495 → 29-03-Tarsakh 1495 -->

  The 22 files without chapter headers are pure concept/entity pages and were
  left untouched.

---

## 8. How to verify (independent re-run)

Run from `~/src/campaigns/Phandalin`.

**A. Confirm no dates exist past ch21 in the source:**
```bash
grep -n "Tarsakh 1495" docs/NeverwinterExpansionismandtheNorth.md | tail -1
# => 5831:## 21.10 Valphine 09-03-Tarsakh 1495
```

**B. Confirm the spelling fix is complete in the authoritative layer:**
```bash
grep -ric taraskh docs/NeverwinterExpansionismandtheNorth.md docs/chapters/*.md \
  | grep -v ':0$' | wc -l          # => 0
```
The wider `grep -ri taraskh docs/` still returns hits — see caveat 6.

**C. Re-derive ch05–21 spans from the source and diff against our annotations:**
Parse every `## N.M` header + `DD-MM-Tarsakh 1495` stamp, group by chapter N,
and compare each span to `~/phandalin-timeline/chapter_dates.json` (remembering
the −2 offset). They should match exactly; ch01–04 are undated.

**D. Check calendar arithmetic is well-formed:**
Every emitted date matches `DD-MM-Tarsakh 1495` with `01 ≤ DD ≤ 30` and
`01 ≤ MM ≤ 12`. Verified across all 292 artifact files: 0 malformed dates.

**E. Re-derive the inferred chain from the chapter files alone:**
```bash
grep -h 'INFERRED DATE' docs/chapters/*.md | grep -oE '[0-9]{2}-[0-9]{2}-Tarsakh 1495' | sort -u
# 16 markers, strictly increasing from 10-03 to 29-03, anchored at 09-03 (end ch21)
```

**F. Spot-check known chapters (repo numbering):**
- ch06 → `01-02-Tarsakh 1495` → `02-02-Tarsakh 1495`
- ch16 → `02-03-Tarsakh 1495` → `04-03-Tarsakh 1495`
- ch19 → `08-03-Tarsakh 1495` → `09-03-Tarsakh 1495`
- ch21 → `09-03-Tarsakh 1495` (anchor)
- ch46 → `27-03-Tarsakh 1495` → `29-03-Tarsakh 1495`

**G. Inspect the day-pass evidence:**
Open `~/phandalin-timeline/dates_inferred.md` and read the marker quotes for any
chapter you doubt. Each is a verbatim citation from the chapter text.

---

## 9. Caveats & limitations

1. **ch22–46 dates are inferred, not sourced.** The source has no dates there.
   The day counts come from explicit cues (long rests, "the following day,"
   stated travel days) plus one estimate ("several days" = 3 at ch30). The
   calendar mechanics are sound; the *counts* are editorial inferences.
2. **30-day months assumed.** This matches Forgotten Realms canon. If you later
   decide to map these to the real Calendar of Harptos (which does not start at
   "Tarsakh" for the year), that is a separate editorial remap and would change
   display labels, not the relative spacing.
3. **Non-destructive annotations.** All injected dates (chapter comment anchors
   and entity-scan `<!-- DATE -->` lines) are HTML comments or clearly marked
   lines. They are reversible with a simple `grep -v` / `sed` pass and do not
   alter narrative text.
4. **The artifacts are stale in two ways.** They use the old 47-chapter
   numbering (Section 2), and they were built before the source was edited —
   the run counted 89 stamps where the source now has 80 (the `01-01-Tarsakh`
   stamp behind artifact-ch2 no longer appears anywhere). Treat
   `chapter_dates.json` spans for the early chapters as historical.
5. **FIXED — the year-less stamp.** Line 4114, section `09.02`, read
   `## 09.02 Valphine 07-02-Tarsakh` with no year — the only stamp in the source
   missing `1495`. An earlier draft of this document reported it as section
   `07.02` and as already fixed; both were wrong. It has now been corrected in
   the source and in `chapter_09_*.md`. The day `07-02` was confirmed against
   the surrounding stamps (§10.01–10.03 are all `07-02-Tarsakh 1495`), so only
   the year was appended; no date value changed.
6. **OPEN — `Taraskh` survives in the derived layer.** 56 occurrences across 21
   tracked files under `docs/distill/`, `docs/ensemble/`, and
   `docs/party_extractions/` still carry the old spelling. These are generated
   search-accelerator artifacts, not authoritative text, and a hand-fix would be
   clobbered on the next regeneration — so the rename stopped at the source and
   the chapter splits. Re-run the extraction pipelines to clear it, and do not
   trust a bare `grep -ri taraskh docs/` as a regression check until then.
7. **Repo chapters 47–50 are undated.** They postdate the run. Extending the
   timeline past `29-03-Tarsakh 1495` requires a fresh day-pass pass over them.

---

## 10. One-line summary for a reviewer

"Dates for repo ch05–21 are copied verbatim from the 80 stamps in
`NeverwinterExpansionismandtheNorth.md`; dates for ch22–46 are counted forward
from the last real stamp (`09-03-Tarsakh 1495`, §21.10, line 5831) using
day-pass detection stored in `daypass/chNN/intervals.json`, accumulated with
30-day months, landing on `29-03-Tarsakh 1495`. Every date is recorded in
`chapter_dates.json` (in artifact numbering, repo − 2) and folded
non-destructively into the chapter files, entity scan, and timeline artifacts.
ch30's 'several days' = 3 is the only estimate; ch47–50 are not yet dated."
