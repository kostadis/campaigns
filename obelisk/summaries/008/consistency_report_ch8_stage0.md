# Consistency Report — Session 2026-08-02 (Chapter 8)

## Naming / Canon Spelling

**Location:** Summary, Scenes ("Liberating the Dendars"), Locations, NPCs, Items, throughout
**Issue:** The family name is consistently rendered **"Dendar"** — "Dendar family," "Mirna Dendar," "Nars Dendar," "Nilsa Dendar."
**Evidence:** AUTHORITATIVE CANON registers the family as **Dendrar family / the Dendrars — Thel, Mirna, Nars, and Nilsa Dendrar**, and explicitly notes that "Dendar" is a VTT ASR mishearing handled in `notes/vtt_transcription_corrections.md`, *not* an identity variant. `vtt_transcription_corrections.md` confirms: `Dendar, Dendra → **Dendrar**`. campaign_state and world_state both apply the same correction ("Names normalized … **Dendrar** (not 'Dendar')").
**Suggested fix:** Replace every instance of "Dendar" with "Dendrar" (family, Mirna, Nars, Nilsa, Thel).

---

**Location:** Summary, Scenes ("A Fiery Escape"), NPCs ("Sarnak"), Memorable Moments
**Issue:** The nothic is named **"Sarnak"**.
**Evidence:** AUTHORITATIVE CANON lists the nothic as **Ssarnak** ("Nothic guarding the Redbrands' crevasse cave in exchange for treasure and meat from Glasstaff; communicates via telepathy. [ch2]"). `vtt_transcription_corrections.md` adds an explicit session-8 row: `Sarnak → **Ssarnak**` ("module spells it with a double S"). world_state also uses "the nothic (Ssarnak)."
**Suggested fix:** Rename to **Ssarnak** throughout — NPC entry header, summary prose, scene beats, and the Memorable Moments attribution line.

---

**Location:** Summary, Scenes ("Revelations and Rest in Phandalin"), NPCs ("Toblin Stonehill"), Locations ("Stonehill Inn")
**Issue:** The innkeeper is named **"Toblin Stonehill."**
**Evidence:** AUTHORITATIVE CANON registers **Toblen Stonehill / Toblen**. `vtt_transcription_corrections.md` lists `Toblin, Hoblin, Talbot, Poglin → **Toblen**` and `Tobelin, Tublin → **Toblen**`. world_state and campaign_state both use "Toblen."
**Suggested fix:** **Toblen Stonehill** in all four places.

---

**Location:** NPCs ("Droop")
**Issue:** Droop is described as "a miserable goblin from the **Cragmaw clan**."
**Evidence:** AUTHORITATIVE CANON: "**Droop** — Goblin of the **Scraptops** clan, bullied by the bugbears in the guard barrack; wants only to go home. [ch2]" and "**Scraptops** — Goblin clan known for scavenging and tinkering; Droop is a member." Both prep docs (`redbrand_hideout.md`, `everyone_is_a_suspect.md`) stress he is "a Scraptop goblin (scavenger/tinkerer clan, **not Cragmaw**)." Note: `vtt_transcription_corrections.md` has a session-8 row `Scrap Tops → **Sawplee**` which contradicts canon — flag that row for review; canon says Scraptops.
**Suggested fix:** "A miserable goblin of the **Scraptops** clan." Also raise the erroneous `Scrap Tops → Sawplee` glossary row with the GM.

---

**Location:** NPCs ("Dosarok")
**Issue:** The Redbrand bandit is named **"Dosarok"** (one word).
**Evidence:** AUTHORITATIVE CANON: "**Dosa Rook** — Redbrand bandit killed by the party in the upper-cellar brawl beneath Tresendar Manor. Name confirmed on tape (GM: 'the bandit, whose name is Dosa Rook')." campaign_state and world_state both use "Dosa Rook."
**Suggested fix:** **Dosa Rook** (two words).

---

**Location:** Locations ("Shrine of Luck"), NPCs ("Sister Garaele")
**Issue:** Not an error, but flagging for spelling confirmation: the recap uses "Tymora" and "Garaele" correctly. No action needed.

---

## Wrong Character / Attribution

