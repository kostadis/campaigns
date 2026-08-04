# Consistency Report — Chapter 60 Recap

---

## CRITICAL: Session Numbering Mismatch

**Location:** Chapter heading ("# Chapter 60") and throughout all sections
**Issue:** The recap is labelled **Chapter 60**, but based on the campaign context this is almost certainly a mislabel. The campaign state, working docs, and stale-docs issue report all describe the High Tower confrontation, Manshoon reveal, and sapphire theft as occurring during what the table calls **Chapter 60** — but the file `20260727_candlekeep_the_man_with_the_metal_hand.md` and the stale-docs issue report (`20260727_grounding_docs_stale_ch62.md`) place these events at **Chapter 62** (or the session that follows Ch.62). The gm-assist.md export also labels this session "Chapter 60 / Date: 2026-07-27."
**Evidence:** The stale-docs issue report notes that chapters 61–62 involve the helmed horror ambush and the North Gallery/Moziqodo events. The High Tower confrontation is staged as the session *after* those. Session date 2026-07-27 matches the working docs, but the chapter number assigned is internally inconsistent with campaign state counters.
**Suggested fix:** Verify the authoritative chapter counter (bible-file number vs. session number vs. internal header — the stale-docs report flags all three as out of sync). If this session is correctly "Chapter 60," then all campaign-state references to the High Tower events being "Ch.62" need reconciling. Flag for GM review before promoting to canon.

---

## 1. Bookwyrm — Described as Dead; Campaign State Says Alive

**Location:** Summary ("Bookwyrm dead"), Scenes → Confrontation at the High Tower ("A'lai looked around at the carnage — Bookwyrm dead"), NPCs → Bookwyrm
**Issue:** The recap's NPC section describes Bookwyrm as having been "brutally murdered — her throat torn apart by Moziqodo's claws." However, the campaign_state.md and world_state.md both list Bookwyrm as **Alive** (status post-key-seizure unconfirmed). The stale-docs issue report confirms this is a known staleness problem in the grounding docs, but also notes that Bookwyrm's death is canon per chapter_62 content. The recap treats her death as established backstory without flagging it as a development within this session.
**Evidence:** campaign_state.md NPC table: "Bookwyrm (First Reader) | Alive | Candlekeep | Manipulative, self-preserving." world_state.md Candlekeep NPC table: "Bookwyrm | Alive." The stale-docs report confirms she is dead per ch.62 content, but the grounding docs haven't caught up.
**Suggested fix:** If Bookwyrm's death is confirmed canon (from ch.62 or earlier), the NPC entry in this recap is accurate but should note *when* she died (prior session, not this one). The recap's NPC blurb for Bookwyrm reads as if her death is being introduced here for the first time, but A'lai references it mid-combat as already-known. Clarify: was her death revealed to the party *in this session* or was it prior knowledge?

---

## 2. Bookwyrm's Title and Species

**Location:** NPCs → Bookwyrm
**Issue:** The recap describes Bookwyrm as "A high-ranking member of Candlekeep." The world_state.md and entity registry specify she is the **First Reader** (acting head of Candlekeep) and a **green dragonborn**. The recap omits both her title and species.
**Evidence:** world_state.md: "Bookwyrm (First Reader) | Alive | Green dragonborn acting head of Candlekeep." entity_registry.yaml: "Bookwyrm (First Reader) | aliases: Bookwyrm, Skoda Vanaster, The First Reader, First Reader | note: First Reader (real name; green dragonborn master sage)."
**Suggested fix:** Update the NPC blurb to read: "The First Reader (acting head of Candlekeep), a green dragonborn, who had possessed one of the real High Tower keys."

---

## 3. Fembris — Title and Current Status

**Location:** NPCs → Fembris
**Issue:** The recap describes Fembris as "an acolyte." The entity registry lists him as "acolyte adjutant," and campaign_state.md notes he is the party's **captive** held in Deneir's Sanctum serving as food taster, and is "the only witness to Grygum handing the Hightower key to Daz." The recap's description of his role — confessing that A'lai was in the room when the key's location was reported — is accurate, but omits his current imprisoned status and his identity as sole witness to the key handoff.
**Evidence:** campaign_state.md: "Fembris Lancer | Imprisoned | Deneir's Sanctum (party's captive) | Unwilling; sole witness to key handoff." world_state.md: "Fembris Lancer — Alive, held in Deneir's Sanctum, unwilling companion serving as food taster. The only witness to Grygum handing the Hightower key to Daz."
**Suggested fix:** Add to the NPC blurb that Fembris is currently the party's captive food taster, held in Deneir's Sanctum, and is the sole witness to the key handoff — context that matters for continuity.

