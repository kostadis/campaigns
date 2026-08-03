# MemPalace Horizon — OOTA

Coordination marker between the human and Claude. Tells future
sessions where the palace stands so re-mining decisions can be
explicit.

---

## Current horizon

- **Last campaign chapter played:** 59 — *The Key is Secured* (helmed horrors ambush Deneir's Sanctum hunting the key Daz carries; Detect Magic proves it a decoy; Bookwyrm murdered, throat torn out by the beast; Kalan Strongbranch confesses the real key was entrusted to Tadric and deputizes the party as Watchers of Candlekeep; Fembris places A'lai Aivenmore in the room; Moziqodo slain in the domed rotunda and Tadric saved; real key secured; party to level 9)
- **Last bible chapter file:** `docs/chapters/chapter_62_the_key_is_secured.md`
- **Last session date:** 2026-07-20
- **Palace last fully (re)built:** 2026-07-27 — full rebuild. Not triggered by the split (that was already current: 62 headings, 62 files, nothing renamed) but by the **entity source of record moving** from `docs/npcs/` to `docs/ensemble/merged_dossiers/`. A source swap always needs a rebuild rather than a re-mine, because mining only ever *adds* drawers — the 6,554 `docs/npcs/` drawers and the ensemble-intermediate drawers had to be evicted by starting from empty.
- **Embedding device:** openai-compat — `nomic-ai/nomic-embed-text-v1.5` via vLLM @ `http://192.168.1.147:8000` (DGX Spark). Switched from CPU onnxruntime this rebuild — old palace was unusable because the persisted collection's embedding fn (`default`) no longer matched the active mempalace config (`openai-compat`). Full Spark re-mine on 56 + 55 + 188 files completed in minutes.

> The campaign chapter number (59) and the bible chapter file number
> (62) are different, and **the gap between them is not constant.**
> The splitter assigns file numbers by encounter order, so the two
> counters drift apart wherever the source numbering is irregular:
>
> - **+4 through campaign chapter 54** — the chapter 18 cluster
>   contributes five sub-chapters (`# Chapter 18.05`/`18.1`–`18.4` in
>   `docs/TheUnderdark.md`), which is why campaign 51 landed as
>   `chapter_55_…`.
> - **+3 from campaign chapter 56 onward** — the source skips
>   `# Chapter 55` entirely (`grep -c '^# Chapter 55' docs/TheUnderdark.md`
>   returns 0), so the offset drops by one and campaign 59 lands as
>   `chapter_62_…`.
>
> **Read the campaign number off the heading inside the file, not off
> the filename.** `chapter_62_the_key_is_secured.md` opens with
> `# Chapter 59 The Key is Secured`, and that heading is what the
> session summary and the `oota-chapter-N` tags follow. Deriving the
> campaign number by subtracting a fixed offset from the filename is
> what produces an off-by-one tag.

## Drawer counts at this horizon

| Wing | Source dir | Files (`.md`) | Drawers |
|------|-----------|-------|---------|
| `chronicle` | `docs/distill_extractions/` | 65 | 3212 |
| `narrative` | `docs/chapters/` | 62 | 1814 |
| `abyss` | root campaign reference | 509 | 3265 |
| `notes` | `notes/` | 47 | 1321 |
| `summaries` | `summaries/` | 520 | 8357 |
| **Total** | | **1203** | **17969** |

Per-room breakdown of the two composite wings, since a lopsided room
is the fastest way to spot a bad mine:

| Wing | Rooms |
|------|-------|
| `abyss` | world 1250 · arcs 766 · npcs 618 · general 335 · dead 154 · mechanics 142 |
| `notes` | prep 818 · design 250 · handouts 248 · references 5 |
| `summaries` | summary 3251 · extractions 2430 · narration 2036 · general 640 |

Use these as the regression baseline — significant drift on a no-op
re-mine probably means content was added/removed unintentionally.

