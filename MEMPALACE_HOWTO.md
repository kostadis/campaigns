# How to Build a Campaign Mempalace

Reference for configuring mempalace in a campaign workspace. Point Claude
at this file when you want it to set up, extend, or audit a campaign's
palace.

---

## How to Use This Doc

There are two layers of mempalace docs in this repo:

| Doc | Scope | Audience | Lifecycle |
|-----|-------|----------|-----------|
| **`campaigns/MEMPALACE_HOWTO.md`** (this file) | Generic procedure & principles that apply to any campaign | Anyone setting up or modifying a palace | Stable — update only when the underlying tool changes |
| **`<campaign>/MEMPALACE.md`** | Per-campaign usage guide: actual wing/room counts, exclusions, search patterns, refresh workflow | Whoever's working in that campaign | Refresh after every meaningful palace change |
| **`<campaign>/MEMPALACE_HORIZON.md`** (optional, OOTA-style) | Current horizon marker — last chapter mined, drawer baseline, extend vs rebuild workflow | Anyone re-mining an active campaign | Update on every mine |

**For Claude:** read this whole doc first when asked to configure mempalace,
then read the campaign's `MEMPALACE.md` (and `MEMPALACE_HORIZON.md` if
present). The howto tells you *how*; the per-campaign doc tells you
*what's actually there*.

There is also an automation skill `mempalace-campaign` that follows this
procedure end-to-end. Use it for net-new setup; use this doc when you need
to deviate, extend, or debug.

---

## Procedure for Claude

Before running any command, identify which task you're doing:

| Task | Trigger | Where to start |
|------|---------|----------------|
| **Net-new setup** | Campaign has no `mempalace.yaml` | Step 0 below |
| **Extend** | New session chapters / new docs to mine | Refresh Cheat Sheet (bottom) |
| **Tune** | Search results are off, room taxonomy needs change | Step 2 (architecture) → Step 4 (yaml) → re-mine |
| **Audit** | "Is this campaign's palace healthy?" | Read `<campaign>/MEMPALACE.md`, run `mp status --palace <name>`, sanity-check searches |
| **Full rebuild** | Inconsistency, taxonomy churn, corruption | Refresh Cheat Sheet → "Full rebuild" |

