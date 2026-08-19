# Consistency Report — "New Chapter 3" (session 2025-05-28)

Checked against: `campaign_state` (ch2 archive), `world_state` (ch2 archive), `party_ch02.md`, `planning_ch02.md`, `entity_registry.yaml`, `vtt_transcription_corrections.md`, `vtt_known_additions.md`, and the base `gm-assist.md` export.

---

## Critical — conflicts with campaign_state

**1. The 50 gp message-delivery reward is described as still owed; campaign_state says it was already collected.**
- **Location**: Summary (final paragraph), Scenes › Ambush on the Road, Items › Sending Stones, Scenes › The Skull Cavity (Vukradin: "here for the sending stones and for the hard-earned 50 gold pieces for delivering the message").
- **Issue**: The recap repeatedly frames the 50 gp as uncollected ("the fifty gold pieces still owed for delivering their message about the dragon"; "A separate 50-gold-piece reward… still awaited collection back in town").
- **Evidence**: campaign_state, Completed Encounters: "**Return to Phandalin — Dwarven Quest Reward Collected:** Harbin Wester paid the promised 50 gp." Party doc lists "50 gp — Dwarven Excavation quest reward" among collective resources.
- **Suggested fix**: One of the two is wrong and this is exactly the class of error the archive already produced once (its "sending stones in party's possession" line was overturned by the transcript, GM-confirmed 2026-08-17). Verify against the ch3 VTT; if the recap reflects play, amend the ch2 archive's "Reward Collected" entry rather than the recap.

**2. Timeline discontinuity: campaign_state leaves the party mid-ogre-fight en route to Gnomengarde; the recap opens at the temple ruins with no bridge.**
- **Location**: Summary (opening paragraph), Scenes › Ambush at the Blood-Stained Altar.
- **Issue**: Chapter 3 begins with the party "at a crossroads in the ancient dwarven ruins" and never mentions Ogre #2's resolution, the Gnomengarde trip, or travel back to the ruins. Campaign_state explicitly says the ogre's fate "belongs to whatever chapter narrates it next" — this recap doesn't narrate it.
- **Evidence**: campaign_state, Party Current Situation: "Current location: A narrow, steep-walled mountain valley en route to Gnomengarde, mid-combat with a hungry ogre." Ogre #2: "Prone, fate unresolved."
- **Suggested fix**: Determine from the transcript whether (a) the session opened by resolving the ogre and the recap dropped it, or (b) the hand-authored ch2 prose narrated events (reward collection, Gnomengarde departure, ogres) that actually happened *after* this session. Given issue 1, option (b) is plausible — the ch2 archive's event ordering may need GM correction before the incremental rebuild continues.

