# Consistency Report — Session 2026-08-02 Recap

---

## 1. Droop's clan: "Sawplee" vs. "Scraptops"

- **Location**: Scenes → *Bluffing the Bugbears*; NPCs → *Droop*
- **Issue**: The recap identifies Droop as "a member of Sawplee, a Goblin clan" / "a miserable goblin of the Sawplee clan." Canon marks Droop and the Sawplee Goblins as **confirmed distinct entities**.
- **Evidence**: **AUTHORITATIVE CANON** (NPCs): *"**Droop** — Goblin of the **Scraptops** clan, bullied by the bugbears in the guard barrack; wants only to go home. [ch2]"* Canon also registers **Scraptops** as its own faction: *"Goblin clan known for scavenging and tinkering; Droop is a member repairing a wagon back home."* Separately, **Sawplee Goblins** is a distinct faction — Ruxithid's psionic obelisk-shard goblins [intro, ch1, ch5, ch6], the ones with elongated skulls. `redbrand_hideout.md` also has it right: *"He's a Scraptop goblin (scavenger/tinkerer clan, not Cragmaw)."* Note that `vtt_transcription_corrections.md` contains a **wrong** correction row — `Scrap Tops` → `Sawplee` (session 8) — which is almost certainly the origin of this error. Canon overrides that generated correction row.
- **Suggested fix**: Change to "the **Scraptops** clan" everywhere. Also flag the `Scrap Tops → Sawplee` row in `notes/vtt_transcription_corrections.md` for removal/reversal — it is actively corrupting a canon distinction and will re-corrupt future transcripts. Conflating Droop with the Sawplee goblins mis-links him to the obelisk plot, which is a downstream lore error, not a cosmetic one.

---

## 2. Thundertree shop type: "alchemy shop" vs. herbalist shop

- **Location**: Summary; Scenes → *Liberating the Dendrars*; Locations → *Thundertree*; NPCs → *Mirna Dendrar*; Items → *Emerald Necklace*
- **Issue**: The recap consistently says "her family's old **alchemy shop**."
- **Evidence**: **AUTHORITATIVE CANON** (NPCs): *"**Mirna Dendrar** — Family once ran Thundertree's **herbalist** shop."* `world_state.md` splits the difference: *"the Dendrars' old **herb-and-alchemy** shop."* `redbrand_hideout.md` also: *"her family's old **herb and alchemy** shop."*
- **Suggested fix**: Use "herb and alchemy shop" or "herbalist shop." Low-severity, but worth normalizing before Thundertree is actually visited.

---

## 3. Nosk's quoted line was altered between drafts

- **Location**: Summary; Scenes → *Bluffing the Bugbears*; NPCs → *Nosk*; Memorable Moments
- **Issue**: The recap quotes Nosk as *"It don't matter that **now you know**, because now I kill you."* The `gm-assist.md` source for this same session renders it *"It don't matter that you know, because now I kill you."*
- **Evidence**: `gm-assist.md` (same-session export), Summary section, verbatim.
- **Suggested fix**: This is a quoted line reproduced four times in the recap. Verify against the VTT before it becomes a fixed campaign quotation. Flagged as an accuracy risk, not a confirmed error.

---

## 4. "Sister Maela physically grappled / tackled" — inconsistent mechanic

- **Location**: Summary; Scenes → *A Fiery Escape*; Memorable Moments
- **Issue**: The recap says Maela **grappled** Veyra after a failed Persuasion; `gm-assist.md` for the same session says she **tackled** / "was forced to physically restrain." These are different mechanical actions.
- **Evidence**: `gm-assist.md`: *"Sister Maela physically **tackled** and restrained a distraught Veyra."* Recap: *"a persuasion attempt by Sister Maela fails to talk her down, so Sister Maela **grapples** her."*
- **Suggested fix**: Pick one and use it consistently. The recap's grapple-after-failed-Persuasion version is more specific and more likely correct; if so, correct the gm-assist export rather than the recap.

---

## 5. Sildar's bounty numbers appear only in one draft

- **Location**: Scenes → *A Hero's Reward and a New Bounty*
- **Issue**: The recap states the Iarno bounty as "**200 gold if brought back alive, 100 if dead, and 50 if he cannot be raised from the dead**." The Summary section, by contrast, gives no figures at all and only says Sildar "offered a new bounty."
- **Evidence**: `gm-assist.md` confirms the same three-tier figures, so this is internally corroborated. But no grounding doc records it — `campaign_state.md` and `world_state.md` predate the session.
- **Suggested fix**: No error found; flagged only so the three-tier bounty gets promoted into `campaign_state.md` as an active quest with explicit numbers. "50 if he cannot be raised from the dead" is an unusual clause and will confuse a future GM if it isn't written down verbatim somewhere authoritative.

