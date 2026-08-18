# Consistency Report — "The Skull Cavity" (Ch. 3 scene doc, source: gmassist)

## Major issues

### 1. Timeline conflict with the Chapter 2 archive — is the 50 gp already collected?
- **Location**: Scene summary bullet 4 + Verbatim "[The Moral Debate]" ("…the hard-earned 50 gold pieces for delivering the message")
- **Issue**: `campaign_state` (ch02 archive) lists the delivery reward as **already paid** before this session: "Return to Phandalin — Dwarven Quest Reward Collected: Harbin Wester paid the promised 50 gp," followed by loot sale, Ogre #1, Gnomengarde departure, and Ogre #2 (mid-combat at chapter's end). Yet this session has the party at the temple, and the source gm-assist recap ends with the party "heading back toward town **to collect their final reward**." The quote itself is ambiguous (it can be read as "I'm here for [the owed] stones and [the already-earned] 50 gp"), but the gm-assist ending is not. Either the ch02 archive's event ordering is wrong (return/reward/ogres/Gnomengarde actually follow the temple clearing), or this recap inherits a sequencing error. Ch. 3 also never resolves Ogre #2 or mentions the Gnomengarde trip the archive says was in progress.
- **Evidence**: campaign_state "Completed Encounters" list and "Party Current Situation" (mid-ogre-fight en route to Gnomengarde) vs. gm-assist ch. 3 opening ("crossroads in the ancient dwarven ruins") and closing ("collect their final reward"). The archive is explicitly a DRAFT first-pass extraction; the transcript is authoritative-tier.
- **Suggested fix**: GM ruling required before either document seeds downstream regeneration. Most likely correction: move "Reward Collected / Loot Sold / Ogre #1 / Gnomengarde departure / Ogre #2" in the ch02 archive to after the temple-clearing session, or confirm the quote refers to already-banked coin and fix gm-assist's "final reward" line.

### 2. "We found 10" — summary attributes it to Valphine; the doc's own transcript labels it Soma
- **Location**: Scene summary bullet 4 vs. Verbatim "[The Moral Debate]"
- **Issue**: The summary (following gm-assist's Summary and Memorable Moments) credits Valphine with the underreport. The transcript block in this same document is labeled **Soma**: "10. We found 10 / Really? We're not taking them? Apparently we're not." — and the continuation reads consistently as Soma. The summary also reorders the beat ("We found 10" before "Goddamn your moral streak"; the transcript has the sigh first).
- **Evidence**: Transcript speaker labels in this doc; gm-assist Summary ("Valphine quietly suggested they had found only ten") and Memorable Moments quote card.
- **Suggested fix**: Verify against raw VTT speaker labels / the sibling transcription before this quote hardens as Valphine canon (it *fits* her, which is exactly why an unverified attribution is dangerous). Mark UNVERIFIED until ruled.

### 3. The final gem split is not actually settled at 7/8 in the transcript
- **Location**: Scene summary final bullet; "[The Split]" section header and transcript
- **Issue**: Summary asserts party 7 / dwarves 8. The transcript ends the negotiation with: "We get eight, they get seven? Uh, no, they get eight, you get seven." → "Actually, okay," → GM: "**actually make it eight**" → Soma: "There's four of us, two of them. **We all get two**." The GM's "make it eight" plausibly flips the party's share to eight — which matches Soma's arithmetic (4 × 2 = 8) — contradicting the 7/8 in both summaries. (Soma's math also can't reconcile with a 7-gem party share at all.)
- **Evidence**: Verbatim "[The Split]"; gm-assist Summary/Items say 7/8.
- **Suggested fix**: Check the tape for what "make it eight" changed. Record the ruled split explicitly — it's a 10 gp difference in party treasury that a future audit will trip over.

### 4. "Here for the sending stones and the 50 gold pieces" — attribution spans a suspect speaker split
- **Location**: Verbatim "[The Moral Debate]" + Scene summary bullet 4
- **Issue**: The summary gives the whole line to Vukradin. In the transcript, the first half — "**Norbert or whatever** is withholding payment. I'm here for the" — is labeled **Soma**, and "Norbert" is established two blocks later as *Soma's* characteristic slip ("I don't know why I have Norbert" — Soma). The doc's editorial note ("completing the thought across the transcript's speaker split") assumes Vukradin owns the whole sentence; the internal evidence points at least partly to Soma.
- **Evidence**: Soma's later "What's his name? I keep forgetting… Norbus, sorry. I don't know why I have Norbert."
- **Suggested fix**: Re-split against the tape. Either it's all Soma, or Soma complains about withheld payment and Vukradin picks up the sentence — those are different characterizations and shouldn't be collapsed silently.

## Moderate issues

### 5. "Verbatim" claim on the scene summary is false
- **Location**: Header "Scene summary (from gm-assist, verbatim)"
- **Issue**: gm-assist's Skull Cavity scene is five terse bullets. This doc's version is an expanded rewrite — extra beats (Soma's peek, Scooby-Doo, the "Is he serious?" exchange, Soma's math, Overbrighters) and embedded quotes. Mislabeling an LLM-expanded pass as "verbatim" corrupts the trust hierarchy for future passes.
- **Suggested fix**: Relabel ("expanded from gm-assist against the transcript") or paste the actual verbatim bullets.

### 6. Vukradin's insight is framed backwards
- **Location**: Scene summary bullet 8 ("Vukradin's insight suggests the dwarves have no intention of visiting a museum")
- **Issue**: In the transcript, the "they're not going to take these to a museum" line is table-talk *before* he rolls; his roll then fails, and he says he'd be "diluted [deluded] into thinking that they actually were going to—". Mechanically, post-check Vukradin *believes* the dwarves. Both insight checks (his and Valphine's 7) failed.
- **Suggested fix**: Reword: Vukradin voices a suspicion aloud, then fails the insight check that would have confirmed it. Matters for what Vukradin canonically "knows" going forward.

