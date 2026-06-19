# Ensemble Workflow — Obelisk Campaign

Adaptation of `~/src/CampaignGenerator/docs/cli/ensemble_workflow.md` for this campaign.
Run from `/home/kroussos/campaigns/obelisk/` unless noted otherwise.

---

## Key differences from Phandalin

| Phandalin | Obelisk |
|---|---|
| `docs/chapters/chapter_*.md` — polished narrative | `summaries/*/zoom_summary.md` — VTT bullet-point summaries |
| 45 chapters | 3 sessions |
| `docs/background/dragon-of-icespire-peak-inventory.md` | `docs/background/name_glossary.md` |
| `.dedup_state.json` from prior NPC dedup pass | None yet |
| PC backstory `.md` files | `notes/open.md` + `characters/*.md` |

The session summaries are short (~3–8 KB each). Outputs will be thin but valid — the
main win is populating the currently-empty grounding docs with actual session content.

---

## Prerequisite 0 — spelling correction pass

Before extraction, all proper nouns in the session summaries must be consistent.
The Zoom AI transcriber mangles names differently each session; the ensemble model
will create separate entities for each variant if you don't fix them first.

**The corrections themselves live in one place — do not duplicate them here.**
The single source of truth is **`notes/vtt_transcription_corrections.md`**
(the `vtt-spell-pass` skill reads and appends to it). `docs/ensemble/aliases.json`
is **generated** from that file by `docs/ensemble/build_aliases.py`, so the
ensemble pipeline and the spell-pass skill share one canonical map instead of
drifting copies.

**After each future session:**
1. Run `/vtt-spell-pass` (or hand-correct) against the new
   `summaries/00N/zoom_summary.md`, recording any new garble in
   `notes/vtt_transcription_corrections.md`. Verify canonical spellings against
   `docs/background/name_glossary.md` and `characters/`.
2. Re-run `python3 docs/ensemble/build_aliases.py` to refresh `aliases.json`.
3. Copy the corrected summary into `docs/chapters/` for extraction.

---

## Prerequisite 1 — create chapter copies with unique stems

`ensemble_batch.py` keys workdirs on `file.stem`. All three summaries are named
`zoom_summary.md`, so they'd collide. Copy them with unique names first:

```bash
mkdir -p docs/chapters

cp summaries/001/zoom_summary.md docs/chapters/session_001_threshold.md
cp summaries/002/zoom_summary.md docs/chapters/session_002_cragmaw_cave.md
cp summaries/003/zoom_summary.md docs/chapters/session_003_cragmaw_hideout.md
```

Re-run this copy step after each new session (add `session_004_...md` etc).
These are **copies for extraction only** — the summaries under `summaries/` remain authoritative.

---

## Plan YAML

```bash
mkdir -p docs/ensemble
```

```yaml
# docs/ensemble/plan.yaml
passes:
  - name: small
    agent: extract_facts
    chunk_size: 4000
    annotate_pov: false
  - name: large
    agent: extract_facts
    chunk_size: 8000
    annotate_pov: false
  - name: sweep
    agent: extract_facts_sweep
    chunk_size: 8000
    annotate_pov: false
  - name: temporal
    agent: extract_facts_temporal
    chunk_size: 8000
    annotate_pov: false
  - name: interiority
    agent: extract_facts_interiority
    chunk_size: 8000
    annotate_pov: false
```

`annotate_pov: false` — the zoom summaries use "Discussed Topics" bullet structure,
not `### Speaker` POV headings, so the banner adds nothing here.

Chunk sizes are smaller than Phandalin (4K/8K vs 6K/15K) because the sessions
are short — the whole file will fit in one or two chunks per pass.

---

## Stage 1 — Ensemble extraction

```bash
cd /home/kroussos/campaigns/obelisk/docs/ensemble

python ~/src/CampaignGenerator/ensemble_batch.py \
  --chapters '../chapters/session_*.md' \
  --per-chapter-dir per_chapter \
  --out merged.json \
  --plan plan.yaml \
  --endpoints http://spark:8001/v1 http://spark2:8001/v1 \
  --model Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \
  --chunk-parallel 4 \
  --unit-timeout 0 \
  --embed-endpoint http://spark2:8000 \
  --embed-model Qwen/Qwen3-Embedding-0.6B \
  --embed-threshold 0.93 \
  --chapter-parallel 3
```

Resumable — re-run safely if a session fails. Completed sessions are skipped.

