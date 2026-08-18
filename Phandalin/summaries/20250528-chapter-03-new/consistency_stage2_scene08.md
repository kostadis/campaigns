# Consistency Report — "The Hall of Greed" scene doc (ch. 3)

## 1. Timeline: this scene contradicts the Chapter 2 archive's ending

- **Location**: Entire scene (setting/premise)
- **Issue**: The scene takes place deep inside the Abbathor temple, but `campaign_state` (Ch. 2 archive) ends with the party *mid-combat with Ogre #2 en route to Gnomengarde*, and explicitly states the deeper temple is "an open thread the party has not returned to." Neither this scene nor the parent gm-assist Ch. 3 recap narrates the ogre's resolution or a return trip from the Gnomengarde road. One of the two documents has the sequence wrong.
- **Evidence**: campaign_state: "Ogre Encounter #2 … IN PROGRESS, unresolved at chapter's end… the resolution belongs to whatever chapter narrates it next." gm-assist Ch. 3 opens "at a crossroads in the ancient dwarven ruins" with no bridge.
- **Suggested fix**: GM review needed (the Ch. 2 archive is flagged DRAFT). Either the archive misplaces the Gnomengarde departure/ogre fight, or Ch. 3 needs a one-line bridge noting how the party got back to the temple. Do not let the next regeneration pass silently reconcile this.

## 2. Spliced quote reverses the actual utterance order

- **Location**: Scene summary, "demon statue" bullet
- **Issue**: The bullet renders it as: *"A demon statue holding the glowing gem... I think I've seen that picture in the Dungeon Master's Guide."* On the tape the order is reversed — the DMG line comes first, the "demon statue" naming comes second — and they are separate utterances, as the doc's own verbatim section correctly shows.
- **Evidence**: Verbatim section: Vukradin: "I think I've seen that picture in the Dungeon Master's Guide…" → (cross-talk) → "A demon statue holding the glowing gem."
- **Suggested fix**: Reorder the summary splice to match utterance order, or quote only one fragment.

## 3. "Valphine's verdict" is an inferred attribution — and conflicts with GM's stated fact

- **Location**: Scene summary + Verbatim "[Emerald or Glass?]"
- **Issue**: (a) The verdict line "a worthless glass gem, I think it is" sits under the **GM's label** on the tape; attributing it to Valphine is a reasonable inference (Vukradin addresses her immediately before), but the summary states it flatly while only the verbatim section marks it as folded. (b) More importantly for future sessions: the GM said out-of-character **"It's an emerald"** before the nat-1 roll. "Worthless glass" is the *character's* mistaken belief, not the fact.
- **Evidence**: GM block: "It's an emerald. Um, roll your investigation…" then "A one… this is an emerald, but it could also just be glass."
- **Suggested fix**: Keep the Valphine attribution but mark it inferred in the summary too, and add an explicit note: *gem is an emerald per GM; party believes it is glass (nat-1 investigation)*. Otherwise a future doc will record "worthless glass gem" as canon.

## 4. "Faint magical aura" is an embellishment

- **Location**: Scene summary, Detect Magic bullet
- **Issue**: "Valphine detects a faint magical aura" — the tape only supports "some magic on the gem." "Faint" appears in the gm-assist Ch. 3 summary too, but not on the tape, and aura strength/school can matter for later identification.
- **Evidence**: GM: "All right, you do sense some magic on the gem."
- **Suggested fix**: Drop "faint" or mark it as summarizer wording.

## 5. "The party identifies the area" — actually GM narration

- **Location**: Scene summary, Abbathor bullet
- **Issue**: The identification of the site as sacred to Abbathor is delivered by the GM after the perception roll; no character performs an identification. Minor, but it's an attribution shift the verbatim section itself contradicts (Soma jokes "Who's Abbathor?").
- **Evidence**: GM: "you get the sense of it being some kind of sacred religious… location important to the clerics of Abbathor."
- **Suggested fix**: "The GM reveals the area was once important to the clerics of Abbathor."

