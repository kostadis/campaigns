# How to Build a Campaign Mempalace

A reference guide based on the Out of the Abyss mempalace build.
Captures the decision-making process, not just the commands.

---

## The Goal

A searchable semantic index over curated campaign content that helps you:
- Ground new content in established canon (no plot holes, no contradictions)
- Find specific facts fast without burning tokens reading 8,000+ lines of prose
- Cross-reference between what happened (narrative), when it happened (timeline), and what's true now (reference)

---

## Step 0: Understand What You Have

Before touching mempalace, inventory your campaign directory. You're looking
for these categories:

| Category | Examples | Role |
|----------|---------|------|
| **The Bible** | A master session summary, campaign chronicle | Authoritative source of truth — what actually happened at the table |
| **Extraction intermediates** | distill_extractions/, planning_extractions/, campaign_state_extracts/, party_extract/ | LLM-generated structured views of the bible, organized by lens |
| **Current-state reference** | NPC dossiers, world_state.md, campaign_state.md, planning.md | Synthesized "what's true now" documents |
| **Published source material** | The adventure module (markdown or via 5etools) | Raw module text — location descriptions, encounter details, stat blocks |
| **Design documents** | campaign_master_plan.md, custom_tracking.md | Your modifications to the published adventure |
| **Raw session data** | summaries/, VTT transcripts, logs/ | Unprocessed session recordings |
| **Pipeline inputs** | voice/, examples/, config.yaml | Files that exist only to feed the CampaignGenerator pipeline |
| **Working material** | notes/, encounter drafts, arc designs | Staging area — not canon yet |

### Key questions to answer:

1. **Where is the bible?** The single document (or set of documents) that is
   the canonical record of what happened. Everything else is derived from this.

2. **Is it too large for a single file?** If over ~2,000 lines, it needs to
   be split into chapters for effective indexing.

3. **Do you have a CampaignGenerator pipeline?** If yes, you'll have multiple
   extraction dirs. Not all of them belong in the palace.

4. **What published module are you running?** If it's available via 5etools
   MCP, you don't need it in the palace (too large, dilutes search).

---

## Step 1: Split the Bible

If your campaign bible is a single large document, split it into chapter
files. This is a prerequisite — mempalace indexes per-file, and a single
8,000-line file produces poor search granularity.

**Rules:**
- Split on top-level headings (`# Chapter NN ...`)
- Preserve text verbatim — no editing, no summarizing
- **Do NOT modify or delete the original file** — the pipeline still uses it
- Name files sequentially: `chapter_01_title.md`, `chapter_02_title.md`
- If the original has inconsistent numbering (18, 18.05, 18.1...), renumber
  sequentially in the filenames. The original headings inside the files stay
  as-is. Mempalace indexes by content, not filenames.

**Example:**
```bash
mkdir -p docs/chapters
# Use a Python script to split on "# Chapter" headings
# Output: chapter_01_arrival.md, chapter_02_exploring_the_prison.md, ...
```

Verify the split is clean: total lines across split files should match the
original.

---

## Step 2: Decide the Wing Architecture

### The core question: What are you optimizing for?

Our answer for OotA: **Grounding the endgame in established canon.** Every
encounter and plot thread must be traceable to something that actually
happened at the table.

This drives every subsequent decision.

### Evaluating extraction dirs

If you have a CampaignGenerator pipeline with multiple extraction dirs,
examine each one:

1. **Read the same extraction number from each dir** (e.g., extract_025 from
   all four). Compare what each contains.

2. **Ask: what unique information does this dir carry that no other dir has?**

3. **Ask: is this an LLM summary (search accelerator) or a source of truth?**

For OotA we had four extraction dirs (52 files each):

| Dir | Lens | Unique value | Decision |
|-----|------|-------------|----------|
| `distill_extractions` | World state — factions, locations, events, mysteries, NPC snapshots | Only time-series view of the world itself | **Keep** — chronicle wing |
| `planning_extractions` | NPC prose dossiers | Temporal NPC portraits, but redundant with distill (NPC bullets) + docs/npcs/ (current state) | **Skip** |
| `campaign_state_extracts` | Quest/encounter completion log | Redundant with campaign_state.md (cumulative) and chapters (raw) | **Skip** |
| `party_extract` | PC arcs, relationships, resources | Redundant with party.md (current state) and chapters (raw) | **Skip** |

**The principle:** Only index content that provides a unique retrieval path
you can't get from the other wings. Everything else stays accessible via
file reads but doesn't pollute the search index.

### Evaluating the published module

Published adventure modules (OotA, CoS, etc.) are typically 5,000-10,000+
lines. They dominate the index and dilute search results. If you have
5etools MCP access, exclude the module from the palace entirely.

**Access pattern:** Use `get_section` and `search` via 5etools for raw module
text when needed. Use `tracking.txt` for the structural skeleton of quests
and NPCs.

