# Consistency Report — Recap: "Arrival in Neverwinter"

---

## Issue 1 — Castle Never Naming

**Location:** Scene tag "Castle Never in the Distance" / Memorable Moments verbatim

**Issue:** The recap states the GM said "Castle Neverember" and "Castle Never" as if they are two distinct or interchangeable names for the same structure. The recap text in the Summary section correctly uses "Castle Never," but the verbatim GM quote reads: *"you see, up in the far distance, Castle Neverember, and Castle Never."* This is almost certainly a transcription artifact (VTT garble of "Castle Never" into "Castle Neverember"), but as written it implies two castles or an alternate name "Castle Neverember."

**Evidence:** `vtt_transcription_corrections.md` explicitly lists "Castle Nevermember" → **Castle Never** as a known VTT garble. `world_state.md` identifies the structure as **Castle Never** (founded by Lord Halueth Never). Lord **Neverember** is the current ruler, not the castle's namesake. The castle is named for Halueth Never, not for Dagult Neverember.

**Suggested fix:** In the verbatim quote, note the VTT garble. In the summary and scene tag, retain "Castle Never." Do not use "Castle Neverember" as a valid name for the structure in any canon-forward document.

---

## Issue 2 — "Vukerton" as Fan's Nickname

**Location:** Scene tag "The 'Sold Out' Debate" / Memorable Moments verbatim

**Issue:** A fan refers to Vukradin as "Vukerton." The recap treats this as a live character moment, which is fine narratively, but "Vukerton" also appears in `vtt_transcription_corrections.md` as a known VTT mistranscription of "Vukradin." The recap should flag this as intentional in-world dialogue (a fan mispronouncing/misnaming) rather than a transcription error, or it will create confusion in future VTT cleanup passes.

**Evidence:** `vtt_transcription_corrections.md` lists "Vukerton" → **Vukradin** as a correction target.

**Suggested fix:** Add an editorial note in the recap that "Vukerton" here is intentional in-fiction dialogue by the fan character, not a transcription error, so it is not auto-corrected in future VTT cleanup.

---

## Issue 3 — Spire Naming Inconsistency

