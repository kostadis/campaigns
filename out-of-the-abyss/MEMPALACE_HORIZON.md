# MemPalace Horizon — OOTA

Coordination marker between the human and Claude. Tells future
sessions where the palace stands so re-mining decisions can be
explicit.

---

## Current horizon

- **Last campaign chapter played:** 59 — *The Key is Secured* (helmed horrors ambush Deneir's Sanctum hunting the key Daz carries; Detect Magic proves it a decoy; Bookwyrm murdered, throat torn out by the beast; Kalan Strongbranch confesses the real key was entrusted to Tadric and deputizes the party as Watchers of Candlekeep; Fembris places A'lai Aivenmore in the room; Moziqodo slain in the domed rotunda and Tadric saved; real key secured; party to level 9)
- **Last bible chapter file:** `docs/chapters/chapter_62_the_key_is_secured.md`
- **Last session date:** 2026-07-20
- **Palace last fully (re)built:** 2026-09-11 — full reset. Triggered by
  three things landing together: the Gyrgum spelling pass (#244) rewrote
  27,891 occurrences across 2,129 files, and #245/#246 fixed ten broken
  `.mempalaceignore` rules. All three needed a reset rather than a forward
  mine, because mining only ever *adds* — the old-spelling drawers and the
  wrongly-admitted PC-sheet and pipeline drawers had to be evicted by
  starting from empty. Mined 18:51–19:06 (~15 min) across all five wings.
  **The campaign-chapter fields above were deliberately not bumped:**
  sessions were played on 20260727, 20260809, 20260817 and 20260824, but
  `docs/TheUnderdark.md` has not been extended or re-split, so the last
  bible chapter file is still `chapter_62_…` (`# Chapter 59` internally).
  Assigning those sessions chapter numbers is a GM call, not an inference.
- **Embedding device:** openai-compat — `qwen3-embedding:0.6b` (1024-dim,
  Ollama) @ `http://192.168.1.121:11434`, per
  `~/.mempalace/config.json`. **This doc previously claimed
  `nomic-ai/nomic-embed-text-v1.5` via vLLM @ `192.168.1.147:8000`; that is
  wrong and was wrong before 2026-09-11** — the host answers ping but
  nothing listens on 8000. Read the endpoint off `config.json`, not off
  this line, and confirm it responds before a rebuild:
  `curl -s http://192.168.1.121:11434/api/tags`. The LLM endpoint
  (`qwen3.8-flash-next` @ `192.168.1.147:8001`) is separate and was live.

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
| `chronicle` | `docs/distill/distill_extractions/` | 65 | 3212 |
| `narrative` | `docs/chapters/` | 62 | 1812 |
| `abyss` | root campaign reference | 516 | 2631 |
| `notes` | `notes/` | 64 | 1903 |
| `summaries` | `summaries/` | 567 | 11188 |
| **Total** | | **1274** | **20746** |

Movement against the 2026-07-27 baseline (17969 total), so a future
regression check is read against explained numbers rather than raw drift:

| Wing | Then | Now | Why |
|---|---|---|---|
| `chronicle` | 3212 | 3212 | exact match — strongest evidence the mine was clean |
| `narrative` | 1814 | 1812 | −2 on 62 unchanged files; chunker drift, not content loss |
| `abyss` | 3265 | 2631 | −634. The 12 PC files now excluded (4 root sheets + 8 `docs/party/`) were dense stat tables, and `arcs` alone dropped 286 — that is where the PC sheets were being filed. |
| `notes` | 1321 | 1903 | new prep/handout content since July |
| `summaries` | 8357 | 11188 | five sessions added since July |

Per-room breakdown of the two composite wings, since a lopsided room
is the fastest way to spot a bad mine:

| Wing | Rooms |
|------|-------|
| `abyss` | world 1096 · npcs 633 · arcs 480 · dead 155 · mechanics 148 · general 119 |
| `notes` | prep 1304 · handouts 381 · design 213 · references 5 |
| `summaries` | summary 4277 · extractions 3521 · narration 2269 · general 1121 |

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
   $mp mine docs/distill/distill_extractions   # chronicle
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

- **Acceptance checks that were run after the 2026-09-11 rebuild.** Re-run
  these after any rebuild; each one caught something real:
  1. `search "Zuggtmoy wedding" --wing abyss` → must return dossiers
     (`npc_araumycos.md`), never `TheUnderdark.md`. Passed.
  2. `search "Gyrgum character sheet hit points armor class" --wing abyss`
     → must return **prose**, never a PC sheet or a script. First run
     returned `tools/combat_sim.py` in the top five, which is how the
     missing `*.py` rule was found.
  3. `search "canon guardrails hard rules"` / `"decision ladders"` /
     `"risk levers"` → each must rank its own doc first. Passed; this is
     the check that proves the new exclusions did not take canon with them.
- **`mempalace sync` evicts drawers without a rebuild.** `sync . --wing
  abyss --dry-run` lists drawers whose source is now ignored/deleted/moved;
  `--apply` removes them. This removed the 31 `combat_sim.py` drawers in
  seconds and saved a second 15-minute reset. Reach for it before assuming
  a stray source needs a full rebuild — a *content* change still does.

- **The pipeline output moved under `docs/distill/` and six
  `.mempalaceignore` rules were left behind (found 2026-09-11).**
  `docs/distill_extractions/`, `docs/planning_extractions/`,
  `docs/campaign_state_extracts/` and `docs/party_extract/` all still
  named the pre-reorganisation paths, so 310 pipeline intermediates plus
  the 65-file chronicle wing were unexcluded from the root mine — and
  because `distill_extractions/` *is* the chronicle source, a root mine
  would have double-mined it into `abyss` too. `docs/npcs/` and
  `docs/v2/npcs/` are gone entirely; their successor
  `docs/distill/npcs/` (173 dossiers + 42 `new_notes` fragments) was
  likewise unexcluded and is now excluded on the same one-entity-source
  grounds. The rebuild command block in this file named the old
  chronicle path too, so following it verbatim mined *nothing* for
  chronicle and silently dropped 3,212 drawers.
  **When a path in `.mempalaceignore` stops matching, the rule is dead,
  not satisfied.** Validate before every rebuild:
  ```bash
  grep -vE '^#|^$' .mempalaceignore | grep '/$' \
    | while read d; do [ -d "$d" ] || echo "STALE $d"; done
  ```
  The same check with `grep '\.md$'` and `[ -e ]` catches broken file
  rules — which is how the four PC-sheet lines were found to have never
  fired (they were lowercase against capitalised filenames).

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
- **mempalace binary moved.** It is `/home/kroussos/.venvs/main/bin/mempalace`
  (note the plural `.venvs`; `/home/kroussos/.venv/main/bin/mempalace`, as
  this doc said until 2026-09-11, does not exist).
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
  `merged_dossiers/`, since `npc_daz.md`, `npc_gyrgum.md`,
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
  `docs/distill/distill_extractions/mempalace.yaml` and
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
