# MemPalace Horizon — OOTA

Coordination marker between the human and Claude. Tells future
sessions where the palace stands so re-mining decisions can be
explicit.

---

## Current horizon

- **Last campaign chapter played:** 50 — *Candlekeep Library and the Littlest Drow in Faerun* (Eldeth farewell, drow-spy "Polly Pocket", Avowed assignments)
- **Last bible chapter file:** `docs/chapters/chapter_54_candlekeep_library_and_the_littlest_drow_in_faerun.md`
- **Last session date:** 2026-04-28
- **Palace last fully (re)built:** 2026-05-03
- **Embedding device:** CPU (onnxruntime; GPU swap blocked by torch cu13 vs onnxruntime-gpu cu12 mismatch)

> The campaign chapter number (50) and the bible chapter file number
> (54) are different. The bible has 54 split chapters because the
> source contains five sub-chapters in the chapter 18 cluster
> (`# Chapter 18.05`/`18.1`–`18.4` in `docs/TheUnderdark.md`), and
> the splitter assigns file numbers by encounter order — so source
> heading "# Chapter 50" lands as `chapter_54_…` after the offset.

## Drawer counts at this horizon

| Wing | Source dir | Files | Drawers |
|------|-----------|-------|---------|
| `chronicle` | `docs/distill_extractions/` | 55 | 1547 |
| `narrative` | `docs/chapters/` | 54 | 1239 |
| `abyss` | root campaign reference | 173 | 1585 |
| **Total** | | **282** | **4371** |

Use these as the regression baseline — significant drift on a no-op
re-mine probably means content was added/removed unintentionally.

---

## Workflow

### Adding a chapter (forward extension)

When the user says **"now we have chapter N"**:

1. Confirm the new bible chapter has been appended to
   `docs/TheUnderdark.md` and re-split via
   `python ~/src/CampaignGenerator/split_chapters.py`.
2. Re-mine the affected wings (mempalace's file-hash check skips
   unchanged drawers):
   ```bash
   mp="/home/kroussos/worldanvil_pipeline/venv/bin/mempalace --palace abyss"
   $mp mine /home/kroussos/campaigns/out-of-the-abyss/docs/distill_extractions
   $mp mine /home/kroussos/campaigns/out-of-the-abyss/docs/chapters
   $mp mine /home/kroussos/campaigns/out-of-the-abyss
   ```
3. Bump the **Last campaign chapter played** + **Last bible chapter
   file** entries above. Update the drawer counts.

### Inconsistency rebuild (full reset)

When the user says **"discard, this is the new chapter 0–N"**:

1. Restore campaign content to the desired horizon if needed (git
   checkout, manual edits, etc.).
2. Move the current palace aside:
   ```bash
   mv ~/.mempalace/palaces/abyss ~/.mempalace/palaces/abyss.bak.$(date +%Y%m%d-%H%M%S)
   ```
3. Re-mine all three wings in order: chronicle → narrative → root.
4. Update this file: bump horizon, refresh drawer counts, note
   what was discarded and why.

---

## Backups currently on disk

- `~/.mempalace/palaces/abyss.bak.20260425-222447/` — pre-rebuild snapshot from before this work began (pre-renumber, polluted by old splitter)
- `~/.mempalace/palaces/abyss.bak.20260426-071851-cpu-polluted/` — first CPU re-mine that included `TheUnderdark.md` due to a stale `.mempalaceignore` rule (file had been renamed `The Underdark.md` → `TheUnderdark.md`)
- `~/.mempalace/palaces/abyss.bak.20260503-100052/` — pre-chapter-50 snapshot (last horizon: chapter 49, narrative wing's chapter files numbered with the old `chapter_01_arrival` prologue prefix)

Safe to delete the older two once a few sessions confirm the current
palace is healthy. Keep `20260503-100052` until the chapter-50
re-split has been confirmed correct.

---

## Known caveats at this horizon

- **`.mempalaceignore`** was updated this rebuild to reference the
  renamed `docs/TheUnderdark.md` (no space). Don't revert.
- **Drawer count vs. `MEMPALACE.md` doc estimates:** the doc was
  written when the palace held ~10,300 drawers. Current total is
  ~3,800, mostly from a more conservative chunking strategy in the
  current mempalace version. Retrieval still works (sanity queries
  pass); just calibrate "expected drawer count" against this file,
  not the doc.
- **GPU embedding deferred.** Switching to GPU requires resolving
  the torch cu13 vs onnxruntime-gpu cu12 mismatch (e.g., installing
  CUDA 12 runtime libs alongside torch's bundled CUDA 13). Not
  blocking; CPU mine completes in minutes.
