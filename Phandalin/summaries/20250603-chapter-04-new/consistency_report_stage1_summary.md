# Consistency Report — "New Chapter 4" (2025-06-03 session recap)

**Documents checked against:** archived session record `session_2025_06_03_new_chapter_4.md` (same session, previously reviewed), `chapter_03_to_find_a_shapeshifter.md` (immediately-following narrative), `campaign_state.md`, `world_state.md`, `party.md`, and the entity registry (treated as authoritative canon).

**Name spot-check vs. canon registry:** Toblen Stonehill, Harbin Wester, Linene, Dazlyn, Norbus, Lord Neverember, Gnomengarde, Neverwinter Wood, Lionshield Coster, Townmaster's Hall, Stonehill Inn — all match canon spellings. No canon-divergent names found. End-state also verified: the mountain-pass ogre left prone/halted with Valphine next to act matches the opening of `chapter_03` (she opens with a mace swing; the ogre later flees and is killed by Vukradin, yielding whistle/coins/key per campaign_state's "second ogre" entry).

---

## High severity

**1. Missing placement note — chapter-number collision**
- **Location:** Header ("New Chapter 4")
- **Issue:** The archived copy of this session carries a 2026-08-19 placement note: chronologically this session runs *immediately before* `chapter_03_to_find_a_shapeshifter.md`, and the "Chapter 4" label collides with the existing, unrelated `chapter_04_the_bard_the_kings_and_the_carver.md`. This new recap drops that note and re-presents itself as "New Chapter 4," reintroducing the collision.
- **Evidence:** Placement note in `session_2025_06_03_new_chapter_4.md`; `chapter_03` opens on this session's prone-ogre cliffhanger.
- **Suggested fix:** Carry the placement note verbatim; leave chapter number unassigned until the GM rules.

**2. Ice Knife: "all four remaining orcs" is wrong — only two orcs remained**
- **Location:** Summary, Scenes (A Clash of Ideals and Orcs), Spells (Ice Knife)
- **Issue:** The recap says the exploding shards caught "all four remaining orcs," who all saved. But by the recap's own sequence, orc two (Brewbarry's AoO) and orc one (Soma's Poison Spray) are already dead at that point — and Brewbarry then "finished the last two orcs." Four remaining is internally impossible.
- **Evidence:** Archived session record: "both surviving orcs make their saves." Recap's own kill order confirms two survivors.
- **Suggested fix:** "both remaining orcs (three and four) succeeded on their saves; Valphine failed hers."

**3. The whistling-ogre critical hit — contradictory attribution and value**
- **Location:** Summary, Scenes (The Whistling Ogre), Items (Halberd)
- **Issue:** Three incompatible versions: (a) Summary — a crit "alone shaved fifteen points off the creature's health"; (b) Items — Brewbarry's crit "dealt nineteen points of base damage, halving the ogre's remaining health"; (c) Scenes — the crit belongs to *the ogre*, against Brewbarry, with no Brewbarry crit mentioned at all.
- **Evidence:** Archived session record: "Brewbarry catches the ogre with an attack of opportunity as it closes, landing a critical hit that takes it from full health to less than half" — the crit is Brewbarry's, on an opportunity attack.
- **Suggested fix:** Verify damage number against the transcript; align all three sections on Brewbarry's AoO crit (one number), and either delete or separately attest the ogre-crits-Brewbarry event.

**4. The gem subplot at the excavation is unattested**
- **Location:** Summary, Memorable Moments, Scenes (Return to the Excavation Site), Locations, NPCs (Dazlyn)
- **Issue:** The recap adds a substantial new beat: Dazlyn and Norbus hiding, "weighing their options about the gem they knew the party was carrying," opening with "You're not here for the gem, right?" No context document establishes that the party carries a gem — campaign_state marks the Hall of Greed (E11, the glowing green gem room) as **NOT FOUND IN SUMMARIES**, and the archived record of this same session says only that the dwarves "welcome the party back… relieved to see them alive." If this enters grounding docs unverified it creates a phantom party asset and a phantom dwarf motive.
- **Evidence:** Archived session record (no gem, no hiding); campaign_state "Dwarven Excavation sub-encounters… Hall of Greed trap NOT FOUND IN SUMMARIES"; registry E11 note.
- **Suggested fix:** Verify the entire hiding/gem beat and the Dazlyn quote against the VTT transcript before accepting; otherwise revert to the archived version of the scene.

## Medium severity

**5. Dazlyn gendered "she" — unverified**
- **Location:** NPCs (Dazlyn)
- **Issue:** "she would have preferred a popular local tune." No context document genders Dazlyn; the canon registry note ("Shield dwarf prospector… forthright and honest to a fault") is silent, and the archived record deliberately avoids pronouns.
- **Evidence:** Canon registry (no gender); archived session record (no pronoun).
- **Suggested fix:** Check the transcript / module dossier; if unconfirmed, rewrite pronoun-free.

**6. Sacred Flame — three related problems**
- **Location:** Scenes (A Clash / Whistling Ogre), Spells (Sacred Flame)
- **Issue:** (a) Damage dealt on *successful* saves twice ("the orc makes its save, taking only one point"; "the ogre makes its save, taking four points") — Sacred Flame deals nothing on a success; either the saves failed or the damage is wrong. (b) "used again against the whistling ogre while it was incapacitated" — the whistling ogre was never incapacitated; the prone/halted ogre is the mountain-pass one. (c) "Also attempted against the second ogre in the mountain pass; the ogre's save result was not resolved before the session ended" — contradicts the recap's own end-state (Soma's Poison Spray was the last action; Valphine acts next when play resumes) and `chapter_03`, where Valphine's first action is a mace swing, not a pending Sacred Flame.
- **Evidence:** Recap's own mountain-pass scene; `chapter_03` §03.01; archived record shares error (b), so the transcript is the tiebreaker.
- **Suggested fix:** Re-derive Sacred Flame events from the tape; delete the "unresolved save" claim.

