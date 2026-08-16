# Consistency Report — Chapter 48: "The Only Viable Shipper"

## Errors & Contradictions

### 1. Cullen Sharpe placed at the notary — internal contradiction
- **Location**: Summary (para 8, "a look from Cullen Sharpe made him think better of it") and NPCs → The Fixer ("a look from Cullen Sharpe settling the matter")
- **Issue**: Cullen is described as present at the House Margaster Notary standoff — but the same recap introduces him at the Eastern Quay as "the smooth-talking house representative in the green suit **the party had last seen extorting Lord Cassian**" (i.e., not seen since ch47). Both cannot be true.
- **Evidence**: The Scenes section for "The Notary of House Margaster" has the fixer "reach for his weapon before thinking better of it" with no Cullen. The parallel gm-assist.md export of the same session also has no Cullen at the notary. Prep (`20260728_perrin_opening_moves.md`) explicitly left Cullen's presence at the handoff as an open decision, defaulting to deniable.
- **Suggested fix**: Remove "a look from Cullen Sharpe" from the Summary and the Fixer's NPC entry (the fixer simply thought better of it), or — if the tape shows Cullen was there — correct the Eastern Quay line ("last seen extorting Lord Cassian") instead. Verify against the VTT.

### 2. Don-Jon Raskin listed as a current mine shareholder
- **Location**: Items → Letter of Credit ("the party, the Falcon, and Don Jon hold shares")
- **Issue**: Don-Jon is dead. He cannot currently hold shares.
- **Evidence**: campaign_state: "Don-Jon killed by dwarves (Stonetallow clan)… Safe delivery failed" (ch31); "Party holds Don-Jon's share of the mine." party.md: "Mountain's Toe Gold Mine shares (Brewbarry and Falcon)."
- **Suggested fix**: "…the party (holding the late Don-Jon Raskin's share) and the Falcon hold shares." If the Commission's ledger comically still lists Don-Jon, mark it as the ledger's error, not fact.

### 3. Soma gendered male
- **Location**: Scenes → The Shut Down Shipping Hub ("Soma, won over despite **himself**")
- **Issue**: Soma is female.
- **Evidence**: party.md: "By tortle standards, Soma is old. **She** is patient, maternal…"; "Declared an honorary citizen of Phandalin so **she** could qualify."
- **Suggested fix**: "won over despite herself."

### 4. "Ser Kaelen told me to stay away" — likely misattributed warning
- **Location**: Summary (para 4) and Scenes → The Margaster Hypothesis
- **Issue**: No campaign record has Ser Kaelen warning the party away from House Margaster. The only documented "stay away" warning is **Lord Cassian's**, and it concerned **the Commission**, not Margaster. Kaelen's actual Margaster connection is the opposite: he unknowingly routed the necklace claim through a Margaster-compromised source.
- **Evidence**: campaign_state (ch47): Cassian "warning that 'when it comes to the Commission, one should keep one's distance.'" world_state: "Ser Kaelen located him in good faith and does not know" the source is Margaster-connected.
- **Suggested fix**: If the tape confirms Vukradin said it, keep the quote but annotate it as Vukradin's (probably mistaken) recollection — do not let downstream docs record "Kaelen warned the party about Margaster" as fact.

### 5. Necklace of Fireballs described as belonging to Lady Alagondar herself
- **Location**: Summary (para 6), NPCs → Boney, Items → Necklace of Fireballs ("Boney attests it belonged to Lady Alagondar herself")
- **Issue**: The registered provenance fact is that the necklace was sealed with a **dead wizard** in the Adventurers' Sepulcher (DIP area D7) — a room inside the Dragon Barrow — not interred with Lady Alagondar personally. Boney's on-tape attribution may be a deliberate GM retcon, but the recap states it flatly.
- **Evidence**: entity_registry, Necklace of Fireballs: "FACT (provenance): magic item sealed with the dead wizard in the sarcophagus of the Adventurers' Sepulcher (DIP D7)… Retrieved by VUKRADIN in ch31." (Note also a context-internal conflict: world_state's Objects table says ch33; the registry says ch31 — not the recap's fault, but worth settling.)
- **Suggested fix**: GM ruling needed — either canonize Boney's attribution (necklace = Lady Alagondar's personal grave-goods) and update the registry, or soften the recap to "recovered from her barrow" without asserting personal ownership. "Recovered from Lady Alagondar's own barrow" is safe either way; "belonged to Lady Alagondar herself" is the contested part.

## Questionable — Verify Against Tape

### 6. Elven Chainmail "acquired this session" with no acquisition scene
- **Location**: Items → Elven Chainmail; Summary (para 6); Scenes → The Heir of Alagondar
- **Issue**: The Items entry claims the armor was "acquired by Brewbarry this session," but no scene records any acquisition — the narrative simply has him "don the elven chainmail" (definite article, as if already owned). Possible confusion with existing party armor (e.g., the Mithral Chain Mail from Butterskull, freed up now that Valphine wears White Dragon Plate +1 per her refreshed sheet). The commissioned dragon scale mail (300 gp, "collect before leaving the city") also goes entirely unmentioned, which compounds the oddity of a second new suit of armor.
- **Evidence**: campaign_state: "Dragon Scale Mail Commissioned (ch46)… To be collected before the party leaves the city." party.md KNOWN GAP note: `characters/brewbarry.md` (refreshed 2026-08-13, post-session) shows Elven Chain Mail — so the sheet supports the item existing, but not its origin.
- **Suggested fix**: Verify on tape where the elven chain came from; either add the acquisition beat or reword "acquired this session" to reflect its actual source (hand-me-down, prior unrecorded gear, etc.). Add a GM reminder that the dragon scale mail remains uncollected.