**3. The dwarves' backstory: "amateur archaeologists, days old" vs. "months of prospecting and clearing rubble."**
- **Location**: Summary (Amateur Archaeologists paragraph), Scenes › Amateur Archaeologists, Locations › Hall of Greed ("the very site Dazlyn and Norbus had been hunting for").
- **Issue**: The recap says the dwarves took up archaeology "days ago at most," "had heard the ruins might be an important find and gone looking for the Hall of Greed."
- **Evidence**: campaign_state/planning: Dazlyn "found the ruined settlement **while prospecting for gold**; spent **months** clearing rubble and searching for treasure." Registry: Dazlyn is "forthright and honest to a fault."
- **Suggested fix**: If this is a genuine in-session revelation (the dwarves' ch2 story was embellished), it needs a logged note against the ch2 archive; the "hunting for the Hall of Greed all along" framing in particular contradicts the accidental-discovery account. Confirm with GM before either version seeds future docs.

---

## Attribution — verify against transcript

**4. Dazlyn/Norbus lines swap roles mid-document.**
- **Location**: Memorable Moments › "Soma is knocked unconscious…"; NPCs › Dazlyn.
- **Issue**: The document establishes Dazlyn = party-safety concern, Norbus = site-preservation concern (Summary, first battle scene, both NPC entries). But the Soma-KO moment inverts it: "**Norbus** called from the corridor, 'Did somebody get hurt?' and **Dazlyn** added, 'Again, to the extent possible, please don't damage any of the artwork.'"
- **Evidence**: Base gm-assist NPC entry: Dazlyn's "Is everybody okay there?" is "a separate concern for the party's safety, **distinct from Norbus's warning** about damage to the site."
- **Suggested fix**: Verify speakers on the tape. Either the second exchange genuinely traded roles (possible as a bit) or the enrichment pass swapped the attributions.

**5. Vukradin quote: "clearing out these ogres."**
- **Location**: Scenes › Ambush Behind the Altar.
- **Issue**: "We're doing our job in clearing out these **ogres** for the dwarves" — the temple threat is oozes; the ogres were the ch2 road encounters.
- **Evidence**: campaign_state: Dazlyn's warning was "I think we saw some **oozes** in there."
- **Suggested fix**: Check the tape. If Dave actually said "ogres," keep it as spoken (per the Cassian brother/cousin precedent: quotes stay verbatim, narration gets corrected); if it's a summarizer substitution, fix to "oozes."

---

## Internal inconsistencies

**6. Soma's AC at the moment she goes down: 21 or 17?**
- **Location**: Summary (para 4), Memorable Moments › "Soma is knocked unconscious…", Scenes › Battle with the Ochre Jellies.
- **Issue**: Summary: she "planted herself as a living barrier at armor class 21 — **until** … a pair of pseudopod strikes … overwhelmed her defenses." But the moment says the first hit was "ten acid damage against her **AC 17**," and the scene says "a thirteen-plus-four roll beating Soma's AC **exactly**" (17). A 17 does not hit AC 21.
- **Suggested fix**: She must have emerged from the shell before the hits (Shell Defense ends when she takes an action to emerge). Rewrite the Summary so the shell phase clearly ends before the KO, or the "living barrier until overwhelmed" framing will read as a rules break.

**7. Brewbarry's retroactive Stone's Endurance vs. finishing at 1 HP.**
- **Location**: Summary (para 4), Scenes › Battle with the Ochre Jellies, Spells › Healing Word.
- **Issue**: He takes 12 damage, dropping to 1 HP; later "retroactively shrugs off eleven points of the earlier hit with Stone's Endurance." If 11 of the 12 were negated, he's at ~12 HP — yet Healing Word's entry insists he "was never healed and finished the encounter at a single hit point." Both cannot be true.
- **Suggested fix**: Check the tape for what Stone's Endurance actually applied to (a *later* hit would reconcile everything). Also note Stone's Endurance is a reaction on taking damage; "retroactive on his turn" is a house ruling worth logging if real.

**8. Gary's natural-1 tally doesn't close.**
- **Location**: Scenes › Battle with the Ochre Jellies (final bullet), Scenes › Ambush Behind the Altar, Scenes › The Hall of Greed.
- **Issue**: Fight-1 mace is "the first of Gary's **three** natural ones"; fight-2 mace is "Gary's **third** natural one of the night"; but the Hall of Greed investigation nat-1 comes *after* fight 2 — a fourth. Either the total is four, or the ordinal labels are misplaced.
- **Suggested fix**: Re-derive the tally from the transcript (the "three ones / three twenties" line was probably an end-of-session remark the enrichment pinned to the wrong rolls).

**9. First-battle body count doesn't reconcile — three related claims.**
- **Location**: Scenes › Battle with the Ochre Jellies, Items › Vukradin's Daggers, Spells › Poison Spray.
- **Issue**:
  - "One down, **three** to go" implies four jellies active at Brewbarry's kill; the narrative establishes only three (split pair + ceiling drop).
  - Poison Spray's entry claims "one cast killed a weakened jelly outright with seven damage" — no such kill appears in either battle narrative (the base export has Poison Spray only "whittling down the remaining ooze").
  - The daggers entry claims "four jelly deaths in total"; the narrative supports three (double-kill in fight 1, final ooze in fight 2).
  - The Dissonant-Whispers jelly flees and is never accounted for before "clearing the room."
- **Suggested fix**: Rebuild the fight-1 kill ledger from the transcript before this recap becomes the chapter source. The missing Poison Spray kill (possibly the fled jelly) would explain both the "three to go" count and the room being cleared — but that's a guess, not evidence.

---

## Mechanics — verify against character sheets

**10. Healing Word "2d4+3."**
- **Location**: Spells › Healing Word.
- **Issue**: Healing Word at 1st level is 1d4 + modifier. The recap elsewhere strongly implies the party is level 1 (Soma out of slots after two Ice Knives; Valphine at 9 HP; "Bards don't do much at level one"), so a 2nd-level cast is impossible. The 8-point heal is reachable with 1d4+4.
- **Suggested fix**: Verify Valphine's sheet/level; the dice notation is likely an enrichment invention. Per standing rule, confirm caster mechanics against `characters/*.md` before this feeds anything downstream.

**11. Vukradin's paired daggers are unconfirmed kit — and the recap canonizes them as a signature item.**
- **Location**: Items › Vukradin's Daggers, Summary, both battle scenes.
- **Issue**: The ch2 world_state lists Vukradin's baseline weapons as "clarinet/flute, **rapier**." Daggers appear nowhere in the ch2 docs, yet get their own item entry here ("accounting for four jelly deaths").
- **Suggested fix**: Confirm daggers on the sheet before promoting the item entry. Same check for Valphine's dagger (the sharpening bit) — her documented kit is "mace and/or hand crossbow."

**12. Vukradin's languages: Undercommon and Goblin.**
- **Location**: Scenes › Ambush on the Road.
- **Issue**: Vukradin proposes side conversations in Undercommon and is said to speak Goblin but not Orc. Neither language is confirmed anywhere in the context docs for an Aasimar Neverwinter busker.
- **Suggested fix**: Verify against his sheet; if unlisted, mark the Undercommon proposal as aspirational table talk, not capability.

**13. "His rage useless against acid" — RAW-questionable rationale.**
- **Location**: Summary (second battle), Scenes › Ambush Behind the Altar.
- **Issue**: An ochre jelly pseudopod is bludgeoning + acid; rage resistance applies to the bludgeoning portion. The all-acid framing (and the 17 points called "acid") may be a table simplification — but the base export makes no such mechanical claim; the rationale is enrichment-added.
- **Suggested fix**: Soften to what happened (Stone's Endurance absorbed 9) unless the tape shows the DM ruling it all acid.

**14. Inconsistent split trigger for the jellies.**
- **Location**: Scenes (both battles), Spells › Starry Wisp, NPCs › Ochre Jelly.
- **Issue**: The document states jellies split on slashing but not piercing (RAW), yet also has one split from an 8-point **radiant** hit "driving it below half," and the fight-2 jelly split "under the sustained assault" of bludgeoning and piercing. These can't all be the same rule.
- **Suggested fix**: Establish which rule the table actually ran (split-on-slashing vs. split-at-half-HP) and make the recap consistent — Vukradin's whole dagger gambit depends on the answer.

---

## Minor / editorial

- **"Morning Lord"** (Scenes › Archaeologists and Altars) → **"Morninglord"** per the VTT corrections glossary.
- **"To thenorth"** (Summary, para 5) — missing space.
- **"Brewbarry cleaving one apart"** (Summary, second battle) vs. Items › Halberd claiming he "abandoned the weapon entirely in favor of his fists for the rest of the session" — "cleaving" implies the blade. Pick one.
- **Soma "set the coffer back on the altar"** (Summary, Items › Stone Coffer) — the coffer came from the pillar cavity, not the altar; "back" will confuse future item-provenance passes.
- **Quote variance**: the fleeing moment's header quotes "guys, this is fleeing time" but the body quotes "Guys, we're done here" — fine if both were said sequentially; confirm.
- **Title**: "New Chapter 3" doesn't follow the campaign's "Chapter N: Title" convention (e.g., "Chapter 34: Where Cows Come Home").

---

## Verified consistent — do not "fix"

- **Sending stones timing** matches the GM-confirmed ruling (2026-08-17): withheld until the temple is fully cleared, handed over at session end.
- **"Overbrighters"** is confirmed canon vocabulary (vtt_known_additions, 2026-08-02) — not an ASR garble; leave it.
- **Second-fight HP math** is internally sound: 52 → 43 (Ice Knife 9) → 37 (daggers 6) → 26 (Ice Knife 11) → 20 (mace 6) → 10 (daggers 10) → splits into two 5-HP oozes (half of current, RAW) → crit kill / 1-point Poison Spray ("20% of its hit points" checks out) / 8-point dagger finish.
- **Jelly stat details** match RAW: AC 8, initiative penalty, frightened/prone immunity, psychic and poison susceptibility, punch-don't-slash tactics.
- **Location layout** matches the registry (E5 altar + ceiling jellies, E7 secret tunnel jelly, E8 bed frames, E9 vestry/font/wardrobe, E10 priest skeleton + holy symbol, E11 Hall of Greed). Registry note for the GM: E11's statue is **trapped** — the party left the gem in place, so the trap is still live.
- **Boney correctly absent**; party is the ch2 four.
- **Player attributions** check out: Gary = Valphine, Dave = Vukradin.
- **Vukradin's parley-first instinct** with the road orcs is continuous with his ch2 characterization.