# MemPalace — Obelisk Usage Guide

Semantic search over the campaign's content, organized into a single reference wing.

**Palace DB:** `~/.mempalace/palaces/obelisk/` (always pass `--palace obelisk`)

---

## Wing Architecture

| Wing | Purpose | Source | Drawers | Question it answers |
|------|---------|--------|---------|--------------------|
| `obelisk` | Campaign reference | grounding docs, character files, tracking | ~117 | "What's true now? Who are these people?" |

Single-wing setup — the campaign is early (4 sessions) with no extraction pipeline yet. Add a `narrative` wing when session chapters accumulate; add a `chronicle` wing when the distill pipeline is running.

### Trust Levels
| Wing | Trust | Rule |
|------|-------|------|
| `obelisk` | **Working reference** | Verify against VTT summaries when precision matters |

---

## Wing / Room Taxonomy

| Room | Files | Drawers | Contents |
|------|-------|---------|----------|
| `world` | 6 | ~100 | world_state.md, name_glossary.md, character files (veyra, maela, pip), party.md |
| `mechanics` | 2 | ~14 | mechanics.md, sidekick_progressions.md |
| `arcs` | 2 | ~2 | campaign_state.md, oblesik_tracking.md |
| `npcs` | 1 | ~1 | (sparse — add NPC dossiers to docs/ as campaign grows) |

**Note:** `name_glossary.md` (64 drawers) dominates the `world` room — expected given its size. Character files (veyra, maela, pip) also route to `world` rather than `npcs`; this is a keyword match artifact. Search by name works regardless of room.

---

## What's Excluded (and why)

| Path | Reason | Access via |
|------|--------|-----------|
| `docs/background/obelisk.md` | Published module (~606KB) | 5etools MCP `get_section` / `search` |
| `summaries/` | Raw session data, not yet processed | Direct file read |
| `voice/`, `examples/` | Pipeline rendering inputs only | Direct file read |
| `logs/` | Operational | Direct file read |
| `notes/` | Staging area — not canon | campaign MCP `search_document(scope="notes")` |
| `docs/party/` | Empty | — |
| `config.yaml`, `*.yaml` config files | Tooling | — |
| `.mcp.json`, `entities.json` | Tooling | — |

---

## Search Patterns — When to Use Which Wing

Since there's only one wing, always omit `--wing` (or pass `--wing obelisk`):

```bash
MP="mempalace --palace obelisk"

# NPC or character lookup
$MP search "Veyra"

# World / faction context
$MP search "Redbrand hideout"

# Quest / tracking
$MP search "obelisk quest"

# Rules reference
$MP search "sidekick level up"
```

---

## The Canon Rule

Notes are staging, not canon. To promote:
1. Write/edit the relevant grounding doc or add a dossier to `docs/`
2. Re-mine: `mempalace --palace obelisk mine /home/kroussos/campaigns/obelisk`

---

## Refresh Workflow

```bash
MP=/home/kroussos/worldanvil_pipeline/venv/bin/mempalace

# After updating any grounding doc or adding a new NPC dossier to docs/
$MP --palace obelisk mine /home/kroussos/campaigns/obelisk

# Full rebuild
rm -rf ~/.mempalace/palaces/obelisk/
$MP --palace obelisk mine /home/kroussos/campaigns/obelisk
```

No subdirectory wings yet, so order doesn't matter.

---

## MCP Tools

Available in Claude Code once `.mcp.json` is loaded:

- `mempalace_search` — semantic search across all rooms
- `mempalace_get_drawer` — retrieve a specific drawer by ID
- `mempalace_find_tunnels` — find shared rooms across wings (future use when multi-wing)
- `mempalace_status` — drawer counts by wing/room

---

## Known Quirks

- **`init` overwrites `mempalace.yaml`** — after any `init` run, restore from git: `git checkout mempalace.yaml`
- **`name_glossary.md` dominates `world` room** (64 of ~100 drawers) — expected. Narrow searches by including specific names.
- **Character files route to `world`** (veyra, maela, pip) — keyword match artifact. The files are searchable; room filtering is just cosmetic here.
- **`arcs` room is sparse** (2 drawers) because grounding docs are stubs. Will grow as `campaign_state.md` and `planning.md` fill in.

---

## Expanding to Multi-Wing (future)

When the campaign has 10+ sessions:

1. **Narrative wing:** run `split_chapters.py` on the session summaries bible → `docs/chapters/`, add `docs/chapters/mempalace.yaml`
2. **Chronicle wing:** run the distill pipeline → `docs/distill_extractions/`, add `docs/distill_extractions/mempalace.yaml`
3. Update root `.mempalaceignore` to exclude `docs/chapters/` and `docs/distill_extractions/` from root mining
4. Mine subdirs before root