### The trust hierarchy

This is the most important architectural decision:

| Trust level | What qualifies | Rule |
|-------------|---------------|------|
| **Authoritative** | Content that records what actually happened at the table (session summaries, transcripts) | Verify here before building anything on a claimed fact |
| **Search accelerator** | LLM-generated structured extractions of authoritative content | Use to find the right time window fast, then verify against authoritative source |
| **Working reference** | Synthesized current-state docs (NPC dossiers, grounding docs) | Use for building forward; verify against authoritative source when precision matters |

**Why this matters:** If you're designing an endgame encounter that calls
back to something that happened in session 12, you need to verify the actual
scene, not an LLM's paraphrase of it. The paraphrase might say "Daz
discovered the evidence" when the actual scene shows he saw the books but
didn't take them. That's a plot hole.

### Three-wing architecture (recommended for CampaignGenerator campaigns)

| Wing | Source | Trust | Purpose |
|------|--------|-------|---------|
| `narrative` | Chapter splits from the bible | Authoritative | "What actually happened?" |
| `chronicle` | distill_extractions (or best extraction dir) | Search accelerator | "What was the state at time X?" — find the window, then verify in narrative |
| `<campaign>` | NPC dossiers, grounding docs, design docs | Working reference | "What's true now? What's the plan?" |

**Shared room names create tunnels.** Use `npcs` and `world` in both
`chronicle` and `<campaign>` wings so a single search can cross between
timeline snapshots and current dossiers.

### Two-wing architecture (simpler campaigns without extraction pipeline)

| Wing | Source | Trust | Purpose |
|------|--------|-------|---------|
| `narrative` | Chapter splits | Authoritative | "What happened?" |
| `<campaign>` | NPC dossiers, all reference docs | Working reference | "What's true now?" |

### Single-wing (campaigns with no pipeline at all)

| Wing | Source | Purpose |
|------|--------|---------|
| `<campaign>` | All curated docs | Everything |

---

## Step 3: Set Up Exclusions

Create `.gitignore` in the campaign root. Mempalace respects gitignore during
mining.

### Always exclude:
- `summaries/` — raw session data (synthesized elsewhere)
- `logs/` — operational
- `voice/`, `examples/` — pipeline rendering inputs
- Tooling files: `config.yaml`, `ui_config.yaml`, `*.sh`, `entities.json`
- `.claude/`, `MEMPALACE.md`
- `notes/` — working/staging area, not canon

### For three-wing, also exclude from root:
- Subdirectory wings (`docs/chapters/`, `docs/distill_extractions/`) — mined
  separately to prevent double-mining
