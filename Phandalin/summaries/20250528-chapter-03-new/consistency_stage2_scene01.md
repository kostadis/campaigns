# Consistency Report — "Ambush at the Blood-Stained Altar"

## Issues Found

---

### 1. Timeline gap: the party should be mid-ogre-fight en route to Gnomengarde, not in the temple

- **Location**: Entire scene (Scene summary / all sections)
- **Issue**: This scene (Chapter 3, session 2025-05-28) opens with the party deep in the dwarven excavation, exploring toward the blood-stained altar. But the Chapter 2 archive ends with the party **mid-combat with Ogre #2 in a mountain valley en route to Gnomengarde**, with the temple interior explicitly unexplored. Nothing in Chapter 3 (per the gm-assist doc) resolves the ogre or narrates the return trip to the excavation.
- **Evidence**: `campaign_state`: "Ogre Encounter #2 … **IN PROGRESS, unresolved at chapter's end**"; "Party Current Situation: … mid-combat with a hungry ogre"; "Dwarven Temple — deeper interior unexplored." gm-assist Ch. 3 opens: "The party stood at a crossroads in the ancient dwarven ruins."
- **Suggested fix**: Needs a GM ruling on sequencing before anything regenerates forward. Either (a) the hand-authored Chapter 2 prose (no VTT exists behind it, per the archive caveats) placed the Gnomengarde departure/ogre fight too early, or (b) the ogre resolution + return trip is a genuinely missing scene. Do not let a downstream pass silently backfill either version.

---

### 2. "Gary covering for the absent Stéphane" is asserted, not evidenced

- **Location**: "Brewbarry's Halberd and the Split" (intro bullet)
- **Issue**: The claim that Stéphane was absent and Gary ran Brewbarry has no support in the quoted material — no Brewbarry player line appears anywhere in the excerpt (the GM narrates Brewbarry's whole turn: "All right, Brewbarry So an 11 hits maybe?"). The standing arrangement makes this *plausible*, but plausible-because-of-a-standing-rule is exactly how a false absence gets canonized. There is a known failure mode where naive speaker-label greps drop Stéphane's accented name and fake an absent-player conclusion.
- **Evidence**: Phandalin CLAUDE.md establishes the *arrangement* ("Gary covers when Stéphane is absent") but nothing in the transcript excerpt establishes the *absence* for this session.
- **Suggested fix**: Verify Stéphane's presence in the 2025-05-28 VTT with an accent-safe speaker-label check before keeping this parenthetical. Until verified, soften to "Brewbarry's turn (player at the keyboard unconfirmed)."

---

### 3. "Scene summary (from gm-assist, verbatim)" is not verbatim

- **Location**: Scene summary header
- **Issue**: The gm-assist scene has four plain bullets. This document's version augments every bullet with transcript quotes and adds an **entirely new bullet** (the initiative roll of 19/17) that does not exist in gm-assist at all. Labeling this "verbatim" corrupts provenance — future passes will treat the additions as gm-assist output.
- **Evidence**: gm-assist "Ambush at the Blood-Stained Altar" bullets: "The party decides to investigate a hallway rather than a secret door." / "A blood-stained altar is discovered…" / "An ochre jelly appears right next to the party." / "Brewbarry attacks the jelly with a halberd…" — no quotes, no AC, no initiative bullet.
- **Suggested fix**: Relabel to something like "from gm-assist, augmented with transcript detail," or restore the true verbatim bullets and keep the additions in the Verbatim moments section only.

---

### 4. Soma referred to as "he"

- **Location**: Final verbatim gloss ("*discovering he'd been reading the wrong character sheet for initiative*")
- **Issue**: Soma is consistently "she/her" in every grounding document. The gloss either misgenders the character or silently switches referent to the player (Wade) under a **[Soma]** speaker tag — ambiguous either way, and the kind of thing that seeds pronoun drift in later narration.
- **Evidence**: `world_state`: "trained late in life by a visiting elven druid named Meril, who left **her** an ash staff"; `campaign_state`: "Soma privately noted a white-dragon rumor to **herself**."
- **Suggested fix**: Either "discovering **she'd** been reading…" (character register) or "discovering **Wade** had been reading…" (explicit player register).

---

### 5. "Varas' character sheet" — unregistered proper noun, probable garble

- **Location**: Final verbatim quote ("I was using Varas' character sheet")
- **Issue**: "Varas" appears nowhere in `entity_registry.yaml`, the VTT correction glossary, or any grounding doc. It is presumably the name of a real character sheet Wade had open, garbled by the transcript. The nearest glossary neighbors (Sarvas/Avarus → **Savras**) don't make sense as a character sheet. Unregistered names recurrently false-flag on every future consistency pass (cf. the Bronze Sun precedent).
- **Evidence**: No match in any provided context document.
- **Suggested fix**: Get a GM ruling on what "Varas" actually is (another PC's sheet? a retired character of Wade's?), then either add the correction pair to `vtt_transcription_corrections.md` or promote a new canonical. Until ruled, annotate the quote in-doc as an unresolved garble so it doesn't get treated as a name.

---

### 6. Merged quotes create attribution ambiguity in the summary bullets

- **Location**: Scene summary bullets
- **Issue**: Three bullets fuse quotes from different speakers into a single breath:
  - "big old pile of mustard" (**Soma**) is run together with "There's an AC you don't see every day" (**Vukradin**), reading as one speaker.
  - "We got outranked by a fricking ochre jelly" (**Vukradin**) is paired with "It's been like eight years…" — which the tape splits across Soma's and Vukradin's lines.
  - "Well, that's crap" (**Soma**, per the tape) is appended to the Brewbarry-attack bullet, inviting misattribution to Brewbarry.
- **Evidence**: The document's own Verbatim moments section, which attributes each line correctly.
- **Suggested fix**: Add speaker tags to quotes in the summary bullets, or strip quotes from the summary entirely and rely on the Verbatim section.

---

### 7. Minor unresolved garbles

- **Location**: Verbatim moments
- **Issue / fixes**:
  - **"Devar, are you-"** — flagged in-doc as garbled but not resolved. Almost certainly "**Dave**, are you-" (the reply comes on Vukradin's/Dave's line). Safe non-word; a glossary candidate — but per the spell-pass rule, confirm with the GM before adding any new mapping.
  - **"Flashing"** (for *slashing*) — correctly flagged in-doc. Do **not** add to the glossary: "flashing" is a common English word and would be a landmine row per the glossary's own notes.

---

## Verified as Consistent (no action needed)

- **Halberd** matches Brewbarry's established kit (`party_ch02`, `world_state`).
- **Ochre jelly mechanics** are rules-correct: AC 8, DEX-based −2 initiative, immunity to slashing damage, and splitting when hit by slashing. 52 HP is above average (45) but within rollable range.
- **The ooze encounter pays off Dazlyn's foreshadowing** ("I think we saw some oozes in there, but I could be wrong" — `campaign_state`), and the blood-stained altar matches the entity registry (E5: "bloodstained limestone altar and ochre jellies on the ceiling").
- **The secret door debate** matches the archive's "unexplored secret door" thread from the Chapter 2 temple visit.
- **No anachronisms**: Boney, arc scores, and later-campaign machinery are correctly absent from this early-chapter scene.