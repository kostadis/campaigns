# Consistency Report — "Ambush on the Road" (Chapter 3 scene recap)

## Major Issues

### 1. The 50 gp "final reward" is recorded as already collected
- **Location**: Scene summary (bullet 1) and Verbatim moments ("[Departure — Message Delivered]")
- **Issue**: The recap states the party is heading to town "to collect their final reward — the fifty gold pieces owed for delivering the message." Per campaign_state, that reward was already paid before this session.
- **Evidence**: `campaign_state` (Ch. 2 archive), Completed Encounters: "**Return to Phandalin — Dwarven Quest Reward Collected:** Harbin Wester paid the promised 50 gp." The party's listed resources include "50 gp — reward from the Dwarven Excavation quest." Meanwhile Soma's verbatim table line ("recover our reward for delivering the message") *does* support the recap's framing — meaning either the recap/transcript is right and the Ch. 2 archive mis-ordered the reward collection, or the recap is elevating a player misremembering into narrated fact.
- **Suggested fix**: This needs a GM ruling, not a silent edit — the Ch. 2 archive is explicitly a DRAFT and has already had one ordering error corrected (the sending-stones "in party's possession" line, GM-confirmed 2026-08-17). Either (a) correct the recap to "heading back to town" without the 50-gp claim, or (b) correct the Ch. 2 archive to move the reward collection *after* this session. Also drop "final" — the Gnomengarde (50 gp) and Umbrage Hill (25 gp) rewards remain outstanding either way.

### 2. Timeline conflict: party position contradicts end-of-Chapter-2 state
- **Location**: Scene summary (whole scene premise: "The party departs the ruins, heading back toward town")
- **Issue**: Per campaign_state, Chapter 2 ends with the party in a mountain valley en route to **Gnomengarde**, mid-combat with Ogre #2 ("fate unresolved"). This Chapter 3 session instead opens inside the dwarven ruins and ends on the road *to town* — with no ogre resolution and no Gnomengarde trip anywhere in the session. The two documents cannot both be sequentially correct.
- **Evidence**: `campaign_state` → "Party Current Situation: A narrow, steep-walled mountain valley en route to Gnomengarde, mid-combat with a hungry ogre. **Chapter 2 ends here.**" vs. gm-assist Ch. 3 (dated 2025-05-28): the entire session takes place in the excavation ruins and on the road back to town. Note the transcript evidence in Issue 1 points the same direction: if the reward is still uncollected at the end of Ch. 3, then the Ch. 2 archive's "Return to Phandalin / Lionshield sale / Ogre #1 / Gnomengarde departure / Ogre #2" block likely belongs to *later* chapters and was back-read into the Ch. 2 archive in error.
- **Suggested fix**: Flag the Ch. 2 archive block (everything from "Return to Phandalin" onward) for GM review before the incremental-archive project builds a Chapter 3 rung on top of it. Do not "fix" the recap's location — the session transcript is the authoritative layer.

### 3. "We had servants" — speaker attribution is uncertain but stated as fact
- **Location**: Scene summary (bullet 4); Verbatim moments
- **Issue**: The summary asserts the line as Valphine's ("her fluency explained with chilling drow economy"). The transcript labels the line under **Soma** — and also labels the *reaction* ("Oh, you just made me feel bad") under Soma, which is internally implausible (one speaker both delivering the line and reacting to it). The recap's verbatim annotation acknowledges the mislabel, but the summary presents the Valphine attribution as settled.
- **Evidence**: Recap's own note: "*transcript labels this line under Soma though it answers for Valphine*." In-fiction the line fits Valphine (drow, fled Menzoberranzan per world_state), but attribution is a precision decision. Also worth checking who was actually at the table: Gary covers Brewbarry when Stéphane is absent (Phandalin CLAUDE.md), and the GM frequently voices interjections — the "Valphine does. She does? Makes sense." GM line in the same exchange is already flagged as carrying a second speaker.
- **Suggested fix**: Confirm against the tape (or GM memory) before any downstream doc quotes "I mean, we had servants" as Valphine's dialogue. Until confirmed, keep the hedged annotation in the summary too, not just the verbatim section.