**Location:** Scene tag "The Board Laid Bare" / Memorable Moments verbatim (Brewbarry's innuendo line)

**Issue:** The verbatim quote has Brewbarry say *"the Spire of the Mourning Lord"* (emphasis: "Mourning"). The correct name as established in the session prep documents and entity registry is the **Spire of the Morninglord** (Lathander's title). "Mourning Lord" is an in-character malapropism by Brewbarry that is funny in context, but the scene tag heading in the final session section calls it "the Spire of the Morning Lord" (two words, no "ing" on "Morn-"), while the entity registry uses "Spire of the Morninglord" (one word).

**Evidence:** `20260623_neverwinter_locations_cheatsheet.md` uses "Spire of the Morninglord." `entity_registry.yaml` entry `Spire of the Morninglord`. The canonical Lathander title throughout all documents is **Morninglord** (one word). `vtt_transcription_corrections.md` lists "Mord Lord, Morning Lord" → **Morninglord**.

**Suggested fix:** In the scene tag heading, correct to "Spire of the Morninglord." In Brewbarry's verbatim quote, retain "Spire of the Mourning Lord" as intentional in-character humour with an editorial note that it is a deliberate malapropism, not the canonical name.

---

## Issue 4 — Necklace of Fireballs Item Holder

**Location:** Scene tag "Dragon Scale Armor Commission" / Summary

**Issue:** Valphine says *"I'm hoping that we can barter this, staff and bird calls as part of the"* — suggesting the Staff of Bird Calls as barter for the armor. Vukradin then objects that it is "blood money." The recap summary states the party decided *"to barter Dragon Scales rather than the 'blood money' Staff of Bird Calls."* This is consistent. However, the recap also states in the final bullet: *"discussing returning the necklace of fireballs to the Alagondar family."* According to all campaign documents, the Necklace of Fireballs is held by **Vukradin**, and Ser Kaelen's note identifies the recipient as **Perrin Alagondar** — a *quiet branch* of the family with *no title, no army.* There is no Alagondar royal claim attached to this item, and the entity registry identifies the **Alagondar** faction as the *ruling lineage*, not a quiet collateral branch. The phrasing "the Alagondar family" is ambiguous and could mislead future sessions into treating this as a politically charged royal restitution rather than a private bequest recovery.

**Evidence:** `campaign_state.md` Active Obligations: *"Vukradin holds items for rightful owners: Necklace of Fireballs."* Ser Kaelen's note in the verbatim: *"an Alagondar, quiet, branch, no title, no army… Perrin Alagondar."* `entity_registry.yaml`: Alagondar faction = royal ruling lineage killed in the cataclysm.

**Suggested fix:** Replace "the Alagondar family" with "Perrin Alagondar (a quiet collateral branch, no title, no army)" to preserve the distinction between the royal line and this private recovery.

---

## Issue 5 — Craftsman's Shop / Armor Recipient Naming

**Location:** Scene tag "The Lathander Craftsman"

**Issue:** The GM's verbatim transcript renders the craftsman saying *"Rubbery works for you?"* as a mangled version of "Brewbarry." This is a VTT garble rendered as dialogue. More critically, Valphine says *"This will be for Bernberry, though"* — another VTT garble of "Brewbarry." These appear in the verbatim without editorial correction, which could cause confusion in future sessions about who commissioned the armor.

**Evidence:** `vtt_transcription_corrections.md` lists "Rubbery" and "Rubery/Rubbery" → **Brewbarry**. "Bernberry" is not in the corrections list but follows the same pattern.

**Suggested fix:** Add editorial glosses: *[Rubbery = Brewbarry; VTT garble]* and *[Bernberry = Brewbarry; VTT garble]* at the relevant verbatim lines. Confirm in the scene summary that the armor commission is for **Brewbarry**.

---

## Issue 6 — Boots of Elvenkind Attribution

**Location:** Summary bullet / implicitly in the scene

**Issue:** The recap mentions the party deciding to commission **dragon scale armor** and barter Dragon Scales. No issue there. However, the campaign documents note that **Boots of Elvenkind** were awarded to **Vukradin** (not Valphine) as the Woodland Manse quest reward. The recap does not misattribute the Boots, but it also does not clarify that the dragon scale armor being commissioned here is *new* bespoke armor (presumably for Brewbarry per the craftsman scene) and is separate from existing party items. This is a potential ambiguity rather than an error, but worth flagging: if a future reader confuses the "scale mail" Brewbarry already owns (listed in `party.md` and `world_state.md`) with the new dragon scale armor commission, continuity will be muddied.

**Evidence:** `party.md` Brewbarry: "scale mail (ch41)." `world_state.md` Brewbarry items: "scale mail." The new commission appears to be *dragon scale mail* replacing existing scale mail.

**Suggested fix:** Add a clarifying note in the scene summary that this commission is for *new dragon scale armor* (dragon scales as material) intended to replace Brewbarry's existing scale mail, not a duplicate or additional item.

---

## Issue 7 — Elara Meliamne Referenced as a Living Contact

**Location:** Summary opening bullet / Active Obligations subtext

**Issue:** The recap does not explicitly mention Elara Meliamne, which is correct — she is dead. However, the recap's framing of "outstanding obligations" lists mine money, Zeleen's gem, and Horia's addendum, without noting the **most time-sensitive** Neverwinter obligation: returning the mermaid statue to **Lord Cassian Meliamne** before House Margaster acts further. This is not an error in what the recap *says*, but the omission of this obligation from the outstanding tasks summary is a continuity gap that could mislead future session planning into treating the Neverwinter visit as lower-urgency than it is.

**Evidence:** `campaign_state.md` Active Obligations: *"Return mermaid statue to Lord Cassian Meliamne (Elara Meliamne's cousin — Elara is dead, killed by House Margaster). Urgency: House Margaster agents have been intercepting the statue. Contact: Cassian, not Elara. Before House Margaster intervenes."* `party.md`: same urgency framing. NPC table: Elara listed as **Dead**.

**Suggested fix:** Add to the outstanding obligations bullet: the mermaid statue return to Cassian Meliamne (not Elara, who is dead) as a time-sensitive Neverwinter task, distinct from the mine/gem obligations.

---

## Issue 8 — "Orsik, Defender of Parnast" Title

**Location:** Scene tag "The Lord's Alliance Plaque and Propaganda" / Summary

**Issue:** The recap correctly names the broadsheet subject as **"Orsik, defender of Parnast, champion of the North."** No error here. However, the scene tag heading calls it simply "The Lord's Alliance Plaque and Propaganda," while the verbatim correctly distinguishes the **carved stone plaque** (honoring the Liberators of the Ordning / giant kingdoms) from the **broadsheet** (featuring Orsik). The summary conflates these two items in a single bullet: *"The party observes a carved stone plaque honoring the 'liberators of the Ordning'… and a Lord's Alliance herald in blue and gold distributing propaganda broadsheets."* This is accurate. But then: *"The party notes that the Lord's Alliance broadsheet — fronted by Orsik, Defender of Parnast — shows their territorial jurisdiction now includes Neverwinter Wood, Leilon, and Phandalin via a dotted line."*

The broadsheet's jurisdiction map extending to Phandalin is a significant plot point (Jenna Roscoe's head start, the UBT proclamation implications, the Orsik propaganda machine). Treating it as a casual observation rather than a flagged open thread understates its importance for future sessions.

**Evidence:** `20260623_jenna_roscoe_head_start.md`: *"The broadsheet map (Phandalin inside Alliance jurisdiction) takes on new weight if someone in Neverwinter is already treating the UBT as a sovereignty question."* `20260623_neverwinter_vukradin_present.md` Scene V3: *"the broadsheet's back-page map with a dotted jurisdiction line through Neverwinter Wood, Leilon, and Phandalin — the person who should trip on it is Vukradin."*

**Suggested fix:** Flag the broadsheet / jurisdiction map as an **open thread** in the recap, not merely an observation. Note that this connects to Jenna Roscoe's head start and the UBT proclamation implications.

---

## Issue 9 — Mine Stop Bypass Framing

**Location:** Summary opening bullet

**Issue:** The recap correctly notes the mine stop was bypassed. It lists "Mine money collection, Zeleen's Earthstone Gem retrieval, and Horia's secret addendum" as outstanding. However, the recap does not note that the mine payday was likely **converted to a Letter of Credit redeemable in Neverwinter** per the session prep — or if it was not converted, that the physical mine stop remains an unresolved errand. As written, the recap leaves ambiguous whether the party has simply deferred the mine visit (intending to return) or whether the money was issued as a Letter of Credit to be redeemed in Neverwinter (which would trigger the Golden Ledger Audit scene).

**Evidence:** `20260623_neverwinter_vukradin_present.md`: *"Fold the planned Mountain's Toe payday into Scene V2 rather than running a separate mine stop — the mine's commission and Vukradin's cut are issued as a certified conflict-free Letter of Credit, redeemable in Neverwinter."* `campaign_state.md` Mountain's Toe: *"Mine stop bypassed (ch46) — party went directly to Neverwinter. Money collection, gem retrieval, and addendum remain unresolved."*

**Suggested fix:** Clarify in the outstanding obligations whether the mine payout was issued as a Letter of Credit (redeemable in Neverwinter, triggering the audit scene) or whether the physical mine visit remains a pending errand. This has direct consequences for Scene V2 in subsequent sessions.

---

## Issue 10 — "Vukradin's old haunt" / Common Chord Location

**Location:** Scene tag "Approaching the City" / Scene tag "The Common Chord's Exclusivity"

**Issue:** The recap refers to the Common Chord as "Vukradin's old haunt." The entity registry and location cheatsheet are more specific: the Common Chord is *"where he was periodically allowed to play and then thrown out without pay."* The recap's phrasing makes it sound like a venue Vukradin owned or had ongoing access to, rather than a venue where he was an irregular, under-compensated performer who was repeatedly ejected. This subtly misrepresents the power dynamic, which matters for the scene where Vukradin learns the venue now has weeks of reservations and sky-high prices *because of him*.

**Evidence:** `entity_registry.yaml` (Common Chord): *"Vukradin's old venue, where he was periodically allowed to play and then thrown out without pay; now the hardest ticket in the city."*

**Suggested fix:** Change "old haunt" to "the venue where he used to play — periodically, without pay, and at the owner's discretion" or similar phrasing that preserves the exploitative dynamic.

---

## No Issues Found

The following elements were checked and are consistent with campaign documents:

- Brewbarry holding the Dragon Slayer Sword (correct; `party.md`, `world_state.md`)
- Soma holding Staff of Bird Calls (correct; `campaign_state.md`)
- Vukradin holding Necklace of Fireballs and Obsidian Sword (correct; `party.md`)
- Valphine's golden eyes and Lathander affiliation (correct; `party.md`)
- Ser Kaelen's note about Perrin Alagondar as the necklace recipient (consistent with verbatim)
- Lord's Alliance herald in blue and gold livery (consistent with `world_state.md`)
- Hunting Lodge, Dragon Barrow, Logger's Camp listed as previously cleared (correct; `campaign_state.md`)
- Shrine of Savras noted as abandoned quest (consistent; party acknowledged it as unvisited but chose not to pursue)
- Writ sent ahead from Phandalin confirming party is expected (no contradiction found)
- Vukradin's UBT reference ("UBT") is consistent with the session's in-character slang for Universal Basic Treasure