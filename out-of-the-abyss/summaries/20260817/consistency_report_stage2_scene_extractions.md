# Consistency Report — Stage 2, scene_extractions/ (Session 2026-08-17, Chapter 64)

Six per-scene checks, run 2026-08-24 with `check_consistency.py --model claude-opus-5 --backend claude-code`.
Adjudicated against `GMT20260818-005817_Recording.transcript.cleaned.vtt` by hand; rulings in `.sources.yaml` alongside.

---

## Consistency Report — "The Aftermath at the High Tower"

## 1. Simulacrum vs. Manshoon himself — recap propagates the GM's own recap wording

- **Location**: Scene summary bullets 4–6; Verbatim moments (GM recap block); closing "[Recap and the Race Framed]" bullet 3.
- **Issue**: The recap repeatedly narrates "Manshoon" arriving, conjuring the wall of force, and shattering the door. The document does flag the simulacrum ruling once (parenthetically, on bullet 4), but bullets 5–6, the verbatim recap block, and the closing beat list all still read as the man himself. The closing bullet ("the party moved A'lai out of the lobby just before Manshoon arrived… arriving alone and weakened") drops the qualifier entirely.
- **Evidence**: `campaign_state.md` and `world_state.md` both state "**Manshoon's simulacrum then breached the keep**" / "**MANSHOON'S SIMULACRUM IS INSIDE CANDLEKEEP**" (Ch63). `entity_registry.yaml` (AUTHORITATIVE CANON) records Manshoon as "**appears as Manshoon's Simulacrum**." `20260810_race_to_the_vile_door.md` explicitly scopes this: the CR 6 simulacrum block "remains **correct for the ch63 Candlekeep breach**, which was the simulacrum (GM ruling, 2026-08-19)."
- **Suggested fix**: Apply the simulacrum qualifier consistently — rewrite the closing beat and bullets 5–6 to say "Manshoon's simulacrum," retaining the note that the GM's spoken recap said "Manshoon himself."

## 2. Present-scene wizard behind the wall of force is not disambiguated

