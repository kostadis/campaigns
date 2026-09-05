# Consistency Report — "The Sleeper in the Iron Coffin" (Chapter 34, 2026-08-30)

**Scope note:** `campaign_state.md`, `world_state.md`, and `party.md` end around Chapter 28 (Hartsch's war council). The recap depicts Chapter 34 events consistent with the intervening staging docs (party running the upper Temple, Hartsch/Alrrem dead, Nulb trip). I have therefore **not** flagged post-Ch-28 developments as "events that haven't happened yet" — those grounding docs are stale, not contradicted.

---

## A. High-confidence name errors (canon-backed — correct throughout)

### 1. "Sequioa" → **Sequoia** (pervasive)
- **Location:** Summary (multiple), Scenes (Minotaur's Throne, Storerooms, Ghoul Ambush, Supply Room Ambush, Return to Nulb), Items (Frostbrand), Spells (Healing Word)
- **Issue:** The halfling rogue is spelled "Sequioa" in every occurrence — the exact transposed-letter error the project warns about.
- **Evidence:** **AUTHORITATIVE CANON** — entity registry entry: *"Sequoia — player character… config/party.yaml is authoritative for this spelling. The file docs/party/sequioa.md is simply named wrong."* Glossary also maps `Sequioa, Koya, Sequo, Sequoiah` → **Sequoia**.
- **Fix:** Global replace Sequioa → Sequoia.

### 2. "Falarinth" → **Falrinth** (pervasive)
- **Location:** Summary, Memorable Moments, Scenes (A Message from the Shadows), NPCs, Items (Orb, Scarab, Iron Coffin)
- **Issue:** The wizard's name has an extra vowel throughout.
- **Evidence:** **AUTHORITATIVE CANON** — registry entry **Falrinth** ("Keeper of the Orb of Golden Death… travels with his quasit familiar"). Glossary maps `Falwinth, Valorant, Valorinth` → **Falrinth**. All staging docs (`nobody-told-nulb.md`, `the-sleeping-prince.md`) use Falrinth.
- **Fix:** Global replace Falarinth → Falrinth.

### 3. "Varik Solen" / "Captain Varik Solen" → **Varek Solain**
- **Location:** Summary, Scenes (Garbage Room and the Fire Temple), NPCs (Varik Solen; also referenced in the Necromancer entry), Locations (Fire Temple), Items (Fire Arrows, Flask of Oil)
- **Issue:** The Fire Temple captain's name is a transcription-drift spelling.
- **Evidence:** **AUTHORITATIVE CANON** — registry entry **Varek Solain**. Glossary maps `Varric Solein, Varick Salami, Varik Solane, Varik Sulane, Varik Sullen` → **Varek Solain**, and `Varic, Varric` → **Varek**.
- **Fix:** Global replace → Varek Solain. Also note for reviewers: do **not** conflate with the registry's separate entity **Commander Varek Redflame** (leader of Alrrem's Fire Guards) — two distinct canon NPCs with similar names.

### 4. "Turjon" → **Terjon**
- **Location:** Scenes (The Temple Storerooms: "surrender of a magical trident to Turjon"), Items (Magical Trident)
- **Issue:** Misspelling of the St. Cuthbert prefect who raised Calmer.
- **Evidence:** Glossary: `Turgeon, Turjohn` → **Terjon**. Registry: **Terjon**. The underlying event is confirmed by campaign_state: *"Zinnia tithed a magical trident to Terjon; Calmer successfully raised."*
- **Fix:** Turjon → Terjon (fact is otherwise correct).

---

## B. Canon contradictions (fact-level)

### 5. Zinnia gendered "her"
- **Location:** Summary, ghoul battle: "Zinnia — having, as a masked wanderer, smelled and tasted worse things in **her** life…"
- **Issue:** Wrong pronoun for Zinnia.
- **Evidence:** **AUTHORITATIVE CANON** — registry entry Zinnia: *"elf monk, 'the masked monk'; male, he/him per docs/party/zinnia.md. Extraction passes repeatedly degender him — check pronouns on every recap."* This recap is exactly that failure mode. (Note: `nobody-told-nulb.md` also says "Zinnia is the most perceptive" with he/him usage.)
- **Fix:** "her life" → "his life." Also consider "masked wanderer" → "masked monk," the canonical epithet.

### 6. Alrrem described as current head of the Fire Temple
- **Location:** NPCs ("Alrrem — The head of the Fire Temple…")
- **Issue:** Present-tense framing implies Alrrem is alive and in command. He is dead.
- **Evidence:** **AUTHORITATIVE CANON** — registry entry for Vurakhal: *"surrendered as the last of three fire-pit salamanders after **Alrrem's death** stranded it on the Material Plane."* Staging docs confirm the Fire Temple is now pacified under Varek Solain / Maeris Dorn. (world_state lists Alrrem alive, but it is stale ~Ch 28; canon wins.)
- **Fix:** "The **former** head of the Fire Temple (deceased), mentioned by Varek Solain as having been warned about the necromancer threat but failing to act."

### 7. "Shield +1" vs. canon shield +2
- **Location:** Items (Shield +1), Scenes (The Sunken Treasure)
- **Issue:** The recovered shield's bonus may be wrong.
- **Evidence:** **AUTHORITATIVE CANON** — registry location entry: *"Cistern Chamber — area 236, slippery algae-covered water reservoir hiding a **shield +2**."* The recap's chamber (algae-slicked sloping floor, low stone wall, temple water supply) is unmistakably area 236.
- **Fix:** Verify against the transcript/GM ruling; unless the GM deliberately downgraded it, the item should be **Shield +2** in Items and the +1 reference removed.

---

## C. Unattested name — needs GM ruling (do not silently normalise)

### 8. Informant "Skull" — almost certainly **Skole**
- **Location:** Summary (Return to Nulb), Scenes (Return to Nulb), NPCs (Skull, Captain Tolub), Items (Skull's Note)
- **Issue:** "Skull" appears nowhere in the entity registry, glossary, or vtt_known_additions. The staging doc `nulb-knows-now.md` scripts this exact beat: *"A dockhand presses a folded scrap into Sequoia's or Zinnia's hand: '**Skole** says the captain is still telling people you're dead.'"* Skole is the established Nulb informant who hates Tolub (campaign_state: "Sympathetic informant").
- **Evidence:** Registry: **Skole** ("proprietor of the Boatmens' Tavern"). "Skull" fails the canonical source chain entirely.
- **Fix:** Surface to the GM: this is most likely a transcription garble of **Skole**. If the GM confirms, correct all four occurrences and add `Skull → Skole` to the glossary; if the GM genuinely introduced a new codename "Skull" at table, add it to vtt_known_additions instead. Per project rules, do not pick without the ruling.

---

## D. Internal inconsistencies in the recap

### 9. The Minotaur "speaks only Abyssal" — yet negotiates fluently
- **Location:** Summary ("With no one among them able to speak Abyssal…") vs. NPCs ("A filth-covered creature that speaks only Abyssal") vs. Memorable Moments (two quoted lines of broken Common) and the entire negotiated truce.
- **Issue:** If no PC speaks Abyssal and the creature speaks only Abyssal, the quoted dialogue, the food negotiation, the "No hard feelings," and the terms of the truce are all impossible as written.
- **Fix:** Determine from the transcript how communication actually worked (broken Common, a spell, gesture) and reconcile — likely the NPC entry should read "speaks broken Common" or the "speaks only Abyssal" claim should be dropped.

### 10. Who drafted the Earth Temple curriculum — Calmer or Sequoia?
- **Location:** Summary paragraph 4 ("**[Calmer]** had already begun scribbling notes toward a new educational system…") and Scenes/Storerooms ("**Calmer** begins drafting plans for a new educational system") vs. Summary paragraph 5 ("prompting Sequioa to needle him before **pulling out a scrap of scroll to begin drafting** a chaotic Earth Temple educational curriculum").
- **Issue:** The same activity is attributed to Calmer twice and Sequoia once. Attribution is a precision decision; this will confuse future sessions.
- **Fix:** Verify against the transcript; most likely the paragraph-5 sentence should attribute the drafting to Calmer (with Sequoia only needling Zephyr), or explicitly distinguish two separate documents.

### 11. Zephyr's title: "chief of operations" vs. "Chief of Staff"
- **Location:** Summary ("Zephyr, as chief of operations") vs. Scenes/The Missing Prisoners ("Calmer designating Zephyr as **Chief of Staff** and Zinnia as Chief of Security").
- **Issue:** Two different titles for the same in-fiction appointment.
- **Fix:** Pick the title actually spoken at table and use it in both places.

---

## E. Questionable claims — verify against transcript

### 12. The necromancer's backstory: "served under Barkinar / passed over for promotion" and "the transition between Barkinar and Romag's leadership"
- **Location:** Summary (necromancer hypothesis paragraph; Fire Temple paragraph), NPCs (The Necromancer, Varik Solen)
- **Issue:** Two problems. (a) The phrasing implies Barkinar preceded Romag as Earth Temple leader — canon says Barkinar is **Commander of the Greater Temple's Troops** (registry), not an Earth Temple prophet; the registry's Earth-transition figure is **Landers** ("former leader of the Earth Temple, betrayed and eliminated by Barkinar"). (b) "Passed over for promotion" inverts the GM's established conceit: per `nobody-told-nulb.md` (quoting Romag at table), the predecessor was ***promoted* to the Deep Temple**, after which the undead stopped obeying the Earth Temple — that promotion is the whole explanation for why only Earth Temple corpses rise.
- **Evidence:** Registry entries for Barkinar and Landers (canon); `nobody-told-nulb.md` §2d.
- **Fix:** Check the VTT transcript for what Varek Solain actually said. If the recap garbled it, restore the "promoted to the Deep Temple / Romag was the consolation prize" framing and remove the implication that Barkinar led the Earth Temple. If the GM genuinely retconned it at table, record that ruling explicitly.

### 13. Dren's quote: "The men have **not been paid** for four"
- **Location:** Memorable Moments (Dren Halveth quote), Summary, Scenes (Administrative Headaches)
- **Issue:** The prep script (`nulb-knows-now.md` Scene 1) has Dren say *"The men **have pay** for four"* — i.e., four days of payroll remaining. The recap's version means four days in arrears — the opposite state of affairs. Prep is not transcript, but the inversion changes the temple's finances going forward.
- **Fix:** Verify which version was delivered at table; align the recap.

### 14. Calmer casting *Hold Monster*
- **Location:** Summary (garbage-room creature), Scenes, Spells (Hold Monster)
- **Issue:** Hold Monster is not on the cleric spell list, and party.md sheets Calmer as a War Domain cleric. The glossary confirms "Hold Monster" was said at table (`Fold Monster` → Hold Monster), so this may be a scroll, item, or GM-sanctioned pick — but it doesn't match his sheet as documented.
- **Fix:** Confirm the source (scroll? homebrew list?) and note it, so future recaps don't treat it as a prepared spell.

### 15. Zephyr casting *Chill Touch*
- **Location:** Spells (Chill Touch)
- **Issue:** party.md sheets Zephyr as Rogue (Assassin) — no spellcasting; his documented cantrip use is Thaumaturgy. Chill Touch is plausible only via a tiefling legacy option not recorded in the provided sheet material.
- **Fix:** Verify against Zephyr's current character sheet; document the source if legitimate.

### 16. Orb of Golden Death "previously described by Romag as capable of summoning monsters and destroying anything if fully controlled"
- **Location:** Items (Orb of Golden Death)
- **Issue:** This specific attribution to Romag is not attested in any provided document; canon describes the Orb as the escape key from the Elemental Nodes and the cult's emblem, and world_state records only that Romag *wanted* it and refused to describe the vault. It may come from an earlier session, but as written it puts specific lore in a dead NPC's mouth.
- **Fix:** Verify against earlier transcripts; if unconfirmed, soften to "an artifact the temple factions covet."

---

## F. Minor notes (no action strictly required)

- **"pistol":** Zephyr's weapon is canonically the **custom hand crossbow pistol** looted from Krell (party.md, world_state). "Pistol" is presumably table shorthand, but the recap uses it unqualified five times; a first-mention gloss ("hand-crossbow pistol") would prevent a future firearms confusion.
- **"Calmer dressed as the Earth Cleric":** his established cover title is Prophet / "Lord Master Calmer" of the Earth Temple; harmless paraphrase.
- **Correct spellings worth noting as *right*:** Lucius **Graeme** (matches the 2026-08-23 GM ruling — the earlier "Graham"/"Alrrem" drift did not recur), **Rhennee** (matches the 2026-09-05 ruling), Senshock, Barkinar, Dren Halveth, Tolub, Verbobonc, Nulb, TZGY.

---

**Summary:** Four canon-backed spelling corrections (Sequoia, Falrinth, Varek Solain, Terjon), one wrong pronoun (Zinnia), one dead NPC described as alive (Alrrem), one likely item error (shield +1 vs. canon +2), one unattested name requiring a GM ruling (Skull/Skole), three internal contradictions, and five transcript-verification items — the necromancer-backstory garble (#12) being the one most likely to corrupt future plotting if left uncorrected.