---

## Stage 1a — Alias review (optional for 3 sessions)

With only 3 sessions, alias collisions are unlikely. Skip for now. Revisit after
session 8–10 when the same NPCs start appearing under variant spellings.

---

## Stage 2a — Scope review (--list checkpoint)

```bash
cd /home/kroussos/campaigns/obelisk

python ~/src/CampaignGenerator/facts_to_state.py \
  --corpus 'docs/ensemble/per_chapter/*/merged.json' \
  --known-names docs/background/name_glossary.md \
               characters/pip.md \
               characters/maela.md \
               characters/veyra.md \
  --min-facts 2 \
  --list
```

`--min-facts 2` rather than 3 — at 3 sessions, key NPCs may have only 2 facts each.
Review output:
- Are Zenvon, Pip, Maela, Veyra tagged `[known]`?
- Is Sildar tagged `[known]`? Gundren?
- Are "goblin", "wolf", "bandit" scoped to location? (They should be.)

---

## Stage 2b — Aggregation

```bash
python ~/src/CampaignGenerator/facts_to_state.py \
  --corpus 'docs/ensemble/per_chapter/*/merged.json' \
  --known-names docs/background/name_glossary.md \
               characters/pip.md \
               characters/maela.md \
               characters/veyra.md \
  --known-only \
  --min-facts 2 \
  --out-dir docs/ensemble/state_dossiers \
  --endpoints http://spark:8001/v1 http://spark2:8001/v1 \
  --model Qwen/Qwen3-Next-80B-A3B-Instruct-FP8
```

---

## Stage 2d — Threads track (zero model tokens)

```bash
python ~/src/CampaignGenerator/facts_to_state.py \
  --corpus 'docs/ensemble/per_chapter/*/merged.json' \
  --types thread \
  --min-facts 1 \
  --render-only docs/ensemble/threads.md
```

`--min-facts 1` — with 3 sessions, any extracted thread is worth capturing.

---

## Stage 2e — Merge type-duplicate dossiers

```bash
python3 - <<'PY'
import glob, re, os, shutil
from collections import defaultdict

src = 'docs/ensemble/state_dossiers'
dst = 'docs/ensemble/merged_dossiers'
os.makedirs(dst, exist_ok=True)

def n_facts(path):
    m = re.search(r'^n_facts:\s*(\d+)', open(path).read(), re.M)
    return int(m.group(1)) if m else 0

groups = defaultdict(list)
for f in sorted(glob.glob(f'{src}/*.md')):
    base = os.path.basename(f)
    subject = base.split('_', 1)[1] if '_' in base else base
    groups[subject].append(f)

for subject, files in sorted(groups.items()):
    if len(files) == 1:
        shutil.copy(files[0], os.path.join(dst, os.path.basename(files[0])))
    else:
        primary = max(files, key=n_facts)
        out_name = os.path.basename(primary)
        parts = []
        for f in sorted(files, key=n_facts, reverse=True):
            parts.append(f'<!-- source: {os.path.basename(f)} -->\n')
            parts.append(open(f).read().rstrip())
        with open(os.path.join(dst, out_name), 'w') as fh:
            fh.write('\n\n---\n\n'.join(parts) + '\n')
        print(f'merged → {out_name}')

total = len(list(glob.glob(dst + '/*.md')))
print(f'{total} files in merged_dossiers/')
PY
```

---

## Stage 3a — world_state synthesis

```bash
cd /home/kroussos/campaigns/obelisk

python ~/src/CampaignGenerator/synthesise_world_state.py \
  --dossiers 'docs/ensemble/merged_dossiers/*.md' \
  --dossier-min-facts 2 \
  --party config/party.yaml \
  --threads docs/ensemble/threads.md \
  --output docs/world_state_draft.md \
  --model claude-opus-4-8
```

No backstory files yet (Zenvon's backstory lives in `notes/open.md` — could pass it
via `--backstories notes/open.md` if `synthesise_world_state.py` accepts freeform
files). Add as `--backstories` when there's a dedicated backstory doc.

**Subscription path:**
```bash
python ~/src/CampaignGenerator/synthesise_world_state.py \
  --dossiers 'docs/ensemble/merged_dossiers/*.md' \
  --dossier-min-facts 2 \
  --party config/party.yaml \
  --threads docs/ensemble/threads.md \
  --dump-input /tmp/obelisk_world_state_prompt.md \
  --dump-only

claude -p \
  --system-prompt "$(cat /tmp/obelisk_world_state_prompt.md.system.md)" \
  < /tmp/obelisk_world_state_prompt.md \
  > docs/world_state_draft.md
```