> **The previous baseline (4,712 across three wings) had been stale for
> a long time.** The palace measured 14,019 drawers before this release
> even began, so "drift from baseline" had stopped being a usable
> signal. Two things make this table trustworthy where that one wasn't:
> it covers all five wings rather than three, and it was taken against
> a `.mempalaceignore` that admits prose only. If a future re-mine
> lands far from these numbers, suspect a newly-added directory that
> nobody excluded — that is exactly how `docs/ensemble/` tripled the
> palace in July 2026.
>
> Chapter 59 took three rebuilds to reach these numbers:
> 38,700 drawers (everything mined) → 13,480 (ensemble intermediates
> and `docs/npcs/` excluded, but `notes`/`summaries` accidentally
> dropped) → 17,969 (prose-only rules, all five wings restored).

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
   mp="/home/kroussos/.venvs/main/bin/mempalace --palace abyss"
   cd /home/kroussos/out-of-the-abyss/out-of-the-abyss
   $mp mine docs/distill_extractions   # chronicle
   $mp mine docs/chapters              # narrative
   $mp mine .                          # abyss (root)
   $mp mine notes                      # notes      <- explicit path required
   $mp mine summaries                  # summaries  <- explicit path required
   ```
   Both paths in this block were corrected at the chapter 59 release —
   see "Two checkouts" and "mempalace binary moved" under Known
   caveats. The root mine is slow (well over 10 minutes); run it in
   the background rather than in a foreground shell that can time out.

   **All five wings must be listed.** `notes/` and `summaries/` are in
   the root `.mempalaceignore`, which keeps the root mine from
   double-mining them — it does *not* mean they are unwanted. They are
   configured wings with their own `mempalace.yaml` and their own
   `.mempalaceignore`, and they only get populated when mined by
   explicit path. A rebuild that mines just chronicle/narrative/root
   drops them silently: no error, no warning, ~5,700 drawers simply
   gone from search.
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
3. Re-mine all **five** wings in order: chronicle → narrative → root
   → notes → summaries. Subdirectory wings go before root wherever the
   root ignore does not already exclude them; `notes/` and `summaries/`
   are excluded there, so their position after root is safe.
4. Update this file: bump horizon, refresh drawer counts, note
   what was discarded and why.

---

## Backups currently on disk

- `~/.mempalace/palaces/abyss.bak.20260425-222447/` — pre-rebuild snapshot from before this work began (pre-renumber, polluted by old splitter)
- `~/.mempalace/palaces/abyss.bak.20260426-071851-cpu-polluted/` — first CPU re-mine that included `TheUnderdark.md` due to a stale `.mempalaceignore` rule (file had been renamed `The Underdark.md` → `TheUnderdark.md`)
- `~/.mempalace/palaces/abyss.bak.20260503-100052/` — pre-chapter-50 snapshot (last horizon: chapter 49, narrative wing's chapter files numbered with the old `chapter_01_arrival` prologue prefix)
- `~/.mempalace/palaces/abyss.bak.20260518-205537/` — final chapter-50 palace state (CPU/onnxruntime embeddings). Unusable in current config because mempalace now resolves `embedding_provider=openai-compat`; kept for archive only.
- `~/.mempalace/palaces/abyss.bak.20260518-210006-precronicle/` — first Spark re-mine for chapter 51, before `docs/distill_extractions/mempalace.yaml` was added. Chronicle wing was auto-detected as `distill_extractions`. Superseded by the post-yaml rebuild. Delete next housekeeping pass.
- `~/.mempalace/palaces/abyss.bak.20260727-091900/` — **the polluted pre-chapter-59 palace.** Last state before the source-of-record switch, and the only snapshot that still contains `docs/npcs/`-derived drawers. 38,700 drawers, of which roughly 25k came from mining `docs/ensemble/` wholesale (1,071 per-chapter JSONs, 553 pre-merge `state_dossiers/`, and a 7.7 MB `merged.json`) before `.mempalaceignore` had rules for any of it. Keep until a session or two confirms the chapter-59 palace answers canon queries well; its value is as the fallback if `merged_dossiers/` turns out to have thinner coverage than `docs/npcs/` did, not as a search target.

Safe to delete `20260425-222447`, `20260426-071851-cpu-polluted`,
and the `20260518-210006-precronicle` intermediate once a session
or two confirms the chapter-51 palace is healthy. Keep
`20260503-100052` (last good chapter-50 fallback) and
`20260518-205537` (last good CPU-embedded snapshot — the only path
back to onnxruntime embeddings without re-mining).

---

## Known caveats at this horizon

- **Two checkouts of this repo exist on disk.** `kostadis/campaigns.git`
  is cloned at *both* `/home/kroussos/out-of-the-abyss/` (current, used
  for the chapter 59 release) and `/home/kroussos/campaigns/` (as of
  2026-07-27: 27 commits behind `origin/main`, 209 dirty files, and
  missing `chapter_62_the_key_is_secured.md` altogether). They are
  separate clones, **not** symlinks to one tree — `stat` reports
  different inodes. The `oota-chapter-release` skill and older copies of
  this doc hardcode the `/home/kroussos/campaigns/` path, which would
  cut a release from a tree that lacks the chapter being released.
  Confirm which tree you are in before mining or tagging; the palace is
  a single shared store at `~/.mempalace/palaces/abyss/`, so mining from
  the stale clone would quietly overwrite good drawers with old content.
- **mempalace binary moved.** It is `/home/kroussos/.venvs/main/bin/mempalace`.
  The path in the older docs and in the release skill
  (`/home/kroussos/worldanvil_pipeline/venv/bin/mempalace`) no longer
  exists — that venv is gone, though the `worldanvil_pipeline/` directory
  itself remains, so the failure is a bare "No such file or directory".
- **Entity source of record is now `docs/ensemble/merged_dossiers/`.**
  As of chapter 59 the palace no longer mines `docs/npcs/`. The
  ensemble set is a superset, not a swap — 456 entities spanning
  `npc_`/`object_`/`location_`/`monster_`/`faction_` prefixes, against
  214 NPC-only files before. `docs/npcs/` still lives in git as GM
  working reference; it just doesn't feed search. Two things follow:
  (a) the four PC exclusions had to be **restated** against
  `merged_dossiers/`, since `npc_daz.md`, `npc_grygum.md`,
  `npc_thorin.md`, `npc_zalthir.md` and `npc_daz_issin.md`
  (Daz'issin = Daz's full drow name) all reappear there — moving a
  source silently readmits whatever the old path was filtering;
  (b) only `merged_dossiers/` is canon. `state_dossiers/` is the
  pre-merge per-`(type, subject)` layer that it supersedes, and
  `per_chapter/` is raw JSON — both are excluded.
- **There were three overlapping NPC sources; now there is one.**
  `docs/npcs/` (172), `docs/v2/npcs/` (221, last updated 2026-06-29)
  and `docs/ensemble/merged_dossiers/` (442 entities, current) were all
  being mined into the same wing, so a single entity could have three
  competing dossiers and the stalest could win a query. As of chapter
  59 only `merged_dossiers/` feeds the palace. `docs/v2/`'s *grounding*
  docs (world_state / party / planning / campaign_state / threads) are
  still mined — only its `npcs/` subdir is excluded.
  **Coverage: verified good. An earlier version of this file claimed a
  three-entity gap — that claim was wrong and is retracted.** It said
  `brother_vareth`, `asha_vandry` and `blind_monk` had become
  unsearchable. Checked against the live palace:

  | claimed missing | actually |
  |---|---|
  | `brother_vareth` | `npc_vareth.md` — full dossier, 15 facts, ch54–60 |
  | `asha_vandry` | `npc_asha_vandree.md` — spelling variant |
  | `blind_monk` | no entity dossier, but the scene is in `chapter_55_candlekeep_trials_truths_and_therapy.md` (narrative) and `session_doc_scene_05_zalthir_s_trial_of_the_broken_mirror.md` (summaries) |

  **How the wrong claim was produced, so it isn't repeated:** the check
  compared v2 filenames against merged_dossiers filenames with the
  entity's *full* v2 name (`grep -i brother_vareth`). merged_dossiers
  drops honorifics and normalises spelling, so the file is
  `npc_vareth.md` and the grep found nothing. Grep the **distinctive
  component** (`vareth`, `asha`), never the whole v2 filename.

  This is the same naming trap already known for v2 `bookwyrm` →
  `npc_bookwyrm_first_reader` and v2 `basidia` →
  `npc_sovereign_basidia`. Note also that `docs/v2/npcs/` holds
  *variants of the same entity as separate files* — `vareth.md` **and**
  `brother_vareth.md`; `asha.md`, `asha_vandree.md` **and**
  `asha_vandry.md` — which is precisely the fragmentation the ensemble
  merge collapses. **Any raw name-set diff between v2 and
  merged_dossiers is inflated by this and should not be quoted as a
  coverage figure** (the "97 names missing" number from the chapter 59
  run is unreliable for the same reason).

  Before declaring anything missing, query the palace rather than
  diffing filenames — and remember the narrative wing is authoritative
  per `CLAUDE.md`, so an entity with no dossier can still be fully
  reachable. Re-check whenever ensemble is regenerated.

  > The `oota-chapter-59` tag message and commit `6e31649` still carry
  > the retracted claim. Both are immutable and already fetched, so they
  > were left alone; this file is the living record and wins.
- **The palace indexes prose only.** `.mempalaceignore` now excludes
  `*.json`, `*.yaml`, `*.txt`, `*.pdf`, `*.log`, `*.sqlite3` and
  friends, plus `scratch/`. Before this, the root mine ingested 137
  non-prose files totalling 7.3 MB — four D&D Beyond PDFs, a 305 KB
  entity-triage state blob, and the `scratch/exp-*/` experiment dumps.
  The symptom was `aliases.json`, a bare alias map, ranking above every
  NPC dossier for "Zuggtmoy wedding". Query registry data through the
  `registry` MCP server instead. Note `.mempalaceignore` does **not**
  inherit from `.gitignore` — `scratch/` was git-ignored the whole time
  and still got mined.
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
