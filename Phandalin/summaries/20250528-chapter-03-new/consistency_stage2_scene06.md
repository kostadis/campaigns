# Consistency Report — Scene: "The Priest's Remains" (Chapter 3 session)

Checked against: `gm-assist.md` (parent chapter export), `campaign_state` (ch02 archive), `world_state` (ch02 archive), `party_ch02.md`, `planning_ch02.md`, `entity_registry.yaml`.

---

## A. Issues in the scene document itself

### 1. "Verbatim" provenance label is false
- **Location**: Scene summary header — *"Scene summary (from gm-assist, verbatim)"*
- **Issue**: The bullets are **not** verbatim from gm-assist. They have been expanded with material the gm-assist scene bullets do not contain: the Soma "faff about" quote, the "killed when part of the room collapsed" clause, the palm-or-announce DM question, the "beat a five" DC, the "Surrounded by thieves" line, Valphine's body announcement, and the three-rounds detail.
- **Evidence**: gm-assist's "The Priest's Remains" bullets read only: "The party navigates through collapsed tunnels, noting that digging would be required…", "…finds the skeleton of a dwarf priest…", the holy symbol bullet, "Valphine attempts to secretly pocket the holy symbol, though the rest of the party is aware of the discovery," and "Vukradin runs back to inform the dwarf prospectors…"
- **Suggested fix**: Relabel as "expanded from gm-assist against the session transcript," or visibly separate the verbatim gm-assist bullets from the transcript-sourced additions. A false "verbatim" tag will poison downstream provenance checks.

### 2. Sleight-of-hand *success* is asserted but not evidenced
- **Location**: Scene summary bullet 4 and the **[The Sleight of Hand]** block
- **Issue**: Both state the roll "succeeds." No quoted transcript span shows the roll result — only the DC being set.
- **Evidence**: Verbatim ends at GM: *"You have to beat a five."* The parent chapter's Items section says only "Valphine **attempted** to secretly pocket it," and the chapter Summary implies the symbol was still on the corpse when Vukradin left ("leaving his companions alone with the skeleton and the **glittering holy symbol**").
- **Suggested fix**: Verify the roll outcome against the full VTT. If confirmed, record the symbol (50 gp) in Valphine's inventory explicitly — right now no document says she *has* it, which will surface as a phantom-item discrepancy later. If unconfirmed, mark the theft's outcome unresolved.

### 3. Character knowledge vs. player knowledge is conflated
- **Location**: Scene summary bullet 4; **[The Sleight of Hand]**; verbatim "Surrounded by thieves"
- **Issue**: The summary says "the rest of the party is aware of the discovery" and the bracket says "the whole table watched it happen" — but the transcript establishes that **Vukradin the character explicitly has no sight-line**, and "Surrounded by thieves" is Dave's table-talk, not an in-character line. As written, a future session doc could legitimately conclude Vukradin *knows* Valphine stole a holy symbol — which contradicts his subsequent in-fiction behavior (innocently running off to report the body).
- **Evidence**: Vukradin: *"I'm way back here. I haven't seen it yet, Valphine."* Then, in-character: *"Oh, a body. Let me go tell the dwarves."* Soma's *"We know what's gonna happen"* is likewise a player prediction made *before* the roll, not a character observation.
- **Suggested fix**: Record the split explicitly: **players** all saw it; **in fiction**, Valphine palmed it, Vukradin saw nothing, and whether Soma's/Brewbarry's *characters* noticed needs a GM ruling. Tag "Surrounded by thieves" as a player aside.

### 4. "The table's collective larceny" overstates
- **Location**: Scene summary bullet 4
- **Issue**: Only Valphine attempted larceny. "Collective" is an interpretive flourish that could be read as the whole party stealing.
- **Suggested fix**: "…the table's complicity in Valphine's larceny" or similar.

### 5. "Aware of the discovery" is ambiguous
- **Location**: Scene summary bullet 4 (inherited from gm-assist)
- **Issue**: Aware of the discovery *of the symbol*, or aware *of the palming*? These have very different downstream consequences (see issue 3).
- **Suggested fix**: Specify which.

---

## B. Contradictions between this scene's transcript evidence and the parent gm-assist chapter

### 6. The "standing house rule" about Vukradin's passive perception appears fabricated
- **Location**: gm-assist **Memorable Moments** (final entry)
- **Issue**: Claims "Brewbarry and Soma both notice — but not Vukradin, who **by standing house rule** never notices a party member palming something unless the roll beats his passive perception." Nothing in the transcript supports a house rule; Vukradin's non-noticing is explained on tape by *positioning* ("I'm way back here"). Brewbarry noticing is also unevidenced — Brewbarry has no line anywhere in this scene.
- **Evidence**: Verbatim spans quoted in the scene doc; no such rule appears in any context document.
- **Suggested fix**: Delete the house-rule claim unless the GM confirms it exists. Do not let it propagate into grounding docs as table canon.

