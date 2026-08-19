# Consistency Report — "Battle with the Ochre Jellies" (Ch. 3 scene doc)

## Major Issues

### 1. Timeline conflict: the party shouldn't be in the temple yet (per campaign_state)
- **Location**: Entire scene (setting)
- **Issue**: The scene takes place inside the dwarven temple (blood-stained altar, E5), but the Chapter 2 archive ends with the party *elsewhere* — mid-combat with Ogre #2 in a mountain valley en route to Gnomengarde, with the deeper temple explicitly "not yet returned to." Chapter 3 (this session) opens in the ruins with no bridge: no ogre resolution, no Gnomengarde, no return journey.
- **Evidence**: `campaign_state` — "Ogre Encounter #2 … Chapter 2 ends here — the ogre's fate … is not narrated within this chapter"; "Current location: A narrow, steep-walled mountain valley en route to Gnomengarde." gm-assist Ch. 3 opens: "The party stood at a crossroads in the ancient dwarven ruins."
- **Suggested fix**: GM must reconcile before the archive ladder proceeds: either the hand-authored Chapter 2 reordered events (temple clearing actually preceded the Gnomengarde departure in play), or a transition is missing. Since both archive docs are flagged DRAFT and Ch. 1–2 have no VTT behind them, the likely correction is to the Chapter 2 archive's chronology, not to this recap — but this is a precision (ordering) decision requiring GM sign-off, not a silent fix.

### 2. Dazlyn/Norbus attribution swaps between the two interjections
- **Location**: Verbatim — [The Dwarves Shout from the Sidelines] vs. [The Dwarves Interject Again]; Scene summary bullet 4
- **Issue**: First interjection: Dazlyn = safety concern ("Is everybody okay there?"), Norbus = site-damage concern. Second interjection reverses it: Norbus asks "did somebody get hurt?" and Dazlyn delivers the artwork warning. One of these is almost certainly a mis-attribution.
- **Evidence**: gm-assist NPC dossier: Dazlyn — "'Is everybody okay there?' — a separate concern for the party's safety, **distinct from Norbus's warning about damage to the site**"; Norbus — "urged the party to avoid damaging the ruins." Note also that gm-assist contradicts *itself*: its Summary paragraph says the dwarves shouted concerns "not about the party's wellbeing," which conflicts with its own Dazlyn entry.
- **Suggested fix**: Verify both interjections against the VTT (authoritative tier). Standardize one dwarf per concern, or confirm the GM genuinely swapped voices mid-session; correct the gm-assist Summary paragraph either way.

### 3. Opportunity-attack causality is mechanically impossible as written
- **Location**: Scene summary, bullet 5 ("Vukradin runs to hide behind the altar, triggering an opportunity attack; Brewbarry punches the jelly…")
- **Issue**: As phrased, Vukradin's movement triggers *Brewbarry's* opportunity attack. Vukradin's movement can only provoke from the **jelly**. Per the verbatim, Brewbarry is the one making an OA (punching to avoid a slashing split) — which means a *jelly's* movement provoked it, presumably chasing Vukradin.
- **Evidence**: Verbatim [Behind the Altar]: "Brewbarry considers the opportunity attack, refusing his slashing weapon: '…I guess I should punch then.'"
- **Suggested fix**: Reword to: "Vukradin runs behind the altar; a jelly pursuing him leaves Brewbarry's reach, and Brewbarry takes the opportunity attack as a punch (four damage) rather than risk splitting it." Verify the trigger against the transcript.

### 4. Initiative order contradicts the "First Split" placement
- **Location**: Verbatim — [Initiative] followed by [The First Split]
- **Issue**: The doc says the jelly's 17 "beat the party," yet Brewbarry "opens" with his halberd before the jellies' pseudopods. If the jelly won initiative outright, the pseudopods come first.
- **Evidence**: gm-assist's scene split resolves this: the halberd strike and split belong to the *previous* scene ("Ambush at the Blood-Stained Altar" — jelly appears, Brewbarry attacks, it splits), and "Battle with the Ochre Jellies" begins with "The two ochre jellies attack the party."
- **Suggested fix**: Either move [The First Split] before [Initiative] (pre-initiative strike), or soften "beating the party" — check the transcript for the actual sequence.

