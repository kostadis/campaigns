# Consistency Report — "The Exotic Armorer of Neverwinter"

---

## Issue 1: NPC name — "Brother Aldrich" vs. "Aldric"

**Location:** Scene Summary; Verbatim Moments (multiple instances)

**Issue:** The armorer refers to the Lathander priest as "Brother Aldrich" in the scene summary and in the GM's verbatim dialogue ("Brother Aldric was right!" in the final proprietor quote). The scene summary uses "Aldric" in the last bullet but "Aldrich" earlier — there is inconsistency within the recap itself.

**Evidence:** The entity registry and the `vtt_transcription_corrections.md` file both establish the canonical spelling as **Aldric** (correction entry: "Aldrich, Adric, Adrik, Aldrick, Audric → **Aldric**"). The Neverwinter location cheat sheet names the priest **Brother Aldric Sunmantle**.

**Suggested fix:** Standardize to **Aldric** (or **Aldric Sunmantle** if full name is appropriate) throughout. Replace all instances of "Aldrich."

---

## Issue 2: Character name — "Bernberry" vs. "Brewbarry"

**Location:** Verbatim Moments — scene tag "The Original Quote"; Valphine's line "This will be for Bernberry, though."

**Issue:** The transcript renders the name as "Bernberry" — a clear VTT transcription error.

**Evidence:** The canonical PC name is **Brewbarry** (confirmed in party.md, campaign_state.md, world_state.md, and the corrections glossary, which lists "Brewberry, Burberry, Blueberry…→ **Brewbarry**").

**Suggested fix:** Replace "Bernberry" with **Brewbarry**. This is a standard transcription artifact per the VTT corrections file.

---

## Issue 3: Armor type — scale mail vs. Brewbarry's current equipment

**Location:** Scene Summary (bullet 4, 5); Verbatim Moments (multiple)

**Issue:** The recap states the party is commissioning **scale mail** from dragon scales for Brewbarry. However, Brewbarry already has scale mail listed in his inventory (acquired ch41 per world_state.md and party.md). The commission would be a second suit of scale mail, or potentially something different. The recap does not acknowledge this.

**Evidence:** Brewbarry's items per world_state.md (Brewbarry section): "scale mail (ch41); normally prefers no armor." Party.md also lists scale mail among his gear. Commissioning new scale mail is not inherently contradictory, but it is noteworthy — the armor type may have been intended to be something else (e.g., dragon scale mail as a distinct upgraded type), and the recap offers no clarification.

**Suggested fix:** Add a GM note clarifying whether this is a replacement/upgrade suit (dragon scale mail as a distinct magic item type) or a second identical suit. If the intent was a distinct magic item tier, name it accordingly to avoid future confusion.

---

## Issue 4: Deity title — "her" (feminine pronoun for Lathander)

**Location:** Verbatim Moments — GM narration: "You have the blessing of her!"

**Issue:** The transcript has the proprietor saying "You have the blessing of her!" — a feminine pronoun applied to Lathander, who is canonically a **male** deity.

**Evidence:** The entity registry lists Lathander without gendered specification, but canonical FR lore consistently presents Lathander as male. No campaign document overrides this. More likely this is a transcription artifact (the GM may have said "of Him" or "of the Lord").

**Suggested fix:** Correct "her" to "Him" or "the Morninglord" in the cleaned transcript to avoid lore confusion in future sessions. Flag as probable transcription garble.

---

## Issue 5: Party composition described as "four" — Prutha not accounted for

**Location:** Verbatim Moments — GM line: "Right, so the four of you walk in."

**Issue:** The GM states four party members enter. The active party includes Vukradin, Soma, Valphine, Brewbarry, **plus Prutha** (orc convert who is with the party) and potentially Boney. If Prutha and/or Boney are with the party at this point in Neverwinter, "four" may be inaccurate.

**Evidence:** campaign_state.md (Party Current Situation) lists Prutha as "With party at Woodland Manse" at ch45 end. The NPC state table shows Prutha's disposition as "Loyal (Valphine's follower)." The ch46 re-prep doc notes "Prutha optional" for the Neverwinter session. Boney is listed as traveling with the party.

**Suggested fix:** Clarify in a GM note whether Prutha (and Boney) were left outside, stabled, or absent from this specific scene. If only the four PCs entered, note that explicitly for continuity. "Four" should not be left ambiguous given Prutha's active party status.

---

## Issue 6: Recap states armor will be ready "before they leave Neverwinter" — no timeline established in context docs

**Location:** Scene Summary (final bullet); Verbatim Moments — GM: "I will assert it will be done by the time you're leaving town."

**Issue:** This is not a factual error, but it creates a **standing commitment** that needs to be tracked. No campaign_state.md entry records a pending Neverwinter commission or shop location.

**Evidence:** The GM explicitly notes in the verbatim section: "I just need to put a note here that says I remember" — indicating this was handled informally. Campaign_state.md has no entry for this commission under Active Quests, Pending Objectives, or Outstanding Obligations.

**Suggested fix:** Add to campaign_state.md Active Quests / Neverwinter Pending Objectives: "Dragon scale mail commissioned at armorer in Protector's Enclave — 300 gp paid; emblem of Lathander on back; for Brewbarry; to be collected before party departs Neverwinter." Record shop location on the GM's map as noted.

---

## Issue 7: Ambiguous claim — "The proprietor is a follower of the Morning Lord"

**Location:** Scene Summary (bullet 2); Verbatim Moments — GM setup

**Issue:** The proprietor is introduced as a follower of the Morning Lord who recognizes Valphine's "sign." This creates a new named or unnamed NPC with Lathandrite connections in Neverwinter. He is not listed in the NPC state table, the entity registry, or any prep document.

**Evidence:** No campaign document references this armorer. The Neverwinter prep docs (20260623_neverwinter_vukradin_present.md, locations cheatsheet) do not include an armorer in the Protector's Enclave among the listed NPCs or locations.

**Suggested fix:** Add the armorer as a minor NPC entry in the entity registry (unnamed or name him now) with his location (Protector's Enclave, exotic armorer shop) and disposition (Lathandrite, favorable to party). This prevents future sessions from introducing a contradictory NPC at the same location.

---

## Issue 8: Recap header labels the proprietor's temple contact as "Brother Aldric" speaking of Valphine — but Aldric is stationed at the Spire of the Morninglord in Neverwinter

**Location:** Scene Summary (bullet 2); Verbatim Moments

**Issue:** The proprietor asks Valphine: "Are you the drow that Brother Aldric speaks of?" This implies Aldric Sunmantle has been telling Neverwinter Lathandrites about Valphine before the party arrived — a potentially significant worldbuilding implication that the recap treats as incidental flavor.

**Evidence:** The Neverwinter locations cheatsheet places **Brother Aldric Sunmantle** at the **Spire of the Morninglord** in the Protector's Enclave and frames his scene as Valphine's "golden-eyes confrontation" — a payoff scene, not a pre-arrival background event. The prep doc does not indicate Aldric has been spreading word of Valphine; his scene is framed as a first contact.

**Suggested fix:** Determine whether this is intentional (Aldric learned of Valphine through divine means or prior contact and has been speaking of her in the community) or an improvised line whose implications need to be walked back or canonized. If intentional, update Aldric's NPC entry to note he has been preaching about the converted drow prior to the party's arrival. If improvised flavor, flag it as a loose thread that could create continuity issues when the party meets Aldric at the Spire.