**7. Command duration contradicts itself**
- **Location:** Scenes (Ambush in the Mountain Pass) vs. Spells (Command)
- **Issue:** Scenes: halted "until the end of its next turn." Spells: "expires at the start of the ogre's next turn."
- **Evidence:** Internal contradiction; `chapter_03` shows the ogre standing and attacking on its next turn, favoring the shorter reading.
- **Suggested fix:** Standardize on Command's actual effect (the target loses its next turn's movement/actions), matching chapter_03.

**8. Brewbarry's 14-damage strike — broken parenthetical**
- **Location:** Scenes (Ambush in the Mountain Pass)
- **Issue:** "(seven base plus +2 rage bonus, doubled for the prone-condition advantage)" — advantage from prone doesn't double damage, and the arithmetic gives 18, not 14.
- **Evidence:** Internal math; 5e rules.
- **Suggested fix:** Keep the 14 total, drop the derivation or replace with the actual roll from the tape.

**9. Campaign_state conflicts with both session records on the first ogre (flag the other document)**
- **Location:** Scenes (The Whistling Ogre) / NPCs (Whistling Ogre) — cross-document
- **Issue:** Both session records place the whistling ogre **between the excavation and Phandalin**; campaign_state files it as "Frozen Ogre Encounter (en route to Gnomengarde, first ogre)" — wrong route and an unexplained "Frozen" label. Per the trust hierarchy, session records are authoritative here; the recap is *not* the error. Campaign_state also credits Soma specifically with retrieving the "magical bullets," which the recap leaves generic.
- **Evidence:** Recap + archived record vs. campaign_state Completed Encounters.
- **Suggested fix:** Correct campaign_state's location/label; confirm the Soma-retrieval detail on tape.

**10. Leftover editorial meta-text in the Flute item entry**
- **Location:** Items (Flute, and cross-reference in Clarinet)
- **Issue:** "The distinction matters: the recap's scene description says 'clarinet' for this performance, but the transcript is clear…" — the recap's scene actually says *flute*, so this note describes a defect that isn't present, and it embeds pipeline commentary ("the transcript is clear") in a canon-facing document.
- **Evidence:** Recap Scenes: "Vukradin plays flute for the assembled group"; archived record agrees (flute at the excavation, clarinet at the inn).
- **Suggested fix:** Delete the meta-sentence; keep the flute/clarinet split as plain fact.

## Low severity

**11. Vukradin healed for 11 HP but is "back on nine hit points"** — Scenes; no intervening damage. Reconcile (likely "eleven").

**12. Death-save placement drifts** — Scenes has him failing his first death save after the *first* knockout (pre–Healing Word); Summary says he "failed a death save on the ground" during the *second* down. Pick one per the tape.

**13. Two long rests** — the orc-fight scene ends with "a long rest… resetting all hit points," and the excavation scene then has "their long rest here." One rest, one placement (archived record puts recovery at the excavation).

**14. Thorn Whip damage breakdown inconsistent** — Scenes: "1d6 fall damage (six points total)"; Spells: 1d6 thorn (six) *plus* 1d6 fall. Reconcile.

**15. Poison Spray mechanics muddle** — described as "no saving throw involved" (2024-rules attack cantrip, consistent with Starry Wisp being in play), yet the two ogre scenes justify it via "poor dexterity" and "poor constitution for resisting poison" respectively. Harmonize the rationale.

**16. "You killed my brother and sister" vs. archived "his brother"** — the two records disagree on the quote (and only one prior ogre was killed). Verify wording on tape before it becomes a canonical quote.

**17. Mold Earth scene attribution** — this recap puts the rockslide idea in the mountain-pass fight; the archived record's Scenes put it in the whistling-ogre fight while its own Spells section says mountain pass. The recap's placement is plausibly the deliberate resolution, but confirm once against the transcript.

**18. Innkeeper warning attribution** — "warned by the innkeeper at the Stonehill Inn / told by Toblen Stonehill that orc tribes were descending" appears in no other record of this or prior sessions. Registry canon frames the orcs as driven from their territory by Cryovain ("When Orcs Attack"). Verify the Toblen warning happened before letting it stand.

**19. Table-layer anachronisms in canon-facing prose** — "shared party ledger… dedicated 'Is Blood Money' boolean column," "loot spreadsheet," "the DM pastes the full text into the chat," "the DM calls time at 10:30." Given this campaign's explicit de-anachronization convention (cf. the ch47/48 stage-3 practice), either mark these as table-record framing or rephrase in-world (e.g., "the party's ledger now carries a blood-money mark").

**20. Minor editorial gaps** — Items (Walloping Ammunition): "a DC saving throw" is missing its number (Scenes: DC 10 Strength). Summary "javelins" vs. Scenes "a javelin." Memorable Moments attributes "you killed your ally" to Dave while the Summary attributes it to "the table" — and "killed" overstates (Valphine was unconscious, and made her death save).

---

**Verified-clean highlights:** 50 gp reward from Harbin ✓; Gnomengarde + midwife (Adabra, per registry) quest pair ✓; hide armor sold for 10 gp full value ✓; Neverwinter Wood rumor wording ✓; Valphine's hand-crossbow acquisition this session is consistent with her wielding one at the top of `chapter_03` ✓; session end-state (ogre prone/halted, Valphine to act) dovetails exactly with `chapter_03` §03.01 and campaign_state's "second ogre fled, killed by Vukradin; whistle, coins, key looted" ✓.