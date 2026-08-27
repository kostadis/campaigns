# Consistency Report — Ch48 Scene Docs (session 20260811) vs. Campaign Context

## Errors

**1. Vukradin already carrying the letter of credit (Scene 01)**
- **Location:** Scene 01, *Bathrobe Speech to Empty Room* — "He has his conflict-free letter of credit from the mine payout and he carries it the way I carry the halberd" and the "I guess the letter of credit is for later" exchange.
- **Issue:** Prep-doc leakage presented as played fact. Vukradin did not arrive holding a letter of credit; he learned of it inside the bank.
- **Evidence:** `campaign_state.md` (ch48 fold): "Vukradin collected a Neverwinter Commission letter of credit worth 200 gp" *at* the Counting House. Scene 03 itself contradicts Scene 01: Aurelan announces "there appears to be a notice of credit for you," Vukradin only reads the amount after the R&C table ("I look at the letter properly. Two hundred gold pieces"), and is surprised by the whole arrangement ("Why am I getting 200 gold?" / "somehow I did not know that" re: Commission ownership). The "certified conflict-free Letter of Credit" he carries into the bank exists only in `20260728_linene_margaster.md`, explicitly tagged `[PREP]`.
- **Suggested fix:** In Scene 01, remove the physical letter and the "conflict-free" prep phrasing; render it as Vukradin hoping the mine money finally materializes in Neverwinter (or cut the beat). The "letter of credit is for later" line needs tape verification before keeping.

**2. Dinner with Neverember pinned to "tomorrow" (Scene 07)**
- **Location:** Scene 07, closing line — "Somebody wanted that machine to stay dead, and tomorrow we eat his food."
- **Issue:** Re-fixes a date the GM deliberately unfixed. This is the exact false-positive class the hand-edit was written to stop — but in reverse: the recap is *asserting* a schedule that no longer exists.
- **Evidence:** `campaign_state.md`, "Neverwinter — Immediate Schedule (updated end of ch48)": "THE SCHEDULE HAS SLID… Neither has a fixed date any more; both are simply **upcoming**."
- **Suggested fix:** "…and soon we eat his food" (or "and we are invited to eat his food"). Keep Brewbarry's spoken "Haven't we been invited…to have dinner?" — that line is tape (l.4647).

**3. Concert pinned to "tomorrow" (Scene 08)**
- **Location:** Scene 08 — Vukradin: "We've got a lot going on tomorrow, so we've got a concert."
- **Issue:** Same class as #2. The benefit concert has no fixed date per the schedule ruling; tape l.2407 has "at dawn of whatever the next appropriate day is."
- **Evidence:** Same Immediate Schedule block. Note: Cullen's "come tomorrow" for the gnome's name **is** canon ("the following day," item 5) — don't touch that one.
- **Suggested fix:** Verify against tape. If Vukradin said "tomorrow" verbatim, keep the dialogue but avoid propagating "tomorrow" into narration or future-session prep; if not verbatim, soften to "we've got a concert coming up."

**4. "Dragging Perrin with us" (Scene 08)**
- **Location:** Scene 08, opening — "We arrive dragging Perrin with us."
- **Issue:** Wrong person. Brewbarry scruffed the **fixer**, not Perrin; Perrin came voluntarily.
- **Evidence:** Scene 05: "Brewbarry takes the fixer by the neck… 'No, you're coming.'" `gm-assist.md`: "grabbing the House Margaster fixer firmly by the scruff." Scene 05: "why don't you come with us?" to Perrin.
- **Suggested fix:** "We arrive with Perrin in tow and his fixer in Brewbarry's grip."

**5. Dividend "in Brewbarry's pouch" (Scene 04)**
- **Location:** Scene 04, opening — "the mine's dividend rides heavy in Brewbarry's pouch."
- **Issue:** Misattributed custody. The 200 gp credit was addressed to and collected by Vukradin; Valphine recorded the entry. Nothing supports Brewbarry carrying it.
- **Evidence:** Scene 03 ("Mr. Vukradin, there appears to be a notice of credit **for you**"; "I will let Valphine record the entry"); `campaign_state.md` ("Vukradin collected a Neverwinter Commission letter of credit worth 200 gp").
- **Suggested fix:** "the mine's dividend rides heavy in Vukradin's pack" (or leave custody unstated).

