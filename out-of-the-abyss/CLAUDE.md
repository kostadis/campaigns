# Out of the Abyss — Claude Workspace Guide

D&D 5e campaign workspace, modified OOTA. Managed with the
**CampaignGenerator** toolkit (`~/src/CampaignGenerator/`) and a
three-wing **mempalace** for semantic search.

> Read this first. For deeper detail, the file points at
> `MEMPALACE.md` (full palace usage guide) and `MEMPALACE_HORIZON.md`
> (current horizon + refresh workflows). Don't duplicate their
> content here.

## Key files / where to look

| File / dir | Purpose |
|---|---|
| `MEMPALACE.md` | Full mempalace usage guide — wings, search patterns, refresh, troubleshooting, OOTA-specific operational rules |
| `MEMPALACE_HORIZON.md` | Current horizon marker (last campaign chapter played, drawer baseline, extend/rebuild workflows) |
| `docs/TheUnderdark.md` | Source bible. Split into per-chapter files in `docs/chapters/` via `split_chapters.py`. **Filename has no space** — see gotcha below. |
| `docs/chapters/` | Sequentially-numbered chapter files (narrative wing source) |
| `docs/distill_extractions/` | Pipeline-generated structured extractions (chronicle wing source) |
| `docs/campaign_state.md`, `world_state.md`, `planning.md`, `party.md` | Grounding docs |
| `docs/canon_guardrails.md`, `decision_ladders.md`, `risk_levers.md`, `campaign_master_plan.md`, `campaign_design_frame.md` | High-signal canon set — re-mine first when these change |
| `docs/gauntlgrym/` | Faction-asset packets and scene scripts (active-play set) |
| `docs/npcs/` | NPC dossiers. PC files for Daz / Grygum / Thorin / Zalthir live here but are excluded from mining |
| `voice/`, `examples/`, `summaries/`, `notes/` | Excluded from palace by `.mempalaceignore` |
| `mempalace.yaml`, `docs/chapters/mempalace.yaml`, `docs/distill_extractions/mempalace.yaml` | Per-wing palace configs — **do not delete** |
| `.mempalaceignore` | Mining exclusions. Has a fragile filename rule — see gotcha |
| `.mcp.json` | Project-scoped MCP servers: `campaign`, `5etools` |

## MemPalace setup

Three wings. Live drawer counts and last-mined date in `MEMPALACE_HORIZON.md`.

| Wing | Source dir | What it answers | Trust |
|---|---|---|---|
| `narrative` | `docs/chapters/` | "What exactly happened at the table?" | **Authoritative** — verify here first |
| `chronicle` | `docs/distill_extractions/` | "What was X's state at point in time T?" | Search accelerator — narrow time window, then verify against narrative |
| `abyss` | root | "What's the current state? What's the plan?" | Working reference — verify against narrative when precision matters |

- **Palace location**: `~/.mempalace/palaces/abyss/` (separate DB from Phandalin's palace, despite older docs claiming they share)
- **Mining order**: subdirs **before** root, every time — chronicle → narrative → abyss. Root mining excludes the subdirs via `.mempalaceignore` to prevent double-mining.
- **Embedding device**: CPU (`onnxruntime`). The system has a GPU but the `onnxruntime-gpu` build wants CUDA 12 runtime libs which conflict with torch's bundled CUDA 13. CPU mine completes in minutes; don't swap unless you're prepared to install CUDA 12 alongside.

### Gotchas

- **`.mempalaceignore` filename rule is fragile.** It lists `docs/TheUnderdark.md` (no space). The file was previously `The Underdark.md` (with space) — split + git rename changed it 2026-04-25. If anyone reverts the filename or edits the ignore back to the old form, the bible gets re-mined into the abyss wing on top of the chapter splits and pollutes every search. Sanity check: `mp search "Zuggtmoy wedding" --wing abyss` should return an NPC dossier, **not** `TheUnderdark.md`.
- **Bible file count ≠ campaign chapter count.** Bible has 54 chapter files because the source contains decimal sub-chapters (`# Chapter 18.05`–`18.4`); campaign sessions have only reached chapter 49. The horizon marker tracks both.
- **`split_chapters.py` wipes `docs/chapters/mempalace.yaml`** if you re-split. Restore from git before re-mining: `git show HEAD:out-of-the-abyss/docs/chapters/mempalace.yaml > docs/chapters/mempalace.yaml`.
- **Splitter assigns chapter numbers by encounter order**, not by source heading number. Decimal sub-chapters cleanly become whole-numbered output files that shift everything after them.

## MCP tools

- `campaign` — read-only access to grounding docs; write access only to `notes/`. Use `mcp__campaign__list_notes`, `mcp__campaign__search_document(scope="notes")`, `mcp__campaign__read_document` for note lookup (notes are excluded from the palace on purpose).
- `5etools` — published-module access (`get_section`, `search`, `get_monster`, etc.). Use this for the OOTA module text instead of mining `docs/background/Out of the Abyss.md` (excluded by `.mempalaceignore` for that reason).
- `mempalace` — semantic search across wings (`mempalace_search`, `mempalace_open_drawer`, `mempalace_traverse`, `mempalace_find_tunnels`).

## Conventions

- **Voice files are authoritative** for character speech and personality. Read the voice file before writing dialogue or narrative for a character.
- **Players are the ultimate authority** on their characters' psychology. When a player corrects a characterization, update the voice file.
- **Notes are staging, not canon.** Nothing enters the palace from `notes/`. Promote canon into `docs/` first, then re-mine the affected wing.
- **Published modules stay outside the palace** — use 5etools MCP.
- **Session summaries** use chapter numbering (e.g., "Chapter 49: Out of the Dark and Into the Darkness"). The number here = bible-file chapter, not always equal to session count.

## Common scripts

```bash
# Session prep — single beat
python ~/src/CampaignGenerator/prep.py --beat "..."

# Three-agent pipeline (Lore Oracle → Encounter Architect → Voice Keeper)
python ~/src/CampaignGenerator/prep.py --mode pipeline --beat "..."

# Regenerate grounding docs
python ~/src/CampaignGenerator/campaign_state.py summaries.md --output docs/campaign_state.md
python ~/src/CampaignGenerator/distill.py summaries.md --output docs/world_state.md
python ~/src/CampaignGenerator/party.py --character docs/characters/*.md --summaries summaries.md --output docs/party.md

# Re-split bible (then restore chapters/mempalace.yaml from git, then re-mine)
python ~/src/CampaignGenerator/split_chapters.py docs/TheUnderdark.md --output-dir docs/chapters

# Re-mine (subdirs first, root last)
mp="/home/kroussos/worldanvil_pipeline/venv/bin/mempalace --palace abyss"
$mp mine docs/distill_extractions
$mp mine docs/chapters
$mp mine .
```

Re-mine workflows (forward extension when a chapter is added; full rebuild when an inconsistency is found): see `MEMPALACE_HORIZON.md`.

## Pointers

- Shared architecture across all campaigns: `~/campaigns/CLAUDE.md`
- Full mempalace usage: `MEMPALACE.md`
- Current horizon: `MEMPALACE_HORIZON.md`
- CampaignGenerator script reference: `~/src/CampaignGenerator/CLAUDE.md`
