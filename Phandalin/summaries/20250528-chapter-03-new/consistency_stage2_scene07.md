# Consistency Report — "Ambush Behind the Altar" (Ch. 3 scene doc)

## High-priority issues

### 1. The "Scene summary" is labeled "from gm-assist, verbatim" — it is not verbatim
- **Location**: Scene summary header
- **Issue**: The header claims the bullets are verbatim from gm-assist, but every bullet is heavily augmented relative to the gm-assist source (dice totals, HP figures, quoted dialogue, the odds-or-evens detail, table banter). This launders enriched — possibly LLM-expanded — content under a verbatim provenance claim.
- **Evidence**: gm-assist's actual "Ambush Behind the Altar" bullets are terse ("Upon entering, an ochre jelly slithers out from the shadows to attack" vs. the doc's "Valphine volunteers to enter first — 'I can go in…' — and an ochre jelly, a full-sized 52-hit-point specimen…").
- **Suggested fix**: Relabel as "expanded from gm-assist against the transcript" or restore the actual gm-assist bullets and move the enrichment elsewhere.

### 2. Unsupported quote: "Never tell me the odds"
- **Location**: Scene summary (pseudopod bullet)
- **Issue**: The quote appears only in the augmented summary. It is in neither the Verbatim Moments section nor gm-assist.
- **Evidence**: The verbatim block has only: "Uh, Vukradin, odds or evens? Odds" — no Star Wars line.
- **Suggested fix**: Verify against the tape; if absent, delete the quote and keep the odds-or-evens mechanic description.

### 3. Scene Wrap ending contradicts both the verbatim and gm-assist
- **Location**: Scene Wrap, final bullet ("the party left to report back to the dwarves")
- **Issue**: Vukradin explicitly declines to report at this point, and the next event is the Hall of Greed beyond the channel — the report to the dwarves comes later.
- **Evidence**: Verbatim: Soma needles "You gonna go tell that guy?… go send the message" and Vukradin answers "no, it's okay… He can find out later." gm-assist sequence: "Beyond the altar channel, the party discovered… the Hall of Greed" before returning to Norbus and Dazlyn.
- **Suggested fix**: End the wrap with the party pressing on past the channel, Vukradin (for once) deferring his report.

