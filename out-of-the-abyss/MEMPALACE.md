# MemPalace — Out of the Abyss Campaign Usage Guide

Semantic search over the campaign's content, organized into three wings
for different retrieval needs. Queryable via CLI or via MCP tools inside
a Claude Code session scoped to this project.

---

## Three-Wing Architecture

| Wing | Purpose | Source | Drawers | Question it answers |
|------|---------|--------|---------|-------------------|
| `narrative` | Canonical record of what happened at the table | `docs/chapters/` (52 chapter files split from The Underdark.md) | ~8,400 | "What exactly happened? What did they say?" |
| `chronicle` | Structured world-state snapshots over time | `docs/distill_extractions/` (52 files) | ~1,070 | "What was X's state at that point? What factions were active?" |
| `abyss` | Current-state reference for building forward | NPC dossiers (120), grounding docs, master plan, tracking | ~820 | "What's the current state of X? What's the endgame plan?" |

**Total:** ~10,300 drawers across 3 wings.

**Tunnels:** The `chronicle` and `abyss` wings share the `npcs` and `world`
room names. Graph traversal (`mempalace_traverse`, `mempalace_find_tunnels`)
can cross between wings — e.g. from a timeline NPC snapshot to the current
dossier.

### Trust Levels

| Wing | Trust | Rule |
|------|-------|------|
| `narrative` | **Authoritative** | The bible. Verify here before building anything on a claimed fact. |
| `chronicle` | **Search accelerator** | LLM-generated structured extractions. Use to find the right time window fast, then verify against narrative. |
| `abyss` | **Working reference** | Current-state docs for building forward. Verify against narrative when precision matters. |

---

## Command Line Usage

Set an alias first to save typing:

```bash
alias mp='/home/kroussos/worldanvil_pipeline/venv/bin/mempalace'
```

### The commands you'll actually use

**`mp status`** — health check, shows drawer counts per wing/room.

```bash
mp status
```

**`mp search "query"`** — semantic search, the main workhorse.

```bash
# Cross-wing (find everything about a topic)
mp search "Shal advisor to the Deep King"

# Canonical record — what actually happened at the table?
mp search "Buppido murder Yuk Yuk" --wing narrative

# Timeline facts — what was the state at a point in time?
mp search "Gracklstugh factions" --wing chronicle

# Current state — who's where, what do they want?
mp search "Zuggtmoy wedding" --wing abyss
```

**`mp search --room`** — narrow to a specific room.

```bash
mp search "Hgraam" --wing abyss --room npcs
mp search "heat system" --wing abyss --room arcs
```

---

## Wing / Room Taxonomy

### narrative (chapters)

| Room | Contents | Drawers |
|------|----------|---------|
| `chapters` | 52 chapter splits from The Underdark.md — the campaign bible | ~8,400 |

### chronicle (distill_extractions)

| Room | Contents | Drawers |
|------|----------|---------|
| `npcs` | NPC state snapshots, faction states at each extraction point | ~1,000 |
| `world` | World events, locations, faction movements | ~70 |

### abyss (current reference)

| Room | Contents | Drawers |
|------|----------|---------|
| `npcs` | 120 NPC dossiers (party PCs excluded) | ~600 |
| `world` | world_state.md, world_state_custom.md, planning.md, party.md | ~100 |
| `arcs` | campaign_master_plan.md, custom_tracking.txt, tracking.txt | ~50 |
| `dead` | Archived content (deals, resolved threads) | ~30 |
| `mechanics` | mechanics.md, heat.md | ~30 |
| `general` | Top-level docs that don't fit elsewhere | ~10 |

---

## What's Excluded (and why)

| Content | Reason | Access instead via |
|---------|--------|--------------------|
| `docs/planning_extractions/` | Pipeline intermediate — NPC prose redundant with dossiers | File reads |
| `docs/campaign_state_extracts/` | Pipeline intermediate — quest log redundant with campaign_state.md | File reads |
| `docs/party_extract/` | Pipeline intermediate — party state redundant with party.md | File reads |
| `docs/background/Out of the Abyss.md` | 9,357 lines — too large, dilutes search | 5etools MCP (get_section, search) |
| `docs/The Underdark.md` | Unsplit bible — chapters are mined separately | Read the chapter files |
| `notes/` | Working/staging area — not canon yet | File reads |
| Party PC files (daz, grygum, thorin, zalthir) | PCs tracked separately, not NPCs | File reads |
| `summaries/`, `voice/`, `examples/`, `logs/` | Raw session data, pipeline inputs, operational | File reads |

