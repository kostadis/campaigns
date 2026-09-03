# Stage 0 Consistency Report: GM Assist

**Document:** `session_2026_08_21_chapter_10_the_wizard_of_the_old_owl_well.md`  
**Method:** Direct Codex audit against the transcript and confirmed campaign sources. No external model backend was used for this report.  
**Result:** Two Moderate issues were adjudicated by the GM. Four classes of canonical spelling error were corrected mechanically.

## Severity Summary

| Severity | Count | Status |
|---|---:|---|
| Critical | 0 | None |
| Moderate | 2 | Resolved |
| Minor | 1 grouped finding | Corrected mechanically |
| Trivial | 0 | None |

## Findings

### MODERATE-01: Old Owl Well geography conflicts with the post-session GM ruling

The recap describes the party planning a route through Conyberry, traveling east along the Triboar Trail, and reaching Old Owl Well from the eastern hills (`gm-assist`: lines 14, 18, 47, 62-65, 81-85, 128-131). This is faithful to what was played: the transcript contains the same route discussion and eastward travel.

The confirmed strategy document instead records a GM source ruling that Old Owl Well is northwest of Phandalin and explicitly says it now pairs with Thundertree, not Conyberry or Wyvern Tor (`notes/hamun_kost_strategy.md`: lines 3-8, 24-26, 125-126). The player quest log already uses the northwest placement.

**Ruling:** Preserve the table's spoken eastward route as historical fact. The northwest placement remains the geography ruling for future play and is not being applied retroactively to this recap.

### MODERATE-02: Wyvern Tor enemy identity conflicts with confirmed prep

The recap consistently identifies the Wyvern Tor marauders as bugbears and an ogre, including the lone bugbear sentry (`gm-assist`: lines 22-26, 98-108, 137, 177-183). This is faithful to the transcript: Hamun says there are bugbears and an ogre, the party repeatedly chooses that job on those terms, and the session ends after the GM describes a single bugbear sentry.

The confirmed strategy document identifies the marauders as an orc band (`notes/hamun_kost_strategy.md`: line 33). Campaign state likewise records elongated-skull goblins raiding alongside the orcs at Wyvern Tor (`docs/campaign_state.md`: line 86). The player quest log remains neutral and calls them caravan raiders.

**Ruling:** Preserve the bugbears established at the table. The orcs in prep and campaign state are a different group, not a replacement for the bugbear encounter.

### MINOR-01: Canonical proper-noun spellings

The document used `Nothik`, `Sessnak`, `Glastaff`, and `Miners' Exchange`. The correction glossary and entity registry establish `Nothic`, `Ssarnak`, `Glasstaff`, and `Miner's Exchange`.

**Applied mechanically:** All instances in the Stage 0 document were corrected. No narrative facts were changed.

## Sources Consulted

- Session transcript for Chapter 10
- `docs/entity_registry.yaml`
- `docs/party.md`
- `docs/campaign_state.md`
- `docs/world_state.md`
- `notes/hamun_kost_strategy.md`
- `notes/handouts/player_quest_log.md`
- `notes/cragmaw_castle.md`
- `notes/vtt_transcription_corrections.md`
- `notes/vtt_known_additions.md`

## Stage Gate

Stage 0 is complete. Both Moderate findings preserve the table account, so no narrative edits were required. Stage 1 may proceed using the corrected Stage 0 document as its upstream source.
