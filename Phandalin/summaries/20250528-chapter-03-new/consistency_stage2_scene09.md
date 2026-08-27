# Consistency Report — "Amateur Archaeologists" (Ch. 3 scene extract)

## Issue 1 — Did the party take the green gem, or leave it? (contradiction)

- **Location**: Verbatim moments (Vukradin: "We took a worthless piece of green glass"; coda: "stealing the Gem of Greed") and Scene summary ("the party's success in clearing the ruins… discovery of the intact gem")
- **Issue**: The scene transcript twice implies the gem was **taken** — Vukradin's report opens "We took a worthless piece of green glass," and his coda joke has the dwarves punished "for stealing the Gem of Greed." But the gm-assist Items section states flatly of the Glowing Green Gem: "**It was left in place.**" These cannot both be true, and future sessions need to know whether the gem is in party/dwarf inventory or still in the statue's hands.
- **Evidence**: gm-assist.md → Items → Glowing Green Gem: "It was left in place." vs. scene verbatim "We took a worthless piece of green glass" and "The demon attacks the gnomes for stealing the Gem of Greed."
- **Suggested fix**: GM ruling required. Either annotate the verbatim ("'took' is loose table-speak for 'found/examined'; the gem was left in place per Items") or correct the Items entry. Do not let either version propagate unadjudicated.

## Issue 2 — "Recover our reward for delivering the message" vs. campaign_state (timeline contradiction)

- **Location**: Verbatim moments, Soma's coda ("So we head back to town and recover our reward for delivering the message") and Vukradin's closing line ("Message delivered.")
- **Issue**: Per the campaign_state archive, the message-delivery reward was **already collected before Chapter 2 ended**: "Return to Phandalin — Dwarven Quest Reward Collected: Harbin Wester paid the promised 50 gp." Yet at the end of this Chapter 3 session, the party frames the trip to town as going to collect that reward. Either the ch02 archive folds in events that were actually played *after* this session, or the players misspoke on tape and the scene doc presents it unannotated as the party's live objective.
- **Evidence**: campaign_state.md → Completed Encounters → "Return to Phandalin — Dwarven Quest Reward Collected"; scene coda; gm-assist "Ambush on the Road" ("heading back toward town to collect their final reward").
- **Suggested fix**: Flag for GM. Note that the same archive already contained one confirmed sequencing error on exactly this quest (the sending stones were marked "in party's possession," corrected 2026-08-17 to "withheld until the temple is cleared"). The 50 gp collection may be a second instance of the same drift — the transcript is authoritative and supports *not yet collected* as of end of Ch. 3.

## Issue 3 — Chapter 3's location contradicts the Chapter 2 archive's ending state (timeline/ordering)

- **Location**: Whole scene (and the gm-assist Chapter 3 recap it's cut from)
- **Issue**: The ch02 archive ends with the party "mid-combat with a hungry ogre" in a mountain valley **en route to Gnomengarde**, and lists the deeper temple as "unexplored… the party has not returned to." Chapter 3 (session 2025-05-28) takes place entirely inside that temple, with no narration of the ogre's resolution or the Gnomengarde trip. Either the hand-authored Chapter 2 prose runs ahead of the actual session order (consistent with Issues 1–2), or a resolution scene is missing between the chapters.
- **Evidence**: campaign_state.md → Party Current Situation ("mid-combat with a hungry ogre… en route to Gnomengarde") and Active Quests ("Dwarven Temple — deeper interior unexplored"); gm-assist.md header "New Chapter 3, Date: 2025-05-28" opening at the ruins' crossroads.
- **Suggested fix**: GM should confirm the true session order before the ch02 archive is treated as settled. The archive is explicitly a DRAFT; recommend logging this as a chapter-boundary defect alongside the sending-stones correction rather than editing the recap.

## Issue 4 — The "gnomes" editorial note may misread a canon callback

- **Location**: Verbatim moments, editorial annotation on Vukradin's coda ("the transcript says 'gnomes' though the employers are dwarves")
- **Issue**: The annotation treats "gnomes" as Vukradin misidentifying his dwarf employers. But the known-additions glossary records the *same phrasing* from this same session as established temple-carving lore: the Gem of Greed is "depicted in the carvings of Abbathor's ruined temple; 'a demon attacks the gnomes for stealing the gem of greed.'" If the carvings depict gnomes, Vukradin's line is a deliberate callback to the carving, not a species slip — and the annotation is the error.
- **Evidence**: vtt_known_additions.md → 2026-08-02 entry "Gem of Greed."
- **Suggested fix**: Confirm against the full session transcript whether a carving-description beat precedes this line. If so, rewrite the annotation to "callback to the temple carvings, which depict gnomes stealing the gem" — do not "correct" gnomes→dwarves in any pass.

## Issue 5 — Pre-return banter folded into the report scene (minor ordering)

- **Location**: Scene summary, first bullet ("The party informs Dazlyn and Norbus… and notes that at least 'a dragon didn't find us.'")
- **Issue**: The summary reads as if "a dragon didn't find us" was said *to the dwarves* during the report. The verbatim shows the exchange (GM: "But we didn't find a dragon" / Soma: "You mean a dragon didn't find us") happened among the party **before** heading back to Dazlyn and Norbus.
- **Evidence**: Verbatim sequence — the dragon exchange precedes "So you head back to Dazlyn and Norbus Right?"
- **Suggested fix**: Split the bullet: banter first, then the report to the dwarves.

## Issue 6 — Sending-stones handover appears twice in the transcript (minor ambiguity)

- **Location**: Verbatim moments — GM: "So they give you the sending stones, and they explain…" (mid-scene) and "hands you the Sending S- uh, gives you the Sending Stones" (end)
- **Issue**: The transcript records the handover twice; the scene's final bullet asserts a single end-of-scene delivery. Harmless, but a future pass could misread this as two pairs of stones or a retcon.
- **Evidence**: Both GM cues quoted above; campaign_state's GM-confirmed ruling (2026-08-17) says the stones were handed over "only at the end of that session," which the end-of-scene framing matches.
- **Suggested fix**: Add a one-line annotation that the earlier cue is the GM narrating ahead of himself and the end-of-scene handover is canonical, per the 2026-08-17 ruling.

## Checked and clean

- NPC names/titles: Dazlyn Grayshard and Norbus Ironrune (shield dwarf prospectors), correct throughout; no garbled forms from the VTT glossary present.
- The sending stones as reward *for clearing the temple* (not the original warning job) matches the GM-confirmed 2026-08-17 ruling and entity_registry framing.
- Insight rolls (9, then 17) and the GM's rulings on them match the verbatim exactly.
- "We cleared out the ochre jellies" matches the Chapter 3 combat record.
- The "amateur archaeologists / started the hobby several days ago" beat matches both the verbatim and the gm-assist summary.
- Quote attributions across split cues (Vukradin/GM/Valphine/Soma) are annotated honestly and consistently with the crosstalk notes.