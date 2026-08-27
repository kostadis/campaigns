# Consistency Report — "Return to Phandalin" Recap

---

## ISSUE 1 — Verbatim Moments: "Gruberry" used for Brewbarry

**Location:** Verbatim Moments section, first bullet under "[GM — recap, departing the mine]"
> *"Gruberry made a mental note that a finder's fee would be the right and proper thing to offer on the dragon's recovered hoard."*

**Issue:** "Gruberry" is a VTT transcription corruption of "Brewbarry." The finder's fee mental note is attributed to Gruberry rather than Brewbarry.

**Evidence:** `vtt_transcription_corrections.md` lists "Gruberry" as a known VTT garble for **Brewbarry**. The Scene Summary section correctly attributes the finder's fee idea to Brewbarry. The GM's own verbatim quote in the next block also names Brewbarry.

**Suggested fix:** Replace "Gruberry" with "Brewbarry" throughout.

---

## ISSUE 2 — Scene Summary: Vorga escort marked as happening during this scene, but it was completed in ch46 before this scene begins

**Location:** Scene Summary, bullet beginning "Vukradin fulfills his escort obligation to Vorga…"

**Issue:** The recap presents the Vorga escort delivery as an event occurring *during* this return-to-Phandalin journey. However, `campaign_state.md` marks it as **COMPLETE (ch46)**: "Escort Vorga — COMPLETE (ch46). Delivered to Icespire Hold with her tribe." The `party.md` also notes the Vorga obligation as already discharged. This scene is the party *after* leaving Icespire Hold, not *during* the escort.

**Evidence:** campaign_state.md: "Escort Vorga — COMPLETE (ch46). Delivered to Icespire Hold with her tribe." world_state.md (Icespire Hold): "Current control: Vorga's orc tribe, established as their base as of ch46."

**Suggested fix:** Reframe the bullet as a recap/summary of what was completed prior to this scene, not as an event occurring within it. E.g., "Having fulfilled his escort obligation to Vorga in ch46, Vukradin…" The beat about Prutha and his five orc converts parting ways at Icespire Hold is similarly retrospective and should be framed as already-completed backstory.

---

## ISSUE 3 — Scene Summary: Boots of Elvenkind attributed to wrong character

**Location:** Implicit in asset tracking — the scene does not directly name them, but world_state.md and party.md are clear.

**Issue:** No direct error in this recap, but the scene mentions Vukradin coaching Valphine on spin. Worth flagging for future continuity: the **Boots of Elvenkind** are held by **Vukradin** (acquired ch43), not Valphine. The recap does not contradict this, but if follow-up scenes reference boot wearers, this is the live assignment.

**Evidence:** world_state.md Objects table: "Boots of Elvenkind | Vukradin | Acquired ch43." party.md: "Boots of Elvenkind — Vukradin."

**Suggested fix:** No action needed in this recap. Flag for downstream scenes.

---

## ISSUE 4 — Verbatim Moments: "sheetment" vs. canonical spelling "encheatment"

**Location:** Verbatim Moments, GM quote block on the political agenda; Scene Summary bullet on "direct mayoral elections."

**Issue:** The legal process for forcing a mayoral election is spelled **"sheetment"** throughout the recap. Per `vtt_transcription_corrections.md`, this is a VTT transcription error.

**Evidence:** vtt_transcription_corrections.md, Real-world/table section: `sheetment` → **encheatment**.

**Suggested fix:** Replace all instances of "sheetment" with "encheatment" in recap prose. Quoted dialogue may retain the phonetic transcription if it reflects how a player pronounced it, but should include a bracketed correction: *[encheatment]*.

---

## ISSUE 5 — Scene Summary: "part-owner of a gold mine" — mine ownership is more nuanced

**Location:** Scene Summary, Vukradin's frustration bullet: *"having defeated dragons, cleared mansions, and become part-owner of a gold mine."*

**Issue:** The recap states Vukradin is a part-owner of the gold mine. Per campaign documents, the mine shares are held by **Brewbarry and Falcon**, not Vukradin. The party collectively holds Don-Jon's share, but individual ownership is tracked differently.

**Evidence:** party.md: "Mine shares at Mountain's Toe Gold Mine" listed under collective resources. campaign_state.md: "Party holds Don-Jon's share of the mine." world_state.md: No mention of Vukradin specifically holding mine ownership. party.md character sheet for Brewbarry notes Falcon as his mine co-holder: "holds mine shares with him [Falcon]."

**Suggested fix:** Change "become part-owner of a gold mine" to "the party holds a share of a gold mine" or, if the line is Vukradin speaking in character, frame it as his loose characterization rather than a factual statement of record.

---

## ISSUE 6 — Verbatim Moments: "30 gold pieces" — departure gold amount is ambiguous

**Location:** Verbatim Moments, GM recap quote: *"the party departed the mine with their 30 gold pieces and a growing list of ambitions."*

**Issue:** The campaign state and party documents do not confirm "30 gold pieces" as the specific amount the party had on departing the Woodland Manse area. Vukradin's party.md entry lists "29 gp on hand." The 30 gp figure may be a VTT approximation or a different reference point (e.g., from the mine, not the Manse). The discrepancy is small but could cause confusion in future bookkeeping.

