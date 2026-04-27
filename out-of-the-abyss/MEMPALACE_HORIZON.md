# MemPalace Horizon — OOTA

Coordination marker between the human and Claude. Tells future
sessions where the palace stands so re-mining decisions can be
explicit.

---

## Current horizon

- **Last campaign chapter played:** 49 — *Out of the Dark and Into the Darkness*
- **Last bible chapter file:** `docs/chapters/chapter_54_out_of_the_dark_and_into_the_darkness.md`
- **Last session date:** 2026-04-20
- **Palace last fully (re)built:** 2026-04-26
- **Embedding device:** CPU (onnxruntime; GPU swap blocked by torch cu13 vs onnxruntime-gpu cu12 mismatch)

> The campaign chapter number (49) and the bible chapter file number
> (54) are different. The bible has 54 split chapters because four
> sub-chapters were inserted during the chapter 18 cluster
> (`# Chapter 18.1`–`18.4` plus `18.05` in the source bible).

## Drawer counts at this horizon

| Wing | Source dir | Files | Drawers |
|------|-----------|-------|---------|
| `chronicle` | `docs/distill_extractions/` | 54 | 1156 |
| `narrative` | `docs/chapters/` | 54 | 1170 |
| `abyss` | root campaign reference | 159 | 1482 |
| **Total** | | **267** | **3808** |

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

Safe to delete both once a few sessions confirm the current palace
is healthy.

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