**Location:** Summary (paragraph 2) — "When she pressed for news of Thel, **Sister Maela** gently broke the truth to her"; Scenes ("Liberating the Dendars") — "Sister Maela gently breaks the news to Mirna that Thel's body was likely consumed by the creature in the crevasse."
**Issue:** Possibly correct, but flagged as unverifiable from context and mechanically odd: at this point in the timeline the party had **not yet been down the crevasse** (the descent happens later in this same session). Maela stating Thel "was likely consumed by the creature" is inference, not knowledge — and the recap presents it as "the truth."
**Evidence:** campaign_state (Open Threads): "**The crevasse floor.** Never searched. Holds … **Thel Dendrar's remains and his unicorn pendant** … *Last state:* the party has crossed the bridges twice and never looked down." The scene order in this recap has the crevasse descent *after* the Dendrar liberation.
**Suggested fix:** Soften to "Sister Maela told her what the party suspected — that Thel was dead and his body left below." Confirm with the GM whether Maela was the speaker.

---

**Location:** Summary (paragraph 3) — "**Veyra** conjured the convincing sound of Glasstaff working in his workshop"; Scenes ("The Crevasse and the Hidden Chest") — "**Veyra** uses a minor illusion to mimic the sound…"
**Issue:** Ability attribution unverifiable and possibly wrong. *Minor Illusion* is not listed among Veyra's known spells in any grounding doc.
**Evidence:** world_state party roster: "**Veyra** (of the Blue Candle) — Tiefling mage — Darkvision; ***Firebolt*, *Magic Missile***." party.md lists no cantrip beyond those. Additionally, world_state records "**Veyra ended Ch. 7 completely out of first-level slots**" — a cantrip would be fine, but *Minor Illusion* is not attested.
**Suggested fix:** Verify against Veyra's sheet. If she doesn't have *Minor Illusion*, either correct the spell name or reattribute the distraction. If the GM granted it, flag for the character sheet update.

---

**Location:** Summary (paragraph 4) and Items ("Magical Longsword")
**Issue:** The chest sword is called a generic "finely crafted **magical longsword**" and the Item entry gives it no name.
**Evidence:** AUTHORITATIVE CANON: "**Talon** — **+1 longsword** belonging to the slain knight **Aldith Tresendar**, found in the nothic **Ssarnak's** hoard in the crevasse. [ch2]" world_state and both prep docs describe it identically, with a silver-chased scabbard and bird-of-prey hilt, plus a DC 15 History check to recall Sir Aldith. Note also `vtt_transcription_corrections.md`'s standing warning about the `Talan`/`Talon` collision from session 9 onward — this is exactly the recap that introduces the sword.
**Suggested fix:** Name it **Talon (+1 longsword)** in the Items section and in the summary, and note whether the party made the History check to learn its provenance. If they did not identify it, say so explicitly rather than leaving it anonymous.

---

## Loot / Numbers

