# Continuity Report — "The Universal Basic Treasure Proclamation"

---

## ISSUE 1 — Wrong name used for Ser Kaelen mid-scene

**Location:** Scene tag "Ser Kaelen's eligibility sidebar" — Vukradin's line

**Issue:** After Ser Kaelen raises the eligibility question, Vukradin addresses him as "Valphine": *"Excellent, excellent idea, Valphine!"*

**Evidence:** Ser Kaelen is listed throughout all campaign documents as the person who raises the sidebar. Valphine is a separate PC (drow cleric). The prior line is GM speaking as Ser Kaelen. Vukradin has no reason to address Valphine here; the remark is clearly aimed at the NPC who just spoke.

**Suggested fix:** Change Vukradin's attribution line to *"Excellent, excellent idea, Kaelen!"* (or "Ser Kaelen"). Flag in the raw transcript as a likely mis-hear or VTT garble ("Valfine" / "Valphine" is a documented common transcription error per `vtt_transcription_corrections.md`).

---

## ISSUE 2 — Jenna Roscoe's faction label may need precision

**Location:** Scene tag "Jenna leaves town" and Memorable Moments / NPCs section (GM line: *"The members of the Lord's Alliance are very particular."*)

**Issue:** The recap correctly associates Jenna with the Lord's Alliance. No error there. However, the scene recap describes Jenna as departing *because* she is "appalled" at the UBT populist move and riding toward Neverwinter. Per `20260623_jenna_roscoe_head_start.md`, this departure is load-bearing: Jenna arriving in Neverwinter ahead of the party is a planned consequence with downstream consequences (Alliance letter at the Counting House, disposition worsened from Neutral to hostile, etc.). The recap does not flag this as consequential.

**Evidence:** `20260623_jenna_roscoe_head_start.md` — "After Vukradin's Universal Basic Treasure proclamation…Jenna Roscoe departed Phandalin in visible disgust and headed back to Neverwinter **ahead of the party**…Why this matters: Jenna is a Lord's Alliance agent. With a head start she could: brief Alliance leadership…frame the party as agitators…A Lord's Alliance letter has already arrived at the Counting House…"

**Suggested fix:** Add a note to the recap (in a GM-facing consequences block, not in the scene prose) flagging Jenna's departure as the triggering event for her Neverwinter head start. The scene text itself is not wrong, but the downstream consequence is invisible to anyone reading only this recap.

---

## ISSUE 3 — Meril's Staff attributed as the instrument of Soma's Arcana identification — possible but worth flagging

**Location:** Scene tag "Soma's Arcana check" — GM line: *"Fortunately, Soma has her staff."* / Soma's line: *"I could detect a planar anomaly around this cube…"*

**Issue:** The recap states Soma uses "her staff" (confirmed as Meril's Staff by the GM's prompt) to detect a planar anomaly on the dragon slag. This is plausible — Meril's Staff "glows to detect unnatural things" per `world_state.md` and `party.md`. However, Soma also newly possesses the **Staff of Bird Calls** (acquired ch45, now openly held after the Zone of Truth confession). The recap does not specify *which* staff is used. Given the Staff of Bird Calls has no documented detection ability, Meril's Staff is the correct inference — but the ambiguity exists in the text.

**Evidence:** `world_state.md` — "Meril's Staff: Sentient-like; glows to detect unnatural things." `party.md` — "Staff of Bird Calls — retrieved from the Woodland Manse fireplace…confessed under Zone of Truth; now openly held."

**Suggested fix:** Clarify in the recap that Soma uses **Meril's Staff** specifically (not the Staff of Bird Calls) for the planar anomaly detection. Prevents future confusion about which staff has which capability.

---

## ISSUE 4 — "Cryovain's hoard" treated as a "fused slag of dragon gold" the party donates — possible continuity tension with hoard status

**Location:** Scene tags "Donating the dragon slag" and "The magical nature of the slag"

**Issue:** The party donates a "fused slag of dragon gold" to the UBT fund, described as something recovered from Cryovain and fused inside a magical containment. The campaign state notes that the Cryovain hoard (~3,000 gp) is at Icespire Hold, unclaimed — Vukradin *refused* it (`campaign_state.md`: "~3,000 gp Cryovain hoard at Icespire Hold — unclaimed (Vukradin refused it)"; `party.md` same). There is no prior mention of a "fused slag of dragon gold" in any party inventory or recent encounter record.

**Evidence:** `party.md` — "~3,000 gp Cryovain hoard at Icespire Hold — unclaimed (Vukradin refused it)." The hoard is at Icespire Hold, not in the party's possession. No item called "dragon slag," "fused gold," or similar appears in the tracked items table in `world_state.md` or `party.md`.

**Suggested fix:** Clarify in the recap what the physical origin of this slag is. If it is a portion of the Cryovain hoard the party *did* carry away (separate from what was left at the Hold), that item needs to be added to the tracked inventory retroactively. If it is a newly introduced item from this scene, its origin must be established (GM invention, prior loot not previously catalogued, etc.). As written, the donation of "dragon gold" contradicts Vukradin's documented refusal of the Cryovain hoard.