**Always read the campaign's `CLAUDE.md` and `MEMPALACE.md` first.** They
record campaign-specific gotchas (e.g., OOTA's `.mempalaceignore` filename
fragility, Phandalin's chronicle-room concentration) that override the
generic guidance below.

**Per-campaign palace DBs are the standard** (since 2026-04). Each campaign
gets its own DB at `~/.mempalace/palaces/<campaign>/`, addressed via
`--palace <campaign>` on every CLI call. The shared `~/.mempalace/palace/`
default is legacy.

---

## Step 0: Understand What You Have

Inventory the campaign directory. You're looking for these categories:

| Category | Examples | Role |
|----------|---------|------|
| **The Bible** | A master session summary, campaign chronicle | Authoritative — what actually happened at the table |
| **Extraction intermediates** | `distill_extractions/`, `planning_extractions/`, `campaign_state_extracts/`, `party_extract/` | LLM-generated structured views of the bible |
| **Current-state reference** | NPC dossiers, `world_state.md`, `campaign_state.md`, `planning.md` | Synthesized "what's true now" docs |
| **Published source material** | The adventure module (markdown or via 5etools) | Raw module text — locations, encounters, stat blocks |
| **Design documents** | `campaign_master_plan.md`, `custom_tracking.md`, `canon_guardrails.md` | Modifications to the published adventure |
| **Raw session data** | `summaries/`, VTT transcripts, `logs/` | Unprocessed session recordings |
| **Pipeline inputs** | `voice/`, `examples/`, `config.yaml` | Files that exist only to feed CampaignGenerator |
| **Working material** | `notes/`, encounter drafts, arc designs | Staging — not canon yet |

### Key questions to answer:

1. **Where is the bible?** The single canonical record. Everything else is
   derived from it.
2. **Is it too large for a single file?** Over ~2,000 lines → split into
   chapters. Mempalace indexes per-file; one giant file produces poor
   search granularity.
3. **Is there a CampaignGenerator pipeline?** If yes, you'll have multiple
   extraction dirs. Not all of them belong in the palace.
4. **What published module is running?** If 5etools MCP covers it, exclude
   the module from the palace (too large, dilutes search).

---

## Step 1: Split the Bible

If the bible is one large doc, split into chapter files. **Do not modify or
delete the original** — the CampaignGenerator pipeline still uses it.

**Rules:**
- Split on top-level headings (`# Chapter NN ...`)
- Preserve text verbatim — no editing, no summarizing
- Name files sequentially: `chapter_01_title.md`, `chapter_02_title.md`
- If the original has decimal sub-chapters (`18.05`, `18.1`, ...), renumber
  sequentially in filenames. Original headings inside files stay as-is.
- Output goes into `docs/chapters/`

CampaignGenerator ships `split_chapters.py` for this. **Gotcha:**
`split_chapters.py` wipes `docs/chapters/mempalace.yaml` on every run.
Restore it from git before re-mining:
```bash
git show HEAD:<campaign>/docs/chapters/mempalace.yaml > <campaign>/docs/chapters/mempalace.yaml
```

Verify the split: total lines across split files ≈ original.

---

## Step 2: Decide the Wing Architecture

### The core question: What are you optimizing for?

For active long-running campaigns: **grounding new content in established
canon.** Every encounter and plot thread must be traceable to something
that actually happened at the table. This drives every subsequent decision.

### Evaluating extraction dirs

If you have a CampaignGenerator pipeline with multiple extraction dirs,
examine each one:

1. **Read the same extraction number from each dir** (e.g., `extract_025`
   from all four). Compare what each contains.
2. **Ask: what unique information does this dir carry that no other dir has?**
3. **Ask: is this an LLM summary (search accelerator) or a source of truth?**

Worked example (OOTA had four extraction dirs):

| Dir | Lens | Unique value | Decision |
|-----|------|-------------|----------|
| `distill_extractions` | World state — factions, locations, events, mysteries, NPC snapshots | Only time-series view of the world itself | **Keep** — chronicle wing |
| `planning_extractions` | NPC prose dossiers | Redundant with distill (NPC bullets) + `docs/npcs/` (current state) | **Skip** |
| `campaign_state_extracts` | Quest/encounter completion log | Redundant with `campaign_state.md` + chapters | **Skip** |
| `party_extract` | PC arcs, relationships | Redundant with `party.md` + chapters | **Skip** |

**Principle:** only index content with a unique retrieval path. Skipped
dirs stay accessible via file reads; they just don't pollute search.

### Evaluating the published module

Modules (OotA, CoS, etc.) are typically 5,000–10,000+ lines. They dominate
the index and dilute results. With 5etools MCP available, exclude the
module from the palace and access it via `get_section` / `search`.

### The trust hierarchy

The most important architectural decision:

| Trust level | What qualifies | Rule |
|-------------|---------------|------|
| **Authoritative** | Session summaries / transcripts / chapter splits — what actually happened at the table | Verify here before building anything on a claimed fact |
| **Search accelerator** | LLM-generated structured extractions of authoritative content | Use to find the right time window fast, then verify against authoritative |
| **Working reference** | Synthesized current-state docs (NPC dossiers, grounding docs) | Use for building forward; verify against authoritative when precision matters |

This mirrors the global LLM pipeline rule: LLM extracts → human reviews →
LLM renders inside reviewed structure. Distill extractions are search
accelerators, never architects of new content.

### Three-wing architecture (recommended for CampaignGenerator campaigns)

| Wing | Source | Trust | Question it answers |
|------|--------|-------|--------------------|
| `narrative` | Chapter splits from the bible | Authoritative | "What actually happened?" |
| `chronicle` | `distill_extractions/` (or best extraction dir) | Search accelerator | "What was the state at time X?" |
| `<campaign>` | NPC dossiers, grounding docs, design docs | Working reference | "What's true now? What's the plan?" |

**Shared room names create tunnels.** Use `npcs` and `world` in both
`chronicle` and `<campaign>` wings so a single search can cross between
timeline snapshots and current dossiers via `mempalace_find_tunnels` /
`mempalace_traverse`.

### Two-wing architecture (campaigns without an extraction pipeline)

| Wing | Source | Trust |
|------|--------|-------|
| `narrative` | Chapter splits | Authoritative |
| `<campaign>` | NPC dossiers, all reference docs | Working reference |

### Single-wing (no pipeline, simple campaign)

| Wing | Source |
|------|--------|
| `<campaign>` | All curated docs |

---

## Step 3: Set Up Exclusions

Create `.mempalaceignore` in the campaign root. Mempalace reads
`.mempalaceignore` first; if absent, falls back to `.gitignore`.
**Prefer `.mempalaceignore`** — decouples mining exclusions from
version-control concerns (see `~/src/mempalace/docs/MEMPALACEIGNORE.md`).

### Always exclude from root mining:
- `summaries/` — raw session data
- `logs/` — operational
- `voice/`, `examples/` — pipeline rendering inputs
- Tooling: `config.yaml`, `ui_config.yaml`, `*.sh`, `entities.json`
- `.claude/`, `MEMPALACE.md`, `MEMPALACE_HORIZON.md`
- `notes/` — working/staging area, not canon

### For three-wing setups, also exclude from root:
- Subdirectory wings: `docs/chapters/`, `docs/distill_extractions/` (mined
  separately to prevent double-mining)
- The unsplit bible (replaced by chapter splits in narrative wing)
- Other pipeline intermediate dirs not getting their own wing
- Party PC files in NPC directories (PCs, not NPCs)

### For published modules:
- The full module markdown (use 5etools MCP)

**Filename fragility (gotcha):** `.mempalaceignore` lists exact paths. If
the bible's filename changes (e.g., `The Underdark.md` → `TheUnderdark.md`
after a git rename), update the ignore. Sanity-check after any rename:
search the campaign wing for a known scene — the top hit should be a
dossier or grounding doc, **not** the unsplit bible.

