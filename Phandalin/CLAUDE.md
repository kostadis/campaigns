# Phandalin Campaign — Claude Workspace Guide

This is a D&D 5e campaign workspace managed with the **CampaignGenerator** tool (`/home/kroussos/CampaignGenerator/`).

## Campaign Overview

**Setting:** Phandalin region (Dragon of Icespire Peak / Lost Mine of Phandelver hybrid)
**DM:** Kostadis Roussos
**Urgent threat:** The Carver is marching on Icespire Hold to bind the white dragon Cryovain, then burn Phandalin.
**Party base:** Phandalin (political influence, stake in Mountain's Toe Gold Mine)
**Companion:** Boney, a sentient skeletal horse
**Major past events:** War of the Giants (modified Storm King's Thunder — Hekaton allied with Lord's Alliance), War of the Dragons (modified Tyranny of Dragons)

## Key Files

| File | Purpose |
|------|---------|
| `partyfile.md` | Party overview, character sheets, arc scores |
| `npc_state.md` | Session summaries (chapter format), NPC dossiers |
| `planning.md` | Threat tracker, faction states, active plots, DM planning notes |
| `narrative_session.md` | In-character narrative snippets (character POVs) |
| `config.yaml` | CampaignGenerator workspace config — paths for agents and documents |
| `scene1.md` – `scene9.md` | Individual scene write-ups |
| `tracking.txt` | Lightweight session tracking |
| `voice/` | Per-character voice notes (`vukradin_voice.md`, etc.) |
| `characters/` | Character sheets and mechanical stats |
| `summaries/` | Session transcripts (VTT files), organized by date |
| `docs/world_state.md` | World state document |
| `docs/KP.md` | **KP biography** — Kazneporium Ketternopappux, gnome wizard / planar optimizer. Offstage structural antagonist; tracked via Planar Distortion Score. Aletra is his on-screen agent. Iymrith endgame collision documented here. |
| `docs/CounterForce.md` | **Rimardo and Corrin doctrine** — Savras's manifested counterweight to KP. First playbill clue queued for the Woodland Manse; first public-act payoff queued for the Wayside Inn. Vukradin is the structural receiver. |

**Note on generated docs:** `docs/campaign_state.md`, `docs/world_state.md`, `docs/party.md`, and `docs/planning.md` are CampaignGenerator outputs — do NOT hand-edit. Edits will be clobbered on next regeneration. For hand-authored campaign material, create new dossier files at `docs/` top level (matches `Aletra.md`, `Brundar.md`, `Kraken society.md` convention) and reference them from this CLAUDE.md so they surface in every session.

## Players and Characters

| Player | Character | Class/Race | Key Trait |
|--------|-----------|-----------|-----------|
| David Mendenhall (Dave) | Vukradin | Bard 5 / Aasimar | Naive optimist, sees no tension in his goals, Silver Tongue worldview |
| Wade Brown | Soma | Druid 5 / Tortle | Naturalist, skeptical of mentor Adabra |
| Gary Young | Valphine Sotorra / Brewbarry | Cleric 5 / Drow, Barbarian 5 / Goliath | Valphine: secret Lathander devotee; Brewbarry: combat leader, Dragon Slayer Sword |

## Voice Files

Each character has a voice file in `voice/` and a stat sheet in `characters/`. Voice files are the authoritative reference for how a character speaks and thinks. When writing narrative or dialogue, always read the voice file first.

**Important:** The players are the ultimate authority on their characters' psychology. When a player corrects a characterization, update the voice file. Dave in particular provides sharp meta-commentary about Vukradin that often differs from surface-level reads.

## CampaignGenerator Agents

Defined in `config.yaml`, prompts live in `/home/kroussos/CampaignGenerator/config/agents/`:

- **lore_oracle** — world-building and lore questions
- **encounter_architect** — combat and encounter design
- **voice_keeper** — NPC voice and dialogue consistency

## Scripts

- `narrate_scene.sh` — narrate a scene (likely calls CampaignGenerator pipeline)
- `ui.sh` — interactive UI, configured by `ui_config.yaml`

## Active Threats (from `planning.md`)

| Threat | Tracker | Notes |
|--------|---------|-------|
| Kraken Society | Echoes Score | Party carries illithid-tech beacon |
| Grundar Quartzvein | Brundar's Echo (0) | Secret enemy of House Sotorra / Valphine |
| Adabra Gwynn | Fury of the Wild (0) | On path toward Tiamat alliance |
| Aletra Sotorra | Planar Distortion (0) | Valphine's sister, agent of cosmic entity KP |

## Conventions

- Session summaries use chapter titles (e.g. "Chapter 34 Where Cows Come Home and Deals Are Struck")
- Arc scores track character development — update in `partyfile.md` after significant choices
- Session transcripts are VTT files in `summaries/YYYYMMDD/`
- Logs written to `logs/`
