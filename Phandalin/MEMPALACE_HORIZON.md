# MemPalace Horizon — Phandalin

Coordination marker between the human and Claude. Tells future
sessions where the palace stands so re-mining decisions can be
explicit.

---

## Current horizon

- **Last campaign chapter played:** *A Storm of Bolts and Orcs* — session-summary "Chapter 42" = bible heading "Chapter 41 A Storm is Coming" (same +1 numbering split as last release; the bible's title differs slightly from the session-summary's working title)
- **Last bible chapter file:** `docs/chapters/chapter_42_a_storm_is_coming.md` (file position 42 = bible heading "Chapter 41")
- **Last session date:** 2026-05-19
- **Palace last (re)mined:** 2026-05-22 — incremental re-mine for the chapter-42 release. New: extract_043 (+33), chapter_42_a_storm_is_coming.md (+49), and 32 phandalin-wing files (NPC dossier refresh / new top-level dossiers / new Drubbak NPC, +571 drawers). No full rebuild — chapter file paths unchanged, no orphan-drawer risk. Both sanity searches passed (bible excluded; chapter file reachable).
- **Embedding device:** CPU (onnxruntime; matches OOTA — GPU swap blocked by torch cu13 vs onnxruntime-gpu cu12 mismatch)

> **Tag convention.** Releases use **title-slug tags** (e.g.
> `phandalin-chapter-storm-of-bolts-orcs`) rather than chapter numbers,
> since bible heading numbering and session-summary numbering disagree
> by one (bible "Chapter N" = session-summary "Chapter N+1") and have
> caused tag collisions in the past.

## Drawer counts at this horizon

Fresh counts as of the 2026-05-22 incremental re-mine.

| Wing | Source dir | Files | Drawers | Δ since 2026-05-18 |
|------|-----------|-------|---------|--------------------|
| `distill_extractions` | `docs/distill_extractions/` | 43 | 1081 | +33 |
| `narrative` | `docs/chapters/` | 42 | 1248 | +49 |
| `phandalin` | root campaign reference | 533 | 2887 | +224 |
| **Total** | | **618** | **5216** | **+306** |

Phandalin-wing breakdown: npcs 2061 (+68), arcs 374 (+53), dead 111 (0),
world 264 (+106), mechanics 77 (-3). World-wing growth reflects the new
top-level dossiers (`docs/CounterForce.md`, `docs/KP.md`, `docs/glossary.md`)
landing this release.

Use these as the regression baseline — significant drift on a no-op
re-mine probably means content was added/removed unintentionally.

> **Narrative wing is now clean** (ghost drawer flushed by the 22:58 rebuild;
> `docs/chapters/.mempalaceignore` prevents re-introduction).

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
  corrupted snapshot at the start of the day (two HNSW segments
  quarantined). Replaced by the first 17:24 rebuild. Retain for
  forensics on the HNSW corruption bug.
- `~/.mempalace/palaces/phandalin.bak.20260517-225805` — the first
  rebuild's palace, moved aside for the 22:58 re-rebuild after the
  sync patches landed. Had one stale ghost drawer in `narrative/general`
  from the early `docs/chapters/.claude/settings.local.json` mining.
  Retain until the 22:58 palace is confirmed healthy across a few
  sessions.
- `~/.mempalace/palaces/phandalin.bak.20260518-084340` — the 22:58
  palace, moved aside for the 08:44 rebuild after the HNSW quarantine
  fix landed. Retain until the 08:44 palace is confirmed healthy.

---

## Known caveats at this horizon

- **`mempalace sync` status as of 2026-05-18 morning rebuild:**
  - `--palace <named>` resolution in sync: **FIXED.**
  - Sync against yaml-configured wings (e.g. `narrative`): **FIXED.**
    `Scanned 1199, Kept 1199, Gitignored 0` verified post-rebuild.
  - Sync against root wing (e.g. `phandalin`): **FIXED.**
    `Scanned 2663, Kept 2663, Gitignored 0` verified post-rebuild.
  - Sync against auto-detected wings (e.g. `distill_extractions`):
    **FIXED** (2026-05-18 morning, uncommitted patch on `mempalace/sync.py`).
    `sync --dry-run --wing distill_extractions` reports `Scanned 1048,
    Kept 1048, Gitignored 0` post-fix.
  - **HNSW quarantine on `sync --dry-run` (bug 3): FIXED.** Commit
    `0991677 fix(backends): don't quarantine HNSW segments for unflushed
    metadata`. Verified by running `sync --dry-run` on all three wings
    post-rebuild and confirming no `.drift-*` segments appeared in
    `~/.mempalace/palaces/phandalin/`. `repair-status` now reports the
    expected "leaving vector search enabled" UNKNOWN status for both
    drawers and closets at low row counts.
- **HNSW corruption was observed pre-rebuild.** The pre-2026-05-17
  palace had two HNSW segments fail integrity check (sqlite newer
  than HNSW). Backup retained for forensics; do not restore it.
- **Dual-split chapter pollution resolved.** `docs/chapters/` is now
  clean (41 files for 41 bible chapters). The earlier `docs/doc/chapters/`
  misdirected output was removed before the rebuild.
- **Bible vs session-summary numbering still disagrees by one.**
  Bible heading "Chapter N" = file position N+1 = session-summary
  "Chapter N+1". Going forward, release tags use title slugs to side-step this.
- **GPU embedding deferred.** Switching to GPU requires resolving the
  torch cu13 vs onnxruntime-gpu cu12 mismatch. Not blocking; CPU
  mine completed in a few minutes for this rebuild.
- **5etools MCP not registered for Phandalin.** Unlike OOTA,
  Phandalin's `.mcp.json` only registers the `campaign` server.
  `docs/adventures/` (Essentials Kit modules) is excluded from the
  palace following the OOTA pattern, so module lookups currently have
  no fallback. Either register 5etools in `.mcp.json` or selectively
  un-ignore specific custom encounter files in `.mempalaceignore`.
