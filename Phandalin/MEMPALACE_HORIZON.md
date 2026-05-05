# MemPalace Horizon — Phandalin

Coordination marker between the human and Claude. Tells future
sessions where the palace stands so re-mining decisions can be
explicit.

---

## Current horizon

- **Last campaign chapter played:** 39 — *The Charge of the Light Brigade*
- **Last bible chapter file:** `docs/chapters/chapter_39_the_charge_of_the_light_brigade.md`
- **Last session date:** 2026-04-29
- **Palace last fully (re)built:** 2026-05-04
- **Embedding device:** CPU (onnxruntime; matches OOTA — GPU swap blocked by torch cu13 vs onnxruntime-gpu cu12 mismatch)

> **Known chapter-numbering issue.** `docs/chapters/` currently
> contains **two overlapping splits** (75 files for 39 played
> chapters): the canonical play-session numbering
> (`chapter_NN_<session-title>.md`) and a stale bible-split
> numbering (`chapter_NN_neverwinter_expansionism_…`). The narrative
> wing will mine both until the splitter is re-run cleanly. This is
> tracked as a separate cleanup, not part of the mempalace migration.

## Drawer counts at this horizon

| Wing | Source dir | Files | Drawers |
|------|-----------|-------|---------|
| `distill_extractions` | `docs/distill_extractions/` | 40 | 986 |
| `narrative` | `docs/chapters/` | 75 | 1952 |
| `phandalin` | root campaign reference | 485 | 2513 |
| **Total** | | **600** | **5451** |

Use these as the regression baseline — significant drift on a no-op
re-mine probably means content was added/removed unintentionally.

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

---

## Known caveats at this horizon

- **Dual-split chapter pollution.** `docs/chapters/` has two
  overlapping numbering schemes; the narrative wing will index both
  until the splitter is re-run with a single canonical convention.
  Sanity searches in the narrative wing may return both versions of
  a chapter; treat the play-session-numbered file
  (`chapter_NN_<session-title>.md`) as canonical.
- **GPU embedding deferred.** Switching to GPU requires resolving the
  torch cu13 vs onnxruntime-gpu cu12 mismatch. Not blocking; CPU
  mine completes in minutes.
- **5etools MCP not registered for Phandalin.** Unlike OOTA,
  Phandalin's `.mcp.json` only registers the `campaign` server.
  `docs/adventures/` (Essentials Kit modules) is excluded from the
  palace following the OOTA pattern, so module lookups currently have
  no fallback. Either register 5etools in `.mcp.json` or selectively
  un-ignore specific custom encounter files in `.mempalaceignore`.
