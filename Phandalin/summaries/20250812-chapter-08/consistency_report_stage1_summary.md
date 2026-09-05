# Consistency Report — Chapter 8 Recap ("Tower of Storms: Harpies & Moesko", 2025-08-12)

**Overall verdict:** The recap is a faithful, enriched expansion of the session's `gm-assist.md` export and is largely consistent with canon and campaign state. Critically for a 2025-era backfill, it contains **no anachronistic leakage from the later campaign** (no Boney, no Dragon Slayer Sword, no +1 halberd, no golden eyes, no Prutha — all correctly absent). The issues below are mostly internal contradictions, one canon spelling divergence, and attribution uncertainties typical of the known transcript label problems.

---

## High-confidence issues

### 1. Name diverges from canon: "Krabby McGee"
- **Location:** Scenes — "Exploring the Tower of Storms" (final bullet: *"I don't think Krabby McGee told us that."*)
- **Issue:** The intelligent crab's canonical name is spelled **Crabby**, not "Krabby."
- **Evidence:** **AUTHORITATIVE CANON** (entity registry): `Crabby — Name the party gave the giant intelligent crab at the Tower of Storms… gifted intelligence by the sea elf Miraal` (sourced from the Chapter 07 summary, one session earlier). No "Krabby" or "McGee" alias exists in the registry.
- **Suggested fix:** Render as "Crabby McGee" (the "McGee" riff can stand as table color, but the canonical spelling should be C-, or verify against the ch8 tape and add "McGee" as an alias via entity-triage if it's a recurring nickname).

### 2. Internal contradiction: "natural 1" vs. the quote that disproves it
- **Location:** Summary, Memorable Moments ("Brewbarry rolls a natural one…"), Scenes — "The Battle of the Harpies Continues"
- **Issue:** The recap asserts a **natural 1** on Brewbarry's Wisdom save three times, while simultaneously quoting the table's own arithmetic that it was a **rolled 2 with a −1 modifier, net 1**: *"It's a two minus one, just to be clear. It's a net of a one."* The Summary's gloss — "a natural 1… 'a net of a one' after modifiers" — is self-contradictory (a natural 1 with −1 would net 0).
- **Evidence:** The quote block itself. Note `gm-assist.md` also says "natural one," so the error originates upstream — but the recap adds the contradicting quote, making the incoherence visible.
- **Suggested fix:** "an effective 1 on the save (rolled a 2, minus 1)" throughout; drop "natural."

### 3. Internal contradiction: Soma's hit points after the lightning bolt (2 vs. 11)
- **Location:** Memorable Moments ("leaving Soma at two hit points…") vs. Scenes — "Showdown with Moesko" ("Soma burns her Wild Shape **at 11 hit points**")
- **Issue:** The scene list places the wild shape *after* the lightning bolt, but gives Soma 11 HP where the Memorable Moment (and `gm-assist.md`) says the bolt left her at 2. No intervening healing is recorded.
- **Evidence:** `gm-assist.md`: "leaving Soma at two hit points, Vukradin at three, and Brewbarry at four."
- **Suggested fix:** Verify against the transcript; one number is wrong. gm-assist supports 2 — either correct "11" or establish that 11 was her pre-bolt total and reposition the detail.

### 4. Cross-document conflict: was Brewbarry hit by the lightning bolt?
- **Location:** Summary + Memorable Moments (Brewbarry left at 4 HP by the bolt) vs. `chapter_10` narrative (Soma POV: *"everyone but Brewbarry is struck"*)
- **Issue:** The recap and `gm-assist.md` agree Brewbarry was struck and dropped to 4; the bible narrative chapter says he was the one member *not* struck.
- **Evidence:** As quoted above. The recap matches its generated source, so the narrative chapter is the more likely error — but only the transcript settles it.
- **Suggested fix:** Verify on tape; if the recap is right, queue a correction to `chapter_10` (his 4 HP may instead trace to earlier damage/thunderwave).

### 5. Chapter-numbering conflict: Chapter 8 vs. the bible's `chapter_10`
- **Location:** Document header ("# Chapter 8, Date: 2025-08-12")
- **Issue:** The bible narrative file covering **this exact session** (harpies + Moesko, same beats, same quotes) is titled `chapter_10_the_tower_of_storms…`. That's a two-chapter discrepancy — and the documented 2026-08-18 renumbering only corrected references **≥21**, so it doesn't explain this.
- **Evidence:** `campaign_state.md` timeline: "Ch08–09 | Tower of Storms: Moesko defeated; lighthouse purified" — supports the recap's "Chapter 8." Weekly cadence from `summaries/20250805-chapter-07` also supports 2025-08-12 = ch8. The POV-narrative file says Chapter 10.
- **Suggested fix:** Confirm whether the POV-narrative chapters use a different numbering scheme; if not, one of the two artifacts is misnumbered. Do not let "Chapter 10" propagate into grounding docs for this session.

---

## Medium-confidence issues

### 6. Speaker attributions that read wrong (known transcript-label failure modes)
- **Location:** Memorable Moments
- **Issue:** Several quotes sit oddly against who plays whom (Wade=Soma, David=Vukradin, Gary=Valphine, Stéphane=Brewbarry):
  - *"Yeah, it smells of elderberry. 13 save for your life."* — attributed to **Wade**, but the recap's own Summary and Spells sections make the elderberry insult **Vukradin's** Vicious Mockery, and "13 save" is a caster/DM call. Either Wade was feeding the insult (possible, worth confirming) or this is a label flip.
  - *"Dex saves for everybody."* — attributed to **Gary**; this reads as a DM call.
  - Both natural-1 commentary quotes (*"when I said not great…"*, *"It's a two minus one…"*) go to **Wade**, though the roll and modifier statement belong to Brewbarry's player.
  - *"Dead."* — attributed to David; the kill was Soma's and death announcements are typically the DM's.
- **Evidence:** Player/character table in the campaign CLAUDE.md; the recap's own in-fiction attribution of the mockery to Vukradin. Known issues: Zoom mid-sentence speaker flips and one-player-two-PCs label collapse in this campaign's transcripts.
- **Suggested fix:** Verify these four against the speaker-labelled export before this recap feeds any voice or chronicle pass.

### 7. Moesko: "orc" vs. canon "half-orc"
- **Location:** Scenes — "Showdown with Moesko" ("an **orc** anchorite like those the party has faced before"); Spells — Poison Spray, Cloud of Daggers ("the orc")
- **Issue:** Canon and the recap's own Summary/NPCs sections say **half-orc**; the Scenes and Spells sections drift to "orc." Also, "like those the party has faced before" is thin — the only prior candidate is the coastal-gully orc shaman who shapeshifted into a boar (an anchorite tell), and it's unclear the party knew the order at that point.
- **Evidence:** **AUTHORITATIVE CANON:** `Moesko — Half-orc anchorite of Talos…`; glossary maps `Hafalken → half-orc anchorite`. (`chapter_10` shares the "Orc Anchorite" looseness — it should not be treated as corroboration.)
- **Suggested fix:** Normalize to "half-orc anchorite"; verify the "faced before" wording against the tape.

### 8. Knowledge-boundary leak: "the tower's corrupted beacon"
- **Location:** Summary and Locations (both state the wrecks lie "beneath the tower's corrupted beacon" as narrative fact)
- **Issue:** The same recap records that the party does **not** yet know what lures the ships — the DM "nearly tips his hand… before conceding the party doesn't actually know," capped by the Crabby McGee line. Since the bible functions as the party's shared-knowledge allowlist, stating "corrupted beacon" as fact in ch8 launders GM knowledge into party knowledge two sessions early (the beacon's nature resolves at T9, next session).
- **Evidence:** `campaign_state.md`: heart destruction / beacon extinguished is a separate, later encounter (T9). The recap's own "Exploring" scene.
- **Suggested fix:** Reword to what was observed ("beneath the tower's sickly green beacon" or "the beacon the party did not yet understand").