- **Location**: Scene summary bullets 7–8; Verbatim ("there's this insanely powerful wizard hiding behind a wall of force"); closing beat 6–7.
- **Issue**: The *present* session's antagonist — the wizard behind the wall of force whom the party will race across six boxes — is never labeled. Future readers may assume it is the same ch63 simulacrum, but the campaign prep documents distinguish the ch63 breach (simulacrum) from the Vault-race encounter (a CR 12 "the real man, depleted" build).
- **Evidence**: `20260810_race_to_the_vile_door.md`: "**Manshoon** | Scaled simulacrum, CR 6 | **The real man, depleted** — CR 12 build below," and "this doc's CR 12 build is the live one at the Vile Door."
- **Suggested fix**: Add an explicit note that the figure in the present scene is Manshoon (the GM's live build), distinct from the ch63 breaching simulacrum — or flag it as a GM ruling still needed. Leaving it ambiguous will guarantee a future contradiction.

## 3. "Tadric the Watcher" — title is correct; flag only the disposition drift

- **Location**: Scene summary, last bullet ("Tadric the Watcher is identified among those present…").
- **Issue**: None on the name/title — this is canon-correct and should **not** be flagged as unattested even though `campaign_state.md` calls him only "Crime-scene guard, Kalan's lieutenant."
- **Evidence**: `entity_registry.yaml` (AUTHORITATIVE CANON): `Tadric — Watcher (Kalan's lieutenant; "Tadric the Watcher")`. Canon confirms the title; the grounding docs' omission is not evidence of error.
- **Secondary concern**: `world_state.md` places Tadric "hand-holding the failing ward lattice" — i.e. at his post, not in the High Tower. The recap placing his token on the High Tower battle map is not contradicted by canon, but is worth confirming.
- **Suggested fix**: Leave the title. Optionally note where Tadric is stationed, since the ward-lattice duty and the High Tower map placement may need reconciling.

## 4. Key custody — "Thorin" vs. "Grygum" is correctly self-corrected, but the second-key holder is stated inconsistently

- **Location**: Scene summary bullet 1 ("quietly passed to Zalthir"); Verbatim (GM: "Thorin quietly slipped the key of Zalthir…" then "No, no, that was a typo. Grygum quietly slipped the key to Zalthir").
- **Issue**: The transcript's self-correction is accurately captured, and the recap correctly follows the corrected version. However, the summary bullet omits **who** passed it, which loses the correction. Also, "passed to Zalthir and then tucked away inside Glabbagool" is consistent with canon only because Glabbagool is bonded to Zalthir's forearm — worth making explicit so a future reader doesn't read "Zalthir holds a key" as a standing inventory fact.
- **Evidence**: `campaign_state.md` "Key resources & assets held": "**Glabbagool: A'lai's second real High Tower key**, hidden inside him." `world_state.md` and `party.md` agree the key is inside Glabbagool, not carried by Zalthir. `world_state.md`: Glabbagool is "**Bonded to Zalthir's left forearm**."
- **Suggested fix**: Rewrite bullet 1 as: "Grygum quietly passed A'lai's High Tower key to Zalthir, who stored it inside Glabbagool (bonded to his forearm) for safekeeping."

## 5. "the gelatinous cube standing just a little bit taller" — Glabbagool is no longer a gelatinous cube

- **Location**: Scene summary bullet 1 (quoting the GM verbatim).
- **Issue**: The GM's line calls Glabbagool a gelatinous cube. Canon has him as a **sentient grey ooze, formerly a gelatinous cube**, fused to Zalthir's forearm. Quoting verbatim is correct, but the summary bullet reproduces it without qualification, which will read as a species claim to a future reader.
- **Evidence**: `world_state.md` §3: "**Glabbagool — sentient grey ooze (formerly gelatinous cube)** … Bonded to Zalthir's left forearm."
- **Suggested fix**: Keep the quote but mark it as GM flavour, e.g. "— GM's phrasing; Glabbagool is a sentient grey ooze, formerly a gelatinous cube."

## 6. "Not worth the price of the bullet" — anachronism, correctly caught at the table

- **Location**: Scene summary bullet 10; Verbatim (Grygum).
- **Issue**: No error — the recap already records the in-table correction to "not worth the spell slot." Flagged only so a future extraction pass does not promote the bullet line into canon phrasing.
- **Evidence**: Verbatim transcript shows Grygum immediately supplying "spell slot" and the GM confirming.
- **Suggested fix**: None required. Consider dropping the bullet's first clause and keeping only the corrected line.

## 7. "He sent a courier 11 years" — the eleven years is canon; the courier detail is partially garbled

- **Location**: Scene summary bullet 9; Verbatim (GM as A'lai).
- **Issue**: The quoted line "the courier wear a glove, and I never saw the face" is transcript-accurate. Canon adds a load-bearing detail the recap loses: the glove was **over a metal hand**. That detail is the Manshoon "metal hand" prophecy plant.
- **Evidence**: `world_state.md` §4: "**A'lai's patron for eleven years**, receiving stolen books via a courier who always wore **a glove over a metal hand**." `20260810_race_to_the_vile_door.md`: "⭐ **This is the courier's hand.** The glove over metal that A'lai described for eleven years, and the prophecy's *'his metal hand.'*"
- **Suggested fix**: Note in the summary bullet that the glove concealed a metal hand (per world_state), so the plant is not lost.

## 8. "He's not looking for me… He sent a courier 11 years" — grammar garble left uncorrected

- **Location**: Verbatim moments, GM as A'lai Aivenmore.
- **Issue**: "He sent a courier 11 years, and the courier wear a glove" is a transcription garble (missing "for"; "wear" for "wore"). Not a canon error, but the campaign's own VTT-corrections doc treats ordinary-speech garbles as targeted-edit candidates.
- **Evidence**: `vtt_transcription_corrections.md` — "Non-name fixes" precedent (e.g. "overcrumbed" → "overcome", "Fade from sugaring" → "shuddering").
- **Suggested fix**: If the verbatim block is meant to be readable prose, correct to "He sent a courier for eleven years, and the courier wore a glove." If strict verbatim is required, leave and flag.

## 9. "the depository" — used without definition, and its contents are a live secret

- **Location**: Scene summary bullet 11; Verbatim (GM).
- **Issue**: The recap states A'lai "never told Manshoon the truth about what lay inside the depository" without noting this is his *only remaining leverage* and that the contents are unknown to everyone including the party and the GM's documents. A future session doc could misread "the depository" as a resolved location.
- **Evidence**: `campaign_state.md` Active Quests: "He is withholding what is really in the depository — the one thing Manshoon does not know." `world_state.md` §8 A.2: "**What is actually in the depository?** … Nobody else knows."
- **Suggested fix**: Annotate as an open thread, not a resolved fact: "his last card; contents still unknown to the party."

## 10. "Murmo" — unresolved name in verbatim block

- **Location**: Verbatim moments (GM: "Murmo."), during the map confusion.
- **Issue**: "Murmo" matches no entity in the AUTHORITATIVE CANON registry, nor any campaign document. Zalthir replies "Oh, she's gone," suggesting an NPC. This is most likely a transcription garble during token-hovering chatter, but it is left unexplained and could be mistaken for a new NPC by a future mining pass.
- **Evidence**: Absent from `entity_registry.yaml`, `campaign_state.md`, `world_state.md`, `vtt_transcription_corrections.md`, and `vtt_known_additions.md`.
- **Suggested fix**: Flag as unrecovered and mark it as table chatter, not an NPC. GM ruling needed before it can be promoted; do **not** add to the registry.

## 11. "Bushka woman" / "Babushka woman" — inconsistent rendering within the same block

- **Location**: Verbatim moments (Thorin: "who's the Babushka woman"; Zalthir: "The Bushka woman"; GM: "the babushka").
- **Issue**: Three renderings of the same token nickname. Harmless table chatter, but inconsistent capitalisation/spelling in a verbatim block invites a future spell pass to "correct" one of them into a proper noun.
- **Evidence**: No entity by any of these names exists in canon; the GM's own line resolves it — "This person over here is Tadric… That's who the Babushka woman is."
- **Suggested fix**: Normalise to "babushka woman" (lowercase, descriptive) throughout, and note it resolves to Tadric's token.

## 12. Six-box race framing — no ambiguity flagged, but the win condition is understated

- **Location**: Scene summary bullet 8; closing beat 7.
- **Issue**: The recap says "he gets to box six, he wins" without stating *what* he wins. Future readers will not know the stake is the Book of Vile Darkness in the Vault beneath the House of Alaundo.
- **Evidence**: `campaign_state.md` Active Quests: Manshoon "is working toward the **Book of Vile Darkness** in the Vault beneath the House of Alaundo." `20260810_race_to_the_vile_door.md`: "**The Book of Vile Darkness does not leave Candlekeep in Manshoon's hands.**"
- **Suggested fix**: Add the stake to the bullet: "…box six = he reaches the Book of Vile Darkness."

## 13. Chapter attribution not stated

- **Location**: Document header / scene metadata.
- **Issue**: The recap marks several beats as "Chapter 63 context" but never states which chapter *this* session is. Given campaign_state is "authoritative as of Chapter 63," and the summaries convention uses chapter numbering, the absence of a chapter number for the current session is a timeline hazard.
- **Evidence**: `out-of-the-abyss/CLAUDE.md`: "**Session summaries** use chapter numbering (e.g., 'Chapter 49: Out of the Dark and Into the Darkness')."
- **Suggested fix**: Label the scene with its chapter number (presumably Chapter 64, per the "not a Chapter 64 event" aside) in the frontmatter.

---

## Clean — no issues found

- **A'lai Aivenmore** — spelling matches canon (`entity_registry.yaml`: `A'lai Aivenmore`, aliases `A'lai`, `Aivenmore`). Status as captured/bound and despairing matches `campaign_state.md`.
- **Zalthir, Grygum, Thorin, Daz** — all PC names correct per canon.
- **Glabbagool** — spelling correct.
- **Manshoon** — spelling correct.
- **Wall of force / shattered door** — matches `world_state.md` ("shattering the magical door that the two High Tower keys were meant to protect") and `campaign_state.md` ("shattered the security-control-room door with a `wall of force`").
- **"Alone and visibly weakened, having expended enormous magical resources"** — matches canon depletion framing exactly.
- **Keys kept apart** — matches `campaign_state.md` ("The two real keys are deliberately kept apart") and `party.md`.
- **Multiple ways to stop him including killing him** — consistent with `20260810_race_to_the_vile_door.md` ("There are **two ways to win and both are real**… killing him is a legitimate victory").
---

## Consistency Report — "The Prisoner's Bargain"

## 1. Scene summary — "the null magic prism of Candlekeep"

- **Location**: Scene summary, first bullet (quoted verbatim), and again in the summary heading paraphrase ("Candlekeep's null magic prison").
- **Issue**: The verbatim quote reads "null magic **prism**," and the GM later says "Candlekeep has got null magic **prisms**." The recap's own paraphrase renders it "null magic **prison**." This is an unflagged inconsistency inside a single bullet — a future reader cannot tell whether the facility is a *prism* (an artifact/cell type) or simply a *prison*.
- **Evidence**: `world_state.md` §4 Locations: "**Candlekeep Prison** — nullifies all spellcasting; A'lai is desperate to be put in it." `campaign_state.md` similarly says "magic-nullifying cell." The AUTHORITATIVE CANON registry has no "prism" entity; it lists no null-magic location at all. `20260810_race_to_the_vile_door.md` uses "the null cell" / "null cells" throughout. "Prism" appears to be a VTT mishearing of "prison" that has been preserved verbatim (correctly) but then propagated into paraphrase.
- **Suggested fix**: Keep "prism" inside verbatim quotes, but add a bracketed note — *(VTT: "prism"; canonical term is Candlekeep's magic-nullifying prison / null cells)* — and use "null magic prison" consistently in all non-verbatim prose. Consider adding `prism → prison` to `vtt_transcription_corrections.md`.

## 2. Scene summary — Grygum credited with Tadric's persuasion

- **Location**: Scene summary, bullet 6 ("Thorin appeals to Tadric, invoking the party's deputization by Kalan Strongbranch...").
- **Issue**: The bullet attributes the appeal to **Thorin**, but the quoted speech that follows is **Grygum's**, and the verbatim block confirms it. The Bargain Struck recap correctly says "Grygum persuades Tadric."
- **Evidence**: Verbatim block: **Grygum** — *to Tadric* — "Alright, Tadric, this is how this has gotta be. We need to defeat Manshoon, or the entire tower is at risk." And **Grygum**: "That this, we're in a hurry here, and we've got to make compromises..." Thorin's only contributions in that stretch are "Or we could just hand them over" and "he's not in the position to negotiate."
- **Suggested fix**: Change to "**Grygum** appeals to Tadric, invoking the party's deputization by Kalan Strongbranch..." (Thorin's "not in a position to negotiate" line is already correctly attributed in bullet 5.)

## 3. Scene summary — "successive keepers of Tomes"

- **Location**: Scene summary, bullet 9 (the Fustilugs explanation).
- **Issue**: The summary renders it "successive keepers of **Tomes**"; the verbatim block renders the same line as "successive keepers of **Tobed**." One of these is a silent correction of the other, and the correction is not flagged.
- **Evidence**: Verbatim: **GM** — *as A'lai* — "What I noticed was that successive keepers of **Tobed** had ensured that the knight is never replaced." The canonical Candlekeep title is **Keeper of Tomes** (`entity_registry.yaml`: Janussi, "Keeper of Tomes (victim)"; Daral Yashenti now occupies the post). `vtt_transcription_corrections.md` already carries `Keeper of Toads → Keeper of Tomes`, confirming this garble family.
- **Suggested fix**: The correction is right, but flag it — mark "Tobed" as a VTT garble of "Tomes" in the verbatim block (as was done for the "Dao bowed" line) or add `Tobed → Tomes` to the glossary.

## 4. Scene summary — "the oversized black marble chess pieces"

- **Location**: Scene summary, bullet 9.
- **Issue**: The summary silently corrects the verbatim "black marble **chest** pieces" to "**chess** pieces" without flagging it. Correct as a correction, but unmarked.
- **Evidence**: Verbatim: "one of the oversized black marble **chest** pieces, which see plenty of use on the Philosopher's Court." Module/prep canon: `candlekeep_murders_arc.md` Session 7 clue table — "**Fustilugs** | Philosopher's Court (under the **black marble knight**)"; `vtt_known_additions.md` — "black marble **chess** pieces… on the Philosopher's Court." Chess is correct.
- **Suggested fix**: Flag as a VTT garble in the verbatim block, or add `chest pieces → chess pieces` as a phrase fix.

## 5. Scene summary — "the base insult of a Black Knight"

- **Location**: Scene summary, bullets 8 and 11; Bargain Struck recap.
- **Issue**: Minor, but worth pinning: the recap capitalizes "Black Knight" as a proper noun in some places and the verbatim has it lowercase in others. Not an error, but it should be consistent so a future reader does not treat "the Black Knight" as an NPC.
- **Evidence**: `candlekeep_murders_arc.md` gives the clue verbatim as "*The base insult of a Black Knight*" — a Monty Python reference to the chess piece, not a character. The canon registry has no "Black Knight" NPC.
- **Suggested fix**: Match the module's capitalization ("Black Knight") throughout, and consider a one-line note that this refers to the marble chess piece on the Philosopher's Court, not an NPC.

## 6. Scene summary — "the answers to two riddles"

- **Location**: Scene summary, bullet 8: "A'lai provides the answers to two **riddles**."
- **Issue**: The scene establishes explicitly that the six items are **questions in a cryptogram** (a letter-substitution cipher), not "riddles." The riddle is a separate, later object — the door to B3 whose answer is "candle."
- **Evidence**: GM: "it consists of a set of questions that... guarded the Vault of Secrets"; "Is this a letter substitution cipher?" / "Yeah, it's a latter substitution cipher." `candlekeep_murders_arc.md` and `20260810_race_to_the_vile_door.md` both call these **cryptogram clues** (six of them), distinct from the **riddle door** (answer "candle") in B3.
- **Suggested fix**: "A'lai provides the answers to two of the six **cryptogram questions** (clues #3 and #6)." Reserve "riddle" for the B3 door.

## 7. Scene summary — clue numbering ("number 3" / "number 6")

- **Location**: Scene summary bullets 8–10 omit the clue numbers, which the transcript supplies and which matter for cross-referencing prep.
- **Issue**: Not an error, but an ambiguity that will cost a future session. The transcript is explicit: Fustilugs is **number 3**, Bow is **number 6**.
- **Evidence**: GM: "So, he has the answer to number 3"; and for Bow, "No, this is for **number 6**." This matches the canonical clue table exactly (`candlekeep_murders_arc.md` Session 7 Beat 2 and `candlekeep_day_four.md` Beat 2): #3 = Fustilugs (Philosopher's Court), #6 = Bow (School of Drama / Batbayar). Note the party also hears clue #2 named aloud — Grygum's "the Eastern Light of Mystra's Mantle" — which the GM corrects to "No, this is for number 6."
- **Suggested fix**: Add the clue numbers explicitly: "clue **#3** — Fustilugs" and "clue **#6** — Bow." Also record that clue **#2** ("The Eastern Light of Mystra's Mantle") was spoken at the table but not answered.

## 8. Scene summary — "Batbayar" spelling

- **Location**: Scene summary bullet 10; Bargain Struck recap.
- **Issue**: **No error — confirming the recap is correct**, against a transcript that is not. The verbatim renders it "Bathayar" / "Bauthoyar" in some passes; the recap uses **Batbayar**, which is canonical.
- **Evidence**: AUTHORITATIVE CANON registry: `- name: Batbayar / type: npc / note: legendary halfling bard whose statue dominates the School of Drama`. `vtt_transcription_corrections.md` records this exact trap: *"`Bathayar/Pfaffayar → Bauthoyar` was wrong for four days; the canonical is `Batbayar`... caught by `/staged-consistency` stage 0 on 2026-08-20."* The recap has the right form.
- **Suggested fix**: None. Do not let a future pass "correct" this back toward the sibling transcription's "Bauthoyar."

## 9. Scene summary — "School of the Drama Library"

- **Location**: Scene summary bullet 10 (verbatim-quoted) and the verbatim block.
- **Issue**: The location is rendered "the **School of the Drama Library**." The canonical location is **The School of Drama** (no "the," no "Library"). Because this sits inside quotation marks in the summary bullet, a future reader may treat the garbled form as canonical.
- **Evidence**: AUTHORITATIVE CANON registry: `- name: The School of Drama / type: location`; and the Batbayar entry: "statue dominates the **School of Drama**." `candlekeep_murders_arc.md` clue #6: "School of Drama (Batbayar statue)."
- **Suggested fix**: Keep the verbatim as spoken, but add a bracketed gloss — *(canonical: the **School of Drama**)* — so the location name does not drift.

## 10. Scene summary — "It came to life, and bowed"

- **Location**: Scene summary bullet 10, parenthetical note.
- **Issue**: **No error — flagging as correctly handled.** The recap explicitly marks the VTT garble ("It came to loud, and Dao bowed") and notes "Dao" is not a name, choosing the second transcription's reading.
- **Evidence**: This is exactly the discipline `vtt_transcription_corrections.md` prescribes for orphan words that look like names. Note that the reasoning here is *correct in outcome*, but the file's own standing warning applies — a sibling transcription is not authority for a *name*. In this case the recap is not promoting a name, it is *demoting* one, which is the safe direction.
- **Suggested fix**: None.

## 11. Scene summary — A'lai's Baenre deduction stated as fact

- **Location**: Scene summary bullet 11: "A'lai states he could not trace the payments but **deduces** that only one house in Menzoberranzan could afford to be patient for eleven years: House Baenre."
- **Issue**: The wording is defensible ("deduces"), but the recap gives no signal that this is a **wrong** in-fiction conclusion. A future session doc built on this recap could easily promote "House Baenre is Daz's patron" to campaign fact.
- **Evidence**: `20260810_race_to_the_vile_door.md`, GM-only note: *"He is **wrong.** The patron is **Vizeran DeVir**, through cutouts, and A'lai has no idea Vizeran exists. But the guess is *productively* wrong."* Also `world_state.md` §8.B: "The patron: Who in Menzoberranzan paid Menzoberranzan rates to protect Daz... A'lai and possibly Yvenne know" — listed as an **open thread**, not resolved. And `campaign_state.md`: "A'lai... offers... an **intuition** about a Menzoberranzan house."
- **Suggested fix**: Add a clarifier: "A'lai *believes* — on inference from payment patience, not evidence — that the house is Baenre. **The party has no corroboration; this remains an unverified in-fiction claim.**" Do not resolve the patron thread in the recap.

## 12. Scene summary — "eleven years"

- **Location**: Scene summary bullet 11.
- **Issue**: The recap says "patient for eleven years," but the transcript has A'lai say only "**11 years**" in reference to *his own service* ("All these years I've been doing this work"), not explicitly to the duration of the payments protecting Daz. The recap conflates the two spans.
- **Evidence**: Verbatim: "He goes 11 years. / All these years **I've been doing this work**, and never once a demand." Campaign docs pin eleven years to A'lai's tenure as Manshoon's inside man: `world_state.md` — "**Manshoon's inside man for eleven years**"; "A'lai's patron for 11 years." The recap treats it as the patron's patience window for Daz, which may be A'lai's own inference from his service period.
- **Suggested fix**: Rephrase to preserve the ambiguity: "...deduces from eleven years of patient, demand-free payments (the span of his own service to Manshoon) that only House Baenre could afford such patience." Or flag that A'lai is reasoning by analogy from his own arrangement.

## 13. Scene summary — Tadric's rank/title unstated

- **Location**: Scene summary, throughout; NPC handling.
- **Issue**: Tadric is referenced repeatedly without title, and the GM's framing — "there's another officer there" — is ambiguous. Given that the same scene has Tadric taking a prisoner into custody, a future reader may mis-rank him.
- **Evidence**: AUTHORITATIVE CANON registry: `- name: Tadric / type: npc / note: Watcher (Kalan's lieutenant; "Tadric the Watcher")`. `world_state.md`: "Crime-scene guard, Kalan's lieutenant." `candlekeep_vault_session.md` notes he may become "Kalan's **deputy**" post-arc — but he is **not** Gatewarden at this point in the timeline.
- **Suggested fix**: On first mention, gloss as "**Tadric** (Watcher; Kalan Strongbranch's lieutenant)."

## 14. Scene summary — Kalan Strongbranch's deputization, current status unmentioned

- **Location**: Scene summary bullet 6.
- **Issue**: The recap invokes "the party's deputization by Kalan Strongbranch" without noting that **Kalan has fled and is a fugitive** as of this point in the campaign. As written, a reader may assume Kalan is a sitting authority whose deputization is currently in force — which is exactly the ambiguity Tadric is being asked to overlook.
- **Evidence**: `campaign_state.md`: "**Kalan Strongbranch** | Alive — **fled, 'to the wind'** | Whereabouts unknown | Gave the party a **fake key** to use them as a decoy; admitted it when confronted." `world_state.md` §4: "Kalan admitted the deception when confronted and has since **fled** — 'to the wind.'" The transcript's GM line is "Tadric realizes that, you know, you have been deputized by Kalan Strongbranch" — Tadric accepting a warrant from an absconded superior.
- **Suggested fix**: Add a parenthetical: "...invoking the party's deputization by Kalan Strongbranch (**who has since fled the keep**) and their record of service." This also preserves the dramatic irony.

## 15. Scene summary — "Moziqodo, saved his life"

- **Location**: Verbatim block (GM line), not carried into the scene summary.
- **Issue**: The GM says the party "defeated, Moziqodo, saved his life" — the antecedent of "his" is unclear (Tadric's? Moziqodo's?). The recap does not surface this at all, so the claim is not propagated, but the ambiguity should be noted for whoever writes the next session doc.
- **Evidence**: `campaign_state.md`: "Moziqodo | **Dead — killed by the party in one round (Ch62–63)**." Moziqodo's life was decidedly *not* saved. Reading it as "saved **Tadric's** life" is the only coherent parse — but no campaign document records the party saving Tadric's life. `20260810_race_to_the_vile_door.md` describes a *race* to reach Tadric before Moziqodo did, with "Tadric LIVES · real key denied to Manshoon · **EARNED**" as the good outcome, which would support the reading.
- **Suggested fix**: If this is retained in any downstream doc, disambiguate to "defeated Moziqodo and saved Tadric's life" — and verify against the ch62–63 transcript that the party did in fact intercept Moziqodo before he reached Tadric.

## 16. Scene summary — "the entire tower is at risk"

- **Location**: Scene summary bullet 6, quoted.
- **Issue**: Grygum's stakes-claim is quoted without context. At this point Manshoon is loose in **the keep**, headed for the **Vault beneath the House of Alaundo** — not "the tower." A reader may take "tower" to mean the High Tower (already breached and behind them) rather than Candlekeep generally.
- **Evidence**: `campaign_state.md`: "Manshoon's simulacrum is inside Candlekeep... working toward the **Book of Vile Darkness** in the Vault beneath the House of Alaundo." The High Tower fight is complete (Ch62–63). Grygum is speaking loosely.
- **Suggested fix**: Leave the quote intact; it is in-character imprecision. No summary-level claim should be built on "the tower."

## 17. Scene summary — the vault's contents described as settled

- **Location**: Scene summary bullet 8: "A'lai reveals that a secret room beneath Candlekeep holds artifacts of extraordinary power."
- **Issue**: This is accurate to what A'lai *says*, but the recap does not note that **A'lai is deliberately withholding the depository's true contents** — a fact both grounding docs flag as load-bearing.
- **Evidence**: `campaign_state.md`: "He is withholding what is really in the depository — the one thing Manshoon does not know." `world_state.md` §8.A: "**What is actually in the depository?** A'lai withheld it from Manshoon and is holding it as his last card. Nobody else knows." `20260810_race_to_the_vile_door.md` trade table: "What's *really* in the depository | 🔒 **Withheld** — his only card."
- **Suggested fix**: Add: "*A'lai does **not** disclose what is actually in the depository — per GM notes, this remains his withheld last card.*" Otherwise a future doc may conclude the party now knows the vault's contents.

## 18. Bargain Struck recap — ordering of the laden-swallow joke

- **Location**: "[The Bargain Struck]" bullet list, item 9.
- **Issue**: The recap places "Grygum's laden-swallow joke" **after** "Tadric marches A'lai toward the prison" (item 8) and **before** "The party debates whether to race to the vault" (item 10). In the transcript, the swallow joke occurs *before* the vault-vs-Manshoon debate but also before A'lai actually gives the two answers — and Tadric's "I will take him to the prison" line comes earlier in the transcript than the joke, but A'lai is still present and talking afterward.
- **Evidence**: Transcript order: (a) GM as Tadric — "I will take him to the prison" / "And so it marches them off"; (b) Grygum — "What did we learn?"; (c) the Vault of Secrets explanation; (d) the laden-swallow joke; (e) the vault-vs-Manshoon debate; (f) the two cryptogram answers; (g) Tadric — "Are we done, A'lai?"; (h) Grygum — "send him off to the jail then." A'lai is clearly still in the room for (d)–(g). Tadric's "marches them off" at (a) is narratively premature relative to the rest of the scene.
- **Suggested fix**: Note in the recap that the transcript contains **two** dispatch beats — a premature "marches them off" and a final "send him off to the jail" — and that A'lai remains present and speaking between them. As written, the recap implies a single clean exit.

## 19. Scene summary — Grygum's closing line context

- **Location**: Scene summary, final bullet: "Grygum: 'He only has 2? Oh, well, send him off to the jail then. I'm done with it.'"
- **Issue**: Placed under a bullet whose lead clause is "Tadric takes A'lai Aivenmore into custody and marches him off toward the null magic prison." The quote is Grygum reacting to learning A'lai has only two answers — which *causes* the dispatch. The bullet reverses cause and effect.
- **Evidence**: Verbatim sequence: Grygum "He only has 2?" → GM "Yes." → Grygum "Oh, well, send him off to the jail then." The custody handoff follows the disappointment, not the other way around.
- **Suggested fix**: Reorder: "Learning A'lai has answers to only two of the six questions, Grygum dismisses him — 'send him off to the jail then. I'm done with it' — and Tadric takes A'lai into custody toward the null magic prison."

---

## Not errors (verified correct)

- **A'lai Aivenmore** — spelling matches AUTHORITATIVE CANON (`aliases: Aivenmore, A'lai`). Correct throughout.
- **Manshoon** — correct spelling; his presence inside Candlekeep and the party's need to stop him are consistent with `campaign_state.md` and `world_state.md`.
- **Kalan Strongbranch** — spelling matches canon (`aliases: Strongbranch, Kalan`).
- **Tadric** — spelling matches canon; distinct from the many VTT garbles.
- **Grygum / Thorin / Daz / Zalthir** — all PC names correct; speaker attributions in the verbatim block are internally consistent.
- **Philosopher's Court** — matches canon registry (`- name: Philosopher's Court / type: location`).
- **Vault of Secrets** — matches `vtt_known_additions.md` ("questions inside the secret room that guarded the Vault of Secrets," 20260817).
- **Fustilugs** — matches `vtt_transcription_corrections.md` (`Fustelugs → Fustilugs`) and the module clue table.
- **House Baenre** — spelling correct; canon registry has `House Baenre` as a location entry and `Quenthel Baenre` as Matron Mother. The glossary carries `Bandre → Baenre`.
- **Menzoberranzan** — correct spelling.
- **Candlekeep** — correct spelling.
- **"the wrong time to mention" that the wards failed** — consistent with `campaign_state.md`: "Daz's fireball detonating on the walkway publicly proved **Candlekeep's wards had failed**."
- **Real player names** — none survive into the recap; the GM/PC substitution rule appears to have been applied correctly.
---

## Consistency Report — "Deciphering the Vault Riddles"

## 1. Location name: "Founders Court" vs. canon

- **Location**: Scene summary (final bullet) and `[The Riddles Fall]` (final bullet)
- **Issue**: The recap renders the location as "Founders Court" in the summary and "Founders Court" in the beat list, while the verbatim GM line reads "Founder's Court."
- **Evidence**: AUTHORITATIVE CANON registers the location as **`Founders Court`** (no apostrophe). `vtt_known_additions.md` notes "Zoom wrote Founder's/Founders." So the recap's *summary* spelling is correct and the *verbatim* line preserves the transcript's variant — which is fine for a verbatim block.
- **Suggested fix**: No change needed to the summary. Do not "correct" the verbatim quote to match; leave transcript spelling in verbatim blocks. Flagging only so a future pass does not normalize the wrong direction.

## 2. Photographic memory attributed to Kalan Strongbranch

- **Location**: Scene summary, bullet 2 ("The party moves to the investigator's office, where Kalan Strongbranch — who has photographic memory — transcribes the cryptogram questions")
- **Issue**: **Wrong NPC.** The transcript attributes photographic memory to **A'lai**, not Kalan. The `[The Riddles Fall]` beat list gets this right ("A'lai proposes moving to the investigator's office… and his photographic memory supplies the transcribed questions"), so the recap contradicts itself internally.
- **Evidence**: Verbatim GM line: *"Fortunately, A'lai has photographic memory, so this information is accessible to you."* Kalan does not arrive until much later in the scene — the recap's own later bullet says "Kalan Strongbranch arrives late… only to find the party has already solved the cipher."
- **Suggested fix**: Rewrite to: "The party moves to the investigator's office, where A'lai — who has photographic memory — supplies the transcribed cryptogram questions."

## 3. Timeline contradiction: Kalan present at the start *and* arriving late

- **Location**: Scene summary heading and bullets 2 vs. penultimate bullet
- **Issue**: The heading says the party "is joined by Sylvira Savikas **and Kalan Strongbranch**" as they work the riddles, and bullet 2 has Kalan transcribing at the outset — but a later bullet has Kalan "arrives late, eager to contribute, only to find the party has already solved the cipher." Both cannot be true.
- **Evidence**: Transcript: *"Fortunately, you're in a room full of… with Sylvira, and at that point in time, Kalan Strongbranch arrives, huffing and puffing, explaining that he has the answer to clue number 5."* Kalan enters only after the decode is complete.
- **Suggested fix**: Amend the heading to "…is joined by Sylvira Savikas" and remove Kalan from the opening. Keep the late-arrival bullet as the sole Kalan appearance.

## 4. Kalan Strongbranch's presence contradicts campaign state

- **Location**: Scene summary and `[The Riddles Fall]` (Kalan bullets)
- **Issue**: Kalan appears in-person, helpful and cooperative, offering guard-knowledge of the grounds. Per campaign state he is a **fugitive who fled Candlekeep** after admitting the fake-key deception.
- **Evidence**: `campaign_state.md`: "Kalan Strongbranch | Alive — **fled, 'to the wind'** | Whereabouts unknown | Gave the party a **fake key**… admitted it when confronted." `world_state.md` §4 repeats this. `20260810_race_to_the_vile_door.md` treats his return as a *planned branch* ("Branch — Kalan comes back (ruling: mid-race, ~clue 5)") — i.e., his return is a live GM option, and this session appears to have exercised it.
- **Suggested fix**: This is likely a genuine in-session development rather than a recap error, but it is a material state change and should be called out explicitly: add a line noting that **Kalan has returned from hiding** and update `campaign_state.md` / `world_state.md` accordingly (status: returned, at Candlekeep, cooperating). Also note the recap says nothing about the party's reaction to the man who burned them — a gap future sessions may need filled.

## 5. Kalan described as "a member of the guards"

- **Location**: Scene summary (final bullet), quoting Kalan
- **Issue**: The quoted line "As a member of the guards, I've walked these grounds many times" sits oddly against Kalan's canonical office. He is the **Gatewarden** and reinstated **Head of the Avowed** — a senior officer and archmage, not rank-and-file.
- **Evidence**: AUTHORITATIVE CANON: `Kalan Strongbranch — Gatewarden; archmage`. `campaign_state.md`: "Kalan Strongbranch reinstated as Head of the Avowed." The verbatim transcript does say "as a member of the, guards," so the recap is faithfully quoting.
- **Suggested fix**: No change to the quote. Consider a parenthetical gloss in the summary — "(as Gatewarden, he oversees the Watchers)" — so a future reader does not downgrade him to a common guard.

## 6. Sylvira "arrives" — contradicts her bedridden status

- **Location**: Scene summary, bullet 3; `[The Riddles Fall]`, bullet 3
- **Issue**: Sylvira walks into the investigator's office under her own power and mentions having *walked past* the Astronomicon. Campaign state has her **bedridden**.
- **Evidence**: `campaign_state.md` NPC table: "Sylvira Savikas | Alive, dying of abyssal plague | **Bedridden**, Candlekeep." `world_state.md` §4: "Bedridden." The recap partially reconciles this ("Sylvira is too weak from her illness to act herself"), and the transcript supports her mobility ("the Orrery of the Astronomicon, which I happen to walk by").
- **Suggested fix**: The recap is faithful to play; the grounding docs are now stale. Update `campaign_state.md` and `world_state.md` to "Alive, dying of abyssal plague; mobile but too weak to cast/act in the field" rather than "bedridden."

## 7. Miirym's true name — spelling and status

- **Location**: Scene summary, bullet 5
- **Issue**: The recap gives Miirym's true name as **Vydykyq**. Worth confirming, since the verbatim block never spells it — the transcript only has Thorin fumbling "Okay, so VY…" and the GM saying "here's the true name."
- **Evidence**: `20260810_race_to_the_vile_door.md` (GM prep) confirms "She hands over **Vydykyq** and **Limniz**"; `candlekeep_vault_session.md` and `candlekeep_day_four.md` clue tables both list **Vydykyq** as the answer to clue 1. AUTHORITATIVE CANON registers **`Miirym, the Sentinel Wyrm`** — the recap's rendering matches canon exactly, including the title.
- **Suggested fix**: No change. Correct as written.

## 8. "Eastern Light of Mystra's Mantle" — constellation vs. star

- **Location**: Scene summary, bullet 7
- **Issue**: The recap says Sylvira "identifies the 'Eastern Light of Mystra's Mantle' — **Limniz** — as an **obscure star**." The transcript is more precise: Mystra's Mantle is an obscure **constellation**, and Limniz is its **easternmost star**.
- **Evidence**: Verbatim: *"she explains that, this is an obscure, a rather obscure **constellation**… **which refers to its easternmost star**, which can be looked up on the star charts in the Orrery of the Astronomicon."* The `[The Riddles Fall]` beat list gets this right ("the easternmost star of an obscure constellation"). The scene summary flattens it.
- **Suggested fix**: "Sylvira identifies **Limniz**, the easternmost star of the obscure constellation Mystra's Mantle, findable on the star charts in the Orrery of the Astronomicon."

## 9. Bookwyrm/Sylvira — "so many of the chief avowed dead" capitalization

- **Location**: Scene summary, bullet 6
- **Issue**: "chief avowed" is lowercase in the summary; **the Avowed** is a proper faction name.
- **Evidence**: AUTHORITATIVE CANON registers the faction as **`The Avowed`** (alias `Avowed`). `world_state.md` §4: "Governed by **the Avowed** (senior scholars)."
- **Suggested fix**: "…so many of the chief **Avowed** dead." (The `[The Riddles Fall]` list already capitalizes it correctly — make the summary match.)

## 10. "Dust of Mechanus" vs. "dust of methane"

- **Location**: Scene summary, decoded-riddle bullet; verbatim Thorin line
- **Issue**: The verbatim block preserves Thorin's "we still need the dust of **methane**" — an obvious ASR garble. The summary correctly renders "dust of **Mechanus**." Flagging so a future normalization pass does not propagate the garble upward.
- **Evidence**: AUTHORITATIVE CANON registers **`Mechanus`** as a concept. `vtt_transcription_corrections.md` already lists "Mechanis, Mechanists, Machinus, **methanus** → **Mechanus**." `candlekeep_day_four.md` Beat 3 riddle: "Sprinkle dust of Mechanus on dormant gears."
- **Suggested fix**: No change to the summary. Consider adding **"methane" → Mechanus** to `vtt_transcription_corrections.md` (adjacent to the existing "methanus" entry), with the usual lowercase-landmine caution — "methane" is a real English word and a blanket case-insensitive row is risky.

## 11. Decoded riddle — missing a line and slight reordering

- **Location**: Scene summary, decoded-riddle bullet
- **Issue**: The recap's rendering of the decoded text runs the lines together and omits **"Tread as many steps as he lived in years"**… actually it includes that, but drops the canonical line break structure and merges "One last guardian of knowledge remains / To verify the chosen Reader's claims" — minor, but the recap presents the eight-line riddle as a prose run-on, which risks a future reader treating a reconstructed paraphrase as the canonical text.
- **Evidence**: Canonical eight-line riddle, verbatim in `candlekeep_day_four.md` Beat 3 and `candlekeep_murders_arc.md` Session 7 Beat 3:
  > *Feed the quill of Alaundo the Seer / Tread as many steps as he lived in years / Utter the original prophecy to unseen ears / Sprinkle dust of Mechanus on dormant gears / One last guardian of knowledge remains / To verify the chosen Reader's claims / But those well versed in Candlekeep's lore / May fearlessly pass the Obsidian Door*
- **Suggested fix**: Replace the prose run-on with the eight-line canonical text, marked as the decoded result. Note the recap says "obsidian door" lowercase where canon has "Obsidian Door."

## 12. "the Vault of Secrets" — location naming

- **Location**: Scene summary heading ("the remaining riddles protecting the Vault of Secrets")
- **Issue**: The prep documents consistently call the destination **the Vault** (beneath the House of Alaundo), holding the Book of Vile Darkness. "Vault of Secrets" is a distinct-sounding formulation.
- **Evidence**: AUTHORITATIVE CANON registers **`The Vault`** and **`Side Vault`** as locations; there is no "Vault of Secrets" entry. However, `vtt_known_additions.md` records **"Vault of Secrets — 20260817 — 'questions inside the secret room that guarded the Vault of Secrets' — Candlekeep location"** — i.e., this phrase is attested from this very session's tape and is flagged as a *known addition awaiting promotion*, not a garble.
- **Suggested fix**: Acceptable as written, but note it is **not yet in the entity registry**. Either promote "Vault of Secrets" to `entity_registry.yaml` (as an alias of `The Vault`, or as a confirmed distinct location if the GM rules it so), or normalize the recap to "the Vault." Do not leave it floating — a future pass will re-flag it.

## 13. "Protanther" reference — unexplained callback

- **Location**: Scene summary, bullet on the GM's scholars'-reaction line
- **Issue**: "how first a dwarf convinces Protanther, and now another dwarf solves a riddle" is presented without context. A future reader has no way to know which dwarf, or what convincing.
- **Evidence**: AUTHORITATIVE CANON registers **`Protanther`** as an NPC and **`Protanthians`** as a faction ("third named position in the Question of the Age debate alongside Bahamutians/Stroudites"). The recap does not identify the dwarf; from party composition it is presumably **Thorin** (the only dwarf besides Grygum, who is an **orc**).
- **Suggested fix**: Two issues here. First, clarify which dwarf convinced Protanther. Second — and more important — **Grygum is an orc, not a dwarf.** The GM's "another dwarf solves a riddle" appears to refer to Grygum solving in parallel, which would be a mis-attribution at the table. See finding 14.

## 14. Grygum described (by implication) as a dwarf

- **Location**: Scene summary, GM scholars'-reaction bullet; verbatim GM lines
- **Issue**: The GM's riffing ("the dwarven… the dwarf and the… I'm Grygum solving this… how first a dwarf convinces Protanther, and now another dwarf solves a riddle") implies **Grygum is a dwarf**. He is not.
- **Evidence**: `party.md`: "**Grygum — Cleric 8 (Life Domain) · Orc (Sage) · Player: Ben Pfaff**." `world_state.md` §2: "Grygum — Cleric of Bahamut" (orc). The dwarf in the party is **Thorin** (`party.md`: "Thorin — Fighter 8 (Battle Master) · **Dwarf** (Giant Foundling)").
- **Suggested fix**: The verbatim block should stay as spoken. But the recap's summary bullet should not launder the error into a claim about the scholars' debate. Rewrite as: "The GM riffs on the scholars' reaction — first a dwarf convinced Protanther, and now the party has cracked a riddle guarding an ancient artifact — folding it into 'the endless debate of the great question of our age.'" Drop "another dwarf." **Flag for the GM**: the table appears to have mis-raced Grygum in the moment.

## 15. "The Beast of Candlekeep" — Moziqodo's status correctly handled

- **Location**: Scene summary, bullet 3; `[The Riddles Fall]`, bullet 3
- **Issue**: None — verifying a load-bearing fact.
- **Evidence**: The recap states Sylvira "does not yet know her son Moziqodo is dead." This matches `campaign_state.md` ("⚠️ **Does not know her son Moziqodo is dead, or that the party killed him**"), `world_state.md` §4, `party.md`, and the GM prep's explicit "banked for Gauntlgrym" ruling in `20260810_race_to_the_vile_door.md` Open Decision #2. AUTHORITATIVE CANON registers **`Moziqodo`** — "'The Beast of Candlekeep'; Sylvira's demonspawn son." Spelling correct.
- **Suggested fix**: No change. Correctly preserved.

## 16. Thorin thanked "for saving Tadric" — but the transcript says "Hugh"

- **Location**: Scene summary, bullet 4
- **Issue**: The verbatim GM-as-Sylvira line reads *"Thanks, **Hugh**, for saving, Tadric."* The recap renders this as Sylvira thanking **Thorin**. "Hugh" is almost certainly an ASR garble, but it is not in the correction glossary and the substitution is unattested.
- **Evidence**: `vtt_transcription_corrections.md` lists Thorin mishearings as "Thorne, Thornton, Thurren, Or Torin, Thorian, Thorn" — **"Hugh" is not among them.** However, context supports the recap: the preceding GM line is "she notices, **Thorin**," and Thorin answers the thanks directly ("I do what I can for those that I can").
- **Suggested fix**: The recap's reading is well-supported by surrounding context and should stand. Add **"Hugh" → Thorin** to `vtt_transcription_corrections.md` as a targeted-edit note rather than a blanket glossary row — "Hugh" is a common English name and a case-insensitive row is a landmine.

## 17. Tadric's rescue — unattested in prior state

- **Location**: Scene summary, bullet 4
- **Issue**: Sylvira thanks Thorin "for saving Tadric," and Thorin's OOC aside is "I'm not ready to cop to what we did." This implies a rescue event. Campaign state does not record the party *saving* Tadric.
- **Evidence**: `campaign_state.md`: "Tadric | Alive | Candlekeep — holding the ward lattice by hand | **Dealt straight**: surrendered the real key to Grygum voluntarily." No rescue is recorded. The GM prep (`candlekeep_arc_flowchart_v2.md`) does have a "race for Tadric" branch where the party can save him from Moziqodo — this session's line suggests **that branch fired** and the party won the race.
- **Suggested fix**: Confirm with the GM whether Tadric was saved by the party. If so, add it to `campaign_state.md` (it materially changes the back-half key-state fork per the flowchart's "MASTER FORK"). Also note: Thorin's "I'm not ready to cop to what we did" reads as guilt about **killing Moziqodo**, not about Tadric — the recap should not conflate the two.

## 18. Miirym described as "a dragon that lives in the castle"

- **Location**: Verbatim GM lines ("Miirym. Miirym, is a dragon. This is a dragon that lives in the castle.")
- **Issue**: "Castle" is imprecise for Candlekeep, and Miirym is canonically a **ghost/translucent** dragon, not a living one.
- **Evidence**: AUTHORITATIVE CANON: **`Miirym, the Sentinel Wyrm`** — "**translucent ghost-dragon** guardian of Candlekeep (encountered 'Underneath Candlekeep')." `vtt_transcription_corrections.md` also carries the "sentinel worm → **Sentinel Wyrm**" homophone correction.
- **Suggested fix**: No change to the verbatim quote. If the summary ever glosses Miirym, use "the ghost-dragon guardian who serves in spirit beneath Candlekeep" — which also explains why the riddle phrases it as "she who serves **in spirit**."

## 19. Grygum's Performance modifier

- **Location**: `[The Riddles Fall]`, bullet on the performance check
- **Issue**: The recap states "Grygum, at plus two, is elected to roll." Worth noting the check itself is muddled in the transcript — the GM asks for "an intelligence or performance check," then "roll a, intelligence check," then corrects to "Performance."
- **Evidence**: Verbatim Grygum: "Performance plus 2, yeah." Verbatim Daz: "I only have a plus zero." `party.md` does not list skill modifiers for either character, so there is nothing to contradict. The +2 is player-asserted at the table.
- **Suggested fix**: No change. Recap is accurate to the tape. Flagging only that the ability used shifted mid-call (Intelligence → Performance) and the recap does not note the ambiguity — a future session referencing "the check they made" may be confused.

## 20. "A'lai suggests the venue" — A'lai's custody status

- **Location**: Scene summary, bullet 1
- **Issue**: A'lai is speaking freely, proposing venues, and contributing his photographic memory — with no mention that he is a **bound prisoner in the party's custody**.
- **Evidence**: `campaign_state.md`: "A'lai Aivenmore | **Alive — captured, bound, in the party's custody** | Moved out of the High Tower lobby | Broken; bargaining for a magic-nullifying cell." `world_state.md` §4 identical. `20260810_race_to_the_vile_door.md` Scene 1 has him bound and trading information for a null cell.
- **Suggested fix**: Add a clause establishing his status: "A'lai — bound and in the party's custody — suggests the venue…" Without it, a future reader may assume he is a free collaborator, which materially misreads the scene and the arc.

## 21. Convenience note: "the office is near the prison"

- **Location**: Scene summary, bullet 1
- **Issue**: Minor, but the recap flattens the GM's meta-joke ("Conveniently, the office is near the prison") into what reads as a geographic fact.
- **Evidence**: AUTHORITATIVE CANON registers **`Candlekeep Prison`**… actually it does not appear as a registered location; `world_state.md` §4 Locations lists "**Candlekeep Prison** — nullifies all spellcasting; A'lai is desperate to be put in it." The proximity of the investigator's office to it is newly asserted here.
- **Suggested fix**: Acceptable, but note this establishes new geography. If it matters for future prep (A'lai's transfer to the null cells), promote "investigator's office is adjacent to Candlekeep Prison" to the locations notes.

---

## Summary of material corrections needed

| Priority | Finding | Fix |
|---|---|---|
| **High** | #2 — Photographic memory attributed to Kalan | Change to **A'lai** |
| **High** | #3 — Kalan both present at start and arriving late | Remove from opening; keep late arrival only |
| **High** | #14 — Grygum implied to be a dwarf | He is an **orc**; drop "another dwarf" from the summary |
| **High** | #20 — A'lai's custody status omitted | Add "bound, in the party's custody" |
| Medium | #4 — Kalan's return contradicts "fled" state | Update `campaign_state.md` / `world_state.md` |
| Medium | #6 — Sylvira mobile vs. "bedridden" | Update grounding docs |
| Medium | #8 — Limniz as star vs. constellation | Correct the summary to match the beat list |
| Medium | #11 — Riddle rendered as prose run-on | Restore canonical eight-line text |
| Medium | #17 — Tadric rescue unattested | Confirm with GM; record if it happened |
| Low | #9 — "chief avowed" lowercase | Capitalize **Avowed** |
| Low | #12 — "Vault of Secrets" not in registry | Promote or normalize |
| Low | #10, #16 — Glossary additions | "methane"→Mechanus, "Hugh"→Thorin as targeted-edit notes |

**Names verified correct against AUTHORITATIVE CANON**: Sylvira Savikas, Kalan Strongbranch, A'lai, Moziqodo, Tadric, Miirym the Sentinel Wyrm, Alaundo the Seer, Mechanus, Astronomicon, Founders Court, Protanther, Thorin, Grygum, Daz, Zalthir, Glabbagool.
---

## Consistency Report — "The Statue of Alaundo"

## Location: Scene summary — bullet 3 / Verbatim moments

**Issue:** The recap's summary bullet renders Zalthir's line as *"We did take a sample of the poisoned ink, we could try that."* The verbatim block attributes the same line to Zalthir, but the preceding line — *"I mean, there… there was the whole thing with the ink on the book, and it killed the guy."* — is attributed to Daz. This is internally consistent, but the underlying fact is questionable: the murder weapon was **midnight tears poison dusted onto the page edges of *The Golden Ass***, not "poisoned ink."

**Evidence:** `world_state.md` §4: *"Poisoned via a book laced with **Midnight Tears** (ingested by licking fingers to turn pages)."* `candlekeep_murders_arc.md` Session 4: Alkrist *"poisoned **The Golden Ass** by dusting page edges with **midnight tears**."* Nothing in the context documents attests a "sample of the poisoned ink" in party possession. Grygum's item list (`party.md`, `world_state.md` §2) does not include it, and it appears on no PC's asset line.

**Suggested fix:** Either flag the in-fiction claim as a player misremembering (the poison was on the pages, not in an inkwell), or verify against the transcript whether the party actually retained a physical sample. If they did not, add a note that the "sample of the poisoned ink" is an unverified player assertion, not an inventory item.

---

## Location: Scene summary — bullet 7 / "[The Statue Slides Aside]" bullet 6

**Issue:** Location contradiction. The scene summary bullet 7 says the biography *Alaundo, the Wonder Years* is in the **Hall of Momentous Deeds**; the second bullet list says the **House of Momentous Deeds**. The verbatim GM line says *"the House of Momentous Deeds."*

**Evidence:** The AUTHORITATIVE CANON registry lists the location as **"The Hall of Momentous Deeds"** (type: location, note: *contains **The Whispering Dome***). There is no "House of Momentous Deeds" in canon. Corroborated by `candlekeep_murders_arc.md` Session 7 Beat 3: *"research at the **Hall of Momentous Deeds**."*

**Suggested fix:** Standardize both instances to **Hall of Momentous Deeds**. The GM's spoken "House" is a slip (likely bleed from "House of Alaundo," which the party was standing in); flag it as a transcription/speech artifact, not new canon. Note the recap's summary section already has it right — it's the derived bullet list that drifted.

---

## Location: Scene summary — bullet 1 / "[The Statue Slides Aside]" bullet 1

**Issue:** The party is described as gathering **"at the House of Alaundo in Founders Court."** This is correct, but the recap never notes that the statue sequence is the **entrance to the Vault**, where the Book of Vile Darkness sits and where Manshoon is headed. A future reader could take this as an unrelated exploration beat.

**Evidence:** `world_state.md` §4 Locations: *"**The Vault** (beneath the House of Alaundo, via 97 steps and a lava chamber) — holds ~100 warded tomes, the Echoes of Alaundo, and the **Book of Vile Darkness**. This is where Manshoon is going."* `campaign_state.md` Active Quests: Manshoon *"is working toward the **Book of Vile Darkness** in the Vault beneath the House of Alaundo."* Canon confirms **Founders Court** and **The House of Alaundo** as distinct registered locations, and the registry marks **The House of Alaundo** and **The Echoes of Alaundo** as confirmed-distinct entities.

**Suggested fix:** Add one clause to the summary establishing stakes: this is the Vault descent, and Manshoon is racing them to it.

---

## Location: Scene summary — bullet 6 / final bullet list

**Issue:** The recap states **"the part where Thorin solved the puzzle"** as if Thorin solved it. In the same scene the recap also has **Grygum** decide on ink and **Grygum** pour it in. The two statements sit adjacent without reconciliation.

**Evidence:** The verbatim block supports both readings — Thorin proposed blood (wrong) and flagged the plot hole; Grygum chose ink and poured. The GM's line *"The part where Thorin solved the puzzle is what's causing everybody to be excited"* is the in-fiction **scholars'** (mis)attribution, immediately followed by Grygum making a speech *"so that at least some of it is likely to be written down correctly"* — i.e., the joke is that the record is wrong.

**Suggested fix:** Reword to make the irony explicit: *the assembled scholars credit **Thorin** with solving the puzzle (he did not — Grygum poured the ink), which is why Grygum makes a corrective speech.* As written, a future session could canonize a false attribution.

---

## Location: Scene summary — bullet 8 / final bullet list

**Issue:** The recap says scholars suggest checking **"the grove where the keepers of tomes are buried."** The GM verbatim is *"the grove, where every keeper of tomes is buried."* The recap treats this as if Alaundo were among them — but Alaundo is a **seer/prophet**, not a Keeper of Tomes.

**Evidence:** Canon registry: **Alaundo the Seer** — *"the historical prophet whose 99 prophecies the Endless Chant recites."* He is not registered as a Keeper of Tomes. **Janussi** is registered as *"Keeper of Tomes (victim)"* and **Daral Yashenti** now occupies that post. `candlekeep_murders_arc.md` Session 7 Beat 3 gives the correct source for Alaundo's age: *"Alaundo's tombstone in the **Grove cemetery**"* — a tombstone, listed separately from the Keeper-of-Tomes burials.

**Suggested fix:** Clarify that the grove is the Candlekeep cemetery (canon: **The Grove**), which contains Alaundo's tombstone as well as the Keepers' graves — not that Alaundo was himself a Keeper of Tomes.

---

## Location: Scene summary — bullet 5 / Verbatim moments

**Issue:** Thorin's plot-hole line asks *"How long has the statue been here?"* and observes that nobody has ever poured ink in. The recap presents the GM's *"good plot hole discovery"* as an unresolved in-fiction gap. It is not — the mechanism is a **deliberate Vault seal**, not an unnoticed feature.

**Evidence:** `candlekeep_murders_arc.md` Session 7 Beat 5 and `candlekeep_day_four.md` Beat 5: **Inda** — canon-registered as *"House of Alaundo; half-orc, secretly worships Alaundo as a deity"* — is the one who canonically fills the inkpot, knows the 97 steps *"from devotion alone,"* and afterward **seals the staircase**. The passage is not a secret nobody stumbled on; it has a keeper.

**Suggested fix:** Note that **Inda** exists and is the House of Alaundo's librarian/devotee who knows the inkpot procedure. The recap never mentions her, which is a scene-level omission given she is scripted to appear at exactly this beat. Confirm at the table whether she was present.

---

## Location: Verbatim moments — GM lines

**Issue:** Two transcription artifacts survive into the "verbatim" block unmarked.

**Evidence:**
1. *"a large brass statue of Alaundo bearing a **quilt** and ink pot"* — "quilt" is an ASR error for **quill**; the surrounding lines all say quill.
2. *"What is that name of that? **Anostadamus** of his age."* — `vtt_transcription_corrections.md` Real-world/table section registers **Nostromas → Nostradamus**. "Anostadamus" is the same garble unlisted. The recap's *summary* correctly renders it "Nostradamus."

**Suggested fix:** Mark both as transcription artifacts in the verbatim block, or correct with a bracketed note. Consider adding `Anostadamus` to the Nostradamus row in `vtt_transcription_corrections.md`.

---

## Location: Scene summary — general

**Issue:** No chapter number is assigned. Campaign convention requires one.

**Evidence:** `out-of-the-abyss/CLAUDE.md`: *"**Session summaries** use chapter numbering (e.g., 'Chapter 49: Out of the Dark and Into the Darkness')."* `campaign_state.md` and `world_state.md` are both *"Authoritative as of Chapter 63."* This scene follows the ch63 Manshoon breach, so it is Chapter 64 or later.

**Suggested fix:** Add the chapter number to the front matter.

---

## Location: Scene summary — bullet 2

**Issue:** *"Common superstition holds that touching the quill guarantees 'a well-critiqued piece of academia'"* — the verbatim GM line splits across two utterances as *"you will write a well-critiqued piece" / "Of academia."* The recap's compression is faithful but changes "write" to "touching the quill guarantees," which overstates the superstition into a guarantee.

**Evidence:** GM verbatim: *"Common superstition states that if you touch the quill, you will write a well-critiqued piece."*

**Suggested fix:** Minor; restore "you will write" phrasing to keep it a superstition rather than a mechanical guarantee.

---

## Not flagged (checked, consistent)

- **"Founders Court"** — matches canon registry (`Founders Court`, location). The `vtt_known_additions.md` note that Zoom rendered it "Founder's/Founders" is a spelling variance already resolved in canon's favor; the recap uses the canon form.
- **"Alaundo"** spelling — matches canon (`Alaundo the Seer`, alias `Alaundo`). The transcript garbles (Aluando, Alando, etc.) do not appear.
- **Speaker attributions Thorin / Zalthir / Grygum / Daz** — all four PCs are canon-registered and correctly spelled; no player real names survive into the output, per the scrub rule.
- **97 steps / Alaundo's age at death** — the recap correctly presents this as *unknown to the party*, which matches the canon puzzle structure (`candlekeep_murders_arc.md` Session 7 Beat 3: *"97 steps: Alaundo's age at death"*). The party not knowing it is the intended state.
- **Party composition** — Daz, Thorin, Zalthir, Grygum all present; consistent with `party.md`.
---

## Consistency Report — "The Grave of Alaundo and the House of Mechanus"

## Findings

---

**1. Location — Scene summary, bullet 3 ("Scholars from Candlekeep provide the party with the text of the original prophecy…")**

- **Issue**: The recap's parenthetical correction note is itself questionable — it asserts "Castle Ward is a Waterdeep district — ASR garble corrected" and cites a second transcription reading "Candlekeep". But `vtt_transcription_corrections.md` contains a row that maps **`Kendall Keep` → `Castle Ward`**, and separately establishes `Castle Ward` as a *canonical* Waterdeep district (Rishaal's Pageturners, the Stroud statue). The correction direction here is the opposite of the established glossary handling.
- **Evidence**: `vtt_transcription_corrections.md`, Locations table: `| Kendall Keep | **Castle Ward** |`. Also `vtt_known_additions.md`: "**Castle Ward** — Waterdeep district; Stroud-statue…; Rishaal's bookshop". Meanwhile the *scene* is unambiguously at Candlekeep (grove of the keepers of tomes, Alaundo's grave, Candlekeep scholars).
- **Suggested fix**: The substantive correction (Candlekeep, not Castle Ward) is almost certainly right for this line — but the justification is wrong and will confuse a future cleanup pass. Reword the note to: *"cleaned VTT reads 'Castle Ward'; scene context and the second transcription both give Candlekeep — corrected. Note: this is NOT the Kendall Keep→Castle Ward glossary row; do not add a blanket Castle Ward→Candlekeep rule, since Castle Ward is a live Waterdeep district."*

---

**2. Location — Scene summary, bullet 5 ("The party recruits a scholar who specializes in Candlekeep lore for the 'obsidian door' clause")**

- **Issue**: The summary says the scholar "specializes in Candlekeep lore." The verbatim shows Grygum asking for **local history** experts and the GM confirming a scholar "familiar with **the area**." These are subtly different claims, and the riddle line is *"those well-versed in Candlekeep's lore may fearlessly pass the obsidian door"* — a future session could mistakenly treat this NPC as having already satisfied the riddle's requirement.
- **Evidence**: Verbatim GM: *"you do manage to acquire one of the scholars who happens to be familiar with the area."* Grygum: *"there must be a specialty in local history."* The riddle text in `candlekeep_day_four.md` Beat 3 is *"But those well versed in Candlekeep's lore / May fearlessly pass the Obsidian Door."*
- **Suggested fix**: Reword to "a scholar familiar with local history/the area, recruited against the 'obsidian door' clause." Flag explicitly that it is **unresolved** whether this scholar's expertise actually satisfies the riddle.

---

**3. Location — Scene summary, bullet 5 ("The scholar asks to fetch a few things from his knobs and nabs first")**

- **Issue**: "knobs and nabs" is an unrecovered ASR garble carried into the summary as though it were a real phrase or place.
- **Evidence**: Verbatim GM: *"ask whether he can just take a moment to go get some… a few things in the knobs and nabs."* No such term appears in `entity_registry.yaml`, `vtt_known_additions.md`, or the corrections glossary. Likely "nooks and crannies" or a shop/quarters name.
- **Suggested fix**: Either flag it in place as an unrecovered garble (per the documented practice for e.g. *"HRSA building, okay"*), or paraphrase neutrally: "asks to fetch a few things from his quarters first."

---

**4. Location — Scene summary, bullet 8 ("box-like mechanical creatures from the plane of Mechanus")** and **Verbatim GM line ("they're not from the primaterial plane")**

- **Issue**: "primaterial" is a garble of **Prime Material Plane**. The registry lists `the Material Plane` (alias `Material Plane`) as canon.
- **Evidence**: `entity_registry.yaml`: `- name: the Material Plane / aliases: [Material Plane]`. Also `campaign_state.md` uses "Prime Material" consistently ("Demogorgon now loose on the Prime Material").
- **Suggested fix**: Correct the verbatim to "Prime Material plane" as a targeted edit, and consider a glossary row `primaterial → Prime Material`.

---

**5. Location — Scene summary, bullet 10 ("Daz recalls the letter from the librarian in Milo's book")**

- **Issue**: Two problems. (a) The verbatim reads *"**Baz** remembers that in the book that Milo wrote"* — "Baz" is not in the corrections glossary and is an unhandled garble of **Daz**. (b) The summary states this as "the letter from the librarian," but the verbatim is tentative: *"A gift from the librarian, letter, or something?"* — Daz himself is uncertain what the item was.
- **Evidence**: `vtt_transcription_corrections.md` PC table lists `Adaz, Das, Dez, Dazz, Jazz, Doug, Raz, Gaz, Dad` → **Daz**; "Baz" is absent. The registry has `Milo Goodbarrel` (alias `Goodbarrel`) and the `Account of the War of the Dragons` volumes; there is no registered "letter from the librarian" item.
- **Suggested fix**: Correct "Baz" → "Daz" (and add `Baz` to the glossary's Daz row, checking for lowercase collisions first). Reword the summary bullet to preserve the uncertainty: "Daz half-recalls something in Milo's book — 'a gift from the librarian, a letter, or something' — and muses it would be useful now." Do **not** canonize "the letter from the librarian" as an established item.

---

**6. Location — Scene summary, bullet 12 ("Spanner … the only known ways to obtain it are to kill a modron … or to use special tools his modrons have created")**

- **Issue**: The summary presents two options as Spanner's complete framing, but the verbatim also has the **GM** (out of character, before Spanner speaks) offering a *third* possibility that the summary drops: that the party may not need the dust at all. Grygum raises this ("the description really makes it sound like it's a form of preventative maintenance"), and the GM confirms *"that's another option. You can try to see if you actually do need it."*
- **Evidence**: Verbatim GM: *"That, that, that, that, so that's the… that's another option. You can try to see if you actually do need it."*
- **Suggested fix**: Add a bullet recording the open question — the party has GM-sanctioned license to test whether the dust is required at all. This matters downstream: `candlekeep_day_four.md` Beat 3 lists Mechanus dust as a required riddle step.

---

**7. Location — Scene summary, bullet 12 / prep-doc contradiction (how the dust is acquired)**

- **Issue**: The prep documents state Spanner **gives a bag of gear-dust freely** under siege, with no negotiation. What actually happened at the table is a collateral negotiation, a persuasion roll, and a loan of tools (not dust). Future sessions reading the prep will have the wrong state.
- **Evidence**: `candlekeep_day_four.md` Beat 3: *"**Mechanus dust:** Spanner gives a bag freely under siege."* `candlekeep_murders_arc.md` S7 Beat 3: *"**Spanner the rock-gnome librarian** … has a basket of 'spent gear-dust' from his 13 modrons. **He gives it freely** under siege. No fight needed."* Neither is what the recap records.
- **Suggested fix**: Not a recap error — flag it as a **prep-doc supersession**. Add a note to the recap (or a re-key line in the prep) that the "gives it freely" beat did not happen: the party borrowed **tools**, against a Zalthir/Glabbagool symmetry-interview as collateral, on Grygum's persuasion 14.

---

**8. Location — Scene summary, bullet 12 ("Spanner … gnome librarian")**

- **Issue**: Not an error — but worth stating explicitly, because it was previously wrong on disk. Spanner is a **gnome**, correctly rendered here.
- **Evidence**: `entity_registry.yaml`: `- name: Spanner / note: House of Mechanus librarian; directs the 13 modrons`. `vtt_known_additions.md` carries the correction record: *"**gnome** librarian… *Corrected 2026-08-20 by `/staged-consistency` stage 0: originally filed here as 'modron librarian', which was wrong — the tape says gnome twice.*"* The prep docs additionally call him a "rock-gnome."
- **Suggested fix**: None. ✅ Correct. (Optionally note "rock gnome" if you want the subrace on the record — it appears in `candlekeep_murders_arc.md` but not in the registry.)

---

**9. Location — Scene summary, bullet 14 ("which the GM rewards with a persuasion roll (Grygum rolls 14)") and closing recap bullet ("Grygum's persuasion roll of 14 carries it")**

- **Issue**: The attribution of the *idea* vs. the *roll* is muddled, and Thorin's roll is dropped. Per the verbatim: **Thorin** made the argument ("We don't need to keep the tools"), the GM awarded the roll for *that* idea, Thorin declined on a −1 modifier, Grygum rolled 14 — and Thorin then said "I'll do mine. What do we got here?" with no result recorded.
- **Evidence**: Verbatim — Thorin: *"We don't need to keep the tools, we just need the dust."* GM: *"Roll your persuasion, because that was a very good, Idea."* Thorin: *"My persuasion is negative 1."* Grygum: *"I'll do my, 14."* Thorin: *"I'll do mine. What do we got here?"* / *"I need to reload."* GM: *"He accepts the offer."*
- **Suggested fix**: Reword to credit the argument to Thorin and the successful roll to Grygum, and note that Thorin's own roll was never resolved on tape: "Thorin's counter — 'we don't need to keep the tools, we just need the dust' — earns the roll; Thorin's persuasion is −1, so Grygum rolls it (14). Spanner accepts."

---

**10. Location — Scene summary, bullet 15 ("Zalthir: 'We're game as long as you give us constructive feedbacks…'")**

- **Issue**: The verbatim line is corrupted in a way the summary silently smooths over. The tape reads *"We are… **I consult with Zalthir.** We're game…"* — spoken by the player labelled Zalthir, consulting *with* Zalthir, which is incoherent. This is almost certainly a real-name/label artifact or a Glabbagool reference (Glabbagool is the *other* party to the interview and cannot speak).
- **Evidence**: Verbatim Zalthir: *"We are… I consult with Zalthir. We're game as long as you give us constructive feedbacks."* Compare the documented precedent in `vtt_transcription_corrections.md`: *"'You mean Zalthir?' → **Glabbagool** (the GM's own correction that follows only parses this way)"* and *"'sticking in the middle of Zalthir' → **Glabbagool**."*
- **Suggested fix**: Flag as an unresolved speaker/referent garble rather than presenting it as clean Zalthir dialogue. Most likely reading: "I consult with **Glabbagool**." Get a GM ruling before canonizing either way.

---

**11. Location — Verbatim moments, GM line ("It sits between the Immortal Chambers and Founders Court")**

- **Issue**: Not an error, but the recap does not surface that both locations are registry-attested, nor that the House of Mechanus's placement is now first-established here.
- **Evidence**: `entity_registry.yaml` has `House of Mechanus`, `The Immortal Chambers`, and `Founders Court` all as locations. `vtt_known_additions.md` logs **Immortal Chambers** and **Founders' Court** from the 20260817 session with this exact quote.
- **Suggested fix**: None required. ✅ Consistent with canon.

---

**12. Location — Scene summary, bullet 9 ("Zalthir: 'Have we killed a librarian before?' Thorin: 'But they attacked us first… It was justified.'")**

- **Issue**: Ambiguous claim with no campaign referent. Nothing in `campaign_state.md`'s completed-encounters list, the NPC death roster, or `world_state.md` §7 records the party killing a librarian. This reads as table banter, but the summary presents it flatly and a future session could treat it as an established prior event.
- **Evidence**: `campaign_state.md` NPC death list (Ilvara, Asha, Pudding King, Buppido, Narrak, Plinki, Sarith, Moziqodo, Bookwyrm, the Zhentarim assassin + 2 thugs, Alkrist neutralized, Janussi, Ploopploopeen & Bloppblippodd) contains no librarian. Bookwyrm (First Reader) and Janussi (Keeper of Tomes) both died at Candlekeep, but **neither was killed by the party**.
- **Suggested fix**: Mark the exchange as table banter/joke, not a canon claim: "Zalthir needles Thorin about whether they've killed a librarian before — a joke, with no corresponding event in campaign record."

---

**13. Location — Scene summary, bullet 16 / verbatim ("sounds the party 'can't even figure out how a gnome is actually able to make'")**

- **Issue**: Correct as rendered, and worth noting positively — the recap preserves "gnome" here, which is the load-bearing corroboration for Spanner's species (the second of the two on-tape instances cited in the known-additions correction record).
- **Evidence**: `vtt_known_additions.md`: *"the tape says gnome twice (`…cleaned.vtt:4061`, ':4241')."*
- **Suggested fix**: None. ✅

---

**14. Location — Scene summary, bullet 4 ("Grygum, knowing what scholars want, makes sure everyone knows who lent him the ink")**

- **Issue**: Minor attribution smoothing. Grygum says *"I make sure that everyone knows who lent **me** the ink"*; the GM then adds *"He makes sure that everybody knows the correct spelling of **his** name."* The summary conflates the two into a single Grygum action. Reading is probably correct, but "who lent him the ink" is ambiguous about *whose* ink and *whose* name — the House of Alaundo inkpot is the riddle component, and no lender is identified anywhere on tape or in the prep docs.
- **Evidence**: `candlekeep_day_four.md` Beat 5: *"Inda fills the inkpot."* Registry has `Inda` — *"House of Alaundo; half-orc, secretly worships Alaundo as a deity."* No ink-lender NPC is named.
- **Suggested fix**: Leave the bullet but flag the **open question**: who lent the ink? If it's Inda, say so; if it's unresolved, note it so a future session doesn't invent an answer.

---

**15. Location — Scene summary / closing recap, both ("discovering he died at the age of 97" / "learns he died at 97")**

- **Issue**: Correct and consistent with prep, but the recap does not record the **outstanding riddle step** this unlocks, which matters for continuity.
- **Evidence**: `candlekeep_day_four.md` Beat 3: *"**97 steps:** Alaundo's age at death. Inda the half-orc librarian knows it from devotion alone."* `world_state.md` §4 Locations: *"**The Vault** (beneath the House of Alaundo, via 97 steps and a lava chamber)."* Grygum reads the riddle line on tape.
- **Suggested fix**: Optional — add a line noting the party has now satisfied the "tread as many steps as he lived in years" clause's *knowledge* requirement and holds the original prophecy text, leaving the Mechanus dust (or a test of whether it's needed) and the obsidian-door lore clause outstanding.

---

## Nothing wrong

Correctly rendered and consistent with canon: **Spanner** (gnome, House of Mechanus librarian, directs the modrons), **thirteen modrons**, **Mechanus** as a plane (registry: `type: concept`, "lawful plane, modrons' home"), **Dust of Suleiman** as Grygum's (registry item; `world_state.md` §2 lists it among his abilities), **Glabbagool** bonded to **Zalthir** (matches `world_state.md` §3's explicit reconciliation note), **Immortal Chambers** / **Founders Court** / **House of Alaundo**, **Milo** (Goodbarrel), and the **Great Wheel** cosmology reference.
---

## Consistency Report — "The Descent into the Vault"

## 1. Scene summary — "his dragonborn **Draconic Flight** (GM ruling 2026-08-24: a level-9 dragonborn can fly)"

- **Location**: Scene summary, bullet 1 (and echoed in "Positions on the Staircase" and the Zalthir parenthetical about "the wings are Draconic Flight")
- **Issue**: The recap asserts a named racial ability, **Draconic Flight**, as the source of Zalthir's hovering, and attributes it to a GM ruling. The transcript supports no such thing. The verbatim exchange is `Zalthir: "I mean, I can also fly, like…"` / `GM: "You can hover, right?"` / `GM: "Right, and you have a potion of flying."` — the GM explicitly names **a potion of flying**, not a racial feature. `party.md` lists Zalthir as **Monk 8 (Warrior of Shadow), Bronze Dragonborn** with items "Eldritch Claw Tattoo, Asha Vandree's drow spider-silk cloak, **a Potion of Flying concealed inside Glabbagool**" — no flight ability. `world_state.md` §2 likewise lists "Potion of Flying (concealed in Glabbagool)" and no Draconic Flight. The 2026-08-24 date is also *after* today's date in-workspace context and is unsupported by any document here.
- **Evidence**: `party.md` (Zalthir item list), `world_state.md` §2 (Zalthir abilities/key items), and the recap's own verbatim GM line "you have a potion of flying." The VTT glossary further records `potion of lying → **potion of flying**`, confirming the potion is the established mechanic.
- **Suggested fix**: Delete "Draconic Flight" and the GM-ruling parenthetical entirely. Replace with: "Zalthir joins him on 97, noting he can hover — the GM reminds him of his **Potion of Flying** (stored inside Glabbagool)." Correct the later parenthetical to "(the 'wings' are unexplained at the table; the GM had just referenced his Potion of Flying)."

## 2. Scene summary — "**the party is level 9**, confirmed by the GM 2026-08-24"

- **Location**: Scene summary, Telekinesis bullet
- **Issue**: The party-level claim is presented as a GM confirmation with a date, but nothing in the recap's verbatim section mentions levels at all. It is also stated as a justification for Daz's 5th-level slot, which is a reconstruction, not a transcript fact.
- **Evidence**: `party.md` lists all four PCs at **level 8** (Monk 8 / Fighter 8 / Cleric 8 / Wizard 8) with the note "**Party levels to 9 before the next fight.**" So level 9 may well be correct now, but the recap should not attribute it to an undated/unsupported in-session GM confirmation, and the 2026-08-24 date is unsupported. Note also that Daz at Wizard 8 *does* have 4th-level slots at most per `party.md`'s stated level — Telekinesis is a 5th-level spell, so the level question is materially load-bearing and needs a real source.
- **Suggested fix**: Drop the date and the "confirmed by the GM" framing. Either state plainly "(Telekinesis is 5th-level; per `party.md` the party levels to 9 before this fight)" or flag it as **open**: "⚠️ Daz casts Telekinesis — verify the party has reached level 9, as `party.md` still lists Wizard 8."

## 3. Scene summary — "Grygum provides restorative healing"

- **Location**: Scene summary, healing bullet
- **Issue**: "Restorative" is a loaded word in this campaign — *Lesser Restoration* is a tracked, characterful ability for Grygum. The transcript shows only generic hit-point healing ("Yeah, you got 44 of them back").
- **Evidence**: `world_state.md` §2 on Grygum: "**Deliberately withholds Lesser Restoration** to let others choose mercy." Miscataloguing this as "restorative healing" risks a future reader concluding Grygum's withholding stance has changed.
- **Suggested fix**: "Grygum heals Zalthir for 44 hit points" — drop "restorative."

## 4. Scene summary / Verbatim — Thorin's reroll bonus: "+8" vs. "+9"

- **Location**: Scene summary, Thorin's fall bullet ("a second reroll at +8"); Verbatim moments; "Dexterity Saves and Thorin's Fall"
- **Issue**: The recap fixes the bonus at **+8**, but the verbatim shows Thorin reading "**plus 9** bonus" from his feature and then self-correcting aloud twice ("Or, no, okay, so, wait, plus 9… yeah, plus, plus 8"). The recap presents +8 as settled when the table itself never cleanly resolved it, and the reroll result was never rolled/announced.
- **Evidence**: The recap's own verbatim block, which contains both numbers and no resolution.
- **Suggested fix**: "…then invoking a second reroll feature (Thorin reads +9, then settles on +8 at the table; the discrepancy was never resolved)…"

## 5. Scene summary — Thorin's first save: "rolling a 2"

- **Location**: Scene summary, Thorin's fall bullet; "Dexterity Saves and Thorin's Fall" ("Thorin rolls a 2 on a d20 minus 1")
- **Issue**: The verbatim is ambiguous — Thorin says "U20 minus 1, okay, so… I got a 3, what? I got a 2, but I can…" The recap resolves this to a flat 2, but the transcript contains both 3 and 2, and it's unclear whether 2 is the die or the modified total (d20−1 with a 3 gives 2).
- **Evidence**: The recap's own verbatim block.
- **Suggested fix**: "…rolling a 3 on the die for a total of 2 after his −1 (the transcript is ambiguous)…" — or simply "…failing his save…" and drop the number.

## 6. Scene summary — the hinge span: "between steps 93 and 102"

- **Location**: Scene summary, collapse bullet ("anyone standing between steps 93 and 102 is caught in the hinge")
- **Issue**: Minor, but the GM's verbatim is "That's… anybody standing between 101 and 90… no, **102 and 93**." The recap silently swallows the correction, which is fine — but the recap then says Grygum was on 97 and "makes it on a 16," while Zalthir was also on 97, and Daz was "sufficiently high." The recap does not state where Daz actually was, which matters: the GM offered "96, 95, 93, 92, 90" as options and Daz said only that he'd "stay a little high." Since 93 is *inside* the hinge span, "high" is not automatically "safe" — the recap should not present Daz's safety as a positional inevitability without recording his stated step.
- **Evidence**: Recap verbatim (GM's step list; Daz never names a number; GM later rules "All but Daz, who's standing up sufficiently high").
- **Suggested fix**: Add "(Daz never named a specific step; the GM ruled him above the hinge)."

## 7. Scene summary — "Dexterity saves determine who was caught in time"

- **Location**: Scene summary, Telekinesis bullet
- **Issue**: Slight attribution drift. The recap reads as if the saves determine who Daz caught. The GM's verbatim is "Make… make some dexterity saving throws, just to see if you guys manage, like, **whether he caught it in time**" — ambiguous between "did Daz's spell land in time" and "did each PC grab hold." The subsequent narration ("The rest of you have managed to **hold onto the stairs**") suggests the latter.
- **Evidence**: Recap verbatim, GM's two lines.
- **Suggested fix**: "Dexterity saves determine who manages to hold on as the section drops."

## 8. Scene summary — "Daz takes a position higher up the stairs… while the others position themselves lower"

- **Location**: Scene summary, positioning bullet
- **Issue**: Internally contradictory as written: the same bullet has Daz taking a *high* vantage and "tak[ing] up the rear," and Thorin at the *front*. On a descending staircase, "the rear" and "higher up" are the same place, and "the front" is lower — but the recap doesn't say so, and a future reader could easily invert the geometry. This is exactly the kind of ambiguity that will confuse a positional callback.
- **Evidence**: Daz verbatim: "I'll take up the rear in case somebody attacks us from behind… if I'm at the top of the stairs, I'll be able to see with my ranged." Thorin: "if something's gonna happen, I might as well be at the front."
- **Suggested fix**: Make the geometry explicit: "The party is descending, so 'the rear' is *up* the stairs: Daz takes the rear/highest position for ranged line of sight, Thorin the front/lowest to tank."

## 9. Scene summary — "counting toward the ninety-seventh step to match the years Alaundo the Seer lived"

- **Location**: Scene summary, bullet 1; "Positions on the Staircase"
- **Issue**: The recap states the 97-step logic as established fact in narration. The transcript only has Thorin *inferring* it ("he's 97 years old, and you're like, what, Steph?") and the GM refusing to confirm ("No, I'm… I'm the GM, that's my job, to ask you where you were precisely standing"). Presenting it as settled removes the GM's deliberate non-answer.
- **Evidence**: Prep docs support the 97-step figure as canon (`candlekeep_murders_arc.md` Beat 3: "**97 steps:** Alaundo's age at death"; `world_state.md` §4: "The Vault (beneath the House of Alaundo, via 97 steps and a lava chamber)"), and `entity_registry.yaml` confirms **Alaundo the Seer** as canonical. So the *fact* is right; the *attribution* at the table is not.
- **Suggested fix**: "…counting to the ninety-seventh step on Thorin's inference that it matches Alaundo the Seer's age at death (the GM declines to confirm)."

## 10. Scene summary — the Modron tool vs. Mechanus dust

- **Location**: Verbatim moments (Grygum: "Did we… did we make the dust already?" / GM: "No, you have the tool, which is an alternative."); "Positions on the Staircase"
- **Issue**: The recap calls it "**the Modron tool**" without qualification. The riddle canon requires "**dust of Mechanus** on dormant gears," sourced from **Spanner**'s spent gear-dust. A "Modron tool" as an *alternative* to the dust is a new, in-session substitution, and the recap should flag it as such rather than present it as a known item.
- **Evidence**: `candlekeep_murders_arc.md` Beat 3: "**Mechanus dust:** **Spanner the rock-gnome librarian** at the House of Mechanus has a basket of 'spent gear-dust' from his 13 modrons. **He gives it freely** under siege." `candlekeep_day_four.md` Beat 3: "Mechanus dust: Spanner gives a bag freely under siege." `entity_registry.yaml` (AUTHORITATIVE CANON) registers **Spanner** as "House of Mechanus librarian; directs the 13 modrons" and **Mechanus** as a concept. No "Modron tool" is registered anywhere.
- **Suggested fix**: "…the GM confirms the party did not make the Mechanus dust, but holds **a Modron tool** the GM rules is an acceptable alternative (new — not in prep; the riddle line calls for *dust of Mechanus*)." Flag for promotion to the entity registry / known-additions list.

## 11. Scene summary — "a vast circular well" and the cliffhanger

- **Location**: Scene summary throughout; "The Stairs Give Way"; "Session Ends on a Cliffhanger"
- **Issue**: The recap consistently calls the drop "a vast circular well," which is verbatim-correct. But it never connects this to the known geography, and the omission risks a future reader treating the well as an unmapped new feature. Prep canon has the 97-step descent leading to a **1,000-ft `feather fall` shaft** down into the **lava chamber**. Whether this well *is* that shaft is exactly the kind of thing a continuity doc should either state or explicitly leave open.
- **Evidence**: `candlekeep_day_four.md` Beat 5: "Step hinges open. **`Feather fall` shaft, 1000 ft.**" `20260810_race_to_the_vile_door.md`: "At ~93 the first prophecy is spoken aloud, the step hinges open, and it's a 1,000-ft `feather fall` shaft." Note the recap's hinge span (93–102) matches the prep's "~93" trigger point exactly. Also worth flagging: **the first prophecy was not spoken** in this session, which prep treats as the trigger for the hinge.
- **Suggested fix**: Add a note: "⚠️ The 'vast circular well' is almost certainly the prepped 1,000-ft `feather fall` shaft to the lava chamber (prep: hinge triggers at ~step 93). **However, the party never spoke Alaundo's first prophecy**, which prep lists as the required trigger — confirm whether the GM dropped that requirement or the trap fired early. Also confirm whether feather fall is in play, since the recap presents Thorin's fall as lethal-stakes."

## 12. Prophecy thread — Grygum's interrupted "prophecy"

- **Location**: Verbatim moments (Grygum: "And I… I res…" / GM: "Hold on." / Grygum: "prophecy."); "Positions on the Staircase" ("Grygum commits to step 97 to recite the prophecy")
- **Issue**: The scene-block summary asserts Grygum "commits to step 97 **to recite the prophecy**," but the scene *summary* at the top omits this entirely, and the transcript shows the GM cutting him off mid-declaration. Given item 11, whether the prophecy was actually recited is load-bearing for the trap trigger. The recap gives two different impressions in two places.
- **Evidence**: The recap's own verbatim ("Hold on" interrupts) vs. its scene-block gloss ("to recite the prophecy"). No verbatim line shows the prophecy actually being spoken.
- **Suggested fix**: Harmonize both: "Grygum begins to declare that he will recite the prophecy on step 97 but is cut off by the GM; **the prophecy is never actually spoken on tape.**"

## 13. Scene summary — Zalthir "ends up holding the others by strength"

- **Location**: Scene summary, Zalthir bullet parenthetical; "The Stairs Give Way"
- **Issue**: Presented as resolved. The GM's line is mid-sentence and self-correcting: "while… while Grygum is holding… while **Zalthir** is using his strength to hold you guys, the two… two of you, float." The GM starts to say Grygum, corrects to Zalthir, and the outcome ("float") is not clearly reconciled with Zalthir having no flight source other than an unconsumed potion. The recap's confident "(the question went unanswered at the table — he ends up holding the others by strength)" over-resolves a garbled ruling.
- **Evidence**: Recap verbatim; and see item 1 — if Zalthir is hovering, the mechanism is the Potion of Flying, which nobody is shown drinking.
- **Suggested fix**: "⚠️ The GM narrates Zalthir holding two others while they 'float,' but never establishes what keeps Zalthir aloft (his Potion of Flying is never drunk on tape). Flag for GM confirmation."

## 14. Terminology — "Modrons" / "Mechanus"

- **Location**: Verbatim moments (Grygum's dust question); "Positions on the Staircase"
- **Issue**: No error found, but worth noting for the cleanup pass: the VTT glossary records `Modrums → **Modrons**` and `Mechanis, Mechanists, Machinus, methanus → **Mechanus**`. The recap uses the correct forms.
- **Evidence**: `vtt_transcription_corrections.md`; `entity_registry.yaml` registers **Mechanus** (concept) and **Primus** (modron ruler).
- **Suggested fix**: None — flagged as verified-clean.

---

## Verified clean

The following were checked against canon and are **correct**:

- **Alaundo the Seer** — spelling matches `entity_registry.yaml` (alias "Alaundo"); glossary confirms `Aluando/Alando/Alwando/Alondo/Luando/Al Londo/Elando/Londo/Orlando → **Alaundo**`.
- **Zalthir, Grygum, Thorin, Daz** — all four PC names spelled per canon and the VTT glossary.
- **Telekinesis** as Daz's spell — consistent with `party.md`, which lists **Telekinetic** among his abilities and Evoker as his subclass.
- **97 steps** — matches `world_state.md` §4 and both prep files.
- **The Vault beneath the House of Alaundo** — `entity_registry.yaml` registers both **The House of Alaundo** and **The Vault** as distinct locations, and marks **The House of Alaundo** / **The Echoes of Alaundo** as confirmed-distinct entities. The recap does not conflate them.
- **Luck point reroll** — consistent with Thorin as Fighter/Battle Master with the Lucky feat implied; no contradiction found.
- No real player names survive into the recap (Joe/Gabe/Mike/Ben/Kostadis all correctly rendered as characters/GM).
---