## Moderate Issues

### 5. "Shoved diagonally into a corner" inverts the pushback geometry
- **Location**: Scene summary, bullet 3 (Thunderwave)
- **Issue**: The summary says a jelly was "shoved diagonally **into a corner**." The verbatim shows the opposite: the GM tried to stop the push at 5 ft "'cause there's nowhere to go," and Vukradin's diagonal correction was so the jelly could travel the full 10 ft *away from* the wall.
- **Evidence**: GM: "pushed back five feet, 'cause there's nowhere to go." Vukradin: "I would've been angling it up… so I think he goes diagonally."
- **Suggested fix**: "…one pushed diagonally to clear the wall after Vukradin corrected the angle."

### 6. "One down, three to go" doesn't match the jelly count
- **Location**: Scene summary, bullet 8; Verbatim [Rage and the Critical]
- **Issue**: At the moment of Brewbarry's kill, three jellies exist (the split pair + the ceiling drop). Killing one leaves two — "three to go" implies four on the board. The quote is verbatim table speech, but the summary repeats it without comment, which could seed a phantom fourth jelly in future docs.
- **Evidence**: Doc's own sequence: one jelly splits into two (Brewbarry's halberd), a third drops from the ceiling; no fourth appears until the later Starry Wisp split.
- **Suggested fix**: Keep the quote but annotate it (player miscount, or check the map/transcript for an unrecorded fourth jelly). Don't let downstream docs derive a jelly count from this line.

### 7. Split attributed to radiant damage — a house mechanic being silently canonized
- **Location**: Scene summary ("the eight-point hit drives the last big jelly below half and splits it in two"); Verbatim [Starry Wisp… and the Second Split]
- **Issue**: RAW, ochre jellies split only from slashing (or lightning) damage — which is exactly the fight's own premise (Brewbarry punching to avoid splits, Vukradin's arcana recall about piercing). A radiant hit causing a split contradicts that logic. The GM's actual line is a vague ruling, not a mechanism.
- **Evidence**: GM: "He's probably split by now Yeah, he splits in two." Contrast Vukradin's recall: "piercing them did not seem to split them in half like the slashing did."
- **Suggested fix**: Reword to "the GM ruled the weakened jelly split" without attributing causation to the radiant damage, or confirm with the GM whether "split at half HP" is a deliberate house rule worth recording.

### 8. "Your plus one mace is heavily corroded" — untracked magic item
- **Location**: Verbatim [Starry Wisp, Poison Spray, and the Second Split] (Soma quote)
- **Issue**: No context document gives Valphine a +1 mace — party_ch02 lists only a baseline mace/hand crossbow, and a +1 weapon at a ~level-1–2 party three sessions in is a red flag. Most likely table humor about ooze corrosion, but if taken literally this quote either fabricates an item or implies an item was damaged/destroyed off the books.
- **Evidence**: party_ch02, Valphine: "Mace and/or hand crossbow (baseline kit per character sheet)." No +1 mace anywhere in entity_registry.yaml.
- **Suggested fix**: Confirm with GM whether this was a joke. Do not promote "+1 mace" (or its corrosion) to any inventory or grounding doc without that confirmation.

## Attribution / Transcript Hygiene Issues

