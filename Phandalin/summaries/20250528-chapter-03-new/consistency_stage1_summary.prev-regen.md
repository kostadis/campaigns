# Consistency Report — "New Chapter 3" (session 2025-05-28)

## A. Campaign-state / timeline issues

**1. The Chapter 2 cliffhanger (Ogre #2, en route to Gnomengarde) is unaccounted for**
- **Location**: Summary (opening) / Scenes: "Ambush at the Blood-Stained Altar"
- **Issue**: The recap opens with the party already inside the dwarven ruins. Per campaign_state, Chapter 2 ends *mid-combat with a second ogre in a mountain valley en route to Gnomengarde*, with the Gnomengarde quest in progress and the deeper temple an unreturned-to thread. The recap contains no ogre resolution, no Gnomengarde visit, and no journey back to the ruins.
- **Evidence**: campaign_state: "Ogre Encounter #2 … IN PROGRESS, unresolved at chapter's end … the resolution belongs to whatever chapter narrates it next." Party location: "narrow, steep-walled mountain valley en route to Gnomengarde, mid-combat."
- **Suggested fix**: GM must reconcile the chronology: either the archive mis-sequenced the ogre/Gnomengarde departure (the archive is a DRAFT), or this recap silently skips the ogre resolution and return trip. Do not let a future pass invent a transition; record the actual play order from the VTT.

**2. Sending stones — recap is right, two context docs are stale (protective note)**
- **Location**: Summary / Scenes: "Archaeologists and Altars", "Amateur Archaeologists" / Items: Sending Stones
- **Issue**: The recap has the dwarves withholding the stones until the ruins are cleared, handing them over at session's end. This is correct — but planning_ch02 ("Sending stones already paid in advance") and party_ch02 ("Sending stones (pair) — given by Dazlyn Grayshard and Norbus Ironrune" under Collective resources) contradict it.
- **Evidence**: campaign_state, GM-confirmed 2026-08-17: "the dwarves withhold the stones until the temple is fully cleared and hand them over only at the end of that session."
- **Suggested fix**: No change to the recap. Flag planning_ch02 and party_ch02 for regeneration so a future consistency pass doesn't "correct" the recap the wrong way.

## B. Attribution errors (who said/did what)

**3. "We found 10" — attributed to both Valphine and Soma**
- **Location**: Memorable Moments (quote block) vs. Summary and Scenes: "The Skull Cavity"
- **Issue**: The quote block credits **Valphine**; the Summary ("Soma quietly suggested they had found only ten") and the Skull Cavity scene ("Soma attempts to quietly underreport: 'We found 10. We found 10.'") credit **Soma**. The prior gm-assist export also says Valphine.
- **Evidence**: Both attributions appear inside the same document. Character grounding cuts both ways (Valphine is the plunder-minded one per world_state; but the Skull Cavity scene also gives Valphine a separate beat: "states plainly she would have robbed the grave").
- **Suggested fix**: Verify against the VTT and unify to one speaker in all three places. This is a precision attribution that will propagate.

**4. The "amateur archaeologists" admission and the "several days ago" line**
- **Location**: Summary / Scenes: "Amateur Archaeologists" vs. NPCs: Dazlyn
- **Issue**: Three problems. (a) Summary and scene attribute the admission to **Norbus**; the Dazlyn NPC entry says **Dazlyn** "admitted under pressure." (b) "I would say several days ago" is a **DM table aside** in the Summary, but the Dazlyn entry converts it into Dazlyn's in-fiction admission. (c) The recap gives the aside two different meanings — "when they heard the site might be important" (Summary) vs. "how long they have practiced the hobby" (scene).
- **Evidence**: Summary: "Norbus admitted: 'Oh, we're… amateur archaeologists…' The DM added quietly: 'I would say several days ago.'"
- **Suggested fix**: Attribute the admission to Norbus (matching the direct quote), keep the DM aside as table-level commentary, pick one meaning after checking the tape, and rewrite the Dazlyn NPC entry accordingly.

**5. Dazlyn "Punched Norbus"**
- **Location**: NPCs: Dazlyn
- **Issue**: "Punched Norbus when Norbus offered to tell stories" contradicts every other rendering of the beat, which is verbal ("Dazlyn corrects Norbus before he can object").
- **Evidence**: Summary and "Archaeologists and Altars" scene both use "corrects"; no physical altercation is narrated anywhere else.
- **Suggested fix**: Change to "Cut Norbus off / corrected him" unless the VTT actually shows a punch (likely a garble or invention).

**6. "We had servants" and the party's languages**
- **Location**: Summary (closing) / Scenes: "Ambush on the Road"
- **Issue**: (a) The Summary attributes "We had servants" to **Soma**; the scene has **Wade** (Soma's player) saying it — but as an explanation of *why Valphine speaks Orc*, which only Gary (Valphine's player) could supply in-fiction. The drow-had-orc-servants logic strongly suggests this is Gary/Valphine's line. (b) Vukradin "speaks Undercommon and Goblin" is odd for an Aasimar Neverwinter busker — Undercommon is the classic *drow* language, raising the possibility the languages got swapped between PCs in extraction.
- **Evidence**: party_ch02: Wade Brown plays Soma; Gary Young plays Valphine. Standing rule (memory): verify spell/ability attribution against character sheets before accepting recap claims.
- **Suggested fix**: Check `characters/vukradin.md` and `characters/valphine.md` for languages; fix the speaker attribution from the VTT.

**7. Secret-door passive perception — Valphine or Vukradin?**
- **Location**: Scenes: "Archaeologists and Altars" (Valphine, passive 15, doors near altar) vs. Summary and "Exploring the Stone Bedrooms" (Vukradin, passive 15, bedroom door)
- **Issue**: Two different PCs credited with identical passive perception (15) for secret-door finds; identical scores suggest one attribution may have been copied onto the wrong PC.
- **Evidence**: The earlier gm-assist export credits only Valphine with the altar-area doors.
- **Suggested fix**: Verify both PCs' passive perception against sheets and confirm per-door attribution from the tape.

**8. "Wade confirms it is" (the DMG artwork question)**
- **Location**: Scenes: "The Hall of Greed"
- **Issue**: Vukradin asks the *DM* whether the statue is classic D&D art; the answer is attributed to Wade (Soma's player) rather than Kostadis. Possible but suspicious.
- **Evidence**: The question is directed at the game's presentation ("Is that, like, a classic D&D picture?") — normally a DM answer.
- **Suggested fix**: Verify speaker on the tape; low stakes but easy to fix.

**9. Player line attributed to the character**
- **Location**: Memorable Moments ("Two, killed two creatures in one round. There's a bard for you, Kostadis." — Vukradin)
- **Issue**: The Battle scene correctly attributes this to "Dave (Vukradin's player)" — it is table talk addressed to the DM, not in-fiction speech.
- **Evidence**: Internal inconsistency within the document.
- **Suggested fix**: Attribute the quote to Dave (player) in the Moments block.

## C. Internal mechanical contradictions

**10. Split-trigger rule contradicts itself**
- **Location**: Summary / Scenes: "Battle with the Ochre Jellies", "Ambush Behind the Altar" / NPCs: Ochre Jelly / Spells: Starry Wisp
- **Issue**: The recap asserts (via Vukradin's Arcana 13) that only slashing splits the jellies and that piercing/bludgeoning do not. Yet the first fight's second split is "ruled" as triggered by **Starry Wisp (radiant)**, and the second fight's split follows **dagger (piercing)** hits — both described as happening at an HP threshold ("under twenty hit points"). RAW, splits trigger on slashing/lightning only.
- **Evidence**: "Vukradin's last blow is ruled as what triggered the split" (radiant); "Vukradin hits twice with daggers… The jelly splits into two oozes."
- **Suggested fix**: Record the DM's actual house rule explicitly (e.g., "large jellies split when reduced below a threshold, regardless of damage type") so future sessions don't inherit two incompatible rules.

**11. Soma's AC — hit on a 17 while in her shell at AC 21**
- **Location**: Scenes: "Battle with the Ochre Jellies"
- **Issue**: "The first connects for ten points of damage (rolling a 13+4 = 17, matching her AC exactly)" — but Soma is described as still shelled (AC 21) at that point; 17 matches her *unshelled* AC. An earlier attack against "Soma (AC 21)" missing on 14(+4=18) is consistent with 21, so the 17-hit contradicts.
- **Evidence**: "raising her armor class from 17 to 21"; she "un-withdraws" only after being revived.
- **Suggested fix**: Verify against the tape whether she had emerged before the knockout sequence, or whether the hit roll/AC is misrecorded.

**12. The "stunned" jelly attacks**
- **Location**: Scenes: "Battle with the Ochre Jellies" ("The third (stunned) jelly rolls its pseudopod against Soma and misses.")
- **Issue**: A stunned creature is incapacitated and cannot attack. Presumably the stun (one free round, per the DM ruling) had expired by this point — the "(stunned)" label is stale.
- **Suggested fix**: Reword to "the third jelly (no longer stunned)".

**13. Jelly initiative modifier: −2 vs −1**
- **Location**: Scenes: "Ambush at the Blood-Stained Altar" ("reduced to 17 by a −2 penalty") vs. "Ambush Behind the Altar" ("The jelly gets a −1")
- **Issue**: Same creature type, two different Dex modifiers within one session. (Ochre jelly Dex 6 → −2.)
- **Suggested fix**: Standardize to −2 unless the tape shows otherwise.

**14. Jelly body-count contradiction in the first fight**
- **Location**: Scenes: "Battle with the Ochre Jellies"
- **Issue**: "Soma… uses Poison Spray on the **last surviving jelly** — dealing seven points and killing it" — yet immediately afterward "the surviving jelly attacks Brewbarry" and Vukradin then kills **two** jellies with daggers. The Poison Spray target cannot have been "the last surviving jelly."
- **Evidence**: The double-dagger double-kill is the session's celebrated closer; at least two jellies were alive after Soma's kill.
- **Suggested fix**: Reword to "one of the split jellies." (The arithmetic works: after the second split plus the ceiling jelly, three were alive — Soma killed one, Vukradin killed two.)

**15. Spells section misplaces Poison Spray**
- **Location**: Spells: Poison Spray ("Used by Soma twice **in the first combat**")
- **Issue**: The 1-point / "twenty percent" cast happened in the *second* combat (behind the altar), per both the Summary and the "Ambush Behind the Altar" scene.
- **Suggested fix**: "Once in each combat: 7 points (first fight kill), 1 point (second fight)."

**16. Healing Word — "cantrip slot" and possible upcast**
- **Location**: Scenes: "Battle with the Ochre Jellies" / Spells: Healing Word
- **Issue**: (a) "The cantrip slot allowed pairing with a damage cantrip" is garbled — Healing Word is a 1st-level *bonus-action* spell; the bonus action is what allows pairing with a cantrip. (b) "2d4+3" is an upcast (base is 1d4+mod); party level at this point is unconfirmed (archive presumes ~1st).
- **Evidence**: party_ch02: "Starting level is presumed 1st (unconfirmed on the page)."
- **Suggested fix**: Fix the wording; confirm Valphine's level/slot usage with the GM before this feeds any regenerated chapter.

**17. Tortle shell — emerging as a bonus action**
- **Location**: Scenes: "Battle with the Ochre Jellies" ("As a bonus action she can pop back out"; "un-withdraws from her shell as a bonus action")
- **Issue**: RAW Shell Defense requires an *action* to emerge. If this is a table ruling, it should be recorded as such rather than as rules fact.
- **Suggested fix**: Annotate as a house rule or correct to "action," per the tape.

**18. Crit math on the bare-fist critical**
- **Location**: Scenes: "Battle with the Ochre Jellies" ("The crit deals fourteen points… (1+4+2 base, doubled)")
- **Issue**: Doubling modifiers on a crit is nonstandard (RAW doubles dice only, and an unarmed strike has no die). Fine if it's the table's practice, but shouldn't read as neutral rules fact.
- **Suggested fix**: Mark as table ruling or verify the damage breakdown.

**19. Minor arithmetic/count nitpicks (bundle)**
- **Location**: Scenes: "Ambush Behind the Altar" / Spells: Starry Wisp
- **Issue**: (a) 26 − 6 = 20, but the text says "Jelly **under** 20 HP." (b) "Third natural one of the session for Gary" — only two of Gary's nat-1s are narrated. (c) Starry Wisp's "second cast dealt 4 damage in an earlier exchange" appears nowhere in the scene log.
- **Suggested fix**: Verify each against the VTT or soften the specificity.

## D. Lore / canon cautions

**20. "Uthgard barbarian"**
- **Location**: Summary and Scenes: "The Skull Cavity"
- **Issue**: Canonical spelling is **Uthgardt**. Also note the nuance: Brewbarry is a *Goliath* raised by (and exiled from) an Uthgardt tribe, not an Uthgardt tribesman simpliciter.
- **Evidence**: world_state: "Goliath barbarian, exiled from his adopted Uthgardt tribe"; VTT glossary corrects Utgartian/Uthgardian → Uthgardtian.
- **Suggested fix**: "Uthgardt-raised goliath barbarian."

**21. Ochre jelly at 52 HP**
- **Location**: NPCs: Ochre Jelly (52 HP, AC 8); Scenes: "Ambush Behind the Altar" (43 → 37 → 26 HP tracking implies 52 start)
- **Issue**: Standard ochre jelly is 45 HP. 52 is plausible as rolled HP, but shouldn't be recorded as the creature's stat without confirmation.
- **Suggested fix**: Annotate "(rolled)" or confirm with GM.

**22. The Hall of Greed statue — module says trapped; recap canonizes "probably glass"**
- **Location**: Scenes: "The Hall of Greed" / Items: Glowing Green Gem
- **Issue**: (a) entity_registry E11: "trapped statue of a horned dwarf holding a glowing green gem" — the recap never mentions the trap, which is presumably still live since the gem was left in place. (b) "The DM's own private assessment: probably worthless glass" is DM-private information in a player-facing recap; if it was actually said aloud, it's table color, not established fact — and it partially conflicts with the confirmed magical aura.
- **Suggested fix**: Drop or reframe the "private assessment" line as table banter; do not record the gem's nature as resolved. Leave the trap unspoiled but flag for the GM that it remains armed.

**23. Holy symbol — does the party know Valphine has it?**
- **Location**: Memorable Moments vs. Summary / Items: Holy Symbol of Abbathor
- **Issue**: The Summary and Items say she made the DC 5 sleight of hand (successful palm, Vukradin absent for three rounds); the Moments blurb says she pocketed it "**while the party watches**," and the older gm-assist export goes further ("the rest of the party had already seen exactly what she was doing"). Whether the party knows is a live continuity fact for future sessions.
- **Suggested fix**: GM ruling needed: who witnessed the palm? Record one version everywhere.

**24. Unverified equipment: Vukradin's daggers, Valphine's dagger**
- **Location**: Throughout (Vukradin's double-dagger kills; "Valphine sharpened her dagger pointedly")
- **Issue**: Vukradin's documented kit is clarinet/flute and rapier; daggers are unlisted. Valphine's listed kit is mace and/or hand crossbow. Both are plausible standard-kit items, but per the standing verification rule they should be checked before the "daggers" become his signature.
- **Evidence**: world_state Vukradin key items; party_ch02 Valphine items of significance.
- **Suggested fix**: Grep the character sheets; if confirmed, no change.

**25. Long rest narrated twice / Skull Cavity ordering ambiguity**
- **Location**: Scenes: "Archaeologists and Alt**25. Long rest narrated twice / Skull Cavity ordering ambiguity** *(continued)*
- **Location**: Scenes: "Archaeologists and Altars" (final bullet: "The party takes a long rest; over the course of the evening Norbus forgets Vukradin's name") vs. "Exploring the Stone Bedrooms" (first bullet: "The party takes a long rest and heads north"); Summary ("Earlier in the expedition, the party had also stumbled upon a secret cavity…")
- **Issue**: (a) The same long rest is narrated at the end of one scene and the start of the next — reads as two rests. The Summary describes only one. (b) The Skull Cavity discovery and gem-split negotiation float in time: the scene list places it between the rest scenes; the Summary retrofits it with "Earlier in the expedition." Whether the tense gem negotiation happened before or after the long rest (i.e., before or after the party was rested and the dwarves fed them) changes the social read of the scene.
- **Suggested fix**: Collapse to one long rest; pin the Skull Cavity scene to its actual position in the session from the VTT and drop the "Earlier in the expedition" flashback framing.

**26. "Could you not use such damaging spells?" — solo vs. joint attribution**
- **Location**: Memorable Moments (attributed to Norbus alone) vs. Scenes: "Battle with the Ochre Jellies" ("Norbus **and Dazlyn** shout warnings from the corridor: 'Could you not…'")
- **Issue**: Minor attribution drift — quote credited to one dwarf in one place, both in another. The Norbus NPC entry ("Urged the party not to damage the ruins") supports the solo attribution.
- **Suggested fix**: Credit Norbus; reword the scene bullet to "Norbus shouts (Dazlyn beside him)" or verify on the tape.

**27. "Immune to slashing damage" — correct, for the record**
- **Location**: NPCs: Ochre Jelly; Scenes: "Ambush at the Blood-Stained Altar"
- **Issue**: None — noting affirmatively so a future pass doesn't "fix" it: ochre jellies genuinely are immune to slashing (and lightning) damage, and slashing is the RAW split trigger. The recap's statement is rules-accurate; it is only the *later* splits (issue 10) that contradict it.
- **Suggested fix**: No change here.

---

## Summary of verdicts

| Severity | Issues |
|---|---|
| **Must resolve before this recap seeds anything downstream** | 1 (ogre/Gnomengarde timeline), 3 ("We found 10" speaker), 4 (amateur-archaeologist admission / "several days ago"), 10 (split-trigger rule), 23 (who saw the holy symbol palm) |
| **Fix in place, low ambiguity** | 5 ("Punched"), 9 (Dave/Vukradin quote), 12 (stunned jelly), 14 ("last surviving jelly"), 15 (Poison Spray placement), 20 ("Uthgard"), 25 (double long rest), 26 (quote attribution) |
| **Verify against sheets/VTT** | 6 (languages + "We had servants"), 7 (passive perception), 8 (Wade vs. DM), 11 (Soma AC), 16 (Healing Word), 24 (daggers) |
| **Annotate as table ruling or soften** | 13 (initiative mod), 17 (shell bonus action), 18 (crit math), 19 (arithmetic nitpicks), 21 (52 HP), 22 (gem "probably glass" / live trap) |
| **Context docs stale, recap correct — do not "fix" the recap** | 2 (sending stones vs. planning_ch02/party_ch02) |

Everything else in the recap — location layout (E5/E8/E9/E10/E11 mapping), the Abbathor lore, the 7/8 gem split, Dazlyn/Norbus name usage and personality direction, the sending-stones handover timing, the closing orc ambush, and the Dave/Gary/Wade/Stéphane player mappings where stated — checks out against the provided context.