### 9. Stone Altar entry adds unattested party intent
- **Location:** Items — Stone Altar ("The party eyed it as a likely key to lifting the tower's curse but did not interact with it yet")
- **Issue:** Not in `gm-assist.md`, and the same knowledge problem as #8 — "the tower's curse" is not yet established party knowledge. The module's altar boon (Charm of the Storm) is flagged NOT FOUND IN SUMMARIES in campaign_state, so nothing on record supports "eyed as a key."
- **Suggested fix:** Cut the sentence or soften to "noted and left alone"; verify against tape.

### 10. Fresco### 10. Fresco chamber and altar room: one room or two?
- **Location:** Summary (altar placed *in* the fresco chamber) vs. Locations (lists "a fresco chamber…; an altar room with a salt-encrusted west window" as **separate** rooms)
- **Issue:** The recap disagrees with itself about the tower's layout.
- **Evidence:** **AUTHORITATIVE CANON:** `Shrine of Talos (T4) — Frescoed shrine room with a lightning-fed altar dedicated to Talos` — one room containing both. The Summary matches canon; the Locations section splits them.
- **Suggested fix:** Merge the Locations entry into a single frescoed shrine room with the altar and lightning rod (per T4), unless the tape shows the DM ran them as two rooms.

### 11. "Santorini house" — unattested detail
- **Location:** Scenes — "Showdown with Moesko" ("the industrial-grade router his **Santorini** house needs")
- **Issue:** The Summary and Memorable Moments say only "Greece" / "relatives in Greece"; "Santorini" appears in no context document and only in this one bullet. Given this recap is an enrichment pass over `gm-assist.md` (which omits the outage entirely), the specific island may be an invention.
- **Suggested fix:** Verify against the tape; if not spoken, fall back to "his house in Greece."