---

## 6. "Three potions of healing" from the chest vs. one

- **Location**: Summary; Items → *Potion of Healing*
- **Issue**: The Summary says the chest yielded "**three potions of healing**, climbing and growth." The Items entry says "**One** was recovered from the hidden chest in the crevasse alongside the potions of climbing and growth." These contradict each other within the same document.
- **Evidence**: `world_state.md`, "Not yet recovered (all at the bottom of the crevasse)": *"**The nothic's hoard** — 160 sp, 120 gp, five malachite gems, potions of healing / climbing / growth."* `redbrand_hideout.md` is explicit and singular: *"a **potion of healing**, a potion of climbing, a potion of growth."*
- **Suggested fix**: **One** potion of healing, one of climbing, one of growth. The Summary's "three potions of healing, climbing and growth" is a parsing artifact (three potions total, one of each) that reads as three healing potions. Rewrite as "three potions — healing, climbing, and growth." This matters: Zenvon drinks one during the bugbear fight, and Garaele's reward is separately three potions of healing, so the party's healing-potion count is about to get badly muddled.

---

## 7. Nosk described as "a bugbear stationed in the barracks"

- **Location**: NPCs → *Nosk*
- **Issue**: The NPC entry demotes Nosk to "a bugbear stationed in the barracks." The Summary correctly calls him "the lead bugbear."
- **Evidence**: **AUTHORITATIVE CANON** (NPCs): *"**Nosk** — Bugbear **leader** of the group the Spider sent to reinforce the Redbrands; carries a **key to the hideout**."*
- **Suggested fix**: "Bugbear leader of the group the Black Spider sent to reinforce the Redbrands." Also note the recap never mentions **Nosk's iron key**, which per canon and `everyone_is_a_suspect.md` "locks and unlocks every door in the hideout" — if the party killed or fled Nosk without taking it, that should be recorded explicitly, because the prep doc flagged it as the material prize of the encounter.

---

## 8. Thel's remains and unicorn pendant not accounted for

- **Location**: Scenes → *The Crevasse and the Hidden Chest*; NPCs → *Mirna Dendrar*
- **Issue**: Zenvon descends into the crevasse and finds the chest, but the recap never records whether the party found **Thel Dendrar's skeleton** or his **carved unicorn-head pendant** — both of which are at the bottom of that same crevasse per canon and prep. The recap has Mirna asking the party to "bring Thel's body back if they ever could" *before* the descent, and then says nothing about the body after the descent.
- **Evidence**: **AUTHORITATIVE CANON** (NPCs): *"**Thel Dendrar** — Local woodcarver murdered by the Redbrands...; **his skeleton lies in the crevasse cave**."* `world_state.md`, not-yet-recovered list: *"**Thel Dendrar's remains** and his carved **unicorn-head pendant** — the only answer Mirna is going to ask for."* `everyone_is_a_suspect.md` names this as must-hit #2.
- **Suggested fix**: Add an explicit line stating what happened — either "the party did not search for or find Thel's remains" or a record of the recovery. Leaving it silent means a future session cannot tell whether Mirna's question is still open. This is the highest-value ambiguity in the document.

---

## 9. Two dead psionic goblins in the crevasse — location claim

- **Location**: Summary (Revelations paragraph); Scenes → *Revelations and Rest in Phandalin*
- **Issue**: The recap refers to "the mutated goblins **in the crevasse**" as something the party connects. But per campaign records, the elongated-skull goblin corpses the party actually *found* were discovered in **Ch. 6, in the hideout caverns**, via Veyra's Investigation — not in the crevasse this session. The recap does not record the party descending to the crevasse floor and seeing goblin corpses.
- **Evidence**: `world_state.md`: *"Two dead goblins with **elongated skulls** in filthy rags were found **in the hideout caverns in Ch. 6** *(transcript-confirmed; not in the Ch. 6 session summary)*."* `party.md`: Veyra *"rolled the Investigation that found the **dead goblins with elongated skulls** in the caverns."* Separately, `redbrand_hideout.md` places two such corpses under the southern bridge at the crevasse bottom. It is possible both are true (module has them at the crevasse bottom; the party found them in Ch. 6 in the caverns) — but the recap asserts crevasse without establishing that the party saw them there this session.
- **Suggested fix**: Change to "the mutated goblins they found in the caverns" or clarify whether Zenvon saw additional corpses at the crevasse floor during his descent. As written, a future GM cannot tell whether the party has now seen two sets of corpses or one.