**Location:** Summary (paragraph 4), Scenes ("The Crevasse and the Hidden Chest"), Items
**Issue:** The chest contents are described as "a trove of silver and gold coins, five malachite gems, several magical potions, and a … longsword," and the Items section lists only a *Potion of Climbing* and a *Potion of Growth*.
**Evidence:** world_state ("Not yet recovered — all at the bottom of the crevasse"): "**The nothic's hoard** — **160 sp, 120 gp**, five malachite gems, potions of **healing / climbing / growth**." `redbrand_hideout.md` and `everyone_is_a_suspect.md` agree, and set the malachite value at **12 gp each** (which the recap's Items entry gets right).
**Suggested fix:** State the coin totals (160 sp, 120 gp) and add the **third potion — a *potion of healing*** — to the Items list, unless the GM ruled otherwise.

---

**Location:** Scenes ("A Hero's Reward and a New Bounty") — "Sildar … pays the party the **remaining 150 gold pieces**"; NPCs ("Sildar Hallwinter") — same figure.
**Issue:** The number conflicts with both the campaign state and the module reward.
**Evidence:** campaign_state NPC table: "Sildar Hallwinter — Ally / employer (**paid 150 gp so far**)" — i.e. 150 gp is what he had *already* paid (50 gp escort + 100 gp upfront), not what remains. `everyone_is_a_suspect.md`: "He pays the **200 gp** module reward for eliminating the Redbrand threat `(module)`." `redbrand_hideout.md`: "**Sildar pays 200 gp** for eliminating the Redbrand threat."
**Suggested fix:** Confirm the amount actually paid at the table. If it was the module reward, correct to **200 gp**; if the GM ruled 150, note explicitly that this is *in addition to* the 150 gp already paid, to avoid a future double-count.

---

**Location:** Scenes ("A Hero's Reward and a New Bounty")
**Issue:** "Sildar offers a new bounty … promising **200 gold if he is brought back alive**, **100 if dead**, and **50 if he cannot be raised from the dead.**" These figures appear in no context document, and the third tier ("cannot be raised from the dead") is mechanically ambiguous — is it a lower payment for a destroyed/unrecoverable body?
**Evidence:** No grounding doc records an Iarno-capture bounty. `everyone_is_a_suspect.md` records only that Sildar "wants Iarno **captured and transported to Neverwinter to face the judgment of a higher authority** `(module)`" — no gold figure attached.
**Suggested fix:** Verify the numbers against the recording. Rephrase the third tier unambiguously (e.g. "50 gp if only proof of death is recovered"). Flag as a new campaign_state entry once confirmed.

---

## Items / Inventory

**Location:** Items ("Oil Flasks") — "Several containers of flammable oil **from Zenvon's inventory**"; Summary and Scenes describe Zenvon pouring "flask after flask of oil."
**Issue:** Oil flasks are not attested anywhere in Zenvon's equipment.
**Evidence:** world_state "Zenvon — combat profile": "ornate short sword …, Scimitar (Nick mastery), Dagger, Javelin." party.md: "Scimitar (Nick), Dagger, Javelin, **handaxe**; thieves' tools …; a **whip**." No oil in either. Note also the standing table detail that "Kostadis (DM) does **not** enforce encumbrance," so this may simply be an unrecorded purchase.
**Suggested fix:** Confirm the flasks were on the sheet (or purchased). If so, add oil flasks and the tinderbox to Zenvon's equipment list in `party.md`.

---

**Location:** Items ("Tinderbox")
**Issue:** Same class of problem — the tinderbox is not recorded in any inventory doc. Lower severity (standard adventuring gear), but flagged for sheet consistency.
**Suggested fix:** Add to Zenvon's gear list if confirmed.

---

**Location:** Items ("Jeweled Gold Bracelet") and ("Waterproof Satchel")
**Issue:** Both entries describe events from **Chapter 7**, not this session. The bracelet was found in the crypts and the satchel in the cistern in the prior session.
**Evidence:** campaign_state, Completed Encounters: "**The Tresendar crypts (Ch. 6–7)** … *Consequence:* jeweled gold bracelet (140 gp)"; "**The cellar deception (Ch. 7)** … potion of healing and **potion of invisibility** recovered from the cistern." world_state timeline places both in Chapter 7.
**Suggested fix:** Either mark these as carried-over inventory rather than session finds, or remove them from this session's Items list to avoid a future reader dating them to 2026-08-02.

---

**Location:** Items ("Black Stone") — "found near a **black obelisk** at the very beginning of the party's adventure."
**Issue:** The obelisk framing is unattested and potentially a significant lore error. No grounding doc says Zenvon found his stone near an obelisk.
**Evidence:** world_state: "**The black stone** — Zenvon's, **pocketed on the road**. Undisclosed to the party." party.md: "the black stone he pocketed on the road." campaign_state: "Zenvon's undisclosed black stone." The party has never seen an obelisk; the obelisk is still an unassembled mystery ("The party has all the pieces and has not put them together out loud").
**Suggested fix:** "A mysterious dark fragment Zenvon pocketed on the road at the start of the party's journey." Do not assert an obelisk sighting.

---

**Location:** Items ("Black Spider's Note") and Summary — "a note found in the manor that confirmed Iarno Albrek — Glasstaff — had been working for the Black Spider."
**Issue:** Called a "note"; it is a sealed letter, and the seal is a load-bearing detail.
**Evidence:** world_state: "**Letter sealed with a wax spider** — Orders Iarno to capture the party if possible, kill them if necessary, and deliver any dwarven maps with haste." `redbrand_hideout.md` gives the verbatim text and notes "the wax seal is a spider."
**Suggested fix:** "The Spider's letter, sealed with a wax spider" — and note it was found on Glasstaff's desk in Ch. 6, not this session.

---

## Lore / World Contradictions

**Location:** Summary (final paragraph) and Scenes ("A Delicate Mission at the Shrine of Luck") — Garaele wants "the location of a legendary spellbook belonging to the mage **Bowgentle**."
**Issue:** Correct on the name, but the recap omits the crucial fact that Agatha no longer *has* the book, which will matter next session.
**Evidence:** AUTHORITATIVE CANON: "**Bowgentle** — Author of a spellbook once possessed by Agatha, **who traded it to the necromancer Tsernoth over a century ago**." And "**Tsernoth** — Necromancer from **Iriaebor** who received Bowgentle's spellbook from Agatha in a trade over a century ago; fate unknown."
**Suggested fix:** No correction to the recap's factual claims (Garaele *does* seek the location), but consider adding a note that Agatha's answer will be a lead to Tsernoth, not the book itself, so a future session doesn't treat the book as retrievable at Agatha's lair.

---

**Location:** Locations ("Agatha's Lair") — "located in **the countryside surrounding Phandalin**."
**Issue:** Vague to the point of being misleading.
**Evidence:** AUTHORITATIVE CANON pairs Agatha's Lair with **Conyberry**: "**Conyberry** — Location paired with Agatha's Lair as the chapter 3 destination for Sister Garaele's banshee-related quest." Canon also places Old Owl Well "southeast of Conyberry."
**Suggested fix:** "Near the ruined village of **Conyberry**, in the countryside east of Phandalin."

---

**Location:** Locations ("Thundertree") — "A ruined town **overrun by undead**."
**Issue:** Incomplete and slightly wrong in emphasis; the dragon and cultists are the live threat.
**Evidence:** AUTHORITATIVE CANON: "**Thundertree** — Abandoned village near Neverwinter Wood, **devastated by Mount Hotenow's eruption thirty years ago**; now overrun by **mutated plants and undead**." Canon also places **Venomfang** (young green dragon) and four **Cult of the Dragon** cultists there.
**Suggested fix:** "An abandoned village near Neverwinter Wood, devastated by Mount Hotenow's eruption thirty years ago and now overrun by ash zombies and mutated plants." (What the *party* knows may be less — mark accordingly.)

---

**Location:** Locations ("Tresendar Manor Crevasse") — "Site of a brutal skirmish with **four bugbears**" appears under Bugbear Barracks; the crevasse entry says the fissure is "twenty feet deep."
**Issue:** Both consistent with canon — no action. Flagged only to confirm: canon says "5–10 ft wide, 20 ft deep," matching.

---

**Location:** Locations ("Tresendar Crypt") — listed as a location for this session.
**Issue:** The crypt fight occurred in Chapter 7. Its inclusion here is harmless if the party passed through, but the description ("guarded by skeletal remains") reads as a fresh encounter.
**Suggested fix:** Note that the party merely transited the crypt, with the two surviving skeletons standing down for red cloaks.

---

## Timeline / Sequencing

**Location:** Summary (paragraph 2) — the emerald necklace is revealed *before* the party escorts the family out; Scenes agree.
**Issue:** Consistent internally. No error. Noted only because campaign_state listed this as "unaddressed" going in — this session resolves it.

---

**Location:** Scenes ("The Bugbear Barracks Brawl") — "**Pip Thistlewick** attempts to strike back with **his new sword** but misses."
**Issue:** Timing conflict. The summary states the party "quietly agreed the sword belonged in the hands of their most capable fighter" *before* the barracks fight, so this is internally consistent — but it means Pip was wielding an unidentified +1 longsword in his first swing with it. Worth confirming the handoff happened on-screen before combat.
**Evidence:** Recap paragraph 4 places the handoff immediately after the chest opening and before "they turned their attention to the bugbear barracks."
**Suggested fix:** No change needed if the handoff was explicit at the table; otherwise clarify.

---

**Location:** Scenes ("A Fiery Escape") — "a bugbear begins hacking through the wood with a **hand axe**."
**Issue:** Bugbears in this module carry morningstars and javelins, not hand axes. Minor, and the GM may have improvised.
**Evidence:** The recap itself elsewhere gives Nosk a **morning star**, consistent with the module stat block. No context doc mentions bugbear hand axes.
**Suggested fix:** Low priority — verify or leave as GM improvisation.

---

## Character State / Mechanics

**Location:** Party-wide (not stated anywhere in the recap)
**Issue:** The recap records no **level-up**, despite this being flagged as a must-hit and long overdue.
**Evidence:** campaign_state: "Zenvon Level 2; Veyra, Maela, and Pip still nominally Level 1 with a **long-overdue level-up**." `everyone_is_a_suspect.md` lists the long rest and level-up as the session's **precondition** ("Never cut: the long rest and level-up, the obelisk conversation, Sildar") and specifies sidekicks to **3** with named obelisk features (Pip: "Returned"; Maela: "Consecrating Touch"; Veyra: **"Candlelight Reading"**).
**Suggested fix:** Confirm whether the level-up happened. If yes, record it — especially Veyra's Candlelight Reading, since the prep doc flags the ordering relative to the crevasse as "the single most important ordering decision in the session." If no, note explicitly that it is *still* pending so it doesn't silently vanish.

---

**Location:** Scenes ("The Bugbear Barracks Brawl") — "Veyra follows up with a **bolt of fire**"; also "Zenvon unleashes a wave of **thunderous energy**."
**Issue:** Veyra's *Firebolt* is attested. **Zenvon's "thunderous energy"** is not — no thunder-damage ability appears on his profile.
**Evidence:** world_state Zenvon combat profile: short sword, scimitar (Nick), dagger, javelin, Cunning Action. No spellcasting, no thunder effect. party.md the same. Rogue 2 with no listed subclass has no such option.
**Suggested fix:** **Verify this.** If it was a *thunderstone* or similar consumable, name the item and add it to the Items list. If it was another character's action, reattribute. This is the single most likely mechanical error in the recap.

---

**Location:** Scenes ("The Bugbear Barracks Brawl") — "Zenvon drinks a potion of healing"; Items ("Potion of Healing").
**Issue:** Consistent with the party holding three potions of healing (world_state). No error — but note the count should drop to two before Garaele's three are added (making five, or six if the chest healing potion is included). Worth reconciling.

---

## Ambiguity Likely to Confuse Future Sessions

**Location:** Summary (paragraph 6) — "Zenvon quickly realized that the bugbears served the Black Spider directly, **placing them above Glasstaff in the chain of command**."
**Issue:** Overstated. Canon says the bugbears serve the Spider and are contemptuous of the Redbrands, not that they outrank Glasstaff.
**Evidence:** `redbrand_hideout.md`: "They work for the Spider, not Glasstaff. They were **sent to provide extra muscle**. They are contemptuous of the Redbrands and only minimally loyal to Glasstaff." AUTHORITATIVE CANON: "**Nosk** — Bugbear **leader of the group the Spider sent to reinforce the Redbrands**."
**Suggested fix:** "…served the Black Spider directly rather than Glasstaff, and answered to a different chain of command."

---

**Location:** Summary (paragraph 6) — "Nosk … **blurted out the Black Spider's location**"; Memorable Moments repeats this.
**Issue:** **Critical ambiguity.** The recap never says *what location was revealed.* This is arguably the single most consequential piece of information gained this session and it is unrecorded.
**Evidence:** campaign_state Open Threads: "**Identify the Black Spider.** … No name, no face, **no location**." The bugbears canonically "know the location of **Cragmaw Castle and Wave Echo Cave**" — Nezznar operates out of Wave Echo Cave. `everyone_is_a_suspect.md` also notes the bugbears "will not divulge the locations willingly."
**Suggested fix:** **Record the actual location named at the table** (almost certainly Wave Echo Cave). Without it, the next session's prep cannot tell whether the party knows where to go. This should be the top correction.

---

**Location:** Summary (final paragraph) and NPCs ("Halia Thornton") — "the suspicion that Halia Thornton knew far more about the Redbrands than she was letting on."
**Issue:** Accurate as an *in-character* impression, but risks hardening into a false canon fact if a future session treats it as confirmation that Halia is Glasstaff's handler.
**Evidence:** `everyone_is_a_suspect.md`, GM-only: "**Nobody in Phandalin is Iarno's boss.** … Only the Spider knows Glasstaff's true identity as Iarno Albrek. … **Halia isn't it.**" She is a Zhentarim rival, genuinely shady but innocent of *this*.
**Suggested fix:** Keep the party's suspicion as reported perception, phrased as such ("the party left convinced…"), not as a narrator assertion.

---

**Location:** Summary — "Veyra's missing **advisor**, Orryn Voss"; Scenes ("Revelations and Rest in Phandalin") — "her advisor."
**Issue:** Inconsistent title. Canon and all grounding docs call him her **mentor**; the canon alias is "**Professor** Orryn Voss."
**Evidence:** AUTHORITATIVE CANON: "**Orryn Voss** / **Professor Orryn Voss** — Veyra's **mentor**." world_state and party.md both say "mentor." Note also that canon flags "Oren Voss" as an ASR garble handled in the corrections file — the recap correctly uses "Orryn Voss."
**Suggested fix:** Use **mentor** (or "Professor Orryn Voss") consistently.

---

**Location:** Summary (final paragraph) — the black stone / blue crystal resonance
**Issue:** The recap says "Veyra turned to Zenvon and asked about the black stone he had been carrying since the very beginning." This implies Veyra already knew about it — but Zenvon's stone was, per all grounding docs, **undisclosed to the party.**
**Evidence:** world_state: "**The black stone** — Zenvon's, pocketed on the road. **Undisclosed to the party.**" party.md: "he has a black stone in his pocket, taken on the road, and **he hasn't mentioned it** to the woman whose crystal lights up around such things." `everyone_is_a_suspect.md` treats the reveal as a live branch with a scripted backstop line from Ssarnak.
**Suggested fix:** Clarify *how* Veyra learned of it — did Ssarnak's whisper expose it, did Zenvon volunteer it, or did she deduce it? This is a significant character beat and the mechanism matters for the trust arc. Also note the recap says "Zenvon kept his growing suspicions to himself, but he trusted her more than he had before" — reconcile that with the fact he apparently just handed her his biggest secret.

---

**Location:** Memorable Moments (first two quotes, both attributed to **Wick**)
**Issue:** These are **Chapter 7** moments, not this session's. Wick was executed in Ch. 7.
**Evidence:** AUTHORITATIVE CANON: "**Wick** — … then was executed by Zenvon. **Dead.** [ch7]" campaign_state: "Wick — **Dead** — Executed by Zenvon in the cellar (Ch. 7)." The NPC entry in this recap even says so.
**Suggested fix:** Remove both Wick quotes and the Wick and Dosa Rook NPC entries from this session's document, or clearly mark them as carried-forward context. As written, a future reader would date Wick's death to 2026-08-02.

---

**Location:** Memorable Moments — Sarnak quote rendered "He is not in a place where **dead** is easy"; Summary renders it "a place where **death** was not easy."
**Issue:** Internal inconsistency in the quoted line.
**Evidence:** `redbrand_hideout.md` and `everyone_is_a_suspect.md` both give the prepared line verbatim: *"Your teacher is not dead. He is not in a place where **dead** is easy."*
**Suggested fix:** Use the verbatim form (**"dead"**) in both places, and note the pronoun — the prep line says "**He** is not in a place…" referring to Orryn Voss, which the recap preserves correctly.

---

## Summary of Highest-Priority Corrections

1. **Record what location Nosk actually revealed** — the session's most consequential fact is missing.
2. **Dendar → Dendrar** (canon).
3. **Sarnak → Ssarnak** (canon).
4. **Toblin → Toblen** (canon).
5. **Droop is Scraptops, not Cragmaw** (canon) — and flag the bad glossary row.
6. **Dosarok → Dosa Rook** (canon).
7. **Name the longsword Talon (+1)** (canon).
8. **Verify Zenvon's "thunderous energy"** — no such ability on his sheet.
9. **Reconcile Sildar's payment** (150 vs. 200 gp) to prevent a double-count.
10. **Record or explicitly defer the level-up.**