---

## 4. Grygum's History Check Roll Attributed Incorrectly

**Location:** Summary ("The party's history checks (Grygum 22, Daz 21)"), Scenes → Confrontation at the High Tower ("Daz and Grygum both roll History (22 and 21 respectively)")
**Issue:** The Summary assigns the 22 to Grygum and the 21 to Daz. The Scenes section assigns "22 and 21 respectively" to "Daz and Grygum" — i.e., Daz rolled 22, Grygum rolled 21. These two sections contradict each other.
**Evidence:** Summary: "Grygum 22, Daz 21." Scenes: "Daz and Grygum both roll History (22 and 21 respectively)" — "respectively" here means Daz=22, Grygum=21. The Memorable Moments section doesn't include this roll to break the tie.
**Suggested fix:** Verify against the VTT transcript which player rolled which score. Pick one assignment and apply it consistently throughout the recap.

---

## 5. Zalthir "Staggered" vs. Knocked Unconscious — Internal Contradiction

**Location:** Summary ("hammering Zalthir hard enough to knock him unconscious"), Scenes → Confrontation (same), vs. gm-assist.md Scenes ("battering Zalthir, though the monk stays on his feet")
**Issue:** The full recap (Summary and Scenes) states Zalthir was knocked **unconscious** by A'lai's initial arcane burst volley, then later the party resumed fighting. The gm-assist.md export (the companion document) says "battering Zalthir, though the monk stays on his feet" during the same initial exchange, with Zalthir only going unconscious later after the sapphire theft. The combat board in the resume doc confirms Zalthir is unconscious at the cut.
**Evidence:** gm-assist.md Scenes → Confrontation: "severely wounding Daz and battering Zalthir, though the monk stays on his feet." Full recap Summary: "hammering Zalthir hard enough to knock him unconscious." Resume doc board: "Zalthir | UNCONSCIOUS."
**Suggested fix:** The resume doc is the most authoritative (it was built on what actually happened). Zalthir was knocked unconscious, but it appears to have happened in *two stages* — first hit hard but standing, then knocked out after Daz grabbed the sapphire and retreated. The summary and gm-assist.md are compressing events differently. Clarify the sequence: Zalthir was wounded but still standing during the first exchange, then knocked unconscious after A'lai's enraged follow-up. Both the Summary and the gm-assist.md are partially correct but neither captures the two-stage sequence.

---

## 6. Daz's Spell — "Maximilian's Earthen Grasp" vs. Party Sheet Abilities

**Location:** Summary ("Daz conjured a massive hand of compacted soil"), Scenes → Confrontation, Memorable Moments → "The Counterspell Gambit"
**Issue:** The recap correctly identifies the spell as Maximilian's Earthen Grasp. The party.md entry for Daz lists "Maximilian's Earthen Grasp" in his abilities — consistent. No contradiction. **(No error — flagging for confirmation only.)**
**Evidence:** party.md: "Abilities: Evoker (Fireball, Scorching Ray, Sculpt Spells), Fey Touched, Warcaster, Misty Step, Shape Water, Magic Missile, Maximilian's Earthen Grasp, Hypnotic Pattern, Telekinetic."
**Suggested fix:** No change needed.

---

## 7. Telekinesis — Described as "5th level spell" but Party Sheet Lists "Telekinetic" (Feat)

**Location:** Summary ("Daz used Telekinesis (5th level) to snatch it"), Scenes → Confrontation, Items → Sapphire Artifact, Memorable Moments → "The Telekinetic Snatch"
**Issue:** The recap consistently calls this "Telekinesis (5th level)" — a 5th-level spell from the wizard spell list. However, Daz's party.md entry lists "Telekinetic" (the feat from Tasha's Cauldron of Everything), which grants a *mage hand*-style telekinetic shove, not the full Telekinesis spell. The working doc (`20260727_candlekeep_the_man_with_the_metal_hand.md`) explicitly describes the sapphire grab as using "Telekinetic *mage hand*, at range" — i.e., the feat, not the 5th-level spell.
**Evidence:** party.md Daz abilities: "Telekinetic" (listed as a feat-level ability alongside Fey Touched, Warcaster). Working doc Scene 3: "Daz uses Telekinesis to snatch it from his grasp" but the bracket note clarifies "Telekinetic's *mage hand*, at range." The Telekinesis spell is not listed on Daz's sheet.
**Suggested fix:** The mechanic used was the **Telekinetic feat's bonus-action mage hand shove**, not the 5th-level Telekinesis spell. Update all references from "Telekinesis (5th level)" to "Telekinetic feat (mage hand)." The DC 17 strength save check is consistent with the feat's mechanics (Spell Save DC). This distinction matters for future sessions because it means Daz did not expend a spell slot.