- The unsplit bible (replaced by chapter splits in narrative wing)
- Pipeline intermediate dirs that aren't getting their own wing
- Party PC files from NPC directories (they're PCs, not NPCs)

### For published modules:
- The full module markdown (use 5etools MCP instead)

---

## Step 4: Write mempalace.yaml Files

Each wing needs its own `mempalace.yaml` in its source directory.

### Narrative wing (`docs/chapters/mempalace.yaml`)

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

### Chronicle wing (`docs/distill_extractions/mempalace.yaml`)

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
  description: Content that doesn't fit other rooms
  keywords: []
```

**Note:** In practice, distill extractions route heavily to `npcs` because
they lead with `## NPCs` sections. This is fine — the content is still
searchable. Room filtering just doesn't help much within this wing.

### Campaign reference wing (root `mempalace.yaml`)

```yaml
wing: <campaign_name>
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
- Add campaign-specific keywords (location names, villain names, faction names)
- **Shared room names create tunnels** — use `npcs` and `world` in both
  chronicle and reference wings

---

## Step 5: Init, Dry-Run, Mine

```bash
MP=/home/kroussos/worldanvil_pipeline/venv/bin/mempalace

# Init (generates entities.json — informational only)
$MP init --yes <campaign_dir>

# IMPORTANT: init overwrites your root mempalace.yaml with auto-detected
# config. Restore your custom yaml after init.

# Dry-run each wing to check classification
$MP mine <campaign_dir>/docs/distill_extractions --dry-run 2>&1 | tail -20
$MP mine <campaign_dir>/docs/chapters --dry-run 2>&1 | tail -20
$MP mine <campaign_dir> --dry-run 2>&1 | tail -40

# Check:
# - Room distribution looks balanced
# - No excluded files appear
# - Core docs route sensibly

# Mine for real — SUBDIRS BEFORE ROOT
$MP mine <campaign_dir>/docs/distill_extractions   # chronicle
$MP mine <campaign_dir>/docs/chapters               # narrative
$MP mine <campaign_dir>                              # campaign reference
```

**Order matters:** Root's `.gitignore` excludes subdirs to prevent
double-mining. Mine subdirs first.

---

## Step 6: Register MCP Server

```bash
# From inside the campaign directory:
claude mcp add mempalace -- /home/kroussos/worldanvil_pipeline/venv/bin/python -m mempalace.mcp_server
```

This is project-scoped. Each campaign gets its own registration.

**You must restart Claude Code to pick up the new MCP server.**

---

## Step 7: Verify

```bash
$MP status

# Test each wing
$MP search "<campaign-specific NPC>" --wing chronicle
$MP search "<memorable scene keyword>" --wing narrative
$MP search "<current threat or faction>" --wing <campaign>

# Test cross-wing (no filter)
$MP search "<NPC name>"
# Should return hits from multiple wings
```

---

## Step 8: Write MEMPALACE.md

Create `<campaign_dir>/MEMPALACE.md` as the campaign-specific usage guide.
Document:

1. Wing architecture with trust levels
2. Room taxonomy tables with drawer counts
3. Search patterns — when to use which wing (with examples)
4. What's excluded and why
5. The canon rule (notes → human review → grounding docs → palace)
6. Refresh workflow (per-wing re-mine commands)
7. Known quirks (uneven room distribution, oversized chapters, etc.)

---

## The Notes Directory

Every campaign needs a `notes/` directory as a working/staging area. It stays
OUT of the palace.

```
notes/
  canon/          -- cross-campaign shared history (portable across campaigns)
  <flat files>    -- encounter designs, session prep, arc planning
```

### The canon extraction workflow

1. Design material and cross-campaign history goes in `notes/`
2. Human reviews and identifies what's canon vs. what's planning
3. Canon gets extracted into the right grounding doc or NPC dossier
4. Re-mine the campaign reference wing to pick up new/updated files

### Cross-campaign canon

If you run interlocking campaigns (e.g., Group 1's actions become Group 2's
history), keep shared canon in `notes/canon/`. This directory is portable —
copy or symlink it across campaign workspaces.

**Example:** Group 2 captured Lolth as part of a deal with Vhaerun. That
action motivated the Orthodoxy to convince Gromph Baenre to perform the
ritual that triggered the demon lord incursion in OotA. This fact lives in
`notes/canon/` and gets extracted into OotA's world_state and NPC dossiers
after review.

---

## Key Principles

### 1. The bible is the single source of truth

The session summary / campaign chronicle is authoritative. Everything else —
extractions, dossiers, grounding docs — is a distillation. When building on
a fact, verify against the bible chapters.

### 2. LLM outputs are search accelerators, not architects

Distill extractions and NPC dossiers are LLM-generated. They're excellent
for finding things fast. They're not trusted for precision decisions (scope,
attribution, ordering) without human verification against the bible.

This follows the LLM pipeline rule:
> **Good:** LLM extracts → human reviews → LLM renders inside reviewed structure
> **Bad:** LLM extracts → LLM structures → LLM renders (errors compound silently)

### 3. Only index content with unique retrieval value

If two dirs contain overlapping information, pick the one with the most
unique content and skip the other. The skipped dir remains accessible via
file reads — it just doesn't pollute search results.

### 4. Notes are staging, not canon

Nothing enters the palace directly from working material. The palace indexes
what IS true. Notes contain what MIGHT happen. The human review step between
notes and palace is non-negotiable.

### 5. Published modules stay outside

If you have 5etools MCP, the full module text is better accessed via
`get_section` than indexed in the palace. Module text is large, static, and
available on demand — it doesn't need semantic search.

### 6. The temporal index serves the narrative

The chronicle wing doesn't replace reading the actual scene. It tells you
WHERE to look and WHAT to verify. The workflow is always: search chronicle →
find the time window → read the narrative chapter → confirm the fact.

---

## Refresh Cheat Sheet

| Event | Command |
|-------|---------|
| Updated grounding docs or NPC dossiers | `$MP mine <campaign_dir>` |
| New session chapters added | `$MP mine <campaign_dir>/docs/chapters` |
| Re-ran extraction pipeline | `$MP mine <campaign_dir>/docs/distill_extractions` |
| Full rebuild | `rm -rf ~/.mempalace/palace/` then mine all three in order |

Always mine subdirs before root.

---

## Gotchas

- **`mempalace init` overwrites your root `mempalace.yaml`** with
  auto-detected config. Save your custom yaml before running init, or
  restore it after.
- **The Phandalin (or other campaign) palace shares the same DB.** Status
  shows all campaigns' wings. This is expected — each wing is namespaced.
- **Extraction files route heavily to one room** because they lead with a
  dominant section (e.g., `## NPCs`). Room filtering within that wing
  doesn't help much. Just search the wing directly.
- **Very large chapters produce disproportionate drawer counts** and may
  dominate search results in the narrative wing.
- **Cross-campaign canon needs manual coordination.** There's no automatic
  sync between campaign workspaces. Copy files or use symlinks.
