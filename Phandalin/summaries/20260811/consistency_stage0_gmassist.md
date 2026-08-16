# Consistency Report — Session 2026-08-11 Recap (ch48)

## High-severity: wrong names (systematic, appear throughout)

### 1. "Ondrell B. Vance" → **Aurelan Vance**
- **Location**: Summary, Scenes (Arrival at the Counting House, Securing the Loan, Auditing the Moral Economy), NPCs, Items (Loan Paperwork)
- **Issue**: The banker's name is wrong everywhere it appears. "Ondrell" blends two known wrong-forms from the tape ("Andrell," the GM's spoken self-correction, and "Oral B. Vance," the mishearing the players riffed on). There is no middle initial in canon.
- **Evidence**: `vtt_known_additions.md` 2026-08-13: "GM ruling 2026-08-13: canonical spelling is **Aurelan**… Wrong-forms: `Oral B. Vance`, `Andrell`, `Andrew`…" The glossary maps `Andrell` → **Aurelan** and `Oral B. Vance` → **Aurelan Vance**. The dossier is `notes/npcs/aurelan-vance.md`. (The prep doc's "Ondrel Vance" was a placeholder, superseded by the ruling.)
- **Suggested fix**: Replace every instance with **Aurelan Vance** / **Aurelan**; drop the "B."

### 2. "Corin" → **Corrin**
- **Location**: Summary, Memorable Moments, Scenes (Auditing the Moral Economy), NPCs, Items (Subcommittee Charter)
- **Issue**: Misspelled throughout with one "r".
- **Evidence**: campaign_state, world_state, entity registry, and CounterForce.md all use **Corrin**; VTT glossary maps `Korn/Karwin/Corinne…` → **Corrin**.
- **Suggested fix**: Global replace Corin → Corrin.

### 3. "Linnane" → **Linene (Graywind)**
- **Location**: Summary, Memorable Moments (Brewbarry quote), Scenes, NPCs, Items (Letter of Introduction, Loan Paperwork)
- **Issue**: Brewbarry's wealth-management consultant and Lionshield Coster contact is **Linene Graywind**. "Linnane" is a transcription garble.
- **Evidence**: world_state/campaign_state (Linene Graywind, letter of introduction to the Counting House, ch46); glossary wrong-forms `Laneen, Lenain, Lineni, Linine` → **Linene**.
- **Suggested fix**: Replace all instances, including inside the quoted speech (or mark the quote *[sic]* if you preserve tape wording).

### 4. "Mountain Toes Mine" → **Mountain's Toe Gold Mine**
- **Location**: Summary, Scenes (Securing the Loan, Auditing the Moral Economy), Items (Letter of Credit)
- **Issue**: Wrong form of the mine's name.
- **Evidence**: The glossary explicitly lists `Mountain Toes Mine` → **Mountain's Toe Mine** and `Mountain Toes Gold Mine` → **Mountain's Toe Gold Mine**.
- **Suggested fix**: Replace throughout.

### 5. "Spire of the Morning Lord" → **Spire of the Morninglord**
- **Location**: Summary (×2), Scenes (Notary, Margaster Logistics), Locations
- **Issue**: The temple's canonical name is one word, "Morninglord."
- **Evidence**: Entity registry entry "Spire of the Morninglord"; ch47 summary uses it consistently; glossary maps `Morning Lord` → **Morninglord**.
- **Suggested fix**: Replace throughout.

## High-severity: factual/canon contradictions

### 6. The displacement device attributed to the Lionshield Coster
- **Location**: Summary ("the Lionshield Coster's interplanar displacement device"), Scenes — Securing the Loan ("the Lionshield Coster's shipping issues stem from a mysterious interplanar displacement device") and The Margaster Hypothesis ("sabotaged the Lionshield Coster's displacement shipping device")
- **Issue**: The manifold was never Lionshield's property. It is the **Neverwinter Commission's** Displacement Manifold, operated as a commercial service; the Lionshield Coster was its **primary client**. This ownership distinction is load-bearing for the whole Manifold/Elara/KP thread.
- **Evidence**: world_state ("The Commission… Runs the displacement manifold at the Neverwinter docks as a commercial service… The Lionshield Coster was its primary client"); ch47 summary (Cassian's exposition); entity registry ("Displacement Manifold — built and operated by the Commission").
- **Suggested fix**: Rephrase to "the Commission's interplanar displacement manifold, on which the Lionshield Coster's cheap distribution depended."

### 7. Brewbarry wearing a bathrobe
- **Location**: Summary ("rehearsing a grand speech in his bathrobe"), Scenes — Arrival ("Brewbarry enters the Counting House wearing his bathrobe")
- **Issue**: As of ch45–47 canon, Brewbarry **does not own a bathrobe** — he returned the stolen one under Zone of Truth and "still desires one." Unless he acquired one on-screen in this session, this contradicts the standing item state. It also sits oddly against the same Summary paragraph saying Vance mistook his "authentic Uthgardtian hides" for a costume — is he in hides or a robe?
- **Evidence**: campaign_state ch45 ("Brewbarry confessed stolen bathrobes/slippers and returned his"); world_state Brewbarry uncertainty list ("Bathrobe — returned but still desires one").
- **Suggested fix**: Verify against the ch48 transcript. If he genuinely wore one at the table, add a line noting he has acquired/made a new robe (this updates canon); otherwise change to his hides.

### 8. "Brewbarry Root Smasher Ogoro"
- **Location**: Memorable Moments (first quote), echoed by Summary tone
- **Issue**: Two problems. (a) "Rootsmasher" is one word per the confirmed tape reading. (b) The third name element was groped for aloud at the table (Ogolo / Ogoro / Ogonakanu) and was **deliberately left unresolved** — the recap should not canonize "Ogoro." Note also the character sheet's standing full name is "Brewbarry Root Smasher **Ogalakadu**."
- **Evidence**: `vtt_known_additions.md` 2026-08-13: "Both transcriptions agree on *Rootsmasher*; the third element… is deliberately left unresolved." party.md/world_state: "Ogalakadu."
- **Suggested fix**: Render as "Brewbarry Rootsmasher Og—" with a note, or use Ogalakadu; do not let "Ogoro" propagate into future docs.

### 9. Necklace "only recently been returned by Vukradin"
- **Location**: Summary (Boney's skepticism), Scenes — The Heir of Alagondar (last bullet), NPCs — Boney
- **Issue**: Nothing has been *returned*. Vukradin **recovered** the necklace from a sarcophagus in the Alagondar barrow at Dragon Barrow (ch33) and **still holds it** pending the claim. "Returned" inverts the custody state and muddies the actual hole in Perrin's story — the necklace was grave-goods sitting undisturbed in Lady Alagondar's tomb, so it cannot have been "lost to grave robbers a generation ago."
- **Evidence**: campaign_state Objects of Note ("Necklace of Fireballs — Vukradin (holding for claimant)… Grave goods from the Alagondar barrow at Dragonbarrow (ch33)"); prep docs ("grave-goods, not heirloom" is the designed tell).
- **Suggested fix**: "…the necklace had only recently been recovered from Lady Alagondar's own barrow by Vukradin — meaning it sat in her tomb, not in any family's hands, when Perrin's family supposedly lost it."

### 10. Subcommittee Charter described as "the party's charitable foundation"
- **Location**: Items — Subcommittee Charter (and implicitly Scenes — Auditing the Moral Economy)
- **Issue**: The subcommittee charter is the **UBT distribution-rules drafting subcommittee** (chaired by Linene Graywind under Vukradin's supervision, ch46) — a governance instrument, not a charitable foundation. The party's charitable vehicle is the separate music-studio restricted trust.
- **Evidence**: campaign_state ch46 ("Linene Graywind… took a subcommittee, under Vukradin's supervision, to draft the distribution rules"); the Rimardo audit bit specifically targets the UBT 5% cut ("laundered… through better penmanship").
- **Suggested fix**: "A document chartering the Phandalin UBT distribution-rules subcommittee…"

## Medium-severity: timeline and unverifiable claims

### 11. The booked dawn service and Neverember dinner are unaccounted for
- **Location**: Whole recap; specifically Summary and Scenes treating the Spire event as an **upcoming** "benefit concert"
- **Issue**: Per ch47's end state, the party had a **dawn performance and sermon** at the Spire scheduled for the very next morning, and a **private dinner with Lord Neverember "the following evening."** This recap covers a full day ending in the evening, treats the Spire event as future, and never mentions the dinner. Either these were rescheduled at the table (the recap should say so explicitly) or the recap has dropped two booked commitments — future sessions will trip over this.
- **Evidence**: campaign_state "Neverwinter — Immediate Schedule": items 1 and 2.
- **Suggested fix**: Verify against the transcript and add one sentence establishing where the dawn service and the Neverember dinner now sit relative to this day. Also note the recap's "benefit concert" recasts what ch47 framed as a performance-and-sermon service Valphine intends to take over.

### 12. "Elven Chainmail" item
- **Location**: Items — Elven Chainmail
- **Issue**: No holder is named, no scene mentions it, and no elven chainmail exists in any party inventory (Valphine has Mithral Chain Mail; Brewbarry has scale mail). Meanwhile the **commissioned Dragon Scale Mail** (300 gp, Lathander emblem, to be collected before leaving the city) goes entirely unmentioned in the recap. Possible garble of the armor pickup, or a phantom item.
- **Evidence**: campaign_state Tracked resources and "Dragon Scale Mail — commissioned for Brewbarry, not yet collected."
- **Suggested fix**: Verify against the transcript: who donned what? If this was the dragon scale mail pickup, correct the item name and mark the commission collected; if a genuinely new item, name the wearer.

### 13. "the Bronze Sun"
- **Location**: Scenes — Auditing the Moral Economy ("receipts for every location the party has visited, including the Bronze Sun")
- **Issue**: No establishment called "the Bronze Sun" exists anywhere in canon — not in the entity registry, world_state, or any session summary. Likely an ASR garble or a fresh invention that needs registering.
- **Evidence**: Absent from all context documents; the only near-match is "Bronze Shrine" (unvisited Leilon module content).
- **Suggested fix**: Check the transcript. If real, add to the entity registry / vtt_known_additions; if a garble, correct or cut.

## Low-severity

### 14. Wealthy client: compliment vs. mockery
- **Location**: Summary ("attempted to compliment Brewbarry on his 'commitment to the bit,' and was thoroughly ignored") vs. Scenes — Securing the Loan ("mocks Brewbarry's authentic barbarian attire… attempts to mimic him awkwardly")
- **Issue**: The two sections characterize the same beat differently (sincere fan-compliment vs. mockery). Ambiguity will confuse any future callback to this NPC.
- **Suggested fix**: Pick one framing (the ch47 precedent — the Brewbarry-aesthetic fan who genuinely doesn't realize he's talking to the real one — suggests "compliment").

### 15. "The party discovers a shuttered building…"
- **Location**: Memorable Moments (final entry)
- **Issue**: "Discovers… revealing it as the former home of the interplanar displacement device" overstates novelty — the party learned all of this from Cassian in ch47, and the recap's own Summary correctly says "recognized it immediately."
- **Suggested fix**: "The party passes… and recognizes it as…"

### 16. Boney gloss: "spent centuries researching royal family trees"
- **Location**: Memorable Moments (Boney entry)
- **Issue**: Lady Alagondar slew Azdraka "over a century ago" and Boney died guarding her sword — "centuries" (plural) likely overstates his time dead, and "recently unalived" is his long-standing self-description (party.md calls him "unalived"), not newly minted slang this session.
- **Suggested fix**: Soften to "spent his long interment" or "over a century"; optionally drop the "casually dropping modern internet slang" framing.

### 17. Notary venue vs. the designed evidence chain (GM check, not necessarily a recap error)
- **Location**: Scenes — The Notary of House Margaster; Locations — House Margaster Notary
- **Issue**: Prep staged the necklace apparatus through the **Harbor-authority** recovery office/notary parlour (the Margaster-*endowed* desk, clerk Havel Drest) — the paper trail that eventually proves the forgery. The recap presents an overtly Margaster-owned notary house. If that's how it played at the table, fine — but confirm the Drest/Harbor-authority proof line still has a home, since the "threefold rule" genealogy is the forgery the party will need to crack.
- **Evidence**: `20260623_necklace-of-fireballs-neverwinter.md`, `20260728_perrin_opening_moves.md` (Havel Drest, Harbor-authority parlour).
- **Suggested fix**: No text change required; GM should decide whether "House Margaster Notary" and the Harbor-authority desk are the same institution and record it.

### 18. Missing chapter number/title
- **Location**: Document header ("Session 2026-08-11")
- **Issue**: Convention is chapter-titled summaries (e.g., "Chapter 47: Neverwinter, Never a Dull Moment"). This is ch48 and has neither number nor title.
- **Suggested fix**: Add "Chapter 48: …" heading.

---

## Checked and consistent (no action needed)
- **"Lathander's Death"** as the band name — confirmed ch48 canon (closes the "party has no name" thread).
- **"Divine Accountants and Occasional Entertainers"** billing, folding table, velvet rope — matches the queued Rimardo/Corrin clue arriving on screen.
- **"Eastern Quay"** and **"Neverwinter Commission"** (full form) — both match the 2026-08-13 GM rulings.
- **Perrin's description** (man in his thirties, unfashionable clothes, "waiting for hours," reverence for the cause over the person) — matches prep exactly.
- **Cullen Sharpe's demeanor** (unintimidated, procedural, charming) — matches the "never drops the manners" canon.
- **200 gp mine dividend via letter of credit** — consistent with the prep's Letter-of-Credit device and the party's held mine share.
- The recap correctly does **not** surface the gnome's name (Bimble Nackle remains GM-only).