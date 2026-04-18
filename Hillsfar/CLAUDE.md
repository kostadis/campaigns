# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Hillsfar Campaign Workspace

This is a campaign workspace for **DDEX34: It's All in the Blood**, using the [CampaignGenerator](~/CampaignGenerator) toolkit. All scripts live in `~/CampaignGenerator/`; run them from this directory so `config.yaml` is auto-detected.

## Source material

- `DDEX34_ItsAllintheBlood.pdf` — original adventure PDF
- `adventure-ddex34it.json` — parsed adventure module (use as reference for encounters, NPCs, locations)

## Common commands

```bash
# Session prep — single beat
python ~/CampaignGenerator/prep.py --beat "The party arrives at the docks of Hillsfar"

# Session prep — three-agent pipeline (Lore Oracle → Encounter Architect → Voice Keeper)
python ~/CampaignGenerator/prep.py --mode pipeline --beat "..."

# Session arc — full numbered outline
python ~/CampaignGenerator/prep.py --session "1. ... 2. ... 3. ..."
```

## Grounding document generation

Run these whenever the grounding docs fall out of date with the session summaries:

```bash
# Regenerate campaign_state.md (completed content, NPC states, open threads)
python ~/CampaignGenerator/campaign_state.py summaries.md --output docs/campaign_state.md

# Regenerate world_state.md (living canon)
python ~/CampaignGenerator/distill.py summaries.md --output docs/world_state.md

# Regenerate party.md
python ~/CampaignGenerator/party.py \
    --character docs/characters/*.md \
    --summaries summaries.md --output docs/party.md
```

## Grounding documents (`docs/`)

Loaded by `config.yaml` in this order (campaign_state first — it is the primary grounding doc):

| File | Purpose |
|---|---|
| `campaign_state.md` | Completed encounters/quests, resolved threads, NPC current states, active quests |
| `world_state.md` | Living canon — factions, locations, relationships |
| `mechanics.md` | Arc score systems and tracking |
| `planning.md` | NPC dossiers and threat arcs |
| `party.md` | Character roster, backstories, arc scores, relationships |

Edit these files directly to correct errors or add information not captured by the generators.

## PDFs in `docs/`

The `docs/kosadis_*.pdf` / `docs/kostadis1_*.pdf` files are D&D Beyond character sheets. Convert to markdown with:

```bash
python ~/CampaignGenerator/dnd_sheet.py docs/kosadis_80444987.pdf --output docs/characters/soma.md
```

## Converting the adventure module to 5etools

The PDF converter toolkit lives at `~/5etools-dev/5etools-src/pdf-translators/`. Use it to convert `DDEX34_ItsAllintheBlood.pdf` into 5etools homebrew JSON for use in VTT.

```bash
cd ~/5etools-dev/5etools-src/pdf-translators

# Standard converter (try this first — DDEX34 is a digitally-typeset PDF)
python3 pdf_to_5etools.py ~/campaigns/Hillsfar/DDEX34_ItsAllintheBlood.pdf

# If text extraction is poor, use OCR fallback
python3 pdf_to_5etools_ocr.py ~/campaigns/Hillsfar/DDEX34_ItsAllintheBlood.pdf

# Estimate token cost without making API calls
python3 pdf_to_5etools.py ~/campaigns/Hillsfar/DDEX34_ItsAllintheBlood.pdf --dry-run

# Save chunk I/O for debugging
python3 pdf_to_5etools.py ~/campaigns/Hillsfar/DDEX34_ItsAllintheBlood.pdf --debug-dir /tmp/ddex34-debug
```

Or use the Flask web UI:
```bash
cd ~/5etools-dev/5etools-src/pdf-translators
python3 app.py   # http://localhost:5100
```

Output is a `.json` file loadable via the 5etools **Manage Homebrew** UI. See `~/5etools-dev/5etools-src/pdf-translators/CLAUDE.md` for full options.

## CampaignGenerator reference

See `~/CampaignGenerator/CLAUDE.md` for full documentation: all script flags, the five-pass `session_doc.py` pipeline, the Flask session doc editor, the Streamlit app, and the shared `campaignlib.py` API.