---

## Step 4: Write `mempalace.yaml` Files

Each wing needs its own `mempalace.yaml` in its source directory.

### Narrative wing — `docs/chapters/mempalace.yaml`

```yaml
wing: narrative
rooms:
- name: chapters
  description: Narrative prose chapters from the campaign bible
  keywords: [chapter, session, narrative, story]
- name: general
  description: Fallback
  keywords: []
```

Simple — everything routes to `chapters`.

### Chronicle wing — `docs/distill_extractions/mempalace.yaml`

```yaml
wing: chronicle
rooms:
- name: npcs
  description: NPC state snapshots across the campaign timeline
  keywords: [npc, character, dossier, location, state, faction]
- name: world
  description: World events, locations, faction movements
  keywords: [world, event, location, faction, history, alliance]
- name: arcs
  description: Threads, mysteries, and unresolved plot points
  keywords: [thread, mystery, unresolved, quest, score]
- name: general
  description: Fallback
  keywords: []
```

**Note:** distill extractions route heavily to `npcs` because they lead
with `## NPCs`. Content stays searchable; room filtering inside this wing
just doesn't help much. Documented in the per-campaign MEMPALACE.md.

### Campaign reference wing — root `mempalace.yaml`

```yaml
wing: <campaign_name>   # e.g. phandalin, abyss, hillsfar
rooms:
- name: npcs
  description: NPC dossiers, character profiles, relationships
  keywords: [npcs, npc, dossier, character, profile]
- name: world
  description: World state, lore, background, politics
  keywords: [world_state, world, background, lore, faction]
- name: arcs
  description: Quest tracking, threat trackers, campaign master plan
  keywords: [tracking, arc, quest, score, threat, master_plan]
- name: mechanics
  description: Game mechanics, rules, encounter frameworks
  keywords: [mechanics, rules, encounter, combat]
- name: dead
  description: Archived content, resolved threads
  keywords: [dead, archived, finished]
- name: general
  description: Top-level docs that don't fit
  keywords: []
```

**Tailoring rules:**
- Drop rooms that don't apply (no `dead/` dir → no room)
- Add campaign-specific keywords (location names, villain names, factions)
- Use the same `npcs` and `world` room names in both `chronicle` and
  `<campaign>` wings to enable tunneling

---

## Step 5: Init, Dry-Run, Mine