## Minor Issues

### 4. Language claims not verified against character sheets
- **Location**: Scene summary (bullets 4–5); Verbatim moments
- **Issue**: Two ability claims enter canon here: Valphine speaks Orc (GM-ruled live at the table — "Yeah, that makes sense. She can speak Orc"), and Vukradin speaks **Goblin and Undercommon** but not Orc (player-asserted, no on-tape ruling). Neither is verifiable from the provided context, and the Ch. 2 archive explicitly warns the sheets on file reflect the much-later level-5 builds.
- **Evidence**: `party_ch02.md` / `world_state` level-caveat notes; standing convention to verify claimed abilities against `characters/*.md` before recaps harden them.
- **Suggested fix**: Grep `characters/vukradin.md` and `characters/valphine.md` for language lists. If Undercommon isn't on Vukradin's sheet, note it as a table assertion pending ruling rather than fact. Valphine's Orcish can stand (explicit GM ruling on tape).

### 5. "Gnomes" in the Gem of Greed joke risks confusion with the dwarves — and with Gnomengarde
- **Location**: Verbatim moments (Vukradin's OOC joke)
- **Issue**: The annotation frames "The demon attacks the gnomes for stealing the Gem of Greed" as karmic justice aimed at the "amateur archeologists" — but Dazlyn and Norbus are **shield dwarves**, not gnomes. The "gnomes" in the quote come from the temple carving imagery, not the dwarves. With an actual gnome settlement (Gnomengarde) next on the quest list, a future reader could misread this as gnome involvement with the gem.
- **Evidence**: `vtt_known_additions.md`: "Gem of Greed — Artifact depicted in the carvings of Abbathor's ruined temple; 'a demon attacks the gnomes for stealing the gem of greed.'" `campaign_state` / `entity_registry`: Dazlyn Grayshard and Norbus Ironrune are shield dwarf prospectors.
- **Suggested fix**: Amend the annotation to note the quote transposes the temple-carving imagery (gnomes stealing the gem) onto the dwarves' situation; the dwarves are dwarves.

### 6. Summary splices a GM-completed word into a Vukradin quote
- **Location**: Scene summary (bullet 3)
- **Issue**: The summary quote "Why are they attacking us?" merges Vukradin's truncated line ("Why are they attacking—") with the GM's completion ("us? Yeah, what did we do?"). The verbatim section handles this correctly with annotations; anyone quoting from the summary alone will attribute the composite wholly to Vukradin.
- **Evidence**: The recap's own verbatim section: Vukradin's line marked "(truncated)"; GM marked "*completing and answering*."
- **Suggested fix**: Low priority; acceptable as a readability composite, but keep the verbatim section as the citable layer.

### 7. Illogical linkage in the surprise/spell-slots sentence
- **Location**: Scene summary (bullet 2)
- **Issue**: "nobody in the party is surprised, **despite** entering the encounter with spell slots spent" — spell-slot depletion has no bearing on the surprise condition; the two true facts are joined by a false causal connective.
- **Evidence**: GM verbatim: "All right, nobody was surprised." Soma verbatim: "Entering in with no spells on us, huh?" — separate facts.
- **Suggested fix**: Split into two clauses: no one was surprised; the party entered with spell slots nearly spent.

## Verified as Consistent (no action needed)

- **Sending Stones in hand at departure** — matches the GM-confirmed 2026-08-17 ruling (stones withheld until the temple was cleared, handed over at end of this session) and the gm-assist summary.
- **Four orcs, road to town, initiative-only session end** — matches gm-assist Summary, Scenes, NPCs, and Locations sections.
- **"Orcanese"** — confirmed canon table coinage from this exact session (`vtt_known_additions.md` 2026-08-02); correctly preserved, do not "correct" it.
- **Soma's "hired tour guide" self-description and shell-tanking credit** — consistent with her hired-guide role (party docs) and the ochre-jelly fight (Soma withdrawing into her shell, per gm-assist).
- **Dave = Vukradin's player checking the clock** — consistent with the player roster.