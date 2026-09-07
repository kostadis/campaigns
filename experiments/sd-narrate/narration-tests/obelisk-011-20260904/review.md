# Obelisk scenes 1 and 3 — accepted v1 test

Both drafts were rendered with **gpt-6-astra, medium reasoning**, through `sd_narrate`'s Codex CLI backend. The accepted v1 writing brief is byte-identical to the Phandalin experiment. Zenvon Forepot narrates both scenes; the full voice files for Veyra, Pip, and Sister Maela were also supplied as supporting-character references. Veyra's and Pip's files are the versions explicitly confirmed by the GM.

These are unedited test outputs. Neither the production prompt nor campaign sources, voice files, or configuration were changed. No production narration plan existed; `test_plan.md` is experiment-only scaffolding. The earlier `v1_scene_*` directories contain preparation artifacts only, not comparison generations.

[Read both drafts beside their sources](obelisk_test_reader.html)

## Overall read

The prompt transfers well on these two scenes: description carries the physical situation and decisions, while retained speech still sounds like the speakers. This is a qualitative judgment, not a controlled comparison against an old-prompt Obelisk run. The biggest fidelity concern is the treatment of the pike/bike misunderstanding in scene 1.

| Scene | Narration words, approximately | Quoted share | Read |
|---|---:|---:|---|
| 1 — Arrival at Wyvern Tor | 977 | 23% | Strong spatial and tactical continuity; one weakened table-voice beat. |
| 3 — Scouting the Cave | 645 | 45% | Stronger overall: a substantive conversation supported by observation and reasoning. |

These measurements describe the outputs; neither proportion is a target. The quote check found no consecutive duplicate quoted spans. That check is not a full semantic repetition detector or voice critic.

## Scene 1

[Raw draft](v1_voices_scene_01_trial_01/session_doc_scene_01_arrival_at_wyvern_tor.md) · [Source](../scene_extractions_smoothed/01_arrival_at_wyvern_tor.md)

The meaningful physical and tactical beats survive: ridge, smoke, ravine and distances; unseen scouting; the blind eye, pike, and boredom; the unreadable cave interior; the failed group approach; the sentry investigating south; the northern Mage Hand distraction; the risk of unknown reinforcements; and Pip's distance from the guard. Pip's approach remains a proposed move rather than an invented completed attack. The scene stops with the unresolved sentry and “Tricky here.”

The strongest player-voice preservation is “I feel using the mage hand is more effort. For the same output.” Pip's “You haven't led us wrong yet, Zenvon” also survives. Zenvon's awkwardly precise questions and reconsiderations remain recognizable without reproducing every acknowledgment.

Two reservations:

- **The pike/bike beat is not fully preserved as an interaction.** “Salvaged bike?” becomes an italic internal thought, followed by narrated clarification. The source has a spoken misunderstanding and GM correction. The words survive, but the conversational setup and response do not; in the draft there is no audible “pike” to mishear. This matters because the campaign policy explicitly retains this table-texture beat. It is a useful coverage-review example: matching a phrase does not prove the interaction survived.
- The narrative briefly returns to earlier advice through “he has told me” and “I have weighed his warning aloud.” The source itself frames some advice retrospectively, so this is not a clear invented event, but the shifts make the plan's development harder to follow. Some remnants such as “What do you… guys want to do?” are also still transcript-shaped.

## Scene 3

[Raw draft](v1_voices_scene_03_trial_01/session_doc_scene_03_scouting_the_cave.md) · [Source](../scene_extractions_smoothed/03_scouting_the_cave.md)

The cookfire illumination, four bugbears, ogre, and orc are established clearly. Zenvon and Maela fail to find further insight before Pip notices the authority mismatch. His military reasoning remains his contribution, rather than becoming Zenvon's discovery.

The draft retains Zenvon's praise, Pip's careful disclaimer about his experience, the possibility of breaking morale by killing the leader, the warning about the previous retreat from four bugbears, Zenvon's question about alerting the others, and Maela's closing line. The potential morale effect remains uncertain. No attack occurs and the invisibility potion is not consumed.

One small attribution uncertainty remains: the final source direction says Maela looks at “him”; the draft resolves this to Pip. The immediate preceding speaker is Zenvon. The source does not conclusively settle that referent, so the added specificity deserves review rather than being treated as verified fact.

## What this says about the supporting voices

**Pip gets a meaningful test.** His practical military judgment, caution, and deference to Zenvon remain distinct. His reference examples were not imported as new session dialogue.

**Veyra does not get a meaningful speaking-voice test here.** Her notes were included in both prompts, but neither selected extraction records dialogue for her. The drafts appropriately do not manufacture any. Testing her voice requires a scene where she actually speaks, or an explicitly requested Veyra-POV variant.

## Verification

`run.json` and `render.log` in each trial record the model and reasoning setting. All hashed inputs remained unchanged. `system_prompt.md` and `user_prompt.md` preserve what was submitted; `supporting_character_references.md` records the added voice context.

`quote_review.json` is a lexical diagnostic only. Manual inspection of its seven flags found source-grounded joins: six combine adjacent source quote blocks, and one joins two Zenvon spans across an omitted GM clarification. No unsupported quoted wording was found in that inspection. This does not establish perfect attribution or interaction fidelity; the pike/bike issue above demonstrates that limitation.

The accepted writing brief remains unchanged. These drafts have not been silently repaired or promoted.
