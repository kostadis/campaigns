# MemPalace Horizon — OOTA

Coordination marker between the human and Claude. Tells future
sessions where the palace stands so re-mining decisions can be
explicit.

---

## Current horizon

- **Last campaign chapter played:** 51 — *Candlekeep: Trials, Truths, and Therapy* (Daggerford arrival, Maerith's silent child, Tarvis Ulain monument, Daz cross-examined at Candlekeep, Stroud reckoning)
- **Last bible chapter file:** `docs/chapters/chapter_55_candlekeep_trials_truths_and_therapy.md`
- **Last session date:** 2026-05-11
- **Palace last fully (re)built:** 2026-05-18
- **Embedding device:** openai-compat — `nomic-ai/nomic-embed-text-v1.5` via vLLM @ `http://192.168.1.147:8000` (DGX Spark). Switched from CPU onnxruntime this rebuild — old palace was unusable because the persisted collection's embedding fn (`default`) no longer matched the active mempalace config (`openai-compat`). Full Spark re-mine on 56 + 55 + 188 files completed in minutes.

> The campaign chapter number (51) and the bible chapter file number
> (55) are different. The bible has 55 split chapters because the
> source contains five sub-chapters in the chapter 18 cluster
> (`# Chapter 18.05`/`18.1`–`18.4` in `docs/TheUnderdark.md`), and
> the splitter assigns file numbers by encounter order — so source
> heading "# Chapter 51" lands as `chapter_55_…` after the offset.

## Drawer counts at this horizon

| Wing | Source dir | Files | Drawers |
|------|-----------|-------|---------|
| `chronicle` | `docs/distill_extractions/` | 56 | 1607 |
| `narrative` | `docs/chapters/` | 55 | 1328 |
| `abyss` | root campaign reference | 188 | 1777 |
| **Total** | | **299** | **4712** |

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
- `~/.mempalace/palaces/abyss.bak.20260518-205537/` — final chapter-50 palace state (CPU/onnxruntime embeddings). Unusable in current config because mempalace now resolves `embedding_provider=openai-compat`; kept for archive only.
- `~/.mempalace/palaces/abyss.bak.20260518-210006-precronicle/` — first Spark re-mine for chapter 51, before `docs/distill_extractions/mempalace.yaml` was added. Chronicle wing was auto-detected as `distill_extractions`. Superseded by the post-yaml rebuild. Delete next housekeeping pass.

Safe to delete `20260425-222447`, `20260426-071851-cpu-polluted`,
and the `20260518-210006-precronicle` intermediate once a session
or two confirms the chapter-51 palace is healthy. Keep
`20260503-100052` (last good chapter-50 fallback) and
`20260518-205537` (last good CPU-embedded snapshot — the only path
back to onnxruntime embeddings without re-mining).

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
- **Embeddings moved off-host to the DGX Spark.** This chapter's
  rebuild was the first to use the Spark vLLM server
  (`nomic-ai/nomic-embed-text-v1.5` @ `192.168.1.147:8000`). Rebuild
  was forced — not chosen — because the persisted Chroma collection
  was built with the `default` embedding fn (CPU onnxruntime) and
  the active mempalace config now resolves
  `embedding_provider=openai-compat`. Chroma refuses to load a
  collection whose embedding fn doesn't match the runtime config.
  The local torch cu13 vs onnxruntime-gpu cu12 mismatch is now
  irrelevant — embeddings are remote.
- **Spark must be reachable to mine or search.** If
  `192.168.1.147:8000` is down, both `mp mine` and `mp search` will
  fail immediately on embedding-fn lookup. Falling back to CPU
  embeddings requires another full rebuild (the wire format and
  semantic space differ between providers, so existing drawers
  aren't reusable).
- **Per-wing yaml is local-only (gitignored).**
  `docs/distill_extractions/mempalace.yaml` and
  `docs/chapters/mempalace.yaml` are both excluded by the campaign's
  root `.gitignore` (line 3: `mempalace.yaml`). They live on disk
  but never enter version control. If the chronicle yaml is missing
  before a rebuild, the chronicle wing auto-detects as
  `distill_extractions` (wrong) — confirm both per-wing yamls exist
  before mining. Canonical content for the chronicle yaml:
  ```yaml
  wing: chronicle
  rooms:
  - name: general
    description: LLM-generated structured extractions over campaign time — search accelerator for "what was X's state at point in time T"
    keywords: [extract, distill, snapshot, timeline]
  ```
