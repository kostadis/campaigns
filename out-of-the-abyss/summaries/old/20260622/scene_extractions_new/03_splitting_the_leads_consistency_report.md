# Consistency Report — "Splitting the Leads"

---

## Finding 1: Daz assigned to Sylvira — contradicts campaign-state chronology

**Location:** Scene Summary / Scene Tag

**Issue:** The recap assigns Daz to interview Sylvira in this scene. However, the campaign_state (Completed Encounter #47, Ch. 57 canon timeline, and party.md) records that Daz's interview of Sylvira already occurred in Chapter 57 — it is listed as a *completed* solo action in the canonical session record ("Daz (alone) interviews the framed, dying Sylvira; secured her cooperation across two persuasion rolls").

**Evidence:** campaign_state.md Ch. 57 timeline entry: *"Daz (alone) interviews the framed, dying Sylvira (alone); secured her cooperation across two persuasion rolls."* party.md Characters section: *"Daz — Ch. 57: Interviewed the framed, dying Sylvira (alone); secured her cooperation across two persuasion rolls."*

**Suggested Fix:** If this scene is meant to be a *follow-up* interview with Sylvira (post-confession, new questions), the recap should say so explicitly. If it is describing the original Ch. 57 interview, it is being placed out of chronological order relative to the Alkrist confession scene. Clarify whether this scene precedes or follows the Ch. 57 confession, and adjust accordingly. The scene tag's phrasing — "Daz prepares to interview Sylvira" — may indicate this is a *second* contact, which should be flagged as such.

---

## Finding 2: Kalan Strongbranch's zone of truth framed as future / pending — but it already happened

**Location:** Scene Summary, Verbatim Moments (Zalthir's lines), Scene Tag

**Issue:** The recap treats Kalan's truth-seeking spell as something that still needs to be arranged ("Fembris departs to locate Kalan Strongbranch so he can assist with a truth-seeking spell for the upcoming interrogation of Alkrist"). The campaign_state records this as already completed in Ch. 57: Kalan cast the *zone of truth* (concealed outside the room) and Alkrist's full confession occurred under it.

**Evidence:** campaign_state.md Completed Encounters #47: *"Under a zone of truth cast by Kalan Strongbranch (concealed outside the room), Alkrist confessed the conspiracy."* world_state.md §5: *"The confession (under Kalan's zone of truth, cast concealed outside the room; Thorin & Zalthir in the room)."*

**Suggested Fix:** Two possibilities — (a) this scene is being placed *before* Ch. 57's confession scene in the recap's internal timeline, meaning it describes the lead-up to the interrogation that is already resolved in the campaign state, or (b) this scene is a continuity error treating resolved events as future. If (a), the recap needs an explicit framing note that it predates the Ch. 57 confession. If (b), it should be corrected to reflect that Kalan already provided the spell and the interrogation is complete. Either way, a reader of this recap without the campaign_state would believe the Alkrist interrogation has not yet occurred — contradicting canon.

---

## Finding 3: Grygum assigned to Janussi's chambers / third-story apartment — already completed in Ch. 57

**Location:** Scene Summary, Verbatim Moments (Grygum's lines), Scene Tag

**Issue:** The recap presents Grygum heading to Janussi's chambers / the third-story apartment as an action being planned in this scene. The campaign_state records this as already done: Grygum explored Janussi's third-floor chambers (alone) in Ch. 57, found the damning note on Kalan, and cast *Mending* on the wrapping paper there.

**Evidence:** campaign_state.md Ch. 57 timeline: *"Grygum (alone) finds the damning note in Janussi's chambers."* party.md Ch. 57 beats for Grygum: *"Explored Janussi's third-floor chambers (alone), finding the damning note on Kalan; cast Mending to reassemble the wrapping paper (proving premeditation)."* world_state.md §5: *"Grygum returns from his colloquium; … Grygum (alone) finds the damning note in Janussi's chambers."*

**Suggested Fix:** Same structural issue as Findings 1 and 2. If this recap scene predates Ch. 57 in sequence, it must be labeled clearly. If it is intended to be post-Ch. 57 content, then Grygum's Janussi-chambers investigation should be described as complete and any return trip should be framed as a follow-up with a specific new purpose (e.g., the GM's hint about "further evidence related to Kalan you may not have found" could justify a second visit, but that must be distinguished from the already-completed first visit).

---

## Finding 4: "What Alkrist burned at the feast" open thread — status ambiguous given confession

**Location:** Scene Summary ("open thread"), Verbatim Moments (Grygum's reminder), Scene Tag

**Issue:** The recap flags "what Alkrist burned at the feast" as an open thread Grygum raises before departing. The campaign_state records that Alkrist's full confession under *zone of truth* already answered this: Alkrist burned the midnight-tears vial's label at the Dead Winter tree (the "feast" / Deadwinter celebration context), nearly caught by the staffer Irony. This is not listed as an open thread in the campaign_state.

**Evidence:** campaign_state.md Ch. 57 / world_state.md §5: *"burned the vial's label at the Dead Winter tree — nearly caught by the staffer Irony."* This is presented as resolved information from the confession, not an open question.

**Suggested Fix:** If this scene precedes the confession (see Findings 2–3), flagging it as an open thread is consistent — it was unknown at the time. In that case, the recap should make the pre-confession timeline placement explicit. If the scene follows the confession, calling it an "open thread" is a continuity error; it should be marked as answered.

---

## Finding 5: Zalthir described as proposing "Dragonborn to Dragonborn" approach to Alkrist — species detail accurate, but Alkrist's species should be confirmed in context

**Location:** Scene Summary, Verbatim Moments (Zalthir's lines)

**Issue:** The recap states Zalthir proposes a "Dragonborn to Dragonborn" approach for the Alkrist interview, implying Zalthir and Alkrist share a species connection. Zalthir is indeed a dragonborn (brass) and Alkrist is confirmed as a bronze dragonborn. This is factually consistent. However, the verbatim quote also shows Zalthir suggesting bringing "Kalan?" for this encounter, which slightly muddies whether the "Dragonborn to Dragonborn" rapport is between Zalthir and Alkrist, or Zalthir and Kalan. Kalan Strongbranch's species is not specified in the campaign documents reviewed.

**Evidence:** entity_registry.yaml: Alkrist — *"bronze dragonborn."* party.md: Zalthir — *"Dragonborn (Brass)."* Kalan Strongbranch — no species listed in campaign_state, world_state, or entity_registry.

**Suggested Fix:** Low severity. Clarify in the recap that the "Dragonborn to Dragonborn" framing refers to Zalthir and Alkrist specifically. If Kalan is also a dragonborn, note it in his NPC entry; if not, the verbatim transcript's apparent conflation of "Kalan" into the dragonborn dynamic should be noted as a conversational tangent rather than a factual claim.

---

## Finding 6: Fembris Lancer described as departing to "locate" Kalan, who has "disappeared somewhere"

**Location:** Scene Summary, Verbatim Moments (GM as Fembris), Scene Tag

**Issue:** The recap says Kalan "apparently disappeared somewhere," forcing Fembris to hunt him down. The campaign_state records that after being removed from the case by Bookwyrm, Kalan was ordered to attend to Candlekeep's defenses. His going "missing" in this context is a minor continuity point: the campaign_state does not list him as missing or unlocatable — it records him as reassigned to defense duties by Bookwyrm. The description of him having "disappeared somewhere" may be casual table language, but it could create a misleading impression for future session prep that Kalan is genuinely absent or unaccounted for.

**Evidence:** campaign_state.md NPC table: Kalan Strongbranch — *"Ally; Gate Warden, sidelined from the case by Bookwyrm (at Janussi's instigation); cast the zone of truth."* kalan_strongbranch.new_notes.057.md: *"ordered by Bookwyrm to attend to the library's defenses."*

**Suggested Fix:** Replace "disappeared somewhere" with a note that Kalan was reassigned to defense duties by Bookwyrm and Fembris needs to locate him within the keep. This preserves the sense of mild inconvenience without implying Kalan's whereabouts are genuinely unknown or that his absence is suspicious.

---

## Summary Table

| # | Location in Recap | Issue | Severity |
|---|---|---|---|
| 1 | Scene Summary / Scene Tag | Daz's Sylvira interview described as upcoming; already completed in Ch. 57 | High — contradicts completed canon |
| 2 | Scene Summary / Verbatim / Scene Tag | Kalan's zone of truth / Alkrist interrogation described as future; already completed in Ch. 57 | High — contradicts completed canon |
| 3 | Scene Summary / Verbatim / Scene Tag | Grygum's Janussi-chambers visit described as upcoming; already completed in Ch. 57 | High — contradicts completed canon |
| 4 | Scene Summary / Verbatim / Scene Tag | "What Alkrist burned" flagged as open thread; answered in Ch. 57 confession | Medium — misleading if post-confession |
| 5 | Scene Summary / Verbatim | "Dragonborn to Dragonborn" conflates Zalthir/Alkrist dynamic with Kalan mention | Low — minor ambiguity |
| 6 | Scene Summary / Verbatim / Scene Tag | Kalan described as having "disappeared"; he was reassigned to defense duties | Low — misleading framing |

---

**Overall assessment:** The most likely explanation for Findings 1–4 is that this recap describes events that occurred *before* the Ch. 57 Alkrist confession — i.e., this is the planning scene that leads into the confession. If so, the recap requires an explicit framing note establishing its position in the session timeline *prior to* the confession, so future editors and the GM do not treat it as a post-confession scene. Without that framing, the recap as written directly contradicts three separately documented Ch. 57 completed events.