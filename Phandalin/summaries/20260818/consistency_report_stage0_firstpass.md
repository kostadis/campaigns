# Consistency Report — Session 2026-08-18 Recap (Spire of the Morninglord)

## Critical errors

### 1. "Ondrel Vance" is a dead name — the banker is Aurelan Vance
- **Location:** Summary (final paragraph), Scenes ("Information Gathering: Cullen Sharpe and the Counting House"), Locations ("Counting House"), NPCs ("Ondrel Vance"), Memorable Moments (Assassin's Guild quote caption)
- **Issue:** The Counting House banker is named "Ondrel Vance" throughout. This name does not exist in canon and was explicitly retired.
- **Evidence:** **AUTHORITATIVE CANON** (entity registry): the banker is **Aurelan Vance** — "Banker at the Counting House… The forms 'Oral B. Vance', 'Andrell'… and the summarizer-invented **'Ondrell B. Vance'** are TRANSCRIPTION GARBLES… deliberately NOT aliases." The consolidated live-state doc (GM decision #1, 2026-08-18): "'Ondrel Vance' and 'Mira Tollund' remain **dead names** — don't reuse either." Decisively, the vtt_known_additions entry *for this very session* records: "**Assassin's Guild** — Valphine's proposed route… and the suggestion that turns **Aurelan Vance** pale" — i.e., the banker in this scene was already adjudicated as Aurelan.
- **Suggested fix:** Replace every "Ondrel Vance" with "Aurelan Vance." This is a summarizer resurrection of a retired name and will re-contaminate downstream docs if it survives.

### 2. Valphine receives white dragon scale armor — attribution/timeline conflict
- **Location:** Summary (first paragraph), Scenes ("Arrival at the Spire"), NPCs ("Scales"), Items ("White Dragon Scale Armor")
- **Issue:** The recap has the armorer deliver and fit "Valphine's gleaming white dragon scale armor" at the temple doors, with "a blessing from Lathander as payment." This collides with canon on three points: (a) the outstanding commission at this shop is **Brewbarry's** dragon scale mail (Lathander emblem, **300 gp owed**, "still uncollected as of end of ch47"); (b) per the 2026-08-15 GM ruling (elven chain mail entry), Valphine "has worn White Dragon Plate +1 **since ch46**" — so a first fitting now contradicts that ruling; (c) the Items entry is internally inconsistent, calling it "scale armor" in the title and "a suit of **plate mail**" in the body.
- **Evidence:** campaign_state ("Collect Brewbarry's dragon scale mail… 300 gp owed — still uncollected"; "Dragon Scale Mail Commissioned (ch45)… for Brewbarry"); party.md KNOWN GAP note (Valphine: White Dragon Plate +1 attuned, AC 22); vtt_known_additions 2026-08-15 ("she has worn White Dragon Plate +1 since ch46"). These are generated/working docs, not canon-tier, but they agree with each other.
- **Suggested fix:** GM must reconcile: either this session dramatized the on-screen delivery of **Valphine's** White Dragon Plate (in which case amend the 2026-08-15 "since ch46" rationale, and note Brewbarry's 300 gp scale mail is *still* uncollected), or the recap has mis-attributed **Brewbarry's** commission to Valphine. Also resolve whether the 300 gp was actually paid — "blessing as payment" contradicts the recorded debt (the blessing already bought the 82% discount, not the balance). Fix the scale/plate wording either way.

### 3. "Aldous" → Aldus
- **Location:** Scenes ("Lathander's Death Performance and the Shakedown"), NPCs ("Aldous")
- **Issue:** Neverember's steward is rendered "Aldous," a known transcription garble.
- **Evidence:** **AUTHORITATIVE CANON** (entity registry): **Aldus Hern**, alias "Aldus." The VTT corrections glossary explicitly maps `Aldous` → **Aldus**.
- **Suggested fix:** "Aldus" in both places (optionally "Aldus Hern" in the NPC entry).

### 4. "Spire of the Morning Lord" → "Spire of the Morninglord"
- **Location:** Title usage throughout — Summary, Scenes, Locations, Memorable Moments captions
- **Issue:** The temple name is consistently spelled as two words.
- **Evidence:** **AUTHORITATIVE CANON** (entity registry): the location is "**Spire of the Morninglord**." The corrections glossary maps `Morning Lord` → **Morninglord**.
- **Suggested fix:** Normalize the temple name to "Spire of the Morninglord" everywhere.

### 5. "Meryl Staff" → Meril's Staff
- **Location:** Summary, Scenes ("Lathander's Death Performance"), Items ("Meryl Staff")
- **Issue:** Soma's staff is called "the Meryl Staff."
- **Evidence:** **AUTHORITATIVE CANON** (entity registry): "**Meril's Staff**… Distinct from the ch45 Staff of Bird Calls." Glossary: `meryl, Merrill, Mariel` → **Meril**.
- **Suggested fix:** "Meril's Staff." (The recap correctly does *not* conflate it with the Staff of Bird Calls — keep it that way; canon marks them confirmed distinct.)

## Ability / attribution errors

### 6. Brewbarry cannot cast Thaumaturgy
- **Location:** Spells ("Thaumaturgy"), Scenes ("Brewbarry uses a magically booming voice")
- **Issue:** The Spells section states Thaumaturgy was "used by Brewbarry to boom his voice." Brewbarry is a Barbarian (Path of the Giant) with no spellcasting.
- **Evidence:** party.md / characters sheets: Barbarian 6→7, no spell list. Valphine (cleric) is the only party member who plausibly has Thaumaturgy.
- **Suggested fix:** Verify the tape; most likely Valphine cast Thaumaturgy to amplify Brewbarry's voice. Rewrite as "cast by Valphine on Brewbarry's behalf" (or whatever the tape shows).

### 7. Thaumaturgy credited with Valphine's glowing eyes
- **Location:** Spells ("Thaumaturgy"), Scenes ("eyes blazing with divine light, accompanied by ominous whispers created through magic for theatrical effect")
- **Issue:** The recap attributes the glowing eyes to a Thaumaturgy trick. Valphine's eyes glow gold **permanently** — this is the ch45 "crossed a threshold" development, the central thread of her current arc — not a cantrip effect. Recording it as stagecraft risks demoting a major canon state-change into a parlor trick in future sessions.
- **Evidence:** campaign_state / world_state / party.md, all: "eyes now glow gold," "Valphine of the Blessed," Ser Kaelen's concern, the Aldric consultation. The session prep doc's GM-only note treats the eyes as possibly a *brand*.
- **Suggested fix:** Restrict Thaumaturgy's credit to the phantom whispers; the eyes glow on their own. E.g., "her permanently golden eyes blazing, phantom whispers added via Thaumaturgy."

## Claim-laundering and precision risks

### 8. Perrin's lineage recorded as "confirmed" — the forged provenance is being laundered into fact
- **Location:** Scenes ("The Alagondar Inheritance": "A genealogist confirms that Perrin is a descendant"), NPCs ("Perrin: …after his lineage is confirmed"), Items ("Alagondar Necklace: …returned to Perrin after his Alagondar lineage was verified")
- **Issue:** The recap records witness testimony as verification. Canon-side, the provenance is a **Margaster-routed forgery** that remains unexposed; the witnesses supported the claim, they did not prove it.
- **Evidence:** **AUTHORITATIVE CANON** (entity registry, Necklace of Fireballs): "CLAIM (UNVERIFIED, ch46)… the party has verified nothing. **Do not record the grave-robber story as provenance — it is the claim, and the claim and the provenance are different things.**" campaign_state/world_state: "GM: the provenance is a Margaster-routed forgery; the party does not know." Consolidated notes: Boney's testimony was scrupulous, "did NOT crack the case."
- **Suggested fix:** Rephrase to "after his witnesses supported his claim" / "his lineage claim was accepted by the party." Do not use "confirmed"/"verified" anywhere in this thread.

### 9. The Margaster-affiliation vetting of the witnesses is unrecorded
- **Location:** Scenes ("The Alagondar Inheritance")
- **Issue:** Valphine's stated condition was three witnesses **not affiliated with House Margaster**. The recap never records whether that check was made — and the prep material staged at least two witnesses (the paid genealogist, the frightened notary) as potentially compromised.
- **Evidence:** campaign_state: "three independent witnesses not affiliated with House Margaster… condition Valphine set." Prep doc witness table entries 1, 4, 7.
- **Suggested fix:** Note explicitly whether the affiliation condition was tested or waived. If it was silently waived, that is a live continuity fact worth its own line.

### 10. "Alagondar Necklace" never identified as the Necklace of Fireballs
- **Location:** Summary, Scenes, Items ("Alagondar Necklace")
- **Issue:** The item handed over is the **Necklace of Fireballs** (seven beads — GM-side, the whole point of Margaster's play is the portable arson arsenal). The recap's generic "Alagondar family necklace… a powerful magical item and symbol of the rightful rulers" could be read by a future pass as a different item, and "symbol of the rightful rulers" echoes the forged restoration-banner framing rather than the canon fact (it was Lady Tanamere Alagondar's personal grave goods).
- **Evidence:** **AUTHORITATIVE CANON** (entity registry): "FACT (ownership…): the necklace was LADY ALAGONDAR'S OWN." campaign_state/party.md track it as "Necklace of Fireballs (holding for claimant) — Vukradin."
- **Suggested fix:** Name it "the Necklace of Fireballs" at least once in Summary and in the Items entry; describe it as Lady Alagondar's own grave goods, claimed by Perrin as a dynastic treasure. Also update the party inventory: it has now left Vukradin's possession.

### 11. "Lord Neverember as the Commission's majority holder" — unattested, and in tension with GM notes
- **Location:** Summary (final paragraph), Scenes ("Information Gathering")
- **Issue:** The recap states as fact that Neverember is the Commission's majority holder. No context document attests this, and the GM-side Commission material describes "Neverember **mortgaged and losing his own count**" — the opposite of a stable majority position.
- **Evidence:** world_state ("The Commission… Opaque"); campaign_state (Commission owns Mountain's Toe; membership secret); project notes (`the_commission.md` summary: Neverember mortgaged).
- **Suggested fix:** Verify against the tape. If Aurelan said it, record it as *Aurelan's claim* ("according to Vance, Neverember holds the majority"), not as established fact — a nervous banker's assertion is exactly the kind of thing the GM may want to be wrong later.

## Minor issues

### 12. Boney's "study of family corpses"
- **Location:** Summary, Scenes, NPCs ("Boney")
- **Issue:** Canon has Boney learning genealogy by **reading gravestones and incoming tomb records** during his interment — not "studying corpses."
- **Evidence:** campaign_state ("Boney the Genealogist": "reading the gravestones… the records kept arriving"). That note also warns against letting exaggerations of Boney's tomb-scholarship drift into grounding docs.
- **Suggested fix:** "Boney's study of the barrow's gravestones and interment records."

### 13. "Polo flattery" — probable transcription garble
- **Location:** Memorable Moments (Brewbarry quote)
- **Issue:** "Polo flattery is not the donation I'm looking for" — "Polo" is almost certainly an ASR artifact (this session's Zoom capture is documented as very poor on words: Valphine 0×, Brewbarry 0×).
- **Evidence:** vtt_known_additions 2026-08-23 transcript-preference caveat.
- **Suggested fix:** Check the second transcription for the real word ("Pure"? "Hollow"?) before this quote hardens into canon.

### 14. Internal inconsistency: who set the theological trap
- **Location:** Summary ("he and a scarred sun priest attempted to theologically trap Valphine") vs. Scenes ("threading a theological trap set by the other cleric")
- **Issue:** Summary makes Aldric a co-author of the trap; Scenes attributes it solely to the other cleric. Aldric's disposition toward Valphine is a tracked thread — this matters.
- **Suggested fix:** Pick one per the tape and align both sections.

### 15. Branch name drift: "Lathander's Searing Light"
- **Location:** Summary, Scenes, Locations ("Neverwinter")
- **Issue:** Valphine's order is recorded in canon as the "Church of the Searing Light" (Phandalin temple: "Lathander's Searing Pain of Justice"). "Lathander's Searing Light" may be a genuine new coinage for the Neverwinter branch, or drift.
- **Suggested fix:** Verify against the tape; if new, record it deliberately as the Neverwinter branch's name so three near-identical names don't circulate unadjudicated.

### 16. Mielikki omitted from the garden-blessing beat
- **Location:** Scenes ("Lathander's Death Performance"), Summary
- **Issue:** Per GM ruling 2026-08-23, the syncretic supplicant identified Soma as a follower of **Mielikki** — the first utterance of the name in the campaign, and it matches Soma's sheet (`Faith: Mielikki`). The recap drops the name entirely, and "faking her way through the religious rites" sits oddly if the invoked deity is Soma's actual recorded faith.
- **Suggested fix:** Add the Mielikki identification to the scene bullet; clarify what exactly Soma was "faking" (the rite's formality vs. the faith itself).

## New entities to verify / promote (not errors)

- **"Scales"** (armorsmith, "owner of Dragon Scales R Us") — the shop name is canon ("DO NOT CORRECT" list), but the armorer has only ever been recorded as **"The Proprietor."** Verify "Scales" was actually coined at the table (not summarizer-invented), then promote via entity-triage — and rule whether Scales *is* the Proprietor or a second armorer. Note: the recap doesn't flag it, but per canon, absence from the registry alone is not evidence against him.
- **The scarred sun priest** — new NPC, unregistered.
- **Perrin's three witnesses** (revolutionary, genealogist, notary clerk) — unnamed; the genealogist in particular is GM-flagged prep-side as "paid by someone."
- **The eight followers / Neverwinter branch** — new institution; ties into the Prutha-crusade governance thread.
- **The tortle-merchandise merchant** — matches the prep's Exile Aesthetic licensing beat; connects to Brewbarry's bathrobe venture if pursued.

## Context-document conflict surfaced during this check (not a recap error)

**Cassian: brother vs. cousin.** The recap doesn't mention Lord Cassian, but campaign_state and world_state both carry a "RESOLVED 2026-08-18 — BROTHER" note, while the **AUTHORITATIVE CANON** entity registry states the opposite: "**COUSIN** of Elara Seasong Meliamne — GM ruling 2026-08-03. The Ch. 47 tape has… 'brother'… that was an in-session slip… The ch47 recap narration was corrected to 'cousin.'" Per trust tiering, canon wins and the campaign_state/world_state "brother" resolutions are the entries to flag — but since *both sides cite dated GM rulings* (2026-08-03 cousin vs. 2026-08-18 brother), this looks like two rulings made without reference to each other. A human must reconcile before the pending private-tea scene is run; whichever ruling stands, update the losing document *and* the registry note in the same pass so this stops flip-flopping.

---

**Everything else checked clean:** the dawn service finally occurring (correctly not a schedule error — the slid schedule allowed it), the Bimble Nackle reveal (Cullen's "following day" promise honored; party-knowledge framing in the recap correctly excludes GM-only facts), the band name "Lathander's Death" (canon since the 2026-08-11 tape), the Loviatar/Loviatarite spellings (canon-confirmed for this session), Brewbarry's bathrobe (resolved, correctly not re-flagged), Valphine singing in Undercommon, the Assassin's Guild beat, and the Sending Stone / Magic Mouth surveillance plan (Vukradin can legitimately cast Magic Mouth).