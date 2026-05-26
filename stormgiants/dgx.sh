/home/kroussos/worldanvil_pipeline/venv/bin/python \
    /home/kroussos/src/CampaignGenerator-unified-pipeline/session_doc.py \
    /home/kroussos/campaigns/stormgiants/summaries/20250312/session-summary.md \
    --scene-extractions /home/kroussos/campaigns/stormgiants/summaries/20250312/scene_extractions_new \
    --per-scene-output  /tmp/test-gemma4 \
    --scene 3 \
    --party /home/kroussos/campaigns/stormgiants/docs/party.md \
    --voice-dir /home/kroussos/campaigns/stormgiants/voice \
    --characters "Thistle, Orsik, Vardis, Unla Key" \
    --narrate-tokens 15000 \
    --prose-mode \
    --reflections \
    --narration-genre "High-fantasy epic adventure — First-person comic-noir fantasy memoir — observational, dry, irony-forward, alive to
  absurdity. NOT epic-fantasy adventure prose; NOT literary-introspective register.  NEVER use \"the shape of X\" / \"the quality of X\" /
  \"X had a [shape|quality]\" / \"that particular quality\" to gesture at a pattern — name the thing concretely or cut the sentence." \
    --context /home/kroussos/campaigns/stormgiants/docs/campaign_state.md \
    --context /home/kroussos/campaigns/stormgiants/docs/world_state.md \
    --context /home/kroussos/campaigns/stormgiants/docs/party.md \
    --enhanced-sections /home/kroussos/campaigns/stormgiants/summaries/20250312/narration/enhanced_sections.md \
    --plan-file        /home/kroussos/campaigns/stormgiants/summaries/20250312/narration/plan.md \
    --dgx-endpoint http://192.168.1.147:8001/v1
