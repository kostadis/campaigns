# MemPalace — Temple of Elemental Evil Campaign Usage Guide

Semantic search over the ToEE campaign's content, organized into **five wings**
for different retrieval needs. Queryable via the CLI or via the `mempalace` MCP
tools inside a Claude Code session scoped to this project.

Palace: `toee` → `/home/kroussos/.mempalace/palaces/toee` (2,426 drawers as of setup).

---

## ⚠️ Deliberate divergence from the repo rule

`campaigns/CLAUDE.md` states: *"Notes are staging, not canon. Nothing enters the
mempalace directly from notes/."* **This palace intentionally diverges** — ToEE's
`notes/` holds substantial, durable GM prep (strategy dossiers, faction networks,
handouts, statblocks, area references) that is genuinely worth searching.

The divergence is contained, not a free-for-all:

- `notes/` durable reference → the **`notes`** wing (lowest *canon* trust tier).
- Speculative session-prep (`notes/sessions/`) → the **`prep`** wing, **isolated so
  it can be excluded from search** (mempalace filters are include-only, so isolation
  by wing is the only reliable way to "search around" speculative content).
- Tooling in `notes/` (`*.py`, vtt glossary state, `proper_nouns_*`) is excluded.

The three canon wings (`narrative`, `chronicle`, `toee`) stay pure. If you want
canon-only results, scope to those wings and the `prep`/`notes` wings never appear.

---

## Five-Wing Architecture

| Wing | Purpose | Source | Trust |
|------|---------|--------|-------|
| `narrative` | What actually happened at the table | `docs/chapters/` (chapter splits of the bible) | **Authoritative** |
| `chronicle` | Structured world-state snapshots over time | `docs/distill_extractions/` | Search accelerator |
| `toee` | Current-state reference for building forward | grounding docs + `docs/npcs/` + char sheets | Working reference |
| `notes` | Durable GM prep | `notes/` strategy, networks, handouts, statblocks, refs | GM prep |
| `prep` | Speculative session-prep | `notes/sessions/` | **Speculative — excludable** |

**Tunnels:** `chronicle` and `toee` share `npcs`/`world` room semantics; graph
traversal can cross between a timeline NPC snapshot and the current dossier.

### Trust levels (mirrors `campaigns/CLAUDE.md`)

| Wing | Trust | Rule |
|------|-------|------|
| `narrative` | **Authoritative** | The bible. Verify here before building on a claimed fact. |
| `chronicle` | **Search accelerator** | LLM-generated extractions. Find the time window, then verify against `narrative`. |
| `toee` | **Working reference** | Current-state docs. Verify against `narrative` when precision matters. |
| `notes` | **GM prep** | Designed, not canon. Useful for building forward; not a record of play. |
| `prep` | **Speculative** | "What *might* happen." Never confuse with what *did*. Excluded from canon searches. |

---

## Command-Line Usage

```bash
alias mp='/home/kroussos/worldanvil_pipeline/venv/bin/mempalace --palace toee'
```

```bash
mp status                                   # health check, drawer counts per wing/room
mp search "Belsornig water temple"          # cross-wing (everything, INCLUDING prep)
mp search "Kelno's deal" --wing narrative   # what actually happened
mp search "Earth Temple state" --wing chronicle   # timeline snapshot
mp search "Calmer cover stress" --wing toee       # current reference
mp search "Lucius interrogation" --wing notes     # GM prep / strategy
mp search "the sleeping prince" --wing prep        # speculative prep (opt-in)
```

### Searching so you ignore speculative content

mempalace filters are **include-only** (no "exclude" flag). To keep speculative
`prep` content out of results, **scope to a specific canon wing** — any
`--wing narrative|chronicle|toee|notes` search excludes `prep` automatically. The
only ways `prep` appears are an explicit `--wing prep` or an unfiltered cross-wing
search.

---

## Wing / Room Taxonomy (drawer counts at setup)

### `narrative` — 538 drawers (the bible, Ch00–25)
| Room | Drawers | Contents |
|------|---------|----------|
| `chapters` | 536 | Per-chapter prose from `toee-summary.md` |
| `general` | 2 | Preamble |

> ⚠️ **The bible stops at Chapter 25.** Chapters 26–28 (Air Temple, the
> dungeon-boss promotion, the Fire Temple) are NOT yet in `narrative` — they exist
> only as `summaries/2026052*/gm-assist.md` pending bible regeneration. Re-split
> and re-mine `narrative` once the bible is brought current.