```bash
MP=/home/kroussos/worldanvil_pipeline/venv/bin/mempalace
PALACE=<campaign_name>            # e.g. abyss, phandalin
CAMPAIGN=/home/kroussos/campaigns/<campaign_dir>

# Init (generates entities.json — informational only)
$MP --palace $PALACE init --yes $CAMPAIGN

# GOTCHA: init overwrites your root mempalace.yaml with auto-detected
# config. Restore your custom yaml after init:
git checkout $CAMPAIGN/mempalace.yaml

# Dry-run each wing to check classification
$MP --palace $PALACE mine $CAMPAIGN/docs/distill_extractions --dry-run 2>&1 | tail -20
$MP --palace $PALACE mine $CAMPAIGN/docs/chapters --dry-run 2>&1 | tail -20
$MP --palace $PALACE mine $CAMPAIGN --dry-run 2>&1 | tail -40

# Check:
# - Room distribution looks balanced (within wing constraints — chronicle
#   will skew npcs-heavy, that's expected)
# - No excluded files appear
# - Core docs route to sensible rooms

# Mine for real — SUBDIRS BEFORE ROOT
$MP --palace $PALACE mine $CAMPAIGN/docs/distill_extractions   # chronicle
$MP --palace $PALACE mine $CAMPAIGN/docs/chapters               # narrative
$MP --palace $PALACE mine $CAMPAIGN                              # campaign reference
```

**Order matters:** root's `.mempalaceignore` excludes subdirs to prevent
double-mining. Mine subdirs first so root mining sees its own scope only.

---

## Step 6: Register MCP Server

```bash
# From inside the campaign directory:
claude mcp add mempalace -- /home/kroussos/worldanvil_pipeline/venv/bin/python -m mempalace.mcp_server --palace <campaign_name>
```

Project-scoped. Each campaign gets its own registration. **Restart Claude
Code** to pick up the new MCP server.

---

## Step 7: Verify

```bash
$MP --palace <campaign> status

# Test each wing
$MP --palace <campaign> search "<campaign-specific NPC>" --wing chronicle
$MP --palace <campaign> search "<memorable scene keyword>" --wing narrative
$MP --palace <campaign> search "<current threat or faction>" --wing <campaign>

# Cross-wing (no filter) — should hit multiple wings
$MP --palace <campaign> search "<NPC name>"
```

Sanity tests every campaign should pass:
- A search for a known scene returns the relevant chapter file (narrative
  wing), not a giant unsplit bible
- A search for a current NPC returns the dossier (campaign wing)
- A cross-wing search for an NPC name returns hits from both `chronicle`
  (snapshots over time) and `<campaign>` (current dossier)

---

## Step 8: Write `<campaign>/MEMPALACE.md`

Create the per-campaign usage guide. Use this template:

```markdown
# MemPalace — <Campaign> Usage Guide

Semantic search over the campaign's content, organized into <N> wings
for different retrieval needs.

**Palace DB:** `~/.mempalace/palaces/<campaign>/` (always pass
`--palace <campaign>`)

## Wing Architecture

| Wing | Purpose | Source | Drawers | Question it answers |
|------|---------|--------|---------|--------------------|
| `narrative` | ... | `docs/chapters/` (N files) | ~X | "What actually happened?" |
| `chronicle` | ... | `docs/distill_extractions/` (N files) | ~X | "What was the state at time T?" |
| `<campaign>` | ... | grounding docs, NPC dossiers, tracking | ~X | "What's true now?" |

### Trust Levels
| Wing | Trust | Rule |
|------|-------|------|
| `narrative` | **Authoritative** | Verify here first |
| `chronicle` | **Search accelerator** | Narrow time window, verify in narrative |
| `<campaign>` | **Working reference** | Verify against narrative when precision matters |

### Tunnels
List shared room names that connect wings (typically `npcs`, `world`).

## Wing / Room Taxonomy
One table per wing with room → drawer count → contents. Get counts from
`mp --palace <campaign> status`.

## What's Excluded (and why)
Per-line table: path → reason → access-instead-via.

## Search Patterns — When to Use Which Wing
Concrete example queries showing which wing to filter to for which kind
of question.

## The Canon Rule
Notes are staging, not canon. Promote to docs/ → re-mine the affected wing.

## Refresh Workflow
Per-wing re-mine commands. Mention subdirs-before-root order.

## MCP Tools
List of mempalace_* tools available in this campaign's Claude Code session.

## Known Quirks
Campaign-specific oddities: chronicle-room concentration, oversized
chapters, filename fragility, palace DB sharing or isolation, etc.

## Operational Rules (optional, for active campaigns)
Mining priority order, re-mine triggers, validation checklist.
```