### 7. Chapter Summary's "silence" narration contradicts the tape, and reverses event order
- **Location**: gm-assist **Summary**, priest's-remains paragraph
- **Issue**: "She said nothing, and neither did they, though the silence spoke volumes" — false: Valphine spoke ("Hey, there's a body in here. Did you see this?") and Vukradin responded aloud. The Summary also has Vukradin leaving "his companions alone with the skeleton and the glittering holy symbol," implying the symbol was still in place *after* the theft attempt and that the theft preceded his departure only vaguely. Transcript order: palm-or-announce question → Vukradin disclaims sight-line → roll → Valphine's innocent announcement of the body → Vukradin departs.
- **Suggested fix**: Rewrite the Summary paragraph to the transcript's order and drop the "silence" flourish.

### 8. "Mining tunnels" contradicts the GM's on-tape correction
- **Location**: gm-assist **Locations → Collapsed Tunnels** ("A series of mining tunnels that have suffered significant cave-ins")
- **Issue**: The GM explicitly corrected this.
- **Evidence**: Soma: *"Like mining tunnels or something?"* GM: *"**No**, that they were tunnels that collapsed."* The scene doc's own summary ("caved-in passages") has it right.
- **Suggested fix**: Change to "collapsed passages/tunnels (nature unspecified — GM said not mining tunnels)."

### 9. Dazlyn's concern is internally contradicted within the chapter
- **Location**: gm-assist **Summary** vs. **NPCs → Dazlyn**
- **Issue**: The Summary says the dwarves "shouted their concerns — **not about the party's wellbeing**, but about the potential damage… to the archaeological site." The NPCs section credits Dazlyn with *"Is everybody okay there?"* — explicitly a wellbeing check, "distinct from Norbus's warning."
- **Evidence**: Registry/planning personalities support the split: Dazlyn "forthright and honest to a fault," Norbus "gruff and excessively cautious."
- **Suggested fix**: Summary should read: Norbus worried about the site; Dazlyn asked after the party.

---

## C. Cross-checks against campaign_state (ch02 archive)

### 10. Unnarrated timeline gap: the Ogre #2 cliffhanger
- **Location**: gm-assist chapter as a whole (session opening)
- **Issue**: campaign_state ends Chapter 2 with the party **mid-combat with a second ogre en route to Gnomengarde**. Chapter 3 opens with the party deep in the dwarven temple, with no narrated resolution of the ogre fight, the Gnomengarde leg, or the return to the ruins.
- **Evidence**: campaign_state: "Chapter 2 ends here — the ogre's fate… is not narrated within this chapter… the resolution belongs to whatever chapter narrates it next." Chapter 3 does not narrate it.
- **Suggested fix**: GM should confirm where the ogre resolution and the return trip actually fall (missing session material? out-of-order recap?) before regenerating forward. Do not silently backfill.

### 11. "Collect their final reward" — no such reward exists
- **Location**: gm-assist **Summary** (final paragraph) and **Scenes → Ambush on the Road** ("heading back toward town to collect their final reward")
- **Issue**: Per campaign_state, Harbin's 50 gp for the Dwarven Excavation quest was **already paid in Chapter 2**, and the sending stones — the reward for clearing the temple — were just handed over at the ruins in this very session. There is no outstanding reward in town for this quest line.
- **Suggested fix**: Confirm with the GM what, if anything, "final reward" refers to; most likely a summarizer error to be deleted.

---

## D. Minor / verify-before-trusting

- **Verbatim moments, Soma's "faff about" line**: the gloss says the line's first words "land under the GM's label," but both quote fragments are printed under Soma's label — annotation and rendering disagree. Trivial; tidy for clarity.
- **Unattributed player line**: "there's an obvious door, so we'll go with that" inside a GM span is flagged but never attributed. If it matters later (who chose the route), get a speaker ID from the sibling transcription.
- **gm-assist Spells → Starry Wisp (Vukradin)**: not checkable against the ch02 docs (no Vukradin spell list on file for this era) — per standing practice, verify against `characters/vukradin.md` before this attribution enters grounding docs.

---

**Summary**: The scene document is largely faithful to the transcript, but it (a) falsely claims verbatim provenance, (b) asserts an unevidenced roll success, and (c) blurs the player/character knowledge boundary on the theft — the single most consequential ambiguity, since the parent chapter's competing account invents a "standing house rule" the tape does not support. The parent chapter additionally contains a "silence" narration contradicted by the tape, a "mining tunnels" claim the GM corrected on-screen, an internal contradiction about Dazlyn's concern, a nonexistent "final reward," and sits on top of an unnarrated timeline gap (Ogre #2) inherited from Chapter 2.