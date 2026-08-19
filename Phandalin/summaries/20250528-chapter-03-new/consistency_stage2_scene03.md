# Consistency Report — "Archaeologists and Altars" (Chapter 3 scene extraction)

## Issue 1 — Dazlyn/Norbus role attribution contradicts the gm-assist NPC dossier (HIGH)

- **Location**: Verbatim Moments (the mid-combat dwarf shouts)
- **Issue**: The scene splits the two dwarves' concerns the opposite way from gm-assist's NPC section. Here, **Dazlyn** gets the artwork/preservation lines ("please don't damage any of the artwork… This is an important archeological find") and **Norbus** gets a safety line ("D- did somebody, did somebody get hurt?"). gm-assist's NPC entries say the reverse division: Dazlyn's calls were "a separate concern for the party's safety, **distinct from Norbus's warning about damage to the site**," and Norbus is the one who "urged the party to avoid damaging the ruins with powerful spells."
- **Evidence**: gm-assist.md → NPCs → Dazlyn ("Is everybody okay there?" — a separate concern for the party's safety) and Norbus ("urged the party to avoid damaging the ruins"). Note also entity_registry.yaml characterizes Norbus as "gruff and excessively cautious" and Dazlyn as "forthright" — and Dazlyn/Norbus are a phonetically confusable pair per the VTT corrections glossary ("Dazzlyn/Dazzlin…", "Norbas/Dorbus"), a known swap-risk class.
- **Suggested fix**: Verify each caption's speaker against the VTT (`summaries/20250528-chapter-03-new/`). Either the scene's mid-combat attributions or gm-assist's NPC entries are wrong; align both once confirmed. Do not let this feed NPC dossiers until resolved.

## Issue 2 — Related internal contradiction in the context the scene draws on (MEDIUM)

- **Location**: Verbatim Moments (safety shouts), vs. gm-assist Summary
- **Issue**: gm-assist's Summary claims the dwarves "shouted their concerns — **not about the party's wellbeing**," but the scene's verbatim captions include two explicit wellbeing checks ("Is everybody okay there?", "did somebody get hurt?"), and gm-assist's own Dazlyn entry confirms a safety concern existed. If the scene's quotes are transcript-accurate, the gm-assist Summary line is a mischaracterization that shouldn't propagate.
- **Evidence**: gm-assist.md Summary ¶2 vs. gm-assist.md NPCs → Dazlyn; scene's two safety quotes.
- **Suggested fix**: When resolving Issue 1, correct the gm-assist Summary sentence (or annotate it) so future extractions don't inherit "neither dwarf cared about the party's safety" as fact.

## Issue 3 — Sending-stones negotiation needs an explicit "no stones changed hands" marker (MEDIUM)

- **Location**: Scene summary bullets 2–3; Verbatim Moments ("You take those sending stones now" / "Give us one sending stone now")
- **Issue**: The scene records the demands but never states the outcome. Per GM ruling, the dwarves withheld the stones until the temple was fully cleared and handed them over only at session's end. Vukradin's "You take those sending stones now" is also ambiguously phrased (it's a demand for handover, but reads as if he might be conceding them). A future pass could easily record a stone in the party's possession mid-session.
- **Evidence**: campaign_state → "Sending Stones — promised, not yet delivered… GM-confirmed 2026-08-17 against the session transcript: the dwarves withhold the stones until the temple is fully cleared and hand them over only at the end of that session"; planning_ch02.md Active Plot 2; gm-assist places the handover in the later "Amateur Archaeologists" scene.
- **Suggested fix**: Add one clarifying line to the summary, e.g. "The dwarves deflect both demands — no stone changes hands until the ruins are fully cleared (end of session)."

## Issue 4 — Timeline gap: Ogre #2 and the return from the Gnomengarde route are unaccounted for (MEDIUM)

- **Location**: Scene framing (and the whole Chapter 3 recap it belongs to)
- **Issue**: The most recent campaign_state (Chapter 2 archive) ends with the party **mid-combat with Ogre #2, en route to Gnomengarde**. This Chapter 3 material opens with the party back at the dwarven temple, with no narration of the ogre's fate or the backtrack to the ruins. campaign_state explicitly reserves that resolution for "whatever chapter narrates it next" — and this chapter doesn't.
- **Evidence**: campaign_state → "Ogre Encounter #2 … IN PROGRESS, unresolved at chapter's end… the resolution belongs to whatever chapter narrates it next"; gm-assist Chapter 3 opens "at a crossroads in the ancient dwarven ruins."
- **Suggested fix**: Check the Chapter 3 VTT opening for the ogre resolution/recap; if it exists, capture it in the chapter archive before this scene. If it genuinely isn't on the tape, log it as a GM decision point rather than silently skipping it.

## Issue 5 — Corrupted duplicated caption block (LOW, formatting)

- **Location**: Verbatim Moments, the prospectors' protest
- **Issue**: A copy/paste splice mid-word: `"We're, we're just, w- we have a de**GM** — the prospectors protesting the arrangement > "We're, we're just, w- we have a deal here. We're partners"` — the header and quote are duplicated inside the first quote.
- **Suggested fix**: Delete the truncated first fragment; keep the complete "…we have a deal here. We're partners" caption.

## Issue 6 — "Morning Lord" wrong-form in a verbatim quote (LOW)

- **Location**: Verbatim Moments, GM's Lathanderite-openness ruling
- **Issue**: "from the Morning Lord who shared that information" uses a glossaried wrong-form.
- **Evidence**: vtt_transcription_corrections.md: "Mord Lord, Morning Lord → **Morninglord**" (and "Morning Ford → Morninglord").
- **Suggested fix**: Render as "Morninglord" in the quote (the scene summary already uses the correct form).

## Issue 7 — The "16 perception" credit to Valphine is a GM ruling, not a captured roll (LOW)

- **Location**: Scene summary final bullet; Verbatim Moments ("Okay. 16 perception, if that helps")
- **Issue**: The roll is captured under the GM's label, and Dave's "I can match that" implies at least two rolls in play. The summary states flatly that Valphine rolled the 16; what's actually on tape is the GM *awarding* the find to the cleric ("Actually, to be precise, the cleric finds a set of secret doors"). The verbatim section hedges correctly; the summary doesn't.
- **Suggested fix**: Phrase the summary as "the GM awards the find to Valphine (a 16 on perception, speaker uncertain in the captions)."

## Issue 8 — Brewbarry/Stéphane entirely absent from the captions (LOW, verify)

- **Location**: Whole scene
- **Issue**: Not one caption is attributed to Stéphane or Brewbarry. This may be genuine silence in a social scene — but a known VTT failure mode is that naive speaker-label greps drop "Stéphane" because of the accented character, faking an absent player. (Gary also covers Brewbarry when Stéphane is absent, which would change attribution defaults for the session.)
- **Evidence**: Memory note on VTT speaker-label greps; Phandalin CLAUDE.md coverage rule.
- **Suggested fix**: Confirm Stéphane's presence for the 2025-05-28 session from the raw VTT before this scene's silence is treated as characterization.

## Issue 9 — Minor interpretive stretches worth a [sic]-level flag (LOW)

- **Location**: Scene summary bullets 1–2
- **Issue**: (a) "with four hit points apiece they would have been useless" is an interpretation of a heavily garbled caption ("they're, they're four hit point. They're useless") — plausible, but the referent of "they" is not clean on the tape. (b) The summary says "Norbus **and Dazlyn** emerge from hiding," while the `[Norbus Emerges]` beat narrates only Norbus peeking in (gm-assist has both creeping in afterward — likely Norbus first, both eventually).
- **Suggested fix**: Keep both readings but mark them as inferred from garbled/staggered captions rather than clean quotes.

---

**Checked and found consistent**: dwarf names/spellings (Dazlyn Grayshard, Norbus Ironrune); the reward structure (sending stones for temple clearing, distinct from the already-paid 50 gp); the Abbathor temple and blood-stained altar location (registry E5); the pillar secret door → Skull Cavity linkage; secret doors found *before* the long rest (matches gm-assist's ordering); Soma's Earth Tremor apology; the Dazlyn-thumps-Norbus / "the bard will tell us stories" beat; Valphine as Lathander's (Morninglord's) cleric and the drow "information is power" banter; Vukradin's double-dagger kill framing; no anachronisms (no Boney, no later-campaign entities backdated into Chapter 3).