### 7. Valphine vs. Vukradin — who wanted Perrin inside the temple
- **Location**: Summary (para 9) and Locations → Spire of the Morninglord (attributed to **Valphine**, with quote "I definitely want to see him set foot within the temple")
- **Issue**: The parallel gm-assist.md export of the same session attributes this satisfaction to **Vukradin**. The two exports contradict each other.
- **Evidence**: gm-assist.md: "a venue that Vukradin noted with some satisfaction would require Perrin to set foot inside a temple."
- **Suggested fix**: The detailed recap carries a direct quote for Valphine (and it fits her character), so it is probably the corrected version — but confirm on the tape and reconcile the two exports so only one attribution survives.

### 8. "The Bronze Sun" — unknown establishment
- **Location**: Scenes → Auditing the Moral Economy ("Valphine spots one from the Bronze Sun, which is immediately disclaimed by its owner")
- **Issue**: No establishment called "the Bronze Sun" exists anywhere in campaign canon (entity registry, world_state, location docs, VTT glossaries). Possible transcription garble or an on-the-fly coinage. "Disclaimed by its owner" is also ambiguous (disclaimed by Valphine? by the establishment's owner?).
- **Evidence**: Absent from entity_registry.yaml, world_state Locations, docks_district.md, and vtt_known_additions.md.
- **Suggested fix**: Check the tape. If real, add to vtt_known_additions and clarify the "disclaimed" clause; if a garble, correct via the glossary.

### 9. Cullen's claim that "Ser Kaelen reached out to House Margaster"
- **Location**: Summary (para 9) and Scenes → Confrontation at Margaster Logistics
- **Issue**: Taken literally, this contradicts GM canon (Kaelen matched the necklace in good faith via a recovery-office source he does not know is Margaster-compromised; he did not knowingly contact Margaster). As in-character spin from Cullen it is fine — but future docs must not absorb it as fact.
- **Evidence**: campaign_state: "Ser Kaelen located him in good faith and does not know"; prep: the route runs through clerk Havel Drest at the Margaster-endowed desk.
- **Suggested fix**: Annotate as Cullen's assertion (and possibly deliberate misdirection), not established fact.

## Timeline Issues

### 10. The dawn service and the Neverember dinner are both missing from this day
- **Location**: Whole document (structural)
- **Issue**: Per ch47, the party's booked schedule was (1) **dawn** performance-and-sermon at the Spire of the Morninglord the morning after arrival, then (2) **private dinner with Lord Neverember "the following evening."** Ch48 covers a full day (morning Counting House → "as the evening drew to a close" at the Eastern Quay) — which is exactly dawn-service morning and dinner evening — yet neither event is mentioned, and the Spire concert is repeatedly described as still "upcoming."
- **Evidence**: campaign_state, "Neverwinter — Immediate Schedule": "1. Dawn performance and sermon at the Spire… 2. Private dinner with Lord Dagult Neverember, the following evening." party.md repeats both. Ch47 recap: "Next: dawn service at the Spire of the Morninglord, then the Counting House."
- **Suggested fix**: Establish at the table (and record) whether the dawn service and dinner were postponed, rescheduled, or silently skipped. Related ambiguity: the ch47 "dawn performance and sermon" is now consistently called a "**benefit concert**" — confirm these are the same event rebranded, not two separate Spire commitments.

## Minor / Low Priority

### 11. "Paperwork found authentic" must not overturn the forged-provenance canon
- **Location**: Summary (para 8), Items → Margaster Notary Paperwork ("found the paperwork genuinely authentic")
- **Issue**: Not an error in itself — the *notarization* being genuine is consistent with "forgeries happen off-site and merely get notarized here" — but future consistency passes could misread "authentic" and "Perrin was not lying about the documentation" as canonizing Perrin's claim. GM canon remains: the underlying provenance is a Margaster-routed forgery.
- **Evidence**: campaign_state: "**GM (not known to party): the provenance match was routed through a Margaster-connected source and is forged.**"
- **Suggested fix**: Add a GM-only annotation to the item entry: authentic notarization of a forged claim.

### 12. Boney's "a few hundred years" in the tomb
- **Location**: Summary (para 6), Memorable Moments, NPCs → Boney
- **Issue**: Quoted dialogue says Boney was entombed "a few hundred years" and researched "over centuries"; canon dates Lady Alagondar's dragon-slaying (and thus roughly Boney's death) to "over a century ago."
- **Evidence**: entity_registry, Lady Tanamere Alagondar: "killed Azdraka the green dragon **over a century ago**."
- **Suggested fix**: Leave the quotes as spoken (Boney exaggerating is in character), but don't let "centuries" harden into a dated timeline in grounding docs without a GM ruling.

---

**Everything else checks out**, including: the band name "Lathander's Death" (confirmed canonical, closes the ch47 no-name thread); Aurelan Vance's name and identity (matches the 2026-08-13 GM ruling; the recap correctly avoids all transcription garbles); the Neverwinter Commission owning the mine (matches the 2026-08-13 ruling and the registry's "Neverwinter business consortium"); the 200 gp dividend; Rimardo & Corrin's billing, table, velvet rope, and letter from the Falcon (matches ch45 canon and the queued Counterforce clue finally landing on screen); the Brewbarry full-name footnote (correctly handles the Ogalakadu/Ogolakanu discrepancy per ruling); party level 7; Eastern Quay spelling; Boots-of-Elvenkind and Falcon canon untouched; and Perrin's first-contact details (waited hours, letter read ~40 times, fire at "lineage") matching the session prep.