**6. Knowledge-boundary violation: "demonic trappings" (Scene 06)**
- **Location:** Scene 06 — "No hidden sigils, no demonic trappings, none of the usual Margaster stink on the premises." (Vukradin narration of Valphine's read.)
- **Issue:** No character knows about Margaster's demonic/cambion connections — that is explicitly player knowledge. Narrating an *expectation* of demonic trappings puts the demon association inside character knowledge. The ch48 recap itself correctly reclassified the "Were they Cambions?" exchange as table speech (Scene 04 comment block), so this line contradicts its own reclassification.
- **Evidence:** `Phandalin/CLAUDE.md` → `docs/Margaster.md`: "The cambion connection is player knowledge from another adventure; **no character knows it**."
- **Suggested fix:** Replace with what the characters do suspect: "No hidden sigils, no forger's back room, none of the stink of the writ racket."

## Questionable — verify against tape

**7. Paperwork-crumpling location: notary vs. Eastern Quay (Scene 06 / Scene 08 vs. gm-assist)**
- **Location:** Scene 08 places Brewbarry crumpling the Margaster paperwork and the fixer's aborted weapon-reach at the Eastern Quay warehouse, checked by "Cullen Sharpe's look." `gm-assist.md` places both beats in the **not**ary** scene ("Brewbarry crumples the Margaster paperwork… causing the fixer to briefly reach for his weapon" is listed under *The Notary of House Margaster*).
- **Issue:** The two derived documents disagree on where this happened. Scene 06 (notary, Vukradin narrating) contains no crumpling at all; Scene 08 has it at the quay. One of them is wrong.
- **Evidence:** As above. The Scene 08 detail that the fixer's hand comes off the hilt "exactly as long as it takes Cullen Sharpe to look at him" argues for the quay — Cullen was not at the notary.
- **Suggested fix:** Verify on tape. If the quay is correct (likely), correct `gm-assist.md`'s scene placement rather than the recap; if the notary is correct, move the beat into Scene 06 and strip the Cullen detail.

**8. Layaway offered twice (Scene 06 and Scene 08)**
- **Location:** Scene 06 (notary: "keep the necklace in layaway in House Margaster's warehouses") and Scene 08 (quay: "House Margaster produces its next offer: hand the Necklace of Fireballs to them for safekeeping, a warehouse layaway").
- **Issue:** Possible duplicated beat. `gm-assist.md` records the layaway/safekeeping offer only at the notary. A renewed offer at the quay is plausible but unverified.
- **Suggested fix:** Verify on tape; if not repeated, cut the Scene 08 offer and keep only the refusal-standing ("They know what they gotta do — three witnesses").

**9. "Oral B. Vance" diegetized (Scene 01)**
- **Location:** Scene 01 — "My name is Oral B. Vance." … "this time it comes out Aurelan Vance. Names are slippery today."
- **Issue:** "Oral B. Vance" is a recorded transcription garble, deliberately **not** an alias, per the 2026-08-13 GM ruling. The recap puts the garble in the NPC's mouth as canon (he misspoke his own name), which the "Names are slippery today" framing smooths over. This may be intentional — the players' riffs ("space-based brand," Soma's "weird pun") are real table lines being diegetized — but it creates in-fiction canon out of a documented wrong-form.
- **Evidence:** `entity_registry.yaml` Aurelan Vance entry; `vtt_known_additions.md` 2026-08-13.
- **Suggested fix:** GM decision: either bless the mishearing as an in-fiction beat (then note it on the Aurelan dossier so future passes don't "fix" it), or rewrite the introduction so the party mishears without the NPC saying the wrong-form.

**10. "Title insurance" coinage (Scene 06 vs. gm-assist)**
- **Location:** Scene 06 — Vukradin coins it ("It's title insurance! … I have just invented a product line for House Margaster"; the notary "has never heard the term"). `gm-assist.md` says the Margaster agent offered it "a form of 'title insurance,' **he called it**."
- **Issue:** Direct attribution conflict between the two derived docs on who coined the term.
- **Suggested fix:** Verify on tape; the Scene 06 version has tape texture (the notary shelving it as a future product) and is likely correct — if so, fix `gm-assist.md`, not the recap.

**11. "You, the Falcon and Don-Jon" as mine shareholders (Scene 03)**
- **Location:** Scene 03 — Aurelan: "Yeah, you, you, the Falcon and Don-Jon."
- **Issue:** Don-Jon Raskin is dead (ch31) and the party holds his share. If verbatim tape, this is the Commission's stale ledger and fine as spoken; if summarizer-supplied, it's an error.
- **Evidence:** `campaign_state.md`: "Don-Jon Raskin — Dead"; "Party holds Don-Jon's share of the mine."
- **Suggested fix:** Verify verbatim. If tape, keep — it's a usable hook (the Commission doesn't know he's dead). If not, drop the name.

**12. Valphine's "Chinese wall" line (Scene 03)**
- **Location:** Scene 03 — "Valphine, deadpan at my shoulder: 'I have a Chinese wall between departments.'"
- **Issue:** As rendered, Valphine claims to *have* a Chinese wall, which makes no sense; the line is almost certainly her voicing/mocking the banker's department excuse. Likely a table-speech attribution smoothed into first person.
- **Suggested fix:** "Valphine, deadpan, in the banker's voice: 'He has a Chinese wall between departments.'" — or reclassify.

## Minor

**13. "Her brother" (Scene 04 dialogue).** Vukradin: "they extorted money out of her brother." The brother/cousin conflict is unresolved: `campaign_state.md` uses *brother* with a settle-at-table flag; `entity_registry.yaml` records a 2026-08-03 GM ruling for **cousin** with dialogue-as-spoken left intact. Since this is quoted dialogue, it is permissible under the established policy — but flag it so a future pass doesn't promote "brother" into narration. No narration in these scenes uses either term (correct handling elsewhere).

**14. "Their third appearance in as many days" (Scene 02).** The writ shakedown and Cullen's pitch were both ch47 (evening of arrival, day 1); the banker's steer is ch48 (day 2). Three appearances in *two* days. Suggested: "their third appearance since we reached this city."

**15. Boney: "stuck in a tomb for a few hundred years" (Scene 05).** Registry has Lady Alagondar killing Azdraka "over a century ago" — Boney's interment is ~100–150 years, not "a few hundred." In-character dialogue and possibly Boney exaggerating; keep, but don't let "centuries" propagate into grounding docs (note `gm-assist.md` already says "studying… for centuries" — that's the drift starting).

**16. "Wrote to me last 10 days" (Scene 05).** Setting uses tendays; the prep scripts it as "last tenday." Suggested: "wrote to me last tenday" (or verify Perrin's actual spoken form).

**17. "It adds 15 pounds" (Scene 05).** The rest of the camera-joke cluster ("The camera zooms in," "Very dramatic zoom") was reclassified as table speech, but this line from the same riff was left in-fiction as Soma's. Inconsistent treatment; recommend reclassifying with its siblings or confirming with the user (per the reclassification-confirmation rule).

**18. "Trade his scale mail for the elven chain" (Scene 05).** Correctly implements the 2026-08-15 ruling (Valphine as source, settled at table) — good. Two nits: "trade" implies exchange where the ruling says she *gave* it; and Scene 01 dresses Brewbarry in "hides under the bathrobe" all morning, so the scale mail appears from nowhere at the swap. Cosmetic; consider "hands him the elven chain out of House Sotorra's stores."

## Advisory — not errors, but track before next session

- **Scene 08, Cullen's Kaelen claim** ("Ser Kaelen suggested you might have [problems] when he reached out to us through one of our agents") is new on-screen canon connecting Kaelen to Margaster's apparatus — consistent with the GM design (Kaelen's recovery office routes through the Margaster-endowed desk in good faith), and Valphine's narration correctly holds both readings open. It is recorded in **no grounding doc**. Add to `campaign_state.md` open threads so it isn't lost.
- **Scene 08, Valphine's verdict "It is authentic."** Her examination of the notary paperwork is a *character conclusion about the physical document*, and by design: Margaster's method is real paper over a manufactured claim. The provenance remains a **forgery** per GM canon. Flag so no future pass "corrects" the GM notes to match her read, and so no pass "corrects" her read to say forgery.
- **Valphine's lie-detection ability** (Scene 08 narration "the quiet that lets a lie ring against the ear"; table-speech: "you have a special ability now… where you can detect lies") is a new table-granted mechanic in no character sheet or grounding doc. Record it (golden-eyes threshold ability?) before it's needed again.
- **Boney's genealogy obsession** (Scene 05) is new characterization, internally consistent with his Alagondar history and the necklace-ownership ruling. Worth promoting to his entry.

## Verified — do not re-flag

- **Bathrobe:** worn, plural, prepared-speech-in-bathrobe — all consistent with the ch48 RESOLVED ruling.
- **Dawn service / Neverember dinner not occurring in ch48:** correct per the slid schedule (the issue above is only the recap *re-fixing* dates).
- **"Lathander's Death"** announced at the bank (Scene 01) — matches tape cues 221/223.
- **Boney's "It belonged to Lady Alagondar"** (Scene 05) — matches the 2026-08-15 ownership ruling and the corrected re-transcription (not the "I belong" Zoom garble).
- **"Pengro," "Eastern Quay," "The Bronze Sun," "Aurelan Vance," "Elara Seasong Meliamne" in the quest journal** — all rendered in canonical forms; the previously-removed landmine rows (`Lara→Lyra`, `Bony→Boney`, `Barry→Brewbarry`) did not corrupt these scenes ("I was a bony creature" survives correctly in Scene 05).
- **Brewbarry's full-name fumble** left unresolved in narration ("I trip on the tribe part") with the verbatim grope confined to the table-speech block — matches the 2026-08-13 ruling not to canonize the third element.
- **Vukradin's "fourth-level slot" / Polymorph** (Scene 06) — consistent with the level-7 sheet (trust `characters/*.md` per the KNOWN GAP note).
- **KP leak check:** "I have a feeling I know who the gnome is" is correctly quarantined in table speech; no narration connects the gnome to KP or names him a gnome-the-party-shouldn't-suspect.
- **Cambion lines** correctly reclassified as table speech in Scene 04 (the one narration leak is issue #6).
- **Falcon's letter to Rimardo/Corrin** (Scene 03) — canon (ch45 note, carried by the party).
- **Anachronistic riffs** ("Houston, Texas," "Mandalore," "SystemD," "Zoomer," "recently unalived") — established table style, lampshaded in-fiction; not flags.