# MemPalace Horizon — Phandalin

Coordination marker between the human and Claude. Tells future
sessions where the palace stands so re-mining decisions can be
explicit.

---

## Current horizon

- **Last campaign chapter played:** *Unraveling the Storm God's Secrets* — bible heading "Chapter 40" (session-summary mislabelled it "Chapter 41"; the bible title is canonical, and going forward releases are tagged by **title slug** rather than number to avoid the ongoing bible-vs-session-summary numbering split)
- **Last bible chapter file:** `docs/chapters/chapter_41_unraveling_the_storm_god_s_secrets.md` (file position 41 = bible heading "Chapter 40"; the splitter numbers files 01-NN by position while the bible's internal headings start at "Chapter 00")
- **Last session date:** 2026-05-12
- **Palace last fully (re)built:** 2026-05-04 — **this release deliberately SKIPPED the palace rebuild.** Mempalace code is in a transitional/unstable state; the existing palace dir was found with quarantined HNSW segments and was moved aside to a backup, but no re-mine was performed. Searches will fail until the palace is rebuilt manually after the mempalace code stabilises.
- **Embedding device:** CPU (onnxruntime; matches OOTA — GPU swap blocked by torch cu13 vs onnxruntime-gpu cu12 mismatch)

> **Chapter-numbering cleanup landed.** `docs/chapters/` now contains
> **41 files for 41 bible chapters** (clean 1:1). The earlier dual-split
> pollution in `docs/doc/chapters/` was removed during this release.
> Releases now use **title-slug tags** instead of chapter numbers, since
> the bible heading numbering and session-summary numbering disagree
> by one and have caused tag collisions in the past.

## Drawer counts at this horizon

**STALE — no re-mine performed this release.** The numbers below are
from the 2026-05-04 baseline and have NOT been refreshed. Don't use
them as a current regression baseline until the palace is rebuilt.

| Wing | Source dir | Files (as of 2026-05-04) | Drawers (stale) |
|------|-----------|--------------------------|-----------------|
| `distill_extractions` | `docs/distill_extractions/` | 40 | 1014 |
| `narrative` | `docs/chapters/` | 76 (now 41 after dual-split cleanup) | 2004 |
| `phandalin` | root campaign reference | 485 | 2617 |
| **Total** | | **601** | **5635** |

Phandalin-wing breakdown (stale): npcs 1972, arcs 369, dead 111,
world 91, mechanics 74.

To refresh after the palace is rebuilt, run `mempalace status` against
the rebuilt palace and replace this block.

> The phandalin-wing file count (485) is high because mempalace mines
> every non-ignored file under the campaign root, including 458 NPC
> dossier files in `docs/npcs/`. Drawer count per file averages ~5.2,
> which is consistent with extracted-snapshot density.

> **Note on wing names.** The colloquial label "chronicle" (used in
> docs and the chapter-release skill) corresponds to the actual wing
> name `distill_extractions` in the palace DB, mirroring OOTA's
> setup. The wing name is auto-derived from the source directory
> basename when no per-directory `mempalace.yaml` overrides it.

---

## Workflow

### Adding a chapter (forward extension)

When the user says **"now we have chapter N"**:

1. Confirm the new bible chapter has been appended to
   `docs/NeverwinterExpansionismandtheNorth.md` and re-split via
   `python ~/src/CampaignGenerator/split_chapters.py` (or whichever
   splitter is canonical for Phandalin once the dual-split mess is
   cleaned up).
2. Re-mine the affected wings (mempalace's file-hash check skips
   unchanged drawers):
   ```bash
   mp="/home/kroussos/worldanvil_pipeline/venv/bin/mempalace --palace phandalin"
   $mp mine /home/kroussos/campaigns/Phandalin/docs/distill_extractions
   $mp mine /home/kroussos/campaigns/Phandalin/docs/chapters
   $mp mine /home/kroussos/campaigns/Phandalin
   ```
3. Bump the **Last campaign chapter played** + **Last bible chapter
   file** entries above. Update the drawer counts.

### Inconsistency rebuild (full reset)

When the user says **"discard, this is the new chapter 0–N"**:

1. Restore campaign content to the desired horizon if needed (git
   checkout, manual edits, etc.).
2. Move the current palace aside:
   ```bash
   mv ~/.mempalace/palaces/phandalin ~/.mempalace/palaces/phandalin.bak.$(date +%Y%m%d-%H%M%S)
   ```
3. Re-mine all three wings in order: distill_extractions → chapters → root.
4. Update this file: bump horizon, refresh drawer counts, note
   what was discarded and why.

---

## Backups currently on disk

- `~/.mempalace/palaces/phandalin.bak.20260504-213838` — pre-rebuild
  snapshot from the migration off the old single-wing setup (7,325
  drawers jammed into the `phandalin` wing). Keep until the new
  three-wing palace is confirmed healthy across a few sessions.
- `~/.mempalace/palaces/phandalin.bak.20260517-172458` — partially
  corrupted snapshot at the start of this release (two HNSW segments
  were quarantined; sqlite was newer than HNSW and failed integrity
  check). Moved aside in preparation for a full rebuild that was then
  deliberately skipped because the mempalace code is unstable. The
  next person to touch the palace should rebuild from scratch rather
  than restore from this backup.

---

## Known caveats at this horizon

- **Palace is absent.** This release skipped the re-mine because the
  mempalace code is in a transitional/unstable state. Searches
  against the phandalin palace will fail until it is rebuilt. Other
  campaigns' palaces (abyss, campaign-dev, chat) are unaffected.
- **HNSW corruption observed.** Two segment files in the pre-release
  palace failed integrity check (sqlite newer than HNSW). The
  corrupted state has been preserved in the 20260517 backup for
  forensics; do not restore it as-is.
- **Dual-split chapter pollution resolved.** `docs/chapters/` is now
  clean (41 files for 41 bible chapters). The earlier `docs/doc/chapters/`
  misdirected output was removed during this release.
- **Bible vs session-summary numbering still disagrees by one.**
  Bible heading "Chapter N" = file position N+1 = session-summary
  "Chapter N+1". Going forward, release tags use title slugs to side-step this.
- **GPU embedding deferred.** Switching to GPU requires resolving the
  torch cu13 vs onnxruntime-gpu cu12 mismatch. Not blocking; CPU
  mine completes in minutes (once the palace is rebuildable).
- **5etools MCP not registered for Phandalin.** Unlike OOTA,
  Phandalin's `.mcp.json` only registers the `campaign` server.
  `docs/adventures/` (Essentials Kit modules) is excluded from the
  palace following the OOTA pattern, so module lookups currently have
  no fallback. Either register 5etools in `.mcp.json` or selectively
  un-ignore specific custom encounter files in `.mempalaceignore`.