**Evidence:** party.md, Vukradin section: "29 gp on hand; studio not built; feels poor." No campaign_state entry confirms a "30 gp" departure figure for ch45/46.

**Suggested fix:** Verify the exact gold-on-hand figure with the party sheet. If 30 gp is a GM-round approximation for the recap, note it as approximate. If the figure comes from a specific source (e.g., mine payout), identify that source.

---

## ISSUE 7 — Scene Summary: "untransformed lump of gold from Cryovain's hoard" — item not in tracked assets

**Location:** Verbatim Moments, "[GM — recap, departing the mine]" section: *"Still unresolved: the untransformed lump of gold from Cryovain's hoard."*

**Issue:** This item ("untransformed lump of gold") does not appear in any tracked asset list in campaign_state.md, world_state.md Objects table, or party.md. The Cryovain hoard is noted as approximately 3,000 gp left unclaimed at Icespire Hold (Vukradin refused it), but no specific "untransformed lump of gold" is documented as a separate item in party possession.

**Evidence:** campaign_state.md active obligations: "~3,000 gp Cryovain hoard at Icespire Hold — unclaimed (Vukradin refused it)." world_state.md and party.md: No entry for an "untransformed lump of gold" as a held item.

**Suggested fix:** Clarify whether this item exists as a separate tracked asset in party possession, or whether the GM is referring to the unclaimed hoard at Icespire Hold. If it is a distinct physical item the party carries, it should be added to the tracked assets list with a note on its status.

---

## ISSUE 8 — Scene Summary / NPC State: Prutha described as parting ways "here" at Icespire Hold with "five orc converts"

**Location:** Scene Summary bullet on the Vorga escort.

**Issue:** The recap states Prutha and "his five orc converts" part ways with the party at Icespire Hold to convert Vorga's orcs. This is consistent with the ch46 state. However, the party.md (as of ch45) lists Prutha's status as "With party at Woodland Manse" and notes "Five orc converts under Prutha." The recap implies this transition happened during the ch46 Icespire Hold delivery — which is plausible and consistent with campaign_state.md — but the phrasing "Prutha and his five orc converts" should be verified: world_state.md describes Prutha as leading five converts at the Manse, while campaign_state.md (Icespire Hold location entry) confirms Prutha and five converts are now present there on a missionary mission.

**Evidence:** campaign_state.md (Icespire Hold): "Prutha and five orc converts also present, on a missionary campaign to convert Vorga's orcs to Valphine's Lathanderite faith." party.md (ch45 state): Prutha listed as "With party at Woodland Manse."

**Suggested fix:** No factual error, but add a brief clarifying note that Prutha's separation from the party occurred as part of the ch46 Icespire Hold delivery (already-resolved prior to this scene), not as a new event within the Return to Phandalin scene.

---

## ISSUE 9 — Scene Summary: "Soma counters" in blood money argument — attribution check

**Location:** Scene Summary, final bullet: *"Soma counters that 'blood can be turned into something soft and wonderful, you know, like a Brewbarry bathroom [bathrobe].'"*

**Issue:** The bracketed correction "[bathrobe]" in the recap implies a VTT garble ("bathroom" for "bathrobe") — which is appropriate. However, reviewing the Verbatim Moments section, the actual quote is given to **Brewbarry** ("Yeah, but blood can be turned into something soft and wonderful, like a Brewbarry bathrobe"), not Soma. The Scene Summary attributes it to Soma; the Verbatim Moments section attributes it to Brewbarry.

**Evidence:** Verbatim Moments, "[Vukradin / Brewbarry]" blood money block: *"Yeah, but blood can be turned into something soft and wonderful, like a Brewbarry bathrobe."* — speaker tag is Brewbarry.

**Suggested fix:** Correct the Scene Summary attribution from Soma to Brewbarry for this quote. It is Brewbarry, not Soma, who makes the bathrobe counter-argument to Vukradin.

---

## ISSUE 10 — Verbatim Moments: "Barthen's provisioning" vs. canonical name

**Location:** Verbatim Moments, GM quote: *"Barthen's provisioning."*

**Issue:** The store's canonical name is **Barthen's Provisions**, not "Barthen's provisioning." This is a minor transcription issue but could accumulate as a naming inconsistency.

**Evidence:** entity_registry.yaml: `Barthen's Provisions — General store in Phandalin that fills supply crates for the loggers' camp.` world_state.md (Phandalin section) and campaign_state.md both use "Barthen's Provisions."

**Suggested fix:** Standardize to "Barthen's Provisions" in recap prose.

---

## NO ISSUES FOUND in the following areas:
- The cross-promotion/bathrobe business concept (Brewbarry's, consistently attributed)
- Vukradin's music studio frustration thread (consistent with open thread in campaign_state.md)
- The political agenda / mayoral elections thread (consistent with campaign_state.md: "Phandalin Privy Council — Established" and Vukradin's democratic ambitions)
- Valphine's Talosian boast and the soft-spin coaching (consistent with Woodland Manse clearance in ch45)
- The "yesterday's news" hero reception (consistent with Hero's Welcome Festival in ch37 being long past)
- The were-rat cheese deal (consistent with campaign_state.md: "it was agreed that the were-rats could go by themselves to go get the cheese")
- Vukradin's ethical stance on "blood money" (consistent with his character documentation throughout)
- The Neverwinter commission negotiation as a pending objective (consistent with Active Quests)