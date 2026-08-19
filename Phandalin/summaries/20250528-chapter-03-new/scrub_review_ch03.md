# Scrub Review — Chapter 3 (20250528), narration/

Deterministic scan (`find_residue.py`) + full manual read of all 10 scenes, per the `/scrub` skill.
Scenes 3, 4, 5, 6, 9 are clean — no candidates, scanner or manual. Scenes 1, 2, 3(partial), 7, 8, 10 have
candidates below. Nothing has been rewritten yet — this is the full candidate set for one review pass.

**Legend:** ✅ = you already ruled on this one earlier in this session. Everything else is open.

---

## Scene 01 — Ambush at the Blood-Stained Altar (Brewbarry)

| # | Cat | Line | Context | Match | Proposed rewrite |
|---|-----|------|---------|-------|-------------------|
| 1.1 | ac_number | 37 | Vukradin: *"Oof. AC 8. There's an AC you don't see every day."* | `AC 8` | → *"Oof. Look how slow that thing is — you don't see a target that easy every day."* |
| 1.2 ✅ | dice_verb (manual) | 41 | Soma: *"...You might not get your weapon back... still roll a one."* | `still roll a one` | **Accepted:** → *"...still, no guarantees."* |
| 1.3 ✅ | dice_verb (manual) | 45 | Vukradin: *"Still roll a one... your attack roll spells."* | `Still roll a one` / `attack roll` | **Accepted:** → *"No guarantees," Vukradin says. "This is when you use your attack spells."* |
| 1.4 ✅ | anachronism? (manual) | 57 | Vukradin: *"Eight years. I'm not used to it yet."* | — | **Ruled: keep as in-fiction hyperbole.** No change. |

**Open: 1.1 only.**

---

## Scene 02 — Battle with the Ochre Jellies (Soma)

| # | Cat | Line | Context | Match | Proposed rewrite |
|---|-----|------|---------|-------|-------------------|
| 2.1 | roll_result_dialogue | 15 | Vukradin: *"No, I'm not dead. I have one hit point."* | `I have one` | → *"No, I'm not dead. Just not by much."* |
| 2.2 | level (manual, blind spot) | 19 | Soma (mutter): *"Bards don't do much at level one."* | `level one` | → *"Bards don't do much when they're this new to it."* |
| 2.3 | foot_count | 29 | Narration: *"...a man is standing at zero hit points ten feet from an ooze..."* | `ten feet` | Likely a false positive — plain distance description, not a stat callout. Recommend **protect**, but flagging per policy. |
| 2.4 | dc_number + damage_number (combined) | 53 | Soma: *"...we're dropping an earth tremor right here. Five damage to both, unless they can do a DC 13 dex."* | `DC 13`, `Five damage` | → *"...we're dropping an earth tremor right here. Should knock the wind out of both if they can't get clear fast enough."* |
| 2.5 | hp (manual, blind spot) | 61 | Valphine: *"Save me. I'm at three hit points."* | `three hit points` | → *"Save me. I'm nearly done."* |
| 2.6 | hp (manual, blind spot) | 65 | Soma: *"Hey, I'm back to 11. Thank you."* | `11` | → *"Hey, that's more like it. Thank you."* |
| 2.7 | ac (manual, blind spot) | 79 | Soma: *"So I'm here to get whaled on with a bonus 4 AC."* | `bonus 4 AC` | → *"So I'm here to get whaled on — extra armored up for it."* (linked to 2.8) |
| 2.8 | ac_number | 81 | Vukradin: *"You're gonna sit there at AC 21 now. Interesting tactic."* | `AC 21` | → *"You're basically a wall now. Interesting tactic."* (linked to 2.7, 2.9) |
| 2.9 | ac (manual, blind spot) | 89 | Narration/dialogue: *"Didn't need plus four AC for that."* | `plus four AC` | → *"Didn't even need the extra plating for that."* (linked to 2.7, 2.8 — same running joke, recommend consistent register across all three) |
| 2.10 | damage_number + dice_verb (combined) | 93 | Soma: *"...And I'll roll a natural one just for you. There we go. Seven damage."* | `roll a natural one`, `Seven damage` | → *"...Rolled garbage for that, and it still lands. There we go — that's the little one down."* |
| 2.11 | hp_number | 111 | Unattributed: *"Keep bouncing between one and 10 hit points. Up and down and up and down."* | `10 hit points` | → *"Keep bouncing back and forth like that. Up and down and up and down."* |
| 2.12 | roll_result_dialogue (manual, blind spot) | 97 | Soma: *"Me? 17. Yeesh."* | `17` | → *"Me? Right on the nose. Yeesh."* |
| 2.13 | round_count (manual, blind spot) | 125 | Unattributed: *"Killed two creatures in one round. There's a bard for you"* | `one round` | → *"Killed two creatures in one breath. There's a bard for you"* |