### 4. Natural-one count misattributed to the character in the Wrap
- **Location**: Scene Wrap ("Valphine rolled her third natural one of the night") vs. Scene summary ("Gary's third natural one")
- **Issue**: The count is per-player, not per-character. The doc itself states Brewbarry is run by Gary this session; Brewbarry's "my second natural one tonight" plus Valphine's mace nat 1 = Gary's third. "Valphine rolled her third" falsely implies two earlier Valphine nat 1s.
- **Evidence**: Verbatim annotations "*Brewbarry (run by Gary)*" and "my second natural one tonight" (Brewbarry's turn), then "Nope. That's my third natural one" on the merged GM/Gary track.
- **Suggested fix**: Wrap should read "Gary's third natural one of the night (his first on Valphine's dice)."

### 5. "It's almost like I'm a tank" — attribution contradicts the doc's own facts
- **Location**: Verbatim Moments ("**[Valphine]** — *dry comment after eating the 17-point hit*")
- **Issue**: Valphine did not eat the 17-point hit; Brewbarry did. Since Gary runs both PCs this session, the line on Gary's Zoom track is almost certainly Gary speaking **as Brewbarry** — or at minimum the annotation is false as written.
- **Evidence**: Same document: "You said odds, so it's on, uh, Brewbarry" / "17 points of damage"; Stone's Endurance exchange is Brewbarry's.
- **Suggested fix**: Reattribute to Brewbarry (Gary's track) or reword the annotation; confirm with GM.

## Medium-priority issues

### 6. "Initiative was settled by a roll-off the GM won at 20" is misleading
- **Location**: Scene Wrap, second bullet
- **Issue**: The tape shows the jelly rolled a minus one and acted **last** (after Soma, Valphine, Vukradin, Brewbarry). The "roll off… my roll off is 20 / You win" exchange reads as banter over the jelly's absurd initiative, not something that settled the acting order — and the GM "winning" did not put the jelly first.
- **Evidence**: Verbatim: "that's a minus one for initiative… Well, we'll give him a one"; play order in the same document has the jelly's pseudopod arriving after four PC actions.
- **Suggested fix**: "The jelly rolled a minus-one initiative and went last, to much banter (including a joke roll-off the GM 'won' at 20)."

### 7. Timeline gap against campaign_state (Ch. 2 archive)
- **Location**: Whole document, cross-referenced with campaign_state / party_ch02
- **Issue**: Campaign state leaves the party mid-combat with Ogre #2 in a mountain valley **en route to Gnomengarde**. This Chapter 3 session has them deep inside the dwarven temple with no on-page resolution of the ogre fight, the Gnomengarde quest, or the return trip to the ruins. Not an error in the recap itself, but a continuity hole that will bite any regenerated Chapter 3 pass — and campaign_state explicitly forbids backfilling the ogre's fate from later documents.
- **Evidence**: campaign_state: "Ogre Encounter #2 … IN PROGRESS, unresolved at chapter's end"; "Current location: A narrow, steep-walled mountain valley en route to Gnomengarde." gm-assist Ch. 3 opens with the party already "at a crossroads in the ancient dwarven ruins."
- **Suggested fix**: GM to confirm the actual play order (did the hand-authored Chapter 2 reorder events relative to the sessions?) and where Ogre #2's resolution belongs, before this scene doc seeds anything downstream.

### 8. Unannotated "ogre" garbles risk confusion with the real, unresolved ogre
- **Location**: Verbatim Moments — "What'd the ogre get?" (initiative exchange) and Soma's "We got one more ogre to jelly off"
- **Issue**: Two "ogre"-for-"ochre jelly" transcript garbles lack the "*as transcribed, meaning the oozes*" annotation applied elsewhere. With an actual ogre fight literally unresolved in campaign_state, an unannotated "ogre" in this scene can false-positive future consistency checks.
- **Evidence**: The VTT glossary documents Oker/Ocher/Okre → Ochre confusion; two other instances in this same doc carry the annotation.
- **Suggested fix**: Add matching annotations to both lines.

### 9. Sacred Flame result overstated
- **Location**: Scene summary ("the jelly manages to avoid the brunt of the light") and heading of the Sacred Flame verbatim block
- **Issue**: "Avoid the brunt" implies partial damage; Sacred Flame deals nothing on a successful save, and the HP arithmetic in this very doc confirms zero (43 before, 43 − 6 = 37 after Vukradin's daggers).
- **Evidence**: gm-assist: "radiant light that the creature narrowly avoided"; the running HP totals in the verbatim.
- **Suggested fix**: "…the jelly avoids the light entirely, making its DC 13 save."

## Low-priority / flag-for-GM

### 10. Valphine-volunteers attribution rests on a merged Zoom track
- **Location**: Scene summary first bullet; Verbatim ("Yeah, I can go in. I'm eager… I've got nine hit points" on Dave's track)
- **Issue**: The doc's annotation is reasonable and gm-assist corroborates Valphine entering first — but gm-assist derives from the same tape, so this is one source, not two. A level-1 Vukradin also plausibly has 9 HP, so the line could be Dave volunteering.
- **Suggested fix**: Keep as-is but mark "GM-confirm" on the attribution.

### 11. Vukradin's daggers are not in any grounding doc
- **Location**: Scene summary / Verbatim (multiple dagger attacks)
- **Issue**: world_state ch02 lists clarinet/flute and rapier (baseline kit) for Vukradin; dual daggers are used throughout this session ("That worked well last time," matching the double-dagger kill in the earlier fight per gm-assist). Internally consistent, but absent from the item record.
- **Suggested fix**: GM confirm daggers in Vukradin's kit; add to the next grounding-doc pass.

### 12. Ambiguous transcript line: "I'm kind of done with those daggers. That's nice."
- **Location**: Verbatim Moments / quoted in Scene summary
- **Issue**: "Done with" (abandoning them) clashes with the approving "That's nice" and his repeated dagger success — plausibly a garble of "fond of." As quoted, a future session could read it as Vukradin retiring the daggers.
- **Suggested fix**: Check the tape; if unresolvable, annotate the ambiguity.

### 13. "He's dead, Jim" attribution ambiguous in the summary
- **Location**: Scene summary (Brewbarry-crit bullet)
- **Issue**: The em-dash placement implies Brewbarry said it; the verbatim shows it is Soma's line.
- **Suggested fix**: "…destroys one of the smaller jellies — Soma: 'He's dead, Jim'…"

### 14. Unannotated "There's a portal"
- **Location**: Verbatim Moments (GM line)
- **Issue**: In context this means the doorway/secret passage (module E7 is a mundane Secret Tunnel), but unannotated it could be read as a magical portal in the temple.
- **Suggested fix**: Annotate "*'portal' = the secret-door opening, not a magical portal*."

### 15. Corrupted speaker tag
- **Location**: Verbatim Moments — `**[Vuk**[Vukradin]**` before "Nice. All right. Under 20"
- **Issue**: Broken markdown/label.
- **Suggested fix**: Repair to `**[Vukradin]**`.

## Verified consistent (no action)
- HP arithmetic throughout: 52 → 43 (Ice Knife 9) → 37 (daggers 6) → 26 (Ice Knife 11) → 20 (mace 6) → split at 10 into two 5-HP oozes; poison spray 1 = 20% of 5; final 8 kills.
- Sending stones: "so we can earn our sending stones" matches the GM-confirmed 2026-08-17 ruling (stones withheld until the temple is fully cleared) — do **not** "fix" this to stones-in-hand.
- Brewbarry fighting with fists (avoiding the slashing split seen in the earlier halberd fight), Rage-useless-vs-acid ruling, Stone's Endurance for 9, "twice per long rest" — all match the tape and level-1 goliath barbarian mechanics.
- Soma out of slots after two Ice Knives is consistent with the presumed level-1 build and the pre-scene long rest; Ice Knife/Poison Spray both on her ch02 seen-in-play list; Sacred Flame and mace consistent with Valphine's ch02 record.
- Boney correctly absent; no anachronistic NPCs, factions, or locations; the blood-stained altar, channel, and behind-altar jelly match module areas E5/E7 and the "possibly oozes" open thread from Dazlyn.