### `chronicle` — 709 drawers (timeline extractions)
| Room | Drawers | Contents |
|------|---------|----------|
| `npcs` | 706 | NPC/world snapshots (file-level routing lumps most here — content is still searchable) |
| `world` | 3 | World events |

### `toee` — 699 drawers (current reference)
| Room | Drawers | Contents |
|------|---------|----------|
| `npcs` | 423 | `docs/npcs/` dossiers |
| `party` | 211 | Char sheets (Calmer, Sequioa, Zephyr, Zinnia), `party.md` |
| `world` | 64 | `world_state.md`, `campaign_state.md` |
| `general` | 1 | Misc grounding |

### `notes` — 386 drawers (durable GM prep)
| Room | Drawers | Contents |
|------|---------|----------|
| `references` | 111 | Area refs (212/213), image prompts, scarab note |
| `strategy` | 97 | `hedrack_/falrinth_/lucius_strategy.md` |
| `networks` | 78 | `nulb_network/allies`, `hommlet_threats` |
| `handouts` | 76 | `notes/handouts/` props |
| `statblocks` | 24 | `notes/statblocks/` |

### `prep` — 94 drawers (speculative)
| Room | Drawers | Contents |
|------|---------|----------|
| `prep` | 57 | `the-sleeping-prince.md` |
| `general` | 37 | `war-in-the-temple.md` |

---

## What's Excluded (and why)

Controlled by `.mempalaceignore` at the campaign root and inside `notes/`,
`notes/sessions/`:

- `summaries/` — raw VTT + per-session gm-assist (the curated record is `narrative`)
- `docs/background/` — published-module JSON; use the **5etools MCP** instead
- `docs/toee-summary.md` — the bible itself (replaced by chapter splits)
- `docs/*_extractions/` (state/party/planning), `planning_extractions/` — pipeline intermediates
- `logs/`, `temple/`, `archive/`, `examples/`, `voice/`, `.claude/`
- `notes/` tooling: `*.py`, `.vtt_spell_pass_state.json`, `proper_nouns_*`, vtt glossaries
- Binaries: `*.pdf`, `*.tar.gz`; tooling: `config.yaml`, `ui_config.yaml`, `*.sh`

---

## Refresh Workflow

Re-mine the affected wing after editing its source docs (subdirs before root):

```bash
mp mine docs/chapters --wing narrative           # after bible re-split
mp mine docs/distill_extractions --wing chronicle
mp mine notes/sessions --wing prep
mp mine notes --wing notes
mp mine . --wing toee                            # root LAST (ignore excludes the subdir wings)
```

**When the bible is regenerated to include Ch26+:** re-run the splitter
(`/tmp/split_toee_bible.py` or equivalent), then re-mine `narrative`. Consider
clearing first for a clean rebuild: `rm -rf /home/kroussos/.mempalace/palaces/toee`
then re-mine all five wings.

**Mining respects `.mempalaceignore`.** Embeddings run on the local endpoint in
`~/.mempalace/config.json` (`http://192.168.1.147:8000`, the Spark).

---

## MCP Tools (in-session)

Registered in `toee/.mcp.json` as `mempalace`, pinned to `--palace toee`.
Primary tools: `mempalace_search` (wing/room filters), `mempalace_search_hierarchical`,
`mempalace_status`, `mempalace_list_wings`/`list_rooms`, `mempalace_add_drawer`
(manual filing of new canon). **A session reload is required** for the new MCP
server to appear.

---

## Tuning

Room routing lives in each wing's `mempalace.yaml`:
`mempalace.yaml` (root, `toee`), `docs/chapters/`, `docs/distill_extractions/`,
`notes/`, `notes/sessions/`. Edit keywords there and re-mine to re-route.

---

## Troubleshooting

- **MCP tools don't appear** — reload the session; the server is project-scoped in `.mcp.json`.
- **`unknown palace alias: 'toee'`** — the alias must exist in `~/.mempalace/config.json` under `palaces`.
- **Stale content after doc edits** — re-mine the affected wing.
- **Segfault on search** — `mp repair`.
- **Speculative content showing in results** — you ran an unfiltered or `--wing prep` search; scope to a canon wing.

## Known quirks

- `chronicle` routes almost everything to `npcs` (file-level routing keys on the
  first topic heading). Content is fully searchable; the room filter just isn't
  discriminating within that wing.
- `narrative` is **Ch00–25 only** until the bible is regenerated (see above).