---

## 10. "an unexplored door leading up and out the front of the building"

- **Location**: Summary; Scenes → *Escape from Tresendar Manor*; Locations → *Tresendar Manor*
- **Issue**: The recap presents this as a newly used, previously unexplored exit. Prior campaign records establish the party's known routes as (a) the forest tunnel ~100 ft from the manor and (b) the cellar stairs to an upper landing.
- **Evidence**: `world_state.md`: *"**Cellar** — Kegs, barrels, stone cistern, **stairs to an upper landing**."* The manor is described as the "front door" entry route in `redbrand_hideout.md` (Entry B), so an exit through the manor ruins is consistent with the module — but calling it "unexplored" conflicts with the cellar stairs already being mapped.
- **Suggested fix**: Minor. Either drop "unexplored" or specify it as the manor-ruins front exit above the cellar stairs. Flagged because "an unexplored door" implies a new map feature that may not exist.

---

## 11. Halia's motive gloss: "protecting local trade"

- **Location**: NPCs → *Halia Thornton*
- **Issue**: The NPC entry ends with *"She claims her interest is protecting local trade and business from disruption"* — presented flatly. Elsewhere the recap correctly frames this as a claim she made. The NPC dossier is the doc a future GM reads fastest, and it does not record that she is a **Zhentarim agent** whose stated motive is a cover.
- **Evidence**: **AUTHORITATIVE CANON** (Factions): *"**Zhentarim** — Faction **Halia Thornton recruits characters into**."* `everyone_is_a_suspect.md` (GM-only): *"Halia is an agent of the **Zhentarim**... She wants Glasstaff removed **so she can take the Redbrands over herself**."* `world_state.md` lists her as **Ambiguous**, actively suspicious.
- **Suggested fix**: Append a GM-facing note to the Halia entry — that the trade-protection line is a cover, that the party's suspicion is warranted, and that she is not Glasstaff's handler. Without it, a future session risks either treating her as benign or wrongly promoting her to "the boss in town."

---

## 12. Sildar's total reward: 250 vs. 200

- **Location**: Scenes → *A Hero's Reward and a New Bounty*
- **Issue**: The recap states "**250 total** for eliminating the Redbrand threat, with 100 paid up front" and a remaining 150 gp.
- **Evidence**: `everyone_is_a_suspect.md` and `redbrand_hideout.md` both cite the module figure: *"**Sildar pays 200 gp** for eliminating the Redbrand threat."* Meanwhile `campaign_state.md` records the prior payments as *"**50 gp** paid, **100 gp** negotiated upfront"* — i.e. 150 gp already paid, of which only the 100 gp was an advance against the Redbrand job. `party.md`: *"150 gp paid so far."*
- **Suggested fix**: Reconcile. If the table used 250 as the negotiated total (100 advance + 150 balance), record that explicitly as a **table deviation from the module's 200 gp** so the discrepancy doesn't get "corrected" later. If the intended figure was the module's 200, the balance owed was 100, not 150.

---

## 13. Thunderwave attributed to Zenvon, then to Veyra

- **Location**: Summary and Scenes → *The Bugbear Barracks Brawl* attribute *Thunderwave* to **Zenvon**; Spells → *Thunderwave* attributes it to **Veyra**
- **Issue**: Direct internal contradiction on who cast the spell that opened the fight.
- **Evidence**: Recap Summary: *"**Zenvon** cast *Thunderwave*."* Recap Scenes: *"**Zenvon** opens with *Thunderwave* (spell save DC 12)."* Recap Spells section: *"**Veyra's** evocation (spell save DC 12, 2d8 thunder damage)... Cast to open the bugbear brawl."* Mechanically, Zenvon is a **Rogue (Arcane Trickster)** — canon and `party.md` confirm halfling rogue — and an Arcane Trickster gains **no leveled spell slots and no evocation spells at 3rd level**; *Thunderwave* is not on the Arcane Trickster list at all. `world_state.md` lists Veyra's known spells as *Firebolt* and *Magic Missile*, with no *Thunderwave*.
- **Suggested fix**: **This is the most serious mechanical error in the document.** Zenvon cannot cast *Thunderwave*. Attribute it to Veyra throughout and reconcile with her spell list — either *Thunderwave* was added at her level-3 bump (in which case update `characters/` and `world_state.md`), or the spell was something else. Note also that `everyone_is_a_suspect.md` states Veyra's level-3 progression grants **no new spells**, only the Candlelight Reading feature, which makes a newly-acquired *Thunderwave* itself questionable. Resolve at the table before this propagates.