---

## Search Patterns — When to Use Which Wing

**"What exactly did Daz say to Asha about Lolth?"**
→ `--wing narrative` — you need the verbatim scene

**"When did the party first learn about Shal?"**
→ `--wing chronicle` — find the extraction number, then read that chapter

**"What is Shal's current status and what do we know?"**
→ `--wing abyss` — current NPC dossier

**"I'm designing a callback to Gracklstugh — what threads are dangling?"**
→ no wing filter — cross-wing search hits timeline, current state, and raw narrative

**"Is this encounter design consistent with what happened?"**
→ Start with `--wing chronicle` to narrow the time window, then `--wing narrative` to verify the specific scene

---

## The Canon Rule

**Notes are staging, not canon.** Nothing enters the palace directly from
`notes/`. The workflow:

1. Design material goes in `notes/` (encounters, arc designs, cross-campaign canon)
2. Human reviews and identifies what's canon vs. planning
3. Canon gets extracted into the right grounding doc or NPC dossier
4. Re-mine the `abyss` wing to pick up the new/updated files

Cross-campaign canon lives in `notes/canon/` — portable across campaign
workspaces (e.g., can be copied/linked to Phandalin).

---

## Refresh Workflow

### After updating grounding docs or NPC dossiers (abyss wing)

```bash
mp mine /home/kroussos/campaigns/out-of-the-abyss
```

### After a new session (new chapters added)

```bash
mp mine /home/kroussos/campaigns/out-of-the-abyss/docs/chapters
```

### After re-running the extraction pipeline (new distill extractions)

```bash
mp mine /home/kroussos/campaigns/out-of-the-abyss/docs/distill_extractions
```

### Full rebuild (nuclear option)

```bash
rm -rf ~/.mempalace/palace/
mp mine /home/kroussos/campaigns/out-of-the-abyss/docs/distill_extractions
mp mine /home/kroussos/campaigns/out-of-the-abyss/docs/chapters
mp mine /home/kroussos/campaigns/out-of-the-abyss
```

Order matters: mine subdirs before root. Root's `.gitignore` excludes subdirs
to prevent double-mining.

---

## MCP Tools

When Claude Code is running in this project, the mempalace MCP server
provides these tools:

| Tool | Use |
|------|-----|
| `mempalace_search` | Semantic search across wings/rooms |
| `mempalace_open_drawer` | Read full drawer contents |
| `mempalace_traverse` | Follow connections from a drawer |
| `mempalace_find_tunnels` | Find cross-wing connections (chronicle ↔ abyss) |
| `mempalace_kg_query` | Query the knowledge graph |
| `mempalace_kg_add` | Add knowledge graph entries |
| `mempalace_add_drawer` | Manually file a new drawer |
| `mempalace_status` | Palace health check |

---

## Troubleshooting

- **"No mempalace.yaml found"** — running mine from wrong dir. Each wing's
  source dir needs its own yaml (chapters/, distill_extractions/, and root).
- **Everything routes to `general`** — keywords too weak. Add folder/topic names.
- **MCP tools don't appear** — server registered at wrong scope or Claude Code
  wasn't restarted. Check `~/.claude.json`.
- **Stale content after doc edits** — re-mine the affected wing.
- **Segfault on search** — run `mp repair`.
- **Full rebuild** — `rm -rf ~/.mempalace/palace/` then re-mine all wings.

---

## Known Quirks

- Chronicle wing is NPC-heavy (46 of 52 files route to `npcs` room) because
  the distill extractions lead with `## NPCs` sections. Room filtering within
  chronicle isn't very useful — just search the wing directly.
- Chapter 52 (A Spore-Filled Finale) is very large (~7,400 drawers). Searches
  in the narrative wing may be weighted toward this chapter.
- The Phandalin campaign's mempalace shares the same palace DB. Status shows
  both campaigns' wings. This is expected — each wing is namespaced.
