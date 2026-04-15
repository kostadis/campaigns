#!/usr/bin/env bash
# Launch the Session Doc UI.
# Open http://localhost:5000 in your browser.

cd "$(dirname "$0")"

python ~/CampaignGenerator/session_doc_ui.py session-mar \
    --extract-dir scene_extractions/ \
    --roleplay-extract-dir vtt_roleplay_extractions/ \
    --output-dir . \
    --party partyfile.md \
    --voice-dir voice/ \
    --narrate-tokens 4000