---

## Low-severity notes

### 12. Thunderwave: who was pushed?
- **Location:** Summary ("pushed the party back ten feet") vs. Scenes ("Soma shrugs off the worst on her Constitution save") vs. `chapter_10` (Soma: "pushes me back")
- **Issue:** A successful Thunderwave save means half damage and **no** push — so the recap's scene bullet (Soma saved) contradicts both its own Summary and the narrative chapter (Soma pushed). Minor, but one of the three is wrong.
- **Suggested fix:** Verify; adjust either the save note or the "party pushed back" generalization.

### 13. "Valphine, freshly saved against the charm"
- **Location:** Scenes — "Silence at the Tower of Storms"
- **Issue:** Per the Summary and `chapter_10`, Valphine was **charmed and then freed by the Silence sphere**, not by a save — unless this refers to a later, second song attempt she did save against.
- **Suggested fix:** "freshly freed of the charm" unless the tape shows a successful save.

### 14. Bardic Inspiration used on self — table ruling, not RAW
- **Location:** Summary, Memorable Moments, Spells — Bardic Inspiration
- **Issue:** Both 2014 and 2024 rules restrict Bardic Inspiration to "a creature **other than yourself**." Not an error to fix — the recap, `gm-assist.md`, and `chapter_10` all agree this is what was played — but it should be recorded as a house ruling so a future mechanics or consistency pass doesn't "correct" the scene and break the "failing upward" moment.
- **Suggested fix:** None to the recap; consider a one-line house-rule note in mechanics/planning docs.

### 15. Silence phrasing: "twenty-foot sphere"
- **Location:** Summary
- **Issue:** Reads as a 20-foot-diameter sphere; the spell (and the recap's own Spells section) is a 20-foot-**radius** sphere. Trivial.
- **Suggested fix:** "twenty-foot-radius sphere."

---

## Errors in OTHER documents surfaced by this check (recap is correct; do not "fix" the recap toward them)

### 16. "Miral" spelling in generated grounding docs
- **Issue:** The recap correctly spells **Miraal** throughout. But `campaign_state.md`'s timeline ("Miral's ghost warns…", Ch08–09 row) and `world_state.md`'s Leilon section ("Miral (ch09) warned…") carry the garbled form, and `chapter_10` has both "Miral the Sea Elf" and the badly garbled "Miral the Self" (= "Miraal the Sea Elf").
- **Evidence:** **AUTHORITATIVE CANON:** `Miraal — Sea elf slain by Moesko; her spirit haunts the Haunted Cave as a banshee`. The VTT glossary independently maps `Miral → Miraal`.
- **Suggested fix:** Correct the two grounding docs and queue a `chapter_10` repair ("Miral the Self" especially, which reads as a different phrase entirely). Never regress the recap's spelling.

### 17. `chapter_10`'s "everyone but Brewbarry is struck"
- Already covered in finding #4 — if the transcript confirms the recap/gm-assist version, the bible chapter needs the correction, not the recap.

---

## Verified clean (checked, no action needed)

- **Statblock facts:** harpy INT 7, AC 11, 300-ft song range, 24-hour per-harpy immunity on a successful save, incapacitated-and-compelled charm, rage lapsing from disuse, Thorn Whip pulls (doesn't knock prone), Cloud of Daggers 5-ft cube, Thunderwave 2d8/CON/10-ft push, Lightning Bolt 8d6, Moesko AC 13 / 58 HP — all consistent.
- **Canon geography:** 80-ft outcropping, rough-hewn stairs on the eastern face, 15-ft-high empty foyer (T3), harpy nest on a ledge (T5, potion of water breathing location) — all match the registry.
- **Party knowledge of Miraal/the conch:** established in Chapter 7 via Crabby (registry, ch07 source) — the recap's "the party knew they had to take it back" is legitimate.
- **Kill credits and sequence:** Valphine one harpy, Brewbarry one, Vukradin one (mockery); Soma's final blow on Moesko after dropping bear form — matches `gm-assist.md` and `campaign_state.md` ("Moesko killed; Soma delivered final blow").
- **Scope discipline:** heart destruction (T9), Miraal's laying to rest (T1), sharks, and shipwrecks are correctly **absent** — the recap ends with the conch unexamined, matching "next week."
- **"Soma's heard better songs":** correctly de-garbled (tape says "Soba's"; glossary confirms the ch08 provenance of this exact line).
- **No back-contamination:** no Boney, no Dragon Slayer Sword, plain halberd and hand axes only, mundane crossbow/mace for Valphine — the gear and companions are period-correct for Chapter 8.