---

## 8. Grygum's Tasha's Caustic Brew Damage — Inconsistency Between Summary and Scenes

**Location:** Summary ("one died instantly as the corrosive brew melted through him (8 damage on top of Thorin's previous blows)") vs. Scenes → Confrontation ("one raider takes 8 acid damage at the start of his turn and dies instantly")
**Issue:** The Summary says the 8 damage came "on top of Thorin's previous blows" (implying Thorin already reduced the thug's HP before Grygum finished him). The Scenes section describes the 8 acid damage as occurring "at the start of his turn" — i.e., the ongoing acid damage from a prior round, not direct damage from the spell. These are consistent with each other (the acid from a previous cast of Tasha's ticking at the start of the thug's turn), but the Summary's phrasing is ambiguous enough that it could be misread as Grygum dealing 8 direct damage this turn.
**Evidence:** Tasha's Caustic Brew deals ongoing acid damage at the start of the target's turn on a failed save. The NPC entry for Zhentarim Raiders confirms: "one died instantly when the acid dealt 8 damage at the start of his turn (on top of Thorin's prior damage)."
**Suggested fix:** Minor phrasing cleanup in the Summary: "one died as the ongoing acid ate through him (8 damage at the start of his turn, on top of Thorin's prior strikes)" to make the sequence unambiguous.

---

## 9. Daz's Passive Investigation — Described as 24; Verify Against Sheet

**Location:** Memorable Moments → "Sherlock Daz," Scenes → The Path to the High Tower
**Issue:** The recap states Daz's Passive Investigation is 24, which the DM rules makes him "basically Sherlock Holmes." Daz's party.md does not list a Passive Investigation score explicitly. At Wizard 8/9 with INT as primary stat, a Passive Investigation of 24 would require INT modifier +7 and Expertise in Investigation, or +6 INT and Expertise — unusually high. This is plausible for a high-INT Evoker but should be verified.
**Evidence:** party.md lists Daz's items and abilities but does not state ability scores or Passive Investigation. The Dustsight Spectacles (attuned) may contribute. No contradiction can be confirmed without the full character sheet.
**Suggested fix:** Flag for verification against the full character sheet. If correct, no change needed. If the score is lower, the "Sherlock Holmes" deduction scene may need re-narrating.

---

## 10. "Guiding Bolt" — Correct Spell for Grygum, But Description Says "Deflected by Mage Armor"

**Location:** Memorable Moments → "The Wizard's Defense," Scenes → Confrontation
**Issue:** The recap states Grygum's Guiding Bolt "missed" because A'lai has Mage Armor. Mage Armor sets AC — it doesn't deflect spells; a spell attack roll simply fails to meet AC. This is mechanically correct but the narrative phrasing ("magical defenses deflected it entirely") in the Summary implies a different mechanic (like a Shield spell or Counterspell) rather than a miss. The Scenes section correctly identifies it as an attack roll that failed to meet AC.
**Evidence:** Summary: "A'lai Aivenmore's magical defenses deflected it entirely." Scenes: "A'lai's mage armor deflects the attack" (accurate mechanically).
**Suggested fix:** Update the Summary's phrasing from "deflected it entirely" to "fell short of the wizard's mage-armored defenses" or similar, to avoid implying a reactive spell was used.

---

## 11. Moziqodo — Identity and Relationship to Sylvira

**Location:** NPCs → Moziqodo, NPCs → Tadric ("Sylvira about her son's death"), Summary
**Issue:** The recap describes Moziqodo as "the terrifying abyssal spawn son of Sylvira." The entity registry describes him as "The Beast of Candlekeep"; Sylvira's abyssal plague entry in the registry notes it was "given to her by her son." The working doc and campaign state confirm he is Sylvira's demonspawn son. This is consistent. **(No error.)**

However: the recap's NPCs section for Moziqodo includes the line "He was slain by the party in the north gallery rotunda." The stale-docs issue report notes this happened in **Chapter 62** (or the chapter the stale docs mislabel as 62). If this recap is correctly labeled Chapter 60, Moziqodo's death cannot be described here — it would need to be in a different chapter's recap. This circles back to **Issue #1** (session numbering).
**Suggested fix:** Resolve the chapter numbering issue (Issue #1) first. If Chapter 60 is correct, the north gallery events must have also occurred this session — which means this session covered a great deal of ground. Verify against the VTT.

---

## 12. Thorin's Menacing Attack — Target Named Inconsistently

**Location:** Summary ("Thorin engaged the Zhentarim thugs directly, striking one with Dawnbringer and using Menacing Attack"), Scenes → Confrontation (same)
**Issue:** No contradiction — the Menacing Attack is a Battle Master maneuver, which is consistent with Thorin's Fighter 8 (Battle Master) build per party.md. The thug resisting is consistent with the DC 16 Wisdom save listed. **(No error.)**

---

## 13. Grygum "Cast Bless" — Number of Targets

**Location:** Scenes → The Path to the High Tower ("Grygum casts Bless on the three party members who are present")
**Issue:** The recap says Grygum cast Bless on "three party members who are present." Bless (1st level) targets up to 3 creatures, which is consistent. However, the party at this point includes Daz, Zalthir, Thorin, Grygum, Tadric, and Glabbagool. If Grygum is one of the three targets, the remaining two would be two of the other PCs. The recap doesn't specify which three, which could matter for future sessions (concentration, who had the bonus, etc.).
**Evidence:** Memorable Moments → "The Wizard's Defense": "Grygum's subsequent roll with Bless yields a 1 on the d4" — confirming Grygum himself was under Bless (or that Bless had been cast; the d4 applies to attack rolls and saving throws for *blessed* targets). The three targets are unspecified.
**Suggested fix:** Clarify which three party members received Bless. Minor but useful for continuity.

---

## 14. The Sapphire — "Instant Summons" Component vs. "Stolen from Janussi's Safe"

**Location:** Items → Sapphire Artifact
**Issue:** The recap describes the sapphire as "A magical gem held by A'lai Aivenmore, which he produced and threatened to smash to trigger a specific effect." The recap adds: "The DM notes they don't know what smashing it would do — 'For all we know, it summons an elemental to kill us all.'" The working doc (`20260727_candlekeep_the_man_with_the_metal_hand.md`) is explicit that the sapphire is **Janussi's missing safe-stone**, a component of *instant summons* attuned to Manshoon, and that smashing it signals Manshoon. The recap's NPC section on A'lai also omits the sapphire's identity as the third pillar of the Threefold Proof.
**Evidence:** Working doc Scene 3: "It is | Worth | A 1,000 gp sapphire | The material component for instant summons. | ⭐ The third pillar of the Threefold Proof | It is the single stone missing from Janussi's blasted safe." Carry-forward table: "The sapphire is Janussi's missing safe-stone; taken from A'lai's hand before four deputised Watchers. Kalan has been shown it. The Threefold Proof is complete."
**Suggested fix:** If Kalan was shown the sapphire this session and recognized it as the third pillar of the Threefold Proof, this is a major plot beat that the recap omits entirely. Verify against the VTT whether the Kalan/sapphire/Threefold Proof exchange occurred this session. If it did, add it. If it's planned for a future session, note that in the carry-forward rather than leaving it unmentioned.

---

## 15. Party Level — Recap Assumes Level 9; Party.md Says Level 8

**Location:** Scenes → Confrontation ("Daz casts Maximilian's Earthen Grasp (2nd level)"), general
**Issue:** The stale-docs issue report explicitly flags that party.md lists all four PCs at **level 8**, but the party milestoned to **level 9** at the end of Chapter 62. The working doc header states "Level 9 as of this session." If the High Tower session is post-level-up, the characters' capabilities should reflect level 9, but no level-up events are described in the recap.
**Evidence:** Stale-docs report: "⭐ The party milestoned to 9 at the end of Ch.62." Working doc (resume): "Daz | Level 9 as of this session." party.md: "Zalthir — Monk 8 / Thorin — Fighter 8 / Grygum — Cleric 8 / Daz — Wizard 8."
**Suggested fix:** If the milestone happened at the *end* of Chapter 62 (the session before this one), the recap's session should reflect Level 9 characters. If the milestone happens at the end of *this* session, it should be noted in the carry-forward. Either way, the party.md needs updating to Level 9 before the next session prep.

---

## Summary of Issues by Severity

| Severity | Issue |
|---|---|
| **Critical** | Session numbering mismatch (#1); Telekinesis vs. Telekinetic feat (#7); Zalthir unconscious sequence contradiction (#5) |
| **High** | Grygum/Daz history roll attribution contradiction (#4); Sapphire identity/Threefold Proof beat omitted (#14); Party level (#15) |
| **Medium** | Bookwyrm status and title (#1b, #2); Fembris current status omitted (#3); Tasha's Brew damage sequence ambiguity (#8) |
| **Low** | Guiding Bolt narrative phrasing (#10); Bless targets unspecified (#13); Passive Investigation score unverified (#9) |