---

## Stage 3b — campaign_state synthesis

```bash
mkdir -p /tmp/obelisk-cstate/extracts
cp docs/world_state_draft.md /tmp/obelisk-cstate/extracts/extract_001_world_state.md
cp docs/ensemble/threads.md  /tmp/obelisk-cstate/extracts/extract_002_threads.md

python ~/src/CampaignGenerator/campaign_state.py \
  --synthesize-only \
  --extract-dir /tmp/obelisk-cstate/extracts \
  --output docs/campaign_state_draft.md \
  --model claude-opus-4-8
```

---

## Stage 3c — party synthesis

```bash
# Copy PC dossiers (names may vary — check merged_dossiers/ after Stage 2e)
mkdir -p /tmp/obelisk-party/extracts
cp docs/ensemble/merged_dossiers/npc_zenvon*.md  /tmp/obelisk-party/extracts/extract_001_zenvon.md  2>/dev/null || true
cp docs/ensemble/merged_dossiers/npc_pip*.md     /tmp/obelisk-party/extracts/extract_002_pip.md     2>/dev/null || true
cp docs/ensemble/merged_dossiers/npc_maela*.md   /tmp/obelisk-party/extracts/extract_003_maela.md   2>/dev/null || true
cp docs/ensemble/merged_dossiers/npc_veyra*.md   /tmp/obelisk-party/extracts/extract_004_veyra.md   2>/dev/null || true

python ~/src/CampaignGenerator/party.py \
  --synthesize-only \
  --extract-dir /tmp/obelisk-party/extracts \
  --output docs/party_draft.md \
  --model claude-opus-4-8
```

Note: All summaries now use "Zenvon" consistently. The `--list` output should show
a single "Zenvon" entity. If it shows variants, check whether a new session
introduced a new misspelling.

---

## Stage 3d — planning synthesis

```bash
# At 3 sessions all dossiers are worth including — skip the threshold cut
NPC_FILES=(docs/ensemble/merged_dossiers/npc_*.md)

python ~/src/CampaignGenerator/planning.py \
  --npc "${NPC_FILES[@]}" \
  --output docs/planning_draft.md \
  --model claude-opus-4-8
```

No arc score files yet. Add them when you build arc tracking for the obelisk
fragments / psionic goblin threat.

---

## Stage 4 — Review and promotion

```bash
diff docs/world_state.md    docs/world_state_draft.md    | less
diff docs/campaign_state.md docs/campaign_state_draft.md | less
diff docs/party.md          docs/party_draft.md          | less
diff docs/planning.md       docs/planning_draft.md       | less
```

All four grounding docs are currently empty templates — the diffs will be large.
Review each draft and promote when satisfied:

```bash
cp docs/world_state_draft.md    docs/world_state.md
cp docs/campaign_state_draft.md docs/campaign_state.md
cp docs/party_draft.md          docs/party.md
cp docs/planning_draft.md       docs/planning.md
```

---

## After each future session

1. Correct spelling in `summaries/00N/zoom_summary.md` (see Prerequisite 0), recording any new garble in `notes/vtt_transcription_corrections.md`, then re-run `python3 docs/ensemble/build_aliases.py` to refresh `aliases.json`
2. Copy into `docs/chapters/session_00N_<slug>.md`
3. Re-run Stage 1 (batch is resumable — only the new session extracts)
4. Re-run Stage 2b (resumable — existing dossiers update, new entities added)
5. Re-run Stage 2d (threads)
6. Re-run Stage 2e (merge)
7. Re-run `build_recent_events.py` — the short-term world state, **and** the chronological spine for synthesis (use `--window 0` for the spine; window the human-facing copy once past a few chapters):
   `python ~/src/CampaignGenerator/build_recent_events.py --corpus 'docs/ensemble/per_chapter/*/merged.json' --output docs/recent_events.md --window 0`
8. Re-run Stage 3a–3d (synthesis — feed `recent_events.md` + `threads.md` combined via `--threads` so the timeline is anchored, not reconstructed)
9. Diff and promote (`world_state`, `campaign_state`, `party`, `planning`; `recent_events.md` is already promoted by step 7)

---

## Watch-outs for this campaign

