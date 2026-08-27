# Consistency Report — "New Chapter 3" vs. Chapter 2 Archive Docs

**Caveat on authority:** the Chapter 2 archive docs are explicitly marked *DRAFT, pending GM review*, while this recap appears to derive from an actual session transcript (`summaries/20250528-chapter-03-new/`). Several conflicts below may therefore be errors in the *archive*, not the recap — each flagged item states which direction the fix likely runs, but the GM must adjudicate.

---

## Major continuity contradictions

### 1. The recap opens in the wrong place — the Ogre #2 fight and the Gnomengarde detour have vanished
- **Location**: Summary (opening paragraph); entire document
- **Issue**: Chapter 2 ends with the party mid-combat with a second ogre in a narrow mountain valley *en route to Gnomengarde*. This recap opens with the party already inside the dwarven ruins with no mention of the ogre's resolution, the Gnomengarde trip being abandoned/postponed, or the return journey to the ruins.
- **Evidence**: `campaign_state` — "Ogre Encounter #2 … **Chapter 2 ends here — the ogre's fate … is not narrated within this chapter**"; Party Current Situation: "Current location: A narrow, steep-walled mountain valley en route to Gnomengarde, mid-combat with a hungry ogre."
- **Suggested fix**: GM must adjudicate the true session ordering. Either (a) the temple-clearing session actually happened *before* the Gnomengarde departure and the hand-authored Chapter 2 prose runs ahead of the session timeline (plausible — see issue 3), in which case the ch02 archive's ending needs correction; or (b) the recap is missing its opening (ogre resolution + travel back to the ruins) and should have a bridging passage added. Do not let a regenerated chapter ship with this gap.

### 2. Sending stones: already in the party's possession per Chapter 2, but paid out at the end of this session per the recap
- **Location**: Summary ("The party demanded their sending stones…"; "…handed over the sending stones, the party's hard-earned reward"); Scenes → Amateur Archaeologists; Items → Sending Stones
- **Issue**: The recap stages the sending stones as withheld until the ruins are cleared, then handed over as end-of-job payment. The Chapter 2 archive says the stones were **given in advance** as goodwill, at Valphine's suggestion.
- **Evidence**: `campaign_state` → "Sending Stones — **in party's possession**. Given by Dazlyn and Norbus as advance goodwill/incentive for the deeper-temple job, at Valphine's suggestion"; also listed under Party "Key resources." Conversely, `entity_registry.yaml` → sending stones: "offered by Dazlyn and Norbus **as reward for clearing the temple**" — which matches the recap.
- **Suggested fix**: GM ruling required. If the transcript supports the end-of-job handover, correct the ch02 archive (move stones from "possessed" to "promised") — the registry already agrees with the recap. Whichever way it goes, pick one and record it, since "who holds the stones during the temple crawl" affects any regenerated Chapter 3 prose.

### 3. "Heading back toward town to collect their final reward" — no outstanding town reward exists per Chapter 2
- **Location**: Scenes → Ambush on the Road ("heading back toward town to collect their final reward")
- **Issue**: Per Chapter 2, Harbin Wester's 50 gp for the Dwarven Excavation quest was **already collected**, and the deeper-temple job's reward was the sending stones (delivered in-session per this recap). There is no reward waiting in town on record.
- **Evidence**: `campaign_state` → "Return to Phandalin — Dwarven Quest Reward Collected: Harbin Wester paid the promised 50 gp."
- **Suggested fix**: Either delete "to collect their final reward," or — if the transcript genuinely has an uncollected reward — this is further evidence that this session actually precedes the Phandalin-return scenes in the Chapter 2 prose (see issue 1). Adjudicate together with issue 1.