### 9. "Hey, he healed me very well, though" — line split across the wrong speakers
- **Location**: Scene summary bullet 10; Verbatim [Healing Word and the One-Point Flame]
- **Issue**: The line starts in Vukradin's block and is "completed" by Soma — but the *healed* character was Soma ("I'm back to 11"), so the whole line is almost certainly Soma's, split by a transcript block boundary. Also, "he" refers to Gary the player; Valphine is female, and leaving this unglossed invites a future pronoun error for Valphine.
- **Evidence**: Verbatim: Soma — "Hey, I'm back to 11. Thank you"; the doc itself notes the truncation ("continues into the next block").
- **Suggested fix**: Attribute the full line to Soma and gloss "he" as the player (Gary), not Valphine.

### 10. "Well done, Gary" inside "Valphine's own block" — and GM-block diarization throughout
- **Location**: Verbatim [Valphine's First Natural One]; also every "inside a GM-labeled block" note (Brewbarry's turns, Valphine's turns, Healing Word)
- **Issue**: Gary *is* Valphine's player; a line addressed to "Gary" sitting in Valphine's block is either self-mockery or a mislabeled speaker. More broadly, the recurring pattern of Brewbarry's and Valphine's actions resolving "inside GM-labeled blocks" indicates VTT speaker-label merging — it should **not** be read as evidence Stéphane was absent (Zoom VTTs use inline `Name:` labels and naive greps drop Stéphane's accented name, faking absent-player signals).
- **Evidence**: Doc's own repeated annotations; known VTT speaker-label pitfall for this table.
- **Suggested fix**: Verify speaker labels against the raw VTT before any future doc asserts who was present or who spoke these lines; treat the block labels as unreliable in this recap.

### 11. "Lucrotten" — new Vukradin garble not in the glossary
- **Location**: Verbatim [Starry Wisp, Poison Spray, and the Second Split]
- **Issue**: The doc correctly identifies "Lucrotten" as a transcript garble of Vukradin, but this wrong-form isn't in `vtt_transcription_corrections.md` (the row has ~130 variants; not this one).
- **Evidence**: Vukradin wrong-forms list contains "Lucradine, Lucardin, Lukerdin…" but no "Lucrotten."
- **Suggested fix**: Propose `Lucrotten → Vukradin` as a glossary candidate — confirm with the user before adding, per the standing spell-pass protocol.

### 12. Duplicated/corrupted text fragment
- **Location**: Verbatim [Starry Wisp, Poison Spray, and the Second Split]
- **Issue**: "**Soma** — *environmental tex**Soma** — *environmental texture on the split*" — a copy-paste duplication corrupts the speaker header.
- **Evidence**: Visible in the doc text.
- **Suggested fix**: Delete the truncated first fragment, keeping the complete header and quote.

## Verified Clean (no action)

- All damage/HP arithmetic checks out internally: 12 dmg → Brewbarry at 1 hp; Soma 3 + 8 = 11, −10 = 1, then downed; 13-hp jelly splitting 7/6; 1+3 punch = 4; crit 7×2 = 14; Thunderwave 8 apiece (2d8), Healing Word 8 (2d4+3), Sacred Flame 6 and min-1 (1d8), Dissonant Whispers 10 (3d6), Starry Wisp 4 and 8 (1d8), Earth Tremor 5 vs DC 13.
- Monster math matches 5e ochre jelly: AC 8, DEX −2 initiative, +4 pseudopod, slashing immunity/split, no stun immunity, jellies on the E5 temple ceiling (entity registry).
- Spell↔caster attributions all match class/race: Stone's Endurance (goliath Brewbarry ✓), Thunderwave/Dissonant Whispers/Starry Wisp (bard ✓), Sacred Flame/Healing Word (cleric ✓), Earth Tremor/Poison Spray (druid ✓). Shell Defense 17+4 = AC 21 ✓.
- All mechanics are consistent with a low-level party — nothing from the level-5 sheets (Dragon Slayer Sword, Silver Tongue, Boney, arc scores) leaks backward into this snapshot.
- Setting details (blood-stained limestone altar, Abbathor temple, dwarves foreshadowed oozes in Ch. 2) match campaign_state and the entity registry.