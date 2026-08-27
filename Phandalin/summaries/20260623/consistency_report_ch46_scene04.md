# Consistency Report

---

## Issue 1

**Location:** Scene tag — Departure for Neverwinter / Abandoning the Shrine of Savras

**Issue:** The recap states the party is departing "toward Neverwinter" and explicitly abandons the Shrine of Savras quest. However, the campaign_state document clearly notes the party's planned route as: Phandalin → Mountain's Toe Mine (collect money) → Neverwinter. The mine stop is listed as an outstanding obligation and the party had not yet bypassed it as of Chapter 45. The recap describes a direct departure for Neverwinter without a mine stop, which contradicts the stated plan in party.md and campaign_state.md.

**Evidence:** campaign_state.md: "Current location: Returning from Woodland Manse area toward Phandalin. Full party alive. Next destination: Phandalin (celebration / rest), then Mountain's Toe Mine (collect money), then Neverwinter." party.md: "Next stop: Mountain's Toe Mine (payday), then Neverwinter." campaign_state.md Active Quests: "Mine stop bypassed (ch46) — party went directly to Neverwinter." (This ch46 note is future relative to the scene being recapped, which appears to be the pre-departure scene in Phandalin.)

**Suggested fix:** Clarify whether this scene occurs after the mine stop was already bypassed (consistent with ch46 per campaign_state) or whether the departure decision made here is itself the bypassing. If this is the scene where they choose to skip the mine, note that explicitly so future continuity editors understand ch46's "bypassed" entry refers to this decision.

---

## Issue 2

**Location:** Scene summary — Brewbarry's Bathrobe Business Plan / Verbatim moments

**Issue:** The recap states that Linene mentions the supply chain problem with the "Lion Shield Coster" and their "formerly cheap distribution method" being replaced by costlier ones. The scene summary also states Linene flags "her past obsession with planar-magic goods (the phasing animal hides from the Whispering Grove)." However, the recap does not identify this supply chain disruption as the Displacement Manifold incident — the actual known cause documented in campaign/world state. The scene is factually consistent with the known lore, but the framing is potentially misleading: Linene asks the party to "investigate in Neverwinter," as though the cause is unknown to her. Campaign context establishes the Displacement Manifold went dark after the Commission refused Aletra's ultimatum, and House Margaster filled the gap. The recap's framing could mislead future editors into treating the cause as genuinely unresolved in-world, when it is only unresolved from the party's perspective.

**Evidence:** world_state.md: "Displacement Manifold Incident: ~1493 DR [Campaign Canon]; Commission refused Aletra Sotorra's treaty ultimatum, Manifold went dark, Bimble Nackle was disappeared, Lionshield Coster's distribution network collapsed, House Margaster filled the gap." campaign_state.md NPC table: "Linene Graywind — Friendly; interdimensional supply chain disrupted." 20260623_neverwinter_vukradin_present.md: references the Counting House Letter of Credit and Manifold connection as a known plot thread.

**Suggested fix:** Add a GM note clarifying that Linene's stated ignorance of the root cause is in-character (she knows the Manifold went dark but not why), and that the Displacement Manifold / Aletra / Margaster connection is GM-layer knowledge not yet shared with the party. This prevents future editors treating the cause as a genuine mystery at the campaign-state level.

---

## Issue 3

**Location:** Scene tag — The Alagondar Note (Necklace of Fireballs); Verbatim moments

**Issue:** The GM in the verbatim transcript first offers "Alexander" as the claimant's name before correcting to "Perrin Alagondar." The scene summary correctly records "Perrin Alagondar" as the claimant. However, the recap does not flag "Alexander" as an in-session error. If this transcript is used as a source document, the "Alexander" reference could cause future confusion about the claimant's name.

**Evidence:** Verbatim: "[GM] So, Alexander. / It's an Alagondar, so… / Yes, so you… there is a… I don't want to find out the name… / Alright, yes. So, Perrin… Alagondar. / Is his name." campaign_state.md: "Vukradin holds items for rightful owners: Necklace of Fireballs" with no claimant name previously on record. 20260623_jenna_roscoe_head_start.md references "Perrin Aligonder" (itself a spelling variant — see below).

**Suggested fix:** Add a parenthetical in the recap noting "Alexander" was a mid-sentence self-correction by the GM and the canonical name is Perrin Alagondar. Also flag that 20260623_jenna_roscoe_head_start.md spells the name "Perrin Aligonder" — this should be normalized to "Perrin Alagondar" per the vtt_transcription_corrections.md rule ("Aligonder → Alagondar").