---

## 14. Party level inversion not flagged

- **Location**: Scenes → *Third Level*
- **Issue**: The recap states the whole party — Zenvon, Veyra, Maela, Pip — reaches 3rd level together, with no note that this resolves a documented rules conflict.
- **Evidence**: `world_state.md` (Campaign Mechanics Notes): *"`characters/sidekick_progressions.md` states sidekick level **always equals Zenvon's**."* `everyone_is_a_suspect.md` open decisions: *"Three DM-run companions now outlevel the sole PC... Confirm that's the intent, or say the file's rule is retired."* The prep doc anticipated sidekicks at 3 while Zenvon remained at 2.
- **Suggested fix**: If Zenvon also reached 3 (as the recap says), the inversion never happened and the open decision in `everyone_is_a_suspect.md` should be closed. Add an explicit line: "Zenvon also advanced to 3rd level; sidekick parity maintained." Otherwise a future GM reading the prep doc will assume an unresolved inversion.

---

## 15. Nothic damage / oil-fire figures unverifiable but internally consistent

- **Location**: Scenes → *A Fiery Escape*; Items → *Oil Flasks*
- **Issue**: "Seven pounds of oil," "five points of damage per round," "killed one bugbear outright," "burned for two rounds," "three rounds to break the locked door" — none appear in any grounding doc.
- **Evidence**: These are session-native mechanical rulings; no context document contradicts them. `gm-assist.md` corroborates the narrative shape but omits the numbers.
- **Suggested fix**: No error found. Flagged only because "seven pounds of oil" is an unusual unit (oil flasks are normally counted, not weighed) and "killed one bugbear outright" changes the surviving-bugbear count. Record how many bugbears remain alive behind that door — currently the recap says four bugbears fought, one died to fire, but the NPC and Locations sections still say "four bugbears" without correction.

---

## 16. "Una" — approved name not yet in registry

- **Location**: Not in the recap
- **Issue**: `vtt_known_additions.md` records that a name **Una** was GM-approved in session 008 (this session, 2026-08-02) for the cue "According to Una/Yola," but Una appears nowhere in the recap.
- **Evidence**: `vtt_known_additions.md`: *"**Una** — Name approved in session 008 as the canonical for the cue 'According to Una/Yola'; not yet in `docs/entity_registry.yaml`."* The correction table also carries `Yola` → **Una** (session 8).
- **Suggested fix**: Either the Una reference was cut from the recap (in which case note why), or it was silently dropped. Confirm what "According to Una" referred to and whether it belongs in this session's record. An approved-but-unrecorded NPC name is exactly the kind of thing that vanishes.

---

## Items verified as correct (no action needed)

- **Talon** as a *+1 longsword* belonging to **Aldith Tresendar**, found in **Ssarnak's** crevasse hoard, party unaware of its name — matches canon exactly. The explicit "party made no History check" note is good practice.
- **Ssarnak** spelling (double S) — matches canon; the correction table's `Sarnak → Ssarnak` row is correctly applied.
- **Nars (13)** and **Nilsa (18)** ages and parentage — match canon.
- **Bowgentle**, **Agatha**, **Tsernoth**, **Conyberry** — all match canon, including the forward-looking note that Agatha traded the spellbook to Tsernoth over a century ago.
- **Tymora** as goddess of luck at the Shrine of Luck — matches canon (note: the Scenes section quotes the read-aloud as "the **god** of luck" and the Locations section says "**goddess**"; canon says goddess. Minor, and the Scenes version is flagged as a quotation, so acceptable).
- **Sildar Hallwinter** as Lords' Alliance — correct; the recap correctly uses the possessive **Lords'**, matching the correction table's session-8 fix.
- **Dendrar** spelling throughout, and **Thel** — correct per canon; no "Dendar" garbles survive.
- **Pip Thistlewick** — correctly the human fighter sidekick, not the module's renamed **Tuck Stonehill**. No collision.
- **Cragmaw Castle** as the Black Spider's reported location, revealed by bugbears — matches canon (*"bugbears in the Redbrands' hideout know its location"*).
- **Orryn Voss** as Veyra's mentor — correct spelling and relationship per canon.
- **Miner's Exchange** under the **Lionshield Coster** — consistent with canon's Phandalin geography; Halia as Guildmaster is correct.