---

## ISSUE 5 — Linene Graywind described as producing a "Candlekeep text" — title does not match existing canon item

**Location:** Scene tag "Linene's Candlekeep theorem"

**Issue:** Linene produces a book called "the Sage's Universal Theorem for Income Distribution," described as a Candlekeep text. No such document exists in any campaign context document. There is a **Candlekeep Working Paper No. 27** ("The Hoarding Hero: Or, Why Some Adventurers Are Economically Indistinguishable From The Monsters They Slay") that is documented as a real in-world text in `20260623_neverwinter_vukradin_present.md` and the `entity_registry.yaml`. That paper's thesis (adventurers who hoard = economically indistinguishable from dragons) is thematically adjacent but distinct.

**Evidence:** `entity_registry.yaml` — "Candlekeep Working Paper No. 27: 'The Hoarding Hero…'" `20260623_neverwinter_vukradin_present.md` — same document used as Neverember's lever on Vukradin. No reference to any "Sage's Universal Theorem for Income Distribution" anywhere in the context documents.

**Suggested fix:** Either (a) establish the "Sage's Universal Theorem for Income Distribution" as a new in-world document and add it to the entity registry, or (b) clarify that Linene is producing a different Candlekeep text from Working Paper No. 27 (both exist; both are thematically related to adventurer economics). Either way, the new title should be logged to prevent it being confused with the existing canonised paper in future sessions.

---

## ISSUE 6 — Privy Council membership list inconsistency: "Petunia" listed as a council member

**Location:** Scene tag "The rock concert on the town green" — GM line assembling the crowd includes "Petunia"

**Issue:** "Petunia" appears in the crowd list alongside confirmed Privy Council members. The canonical Privy Council per `world_state.md` is: Harbin Wester, Toblen, Elmar Barthen, Halia Thornton, Linene Graywind, Adabra, and Vukradin. "Petunia" is not a council member and does not appear as a named NPC in any campaign context document. Petunia *is* the name of Alfonse Kalazorn's cow (recovered at Butterskull Ranch, now grazing with Qelline Alderleaf).

**Evidence:** `campaign_state.md` — "Butterskull Ranch — Petunia the Cow Recovery: Soma used Speak with Animals to locate and identify Petunia. Cow secured; grazing arrangement negotiated with Qelline Alderleaf." `world_state.md` — Privy Council members listed; no NPC named Petunia. `entity_registry.yaml` — Petunia is not listed as a human NPC.

**Suggested fix:** Determine whether "Petunia" in this scene is: (a) a VTT transcription garble for another NPC name (e.g. "Halia" or a crowd extra), (b) a newly named Phandalin resident introduced this session who needs to be added to the entity registry, or (c) an error. If it is the cow, her presence at a town meeting on the green is plausible (she grazes nearby) but her being grouped with council members requires clarification. Flag for GM review.

---

## ISSUE 7 — Boots of Elvenkind assigned to wrong character

**Location:** Items table cross-check (implicit — the recap does not directly assign items, but the scene involves Vukradin's inventory claims)

**Issue:** Not a direct recap error, but the recap's scene has Vukradin handling the dragon slag and delegating to Ser Kaelen — consistent with his role. However, the GM prep document (`20260623_neverwinter_vukradin_present.md`) and `party.md` both show **Boots of Elvenkind → Vukradin** (awarded ch43). The `entity_registry.yaml` entry says: "Boots of Elvenkind: Magic item reward offered by Falcon for completing the Woodland Manse Quest." The Woodland Manse Quest reward is confirmed for Vukradin in `world_state.md`. No conflict in the recap itself, but flagging because the Boots' assignment has a minor documentation inconsistency: `world_state.md` objects table says "Boots of Elvenkind — Vukradin — Acquired ch43" while `party.md` also says Vukradin. These are consistent. No action needed on the recap; note filed for completeness.

**Suggested fix:** No change needed to the recap. Internal documents are consistent.

---

## ISSUE 8 — Ambiguous claim: "Soma identifying a planar anomaly via Meril's Staff that requires an expert in Neverwinter"

**Location:** Scene summary closing bullet and scene tag "Soma's Arcana check"

**Issue:** The summary states the dragon slag has a "planar anomaly" requiring a Neverwinter expert. Soma's in-character line connects it to "those weird gnome things" and "the whole reason we're intervening." This appears to link the slag's magical containment to the Gnomengarde gnomes or to the broader planar incursion thread. Neither connection is established in campaign_state.md or world_state.md — the dragon slag's planar nature is new information introduced this scene. Soma's reference to "gnome things" is ambiguous and could be misread in future sessions as an established canon link.

**Evidence:** No prior documentation of the Cryovain hoard having a planar containment property. The planar incursion thread (Whispering Wood rift, Aletra's device, KP's operations) is open but unconnected to dragon gold in any context document.

**Suggested fix:** Add a GM note to the recap clarifying that the planar anomaly in the slag is newly established in this scene and has not yet been connected to any specific prior thread. Soma's "gnome things" line should be flagged as in-character speculation, not confirmed canon, to avoid it being treated as an established link in future session prep.