## 6. Ambiguous quote placement: "You save those for the out of combat rolls, I see"

- **Location**: Scene summary, perception bullet
- **Issue**: The quote is appended to the sentence about Valphine's nat-20 with no speaker, so it reads as possibly Valphine's line. It's Soma needling Gary (verbatim section has it right).
- **Suggested fix**: Attribute it in the summary: *(Soma, to Gary)*.

## 7. Unglossaried garble tokens: "Grym" and "Hoop"

- **Location**: Verbatim "[Entering the Sacred Site]" and "[Detect Magic on the Gem]"
- **Issue**: Both are quoted-as-spoken (correct conservative handling), but neither appears in `vtt_transcription_corrections.md` or `entity_registry.yaml`. "Grym" sits where the GM addresses the player who rolled the nat 20 (plausibly *Gary*); "Hoop" sits where the GM is sorting out which PC is inspecting (plausibly a garbled player/character name). Per standing protocol, no mapping should be written without GM confirmation.
- **Suggested fix**: Queue both for a GM ruling in the next spell-pass; until then leave quoted as spoken. Do not silently gloss.

## 8. Unattributed folded fragment: "Keep encouraging us that we can do anything"

- **Location**: Verbatim "[The Mold Earth Canvass]", Vukradin's first block
- **Issue**: The doc notes "the tape folds a second fragment into it" but leaves the fragment sitting under Vukradin's name. The line doesn't obviously belong to his canvass and no speaker candidate is offered — unlike the other folds, which are hedged with "(apparently X's)."
- **Suggested fix**: Mark it explicitly as unattributed cross-talk, matching the doc's convention elsewhere.

## 9. Anachronism watch: "tanzanite"

- **Location**: Scene summary + Verbatim "[Emerald or Glass?]"
- **Issue**: Tanzanite is a real-world gem named after Tanzania (1967) — an anachronism in Faerûn. Peridot is fine (standard D&D gem list). Precedent (Ch. 48 stage-3 pass: dreamlily, cadet house, Aurum Bee Vance) is that quoted table dialogue stays as spoken, but real-world references don't get promoted into narration.
- **Suggested fix**: No change to the quote; flag for the GM so "tanzanite" doesn't migrate into narrative prose or item records.

## 10. Minor verification note: Mold Earth is a first appearance for Soma

- **Location**: Scene summary + "[The Mold Earth Canvass]"
- **Issue**: Soma's Ch. 2 "spells seen in play" list is Thorn Whip / Poison Spray / Ice Knife; Mold Earth is new. It's table-confirmed on the tape ("I do. Look at my character." + GM approval), so this is not an error — just verify against `characters/soma.md` before any doc treats it as sheet-canon, per the standing spell-caster-attribution rule.
- **Suggested fix**: One-time check of the character sheet; no doc change needed.

## 11. Informational: the registry describes the statue as trapped

- **Location**: Scene summary (gem left in place)
- **Issue**: Not an error in the doc — `entity_registry.yaml` E11 says "trapped statue of a horned dwarf holding a glowing green gem." The party never touched the gem, so nothing triggered, and the doc correctly contains no trap knowledge. Flagged only so a future pass doesn't "helpfully" add the trap to party-facing text.
- **Suggested fix**: None; keep the trap out of party-knowledge documents.

---

**Everything else checks out.** Caster attributions (Soma → Mold Earth, Valphine → Detect Magic/perception/investigation), the GM's north/south statue correction and how the doc documents it, the "in its hands" (not "eyes") final description, the dig-comes-up-empty result, the Abbathor spelling, and the absence of Boney are all consistent with the tape, gm-assist Ch. 3, and the entity registry. Brewbarry has no lines in this scene, which is unremarkable for an exploration beat — he is active elsewhere in the chapter.