### 4. The deal (and the meal) are re-negotiated as if new
- **Location**: Summary, second post-battle paragraph ("the dwarves asked them to finish clearing the rest of the ruins first, sweetening the offer with a hot meal and a place to rest"); Scenes → Archaeologists and Altars
- **Issue**: Per Chapter 2, the deeper-temple job was already agreed (in exchange for the stones) *and* the dwarves already cooked the party a meal after the orc fight. The recap presents both the bargain and the meal offer as struck fresh this session.
- **Evidence**: `campaign_state` → "The two shield-dwarf prospectors … offered a follow-up job (clear something deeper in the ruined temple) in exchange for a pair of sending stones"; "Dazlyn and Norbus cooked the party a meal afterward."
- **Suggested fix**: Reframe as the dwarves *reminding* the party of the standing bargain (or resolve via the ordering adjudication in issues 1–3). Also note the internal wobble: the NPC entry says Norbus offered "a meal and **stories**," the Summary says "a hot meal and **a place to rest**."

---

## Attribution and internal inconsistencies

### 5. Who shouted "don't damage the site" — Norbus or Dazlyn?
- **Location**: Memorable Moments (quote attributed to **Norbus**) vs. NPCs → Dazlyn ("**He** shouted warnings during the battle, urging the party not to damage the interior") vs. NPCs → Norbus ("urged the party to avoid damaging the ruins with powerful spells")
- **Issue**: The same protest is attributed to both dwarves in different sections. Ch2 characterization (Dazlyn talkative/forthright, Norbus gruff/cautious) doesn't settle it.
- **Evidence**: `entity_registry.yaml` — Dazlyn: "forthright and honest to a fault"; Norbus: "gruff and excessively cautious." Neither ch02 doc records this scene (it's new).
- **Suggested fix**: Check the VTT for the actual speaker and attribute consistently; strip the duplicate claim from the other dwarf's NPC entry.

### 6. Soma: impenetrable shield or knocked unconscious? The Summary and the rest of the document disagree
- **Location**: Summary ("her hardened carapace **deflecting blow after blow**") vs. Memorable Moments ("Soma is **knocked unconscious** by a pair of ochre jelly pseudopod strikes… death saves") vs. Scenes → Battle with the Ochre Jellies ("briefly knocking Soma unconscious before she is revived")
- **Issue**: The Summary narrates Soma's shell-tank gambit as a success and never mentions her going down; the Moments and Scenes sections say she was dropped and had to be revived. A regenerated chapter built from the Summary alone would erase a near-death.
- **Evidence**: Internal contradiction within the recap.
- **Suggested fix**: Amend the Summary to include Soma being overwhelmed and revived by Valphine.

### 7. Healing Word's first target — Brewbarry or Soma?
- **Location**: Spells → Healing Word ("Used to restore **Soma** after a near-fatal pseudopod strike, and again to revive her")
- **Issue**: The near-fatal opening pseudopod strike is attributed to **Brewbarry** everywhere else ("striking the barbarian Brewbarry with a blow so powerful it nearly dropped him"; Scenes: "one nearly felling the barbarian"). The Healing Word entry appears to have swapped the recipient, or a heal on Brewbarry has gone unrecorded.
- **Evidence**: Internal contradiction; per user's standing rule, spell/caster/target attributions must be verified against the transcript and character sheets before acceptance.
- **Suggested fix**: Verify against the VTT; likely correct the entry to "restore Brewbarry after the opening strike, and revive Soma later" or record both heals accurately.

---

## Abilities, items, and mechanics to verify

### 8. Vukradin's daggers are not on record — his established weapon is a rapier
- **Location**: Summary ("Vukradin drew his daggers and struck twice"); Scenes (both battles); Memorable Moments
- **Issue**: The dagger double-kill is a centerpiece moment, but no dagger appears in Vukradin's recorded kit; the ch02 baseline is "rapier (per character sheet's baseline kit)." Two attacks in one round also implies two-weapon fighting at presumed 1st level — legal with daggers, but worth confirming this is what happened at the table rather than a summarizer embellishment.
- **Evidence**: `world_state` → Vukradin, Key items: "Clarinet/flute … rapier (per character sheet's baseline kit)."
- **Suggested fix**: Verify against `characters/vukradin.md` and the transcript; if daggers are real, add them to his items going forward.