- **"Zenvon" spelling is now consistent across all summaries** (corrected from Xenophon/Xenobon/Zenovon in earlier versions). If a future session's VTT introduces a new misspelling, record it in `notes/vtt_transcription_corrections.md` (the single source of truth) and re-run `docs/ensemble/build_aliases.py` — never hand-edit `aliases.json`, which is generated from that file.
- **"Pip" is a sidekick AND a module NPC (renamed Tuck):** The module NPC renamed Tuck Stonehill may still appear as "Pip" in extractions from future sessions. Keep an eye on this in the `--list` output.
- **`name_glossary.md` is module-sourced, not session-sourced.** Module NPCs who haven't appeared yet will be tagged `[known]` anyway because the glossary lists them. This is fine — they'll produce empty or near-empty dossiers that the `--min-facts` floor filters out.
- **Marto** (Redbrand watcher from session 4 improv) will not appear in the dossiers until session 4's summary is extracted. He's session-canon now but not in the corpus yet.

---

## Future ideas

### All-Spark pipeline (Stages 3a–3d on the DGX)

Currently the pipeline is split: Stages 1 and 2b run on Spark (free, local), Stages
3a–3d call `claude-opus-4-8` (API cost, high quality). In principle, the synthesis
stages are **render tasks** — they take verified, human-reviewed dossiers and render
them into a readable grounding doc. That's the part where a local model can plausibly
do the job.

The `--dump-input --dump-only` flag already externalizes the prompts (shown in Stage
3a). The gap is wiring the dump output to the Spark endpoint instead of `claude -p`.

**Sketch of a full-Spark synthesis pass:**

```bash
# Dump each synthesis prompt to disk
python ~/src/CampaignGenerator/synthesise_world_state.py \
  --dossiers 'docs/ensemble/merged_dossiers/*.md' \
  --dump-input /tmp/obelisk_ws_prompt.md --dump-only

python ~/src/CampaignGenerator/campaign_state.py \
  --synthesize-only --extract-dir /tmp/obelisk-cstate/extracts \
  --dump-input /tmp/obelisk_cs_prompt.md --dump-only

python ~/src/CampaignGenerator/party.py \
  --synthesize-only --extract-dir /tmp/obelisk-party/extracts \
  --dump-input /tmp/obelisk_party_prompt.md --dump-only

python ~/src/CampaignGenerator/planning.py \
  --npc docs/ensemble/merged_dossiers/npc_*.md \
  --dump-input /tmp/obelisk_plan_prompt.md --dump-only

# Hit Spark with each prompt (parallel — they're independent)
for PROMPT in ws cs party plan; do
  curl -s http://spark:8001/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d "{\"model\": \"Qwen/Qwen3-Next-80B-A3B-Instruct-FP8\",
         \"messages\": [{\"role\": \"user\", \"content\": $(jq -Rs . < /tmp/obelisk_${PROMPT}_prompt.md)}],
         \"max_tokens\": 8192}" \
    | jq -r '.choices[0].message.content' \
    > docs/${PROMPT}_draft.md &
done
wait
```

**What to calibrate:** the synthesis prompts are long (all dossiers in context). At
3 sessions the total is small — Qwen3-80B should handle it. At 15–20 sessions the
context window may be a real constraint. That's the experiment worth running.

**Calibration finding:** `Qwen/Qwen3-Next-80B-A3B-Instruct-FP8` cannot handle
synthesis. The active-parameter count (~3B) is the ceiling — it can recognize and
list but not prioritize and organize across a multi-entity dossier set.
`Qwen/Qwen3.5-122B-A10B-FP8` (10B active) may clear the bar. Use that for Stage 3
at `http://spark:8001/v1` and keep the 80B-A3B for Stage 1 extraction.
Run `/spark-status` to confirm what's currently live before wiring up commands.

### Per-synthesis-section fan-out

Instead of one large prompt per grounding doc, fan out by section — one Spark agent
per NPC for `party.md`, one per faction for `planning.md`, one per location cluster
for `world_state.md`. Merge the outputs in a final pass (could be Claude or another
Spark call). This would:
- Fit larger campaigns in context (each agent sees only its slice)
- Allow parallel execution across both Spark nodes
- Make it easy to re-run only the sections that changed

The shape is the same as Stage 1's per-chapter fan-out — `ensemble_batch.py` is
already the model for this. A `synthesis_batch.py` that fans out over dossier groups
would close the loop on a fully local pipeline.