**Open: all 13.** (2.7/2.8/2.9 are one running joke across three lines — happy to take those as a single combined decision if you'd rather.)

---

## Scene 03 — Archaeologists and Altars (Vukradin)

Scanner: 0 hits. Manual read found 3 — all "character level / hit points / spell slots" blind spots the regex can't see (no digit or fixed phrase to match on).

| # | Cat | Line | Context | Match | Proposed rewrite |
|---|-----|------|---------|-------|-------------------|
| 3.1 | level (manual, blind spot) | 15 | Vukradin: *"What level are you?"* | `What level are you?` | → *"How many fights have you actually been in?"* (keeps the "accounting" bit he's making) |
| 3.2 | hp (manual, blind spot) | 21 | Dwarves: *"We're four hit points. We're useless."* | `four hit points` | → *"We're one good hit from finished. We're useless."* |
| 3.3 | spell slots (manual, blind spot) | 33 | Soma: *"I don't have any spell slots left."* | `spell slots` | → *"I don't have anything left to give."* |

**Open: all 3.**

---

## Scenes 04, 05, 06, 09 — clean

No scanner hits, no manual finds. (Scene 4's gem counts — "15 gemstones," "we found 10" — are loot-counting narrative, not game-mechanical residue, so they're correctly not flagged.)

---

## Scene 07 — Ambush Behind the Altar (Brewbarry)

| # | Cat | Line | Context | Match | Proposed rewrite |
|---|-----|------|---------|-------|-------------------|
| 7.1 | hp (manual, blind spot) | 23 | Valphine: *"I can go in. I'm eager. I've got nine hit points."* | `nine hit points` | → *"I can go in. I'm eager. I can take a hit."* |
| 7.2 | dice_verb (manual, blind spot) | 39 | Brewbarry: *"My second natural one tonight."* | `natural one` | → *"Second time I've swung at nothing tonight."* |
| 7.3 | damage_number (manual, blind spot) | 61 | Valphine: *"...Hit — and this is six bludgeoning."* | `six bludgeoning` | → *"...Hit — and that one lands solid."* |
| 7.4 | dice_verb (manual, blind spot) | 67 | Brewbarry: *"I crit one of them, so we can just cleave that guy out. He's dead."* | `I crit` | → *"Caught that one clean, so we can just cleave that guy out. He's dead."* |
| 7.5 | damage_number | 77 | Brewbarry: *"I do one damage. Excellent. Hey, that's 20% of its hit points, guys."* | `one damage` (+ uncaught `20% of its hit points`) | → *"Landed it. Excellent. Hey, that's a real chunk of what's left on it, guys."* |

**Open: all 5.**

---

## Scene 08 — The Hall of Greed (Soma)

| # | Cat | Line | Context | Match | Proposed rewrite |
|---|-----|------|---------|-------|-------------------|
| 8.1 | table_speak (manual, blind spot) | 27 | Soma: *"Beautiful. You save those for the out of combat rolls, I see."* | `out of combat rolls` | → *"Beautiful. You save that focus for when nobody's swinging at you, I see."* |
| 8.2 | dice_verb (manual, blind spot) | 31 | Soma: *"No, I'm just kidding you. I just rolled like garbage, that's all."* | `rolled like garbage` | → *"No, I'm just kidding you. I just didn't have the eye for it today, that's all."* |
| 8.3 | **anachronism** (manual) | 63, 69 | Soma: *"I think I've seen that picture in the Dungeon Master's Guide. Is that a classic D&D picture?"* / Vukradin: *"...this is the intro adventure, right? It should definitely be represented in art."* | `Dungeon Master's Guide`, `classic D&D picture`, `intro adventure` | See below — this is the real catch of the pass. |

**8.3 detail — flagging per the anachronism protocol:** this is a direct fourth-wall break (characters recognizing their own scene as D&D-module iconography), not mechanical residue — a genuine GM scope call, not a mechanical strip. Proposed *replacement* (not deletion), which invents a small piece of new canon — a recurring "demon-statue-clutching-a-gem" motif as Abbathor iconography:

> Soma: *"I think I've seen that shape before — some old temple frieze, back before Phandalin. A demon statue cupping a glowing gem, just like that."*
> Vukradin: *"Oh my God, yeah — you're right." / "It is." / "I mean, if half of what the dwarves say about this place is true, it should definitely be worth a fortune in some scholar's collection."*

If you accept this, the "cupping a glowing gem" motif becomes on-the-fly canon (an Abbathor iconographic convention) and should be logged as such rather than treated as something established earlier — flagging that per the skill's rule on invented anachronism-replacements.

**Open: all 3** (8.3 needs a keep/cut/replace ruling, not just accept/reject).

---

## Scene 10 — Ambush on the Road (Valphine)

| # | Cat | Line | Context | Match | Note |
|---|-----|------|---------|-------|------|
| 10.1 | anachronism? (manual, judgment call) | 67 | Soma: *"It's gonna take the entire campaign. I think that's where we're at."* | `the entire campaign` | Same shape as 1.4 ("Eight years") — "campaign" reads plausibly in-fiction (a military/adventuring campaign), not forced. No rewrite proposed; flagging for a keep/cut call. |

**Open: 1.**

---

## Summary

- **Clean:** scenes 4, 5, 6, 9 (no action)
- **Already ruled this session:** 1.2, 1.3, 1.4 (accepted / accepted / keep)
- **Open for decision:** 1.1 (1) · scene 2 (13) · scene 3 (3) · scene 7 (5) · scene 8 (3, incl. the anachronism) · scene 10 (1) — **26 open candidates**
- **Notable:** scene 8's Dungeon Master's Guide / "intro adventure" lines (8.3) are the highest-value catch — a real fourth-wall break, not just mechanical residue.

How do you want to work through these — batch-accept the straightforward numeric rewrites and go 1x1 only on the judgment calls (8.3, 10.1, and the false-positive-flagged 2.3), or walk the whole list?