### 9. Vukradin's spell list is entirely unverified (Thunderwave, Dissonant Whispers, Starry Wisp)
- **Location**: Summary; Scenes; Spells
- **Issue**: None of these three spells has been seen in play per the ch02 docs, and per standing instruction every "X cast spell Y" claim must be checked against the character sheet before acceptance. Note also the archive's explicit warning that party level at this point is *presumed 1st, unconfirmed* — Thunderwave + Dissonant Whispers is exactly a 1st-level bard's full slot budget, so it's feasible, but the GM should confirm level before this seeds a regenerated chapter.
- **Evidence**: `party_ch02` — "Starting level is presumed 1st (unconfirmed on the page) and should be confirmed by the GM before this document is used to seed a regenerated Chapter 3 pass." (Soma's slot usage — Earth Tremor pre-rest, two Ice Knives post-rest — is likewise level-1-feasible but tight.)
- **Suggested fix**: Confirm against character sheets/transcript; log confirmed spells into the forward grounding docs.

### 10. The second jelly's split is mechanically unexplained — and the Starry Wisp entry gets the mechanic wrong
- **Location**: Summary ("when the creature finally split into two smaller oozes under the sustained assault"); Spells → Starry Wisp ("contributing to the damage that eventually caused it to split")
- **Issue**: Ochre jellies split when hit by **slashing** (or lightning) damage — the recap itself establishes this correctly in battle 1 (Brewbarry's halberd). But the attacks described in the altar-channel fight are ice (piercing/cold), radiant, fists/mace (bludgeoning), and daggers (piercing). Nothing slashing is described, and radiant damage from Starry Wisp cannot "cause it to split."
- **Evidence**: Recap's own NPC entry: "split into smaller versions of themselves **when struck with slashing weapons**."
- **Suggested fix**: Check the transcript for what attack actually triggered the split (or whether the GM ruled otherwise); correct the Starry Wisp entry regardless — it should not claim radiant damage caused the split.

### 11. Valphine's knowledge of Orcish is unestablished
- **Location**: Summary (final paragraph); Scenes → Ambush on the Road
- **Issue**: Nothing on record gives Valphine (drow cleric) the Orc language. The session's transcript does contain orc-language table content ("Do you speak Orcanese?" per `vtt_known_additions`), but the speaker/knower isn't verified.
- **Evidence**: No language list in any ch02 doc; drow default languages don't include Orcish.
- **Suggested fix**: Verify against `characters/valphine.md` before letting "Valphine speaks Orcish" harden into canon — this will matter immediately, since the orc encounter opens the next session.

---

## Ambiguities that will confuse future sessions

### 12. Did Valphine actually pocket the holy symbol of Abbathor?
- **Location**: Summary ("her hand moved toward it… She said nothing, and neither did they"); Memorable Moments ("attempts to secretly pocket it"); Items ("Valphine attempted to secretly pocket it")
- **Issue**: Every mention says "attempted"; none says whether the 50 gp symbol is now in her possession, left on the skeleton, or disclosed to the dwarves (Vukradin reported *the body* — was the symbol part of that report and the gem-split ethics?). This is a Chekhov item (a greed-god relic in the hands of a recovering-drow cleric) — its disposition must be pinned down.
- **Evidence**: Internal ambiguity; no context doc resolves it.
- **Suggested fix**: Check the transcript and record the outcome explicitly in the Items entry and party inventory.

### 13. The Skull Cavity's place in the timeline is contradictory
- **Location**: Summary ("**Earlier in the expedition**, the party had also stumbled upon a secret cavity…" — narrated last) vs. Scenes ordering (Skull Cavity placed between the first battle's aftermath and the long rest/bedroom exploration)
- **Issue**: The Summary and Scenes disagree on when the 15-gem discovery and the 7/8 split negotiation happened relative to the long rest and the sending-stone handover. Since the split negotiation colors the dwarves' trust and the stones payout, the order matters for any regenerated prose.
- **Evidence**: Internal inconsistency between sections.
- **Suggested fix**: Fix a single chronology from the VTT and rewrite the Summary in order (drop the "Earlier in the expedition" retrofit).

### 14. "Recently took up the hobby" sits oddly against Chapter 2's account of the dwarves
- **Location**: Summary; Scenes → Amateur Archaeologists; NPCs → Dazlyn/Norbus
- **Issue**: Not a hard contradiction (their *profession* is prospecting; archaeology can be the new hobby), but ch02 has Dazlyn spending **months** clearing rubble and confidently identifying the site as a temple of Abbathor destroyed as divine punishment — which sits awkwardly with this session's "making most of it up as they went" reveal. Worth confirming the admission is transcript-real and not summarizer color.
- **Evidence**: `world_state` → Dazlyn: "spent months clearing rubble… Identified the site as an old temple of Abbathor… destroyed by an avalanche/earthquake he attributes to the god."
- **Suggested fix**: Verify against the VTT; if real, note in the dwarves' dossiers that their *historical* expertise is shallow even though their site identification (from ch02) was correct.

---

## Minor / cosmetic

### 15. Sending Stones item entry conflates two different jobs
- **Location**: Items → Sending Stones ("as payment for clearing the ruins **and delivering a message**")
- **Issue**: The message delivery (the dragon warning) was the original job-board quest, paid with **50 gp by Harbin Wester** in Chapter 2 — not part of the dwarves' stones deal.
- **Evidence**: `campaign_state` → Completed Encounters (warning delivered; 50 gp paid separately by Harbin).
- **Suggested fix**: Delete "and delivering a message."

### 16. Ochre Jelly listed under NPCs
- **Location**: NPCs section
- **Issue**: A mindless monster type is catalogued as an NPC alongside Dazlyn and Norbus (as are the unnamed "Orcs"). Harmless, but it pollutes NPC-facing downstream passes (dossier generation, entity triage).
- **Evidence**: Structural convention only.
- **Suggested fix**: Move Ochre Jelly (and the generic Orcs entry) to a "Creatures/Encounters" heading.

### 17. Chapter title lacks the campaign's naming convention
- **Location**: Document title ("New Chapter 3")
- **Issue**: Campaign convention is "Chapter N: Title" (e.g., "Chapter 34: Where Cows Come Home").
- **Evidence**: Project `CLAUDE.md` conventions.
- **Suggested fix**: Retitle once the GM picks a chapter name.

---

## Verified-clean items (no action needed)
- Dwarf names (Dazlyn, Norbus), Abbathor as evil dwarven god of greed, the temple room contents (three stone bed frames / E8, font + red leather vestments / E9, priest skeleton with holy symbol / E10, horned-dwarf statue with green gem / E11, jelly behind the altar / E7) all match `entity_registry.yaml`.
- First jelly splitting from the halberd's slashing blow is mechanically correct and matches the recap's own monster description.
- 15 gems worth 10 gp each and the 7/8 split arithmetic are internally consistent; Valphine's "We found 10" underreport is consistent with her ch02 characterization.
- Vukradin's compulsive reporting to the dwarves is strongly consistent with his ch02 "rightful owners" ethic.
- Brewbarry's Goliath toughness (Stone's Endurance flavor) and Soma's shell withdrawal (Tortle Shell Defense) match established species/class.
- One caution for the *next* session's prep: `entity_registry.yaml` describes the Hall of Greed statue as **trapped** (E11: "a trapped statue of a horned dwarf"). The recap has the party examining the gem closely and leaving it — no trap is mentioned as triggered or detected. Not a recap error (GM-side info), but the GM should confirm the trap's current state before the party revisits.