---

## Issue 4

**Location:** Scene summary — The Alagondar Note (Necklace of Fireballs)

**Issue:** The recap states "Ser Kaelen leaves a note identifying the Alagondar family as the rightful owners of the necklace of fireballs, whose ancestor's belongings were stolen by grave robbers a generation ago." The entity_registry.yaml and campaign_state.md identify the Necklace of Fireballs as having been sealed with a dead wizard in the Adventurers' Sepulcher (southeast sarcophagus), not as originating from a grave-robbery of the Alagondar family. The Alagondar connection is new information introduced by Ser Kaelen's note in this scene and is plausible, but it potentially contradicts the item's documented provenance (a dead wizard's burial item in a specific location). This is either a legitimate retcon/new revelation or an error.

**Evidence:** entity_registry.yaml: "Necklace of Fireballs — Magic item sealed with the dead wizard in the southeast sarcophagus of the Adventurers' Sepulcher." campaign_state.md: "Necklace of Fireballs (held for rightful owner) — Vukradin." No prior campaign_state entry connects the necklace to the Alagondar family.

**Suggested fix:** If this is an intentional retcon (the dead wizard in the Adventurers' Sepulcher was Alagondar-affiliated, or the necklace passed through multiple hands), add a note to campaign_state.md and/or the entity_registry.yaml entry documenting that Perrin Alagondar is the confirmed claimant per Ser Kaelen's recovery office match. If it is unintentional, verify with the GM whether the Adventurers' Sepulcher provenance is being overwritten or whether the necklace has a different in-world history than the module default.

---

## Issue 5

**Location:** Scene summary — Departure for Neverwinter / Abandoning the Shrine of Savras; Verbatim moments

**Issue:** The recap describes the party "explicitly abandoning the quest for the Shrine of Savras." In the verbatim, Vukradin says "We're just gonna abandon that quest." The campaign_state.md lists the Shrine of Savras as an "active pending objective, not past content" and notes the party "explicitly noted they have never cleared the shrine despite the dragon's death, and noted intent to visit (ch44)." The recap's abandonment is consistent with what the campaign_state records for ch46 ("Mine stop bypassed (ch46)"), but the Shrine of Savras is listed under "Active Quests & Open Threads" in campaign_state without a corresponding "abandoned" notation.

**Evidence:** campaign_state.md Active Quests: "Shrine of Savras — Zeleen suggested it (ch31); party noted intent to investigate (ch44). Not yet visited." campaign_state.md Tracked Items: "Shrine of Savras — FOUND — UNCLEARED (active objective)."

**Suggested fix:** Update campaign_state.md to mark the Shrine of Savras quest as "Abandoned (ch46)" rather than leaving it as an active objective. The verbatim is unambiguous: the party consciously chose not to pursue it.

---

## Issue 6

**Location:** Scene summary — Cheese Tasting

**Issue:** The recap states "the were-rat assistants (Brin and Giles) to be sent later to collect the cheese." Brin Bundlewine and Giles Slipper-Shine are described in campaign_state.md as "devoted allies of Valphine" located at the Temple of Lathander in Phandalin. They are confirmed as wererats in campaign context (renovated Tresendar Manor, confirmed as wererat workers). However, the recap describes them as being dispatched from the tasting — which is consistent with their Phandalin location — but refers to them as "were-rat assistants" in the context of the party's assistants. No campaign document formally designates Brin and Giles as party assistants or assigns them a cheese-collection role. This is a minor ambiguity rather than a clear error, but it could cause confusion about their primary role (temple staff vs. party errand-runners).

**Evidence:** campaign_state.md: "Brin Bundlewine — Alive, Temple of Lathander, Phandalin, Devoted ally of Valphine." "Giles Slipper-Shine — Alive, Temple of Lathander, Phandalin, Devoted ally of Valphine." campaign_state.md Completed: "Temple of Lathander's Searing Pain of Justice — Founded: renovated by Brin Bundlewine and Giles Slipper-Shine."

**Suggested fix:** Add a clarifying note that Brin and Giles are being tasked in their capacity as party-adjacent allies (Valphine's temple staff) rather than as dedicated party assistants. No correction needed if the GM intended to establish them as generally available for party errands — but the dual-role should be flagged for future session continuity.

---

## Issue 7

**Location:** Scene summary — Linene / Supply Chain; Verbatim moments

**Issue:** The recap describes Linene as suggesting the party "investigate in Neverwinter" whether the "Lion Shield Coster distribution system will be back up and running." The Lionshield Coster is documented as a branch of the Lionshields merchant company based in Yartar, not a Neverwinter-headquartered operation. The Displacement Manifold (the actual disruption point) was a Neverwinter docks installation. The framing of the investigation target as the Lionshield Coster's system rather than the Displacement Manifold is in-character for Linene (who may not know the full picture), but it should be flagged as a potentially incomplete lead for the party.

**Evidence:** entity_registry.yaml: "Lionshields — Merchant company based in Yartar that ships finished goods to Phandalin and other small settlements." entity_registry.yaml: "Lionshield Coster — Trading post selling weapons and armor; Phandalin outpost of the Lionshields merchant company." world_state.md: "Displacement Manifold Incident: Lionshield Coster's distribution network collapsed, House Margaster filled the gap."

**Suggested fix:** No change to the recap itself — Linene's framing is plausible. Add a GM note clarifying that the party's Neverwinter investigation lead (Lionshield Coster distribution) and the known Displacement Manifold cause are the same thread, so future prep documents do not treat them as separate quests.

---

## Issue 8

**Location:** Scene summary — Brewbarry's Bathrobe Business Plan

**Issue:** The recap states the bathrobe plan involves "Lathander's logo." The recap does not clarify whether this branding has been approved by or coordinated with Valphine (founder of the Church of the Searing Light) or the Phandalin temple. Brewbarry is not a Lathander cleric and has no documented authority to use Lathander's symbol for commercial purposes. This is a potential future continuity complication — either Valphine will need to authorize it or it will create friction — but is not recorded as a point of discussion in this scene.

**Evidence:** campaign_state.md: "Temple of Lathander's Searing Pain of Justice — Founded." party.md: Valphine is the Lathander cleric and church founder. No prior document authorizes Brewbarry to use Lathander's symbol commercially.

**Suggested fix:** Flag for future session prep: Valphine should either explicitly endorse or contest Brewbarry's use of Lathander's commercial branding. The scene recap should note whether Valphine was present and silent, or whether this detail was not raised in-session.

---

## Issue 9

**Location:** Verbatim moments — On the Road: Bathrobe Monologue

**Issue:** The GM's closing line is: "Given, you know, Kostadis' compulsive need to create stuff." "Kostadis" is a real-world table participant name (per vtt_transcription_corrections.md: "Costatus, Castadis, etc. → Kostadis"). This is an out-of-character aside about a player, not a in-world event. It is correctly placed in the verbatim section, but if this transcript is processed by automated tools, "Kostadis" could be misread as an NPC reference.

**Evidence:** vtt_transcription_corrections.md: "Costatus, Castadis, And Cassadis, Cassadis, Christatis, Castados, Costas, Kostas, Cassadas → Kostadis." This is listed under "Real-world / table."

**Suggested fix:** Add an editorial tag in the verbatim marking this line as an out-of-character player attribution, not an in-world statement. Recommended format: `[OOC — Kostadis is a player name, not an NPC]`.

---

## Issue 10

**Location:** Scene summary — Brewbarry's Bathrobe Business Plan

**Issue:** The recap states the bathrobe business plan includes "a note for Vukradin's upcoming music studio." Vukradin's music studio is documented throughout campaign_state.md and party.md as a key unresolved goal — "still not built or open." The recap's reference to it as "upcoming" is accurate, but the cross-promotion arrangement (5% discount for buyers of Vukradin's album) implies Vukradin's consent to the commercial tie-in. No scene in the recap documents Vukradin agreeing to this arrangement. If Vukradin is present during the Linene consultation, his silence on this point should be noted; if he was not present, the arrangement was made without his knowledge.

**Evidence:** campaign_state.md: "Vukradin's Music Studio — Still not built or open. Every ethical choice about money ties back to this identity thread." party.md: "Vukradin: 29 gp on hand; studio not built; feels poor." Vukradin's documented ethics include refusing blood money and returning items to rightful owners; a commercial tie-in arranged without his input would be consistent friction for his character.

**Suggested fix:** Clarify in the recap whether Vukradin was present and consented to the album/bathrobe cross-promotion, or whether Brewbarry unilaterally incorporated Vukradin's name and album into the business plan. The latter would be a character moment worth preserving for continuity.