For active campaigns with frequent re-mining, also write a
`MEMPALACE_HORIZON.md` that records the last-mined chapter, drawer
baseline, and forward-extension procedure (see OOTA's for an example).

---

## The Notes Directory

Every campaign needs a `notes/` directory as a working/staging area. It
stays OUT of the palace.

```
notes/
  canon/          -- cross-campaign shared history (portable across campaigns)
  <flat files>    -- encounter designs, session prep, arc planning
```

### Canon extraction workflow

1. Design material and cross-campaign history goes in `notes/`
2. Human reviews and identifies what's canon vs. what's planning
3. Canon gets extracted into the right grounding doc or NPC dossier
4. Re-mine the campaign reference wing to pick up new/updated files

### Cross-campaign canon

If campaigns interlock (Group 1's actions become Group 2's history), keep
shared canon in `notes/canon/`. Portable — copy or symlink across
workspaces. Do not mempalace it directly; promote to a grounding doc in
the receiving campaign first, then re-mine.

---

## Key Principles

### 1. The bible is the single source of truth
Session summaries / chapter splits are authoritative. Everything else —
extractions, dossiers, grounding docs — is a distillation. Verify against
chapters when building on a fact.

### 2. LLM outputs are search accelerators, not architects
Distill extractions and NPC dossiers are LLM-generated. Excellent for
finding things fast. Not trusted for precision (scope, attribution,
ordering) without human verification.

> **Good:** LLM extracts → human reviews → LLM renders inside reviewed structure
> **Bad:** LLM extracts → LLM structures → LLM renders (errors compound silently)

### 3. Only index content with unique retrieval value
Two dirs with overlapping information → pick one, skip the other. Skipped
content stays accessible via file reads.

### 4. Notes are staging, not canon
Nothing enters the palace directly from working material. The palace
indexes what IS true; notes contain what MIGHT happen. Human review is
non-negotiable.

### 5. Published modules stay outside
With 5etools MCP, full module text is better accessed via `get_section`
than indexed. Module text is large, static, and available on demand.

### 6. The temporal index serves the narrative
The chronicle wing doesn't replace reading the actual scene. It tells you
WHERE to look and WHAT to verify. Workflow: search chronicle → find time
window → read narrative chapter → confirm fact.

### 7. Per-campaign palace DBs
Each campaign has its own DB. Always pass `--palace <campaign>`. Don't
let two campaigns share a DB unless you have an explicit reason — they
end up in each other's search results.

---

## Refresh Cheat Sheet

All commands assume `MP="$MP --palace <campaign>"`.

| Event | Command |
|-------|---------|
| Updated grounding docs / NPC dossiers | `$MP mine <campaign_dir>` |
| New session chapters added | `$MP mine <campaign_dir>/docs/chapters` |
| Re-ran extraction pipeline | `$MP mine <campaign_dir>/docs/distill_extractions` |
| Full rebuild | `rm -rf ~/.mempalace/palaces/<campaign>/` then mine all three in order |

Always mine subdirs before root.

---

## Gotchas (consolidated)

- **`mempalace init` overwrites the root `mempalace.yaml`** with
  auto-detected config. Restore from git after init.
- **`split_chapters.py` wipes `docs/chapters/mempalace.yaml`.** Restore
  from git before re-mining.
- **`.mempalaceignore` filename rules are fragile.** Exact path match.
  Renaming the bible breaks the ignore silently and the bible gets
  re-mined into the campaign wing on top of the chapter splits. Sanity
  query after any rename.
- **Subdir-before-root mining order is mandatory.** Root's
  `.mempalaceignore` (or `.gitignore` fallback) excludes the subdir wings
  to prevent double-mining; mine subdirs first.
- **Per-campaign palace DBs need `--palace <name>` on every CLI call.**
  Without it, mempalace falls back to `~/.mempalace/config.json`'s
  default and may write into the wrong DB.
- **Extraction files route heavily to one room** because they lead with
  a dominant section (e.g., `## NPCs`). Room filtering within that wing
  doesn't help much. Just search the wing directly.
- **Very large chapters produce disproportionate drawer counts** and may
  dominate narrative-wing search results. Document in MEMPALACE.md.
- **Cross-campaign canon needs manual coordination.** No automatic sync
  between workspaces. Copy files or symlink `notes/canon/`.
- **MCP server needs Claude Code restart** to pick up the new
  registration; tools won't appear until then.
- **Embedding device:** mempalace uses CPU `onnxruntime` by default. The
  GPU build wants CUDA 12 runtime libs that conflict with torch's bundled
  CUDA 13. CPU mine completes in minutes — don't swap unless you're
  prepared to install CUDA 12 alongside.