### 7. Unknown name "Nick"
- **Location**: Verbatim "[The Moral Debate]" — Soma: "The bard is always the most annoying character, right, Nick?"
- **Issue**: No player (Dave, Wade, Gary, Stéphane), GM (Kostadis), or NPC named Nick exists in the roster, entity registry, or VTT glossary.
- **Suggested fix**: Check the tape — likely a transcription garble. Add the ruled correction to `vtt_transcription_corrections.md`.

### 8. Valphine-labeled block folds in someone else's line
- **Location**: Verbatim "[The Little Door Beckons]" — Valphine: "You're next to the other secret door. Okay, great. It's not like there's a dragon hiding in there. **I'm** right next to the other"
- **Issue**: The "I'm right next to the other [door]" continues directly into Vukradin's next labeled line and describes *Vukradin's* position. At least two speakers are folded under one label; the "dragon hiding in there" sarcasm may not be Valphine's.
- **Suggested fix**: Re-split or annotate like the doc's other folded-block notes.

## Minor issues

### 9. "Stations himself warily" misstates the token beat
- **Location**: Scene summary bullet 1
- **Issue**: The transcript shows Vukradin *protesting* being moved ("Why am I moving? I'm not moving over there, I am over here") and only sarcastically accepting the position. "Stations himself warily" makes it a deliberate choice.
- **Suggested fix**: "Finds his token parked by the other secret door and jokes it will open Scooby-Doo style."

### 10. "The museum only needs half" — speaker uncertain
- **Location**: Scene summary bullet 7 (attributed to Dazlyn)
- **Issue**: Transcript: "Dazlyn thumps Norbus, Norbus thumps Dazlyn, goes, 'Hey…'" — the grammatical subject of "goes" is Norbus. gm-assist's Dazlyn dossier ("opened the negotiation") may be circular with the same extraction.
- **Suggested fix**: Verify or hedge to "one of the dwarves."

### 11. Unattributed dagger-sharpening bit
- **Location**: Verbatim, dwarves'-paranoia GM block ("I'll just pull out my dagger and sharpen it a little bit")
- **Issue**: Folded player line, speaker unknown. If it's Valphine it feeds the drow-paranoia beat; leaving it anonymous invites later misattribution.
- **Suggested fix**: Resolve from the tape or mark speaker-unknown explicitly.

### 12. Formatting corruption in the Coda
- **Location**: "[Coda — The Broke Bard]"
- **Issue**: A `**GM**` speaker tag is embedded mid-quote with the line "L- like, Dave, are, are you sure you wanna live," duplicated.
- **Suggested fix**: Repair the block before it's ingested anywhere.

### 13. "Think so" attribution is an editorial guess
- **Location**: Scene summary bullet 6 ("Soma's answer: 'Don't really know him… Think so.'")
- **Issue**: "Think so" is an unlabeled reply folded into a GM block (the doc says so itself); the summary silently fuses it onto Soma's labeled line. Plausible, but unverified.

### 14. Glossary landmines for future passes (not errors in the doc)
- **"Norbert"** is Soma's on-page, in-character slip, corrected in-scene — do **not** add a `Norbert → Norbus` glossary row; it would erase the joke (same class as the Big Al ruling).
- **"Morning Lord"** appears twice in verbatim quotes; the glossary lists it as a wrong-form for **Morninglord**. Per the Cassian brother/cousin precedent, quoted dialogue is left as spoken — but flag it so a spell-pass doesn't half-correct it.
- **"Scooby-Doo"** is a real-world reference in transcript quotes; fine at this layer, but note for any stage-3 de-anachronization pass if this feeds narration.

## Verified consistent (no action)

- 15 gemstones × 10 gp, dwarf skulls, unlocked stone coffer, pillar cavity — match gm-assist and the temple-of-Abbathor context.
- Sending stones withheld until the temple is fully cleared, handed over at session's end — matches the GM-confirmed 2026-08-17 ruling and `entity_registry.yaml`.
- "Overbrighters" is confirmed canon Underdark vocabulary (vtt_known_additions, 2026-08-02, from this very session) — not a garble; attribution of the sentiment to Valphine (the only Underdark native) is sound.
- Valphine credited with finding the secret doors — matches gm-assist ("Valphine discovers a series of secret doors").
- Skull cavity opened *before* the long rest — consistent with gm-assist's scene ordering.
- Boney correctly absent; no anachronistic items, levels, or arc-score references.
- "The Uthgardt barbarian" for Brewbarry is acceptable (Uthgardt-raised, exiled — the ch. 2 tattoo beat supports the dwarves reading him that way), though "Uthgardt-raised" would be more precise.