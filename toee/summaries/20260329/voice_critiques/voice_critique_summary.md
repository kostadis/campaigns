# Voice Critique Summary — gm-assist-doc.md (Chapter 26)

**Source:** /home/kroussos/toee/toee/summaries/20260329/gm-assist-doc.md
**Sections:** 7 (Zinnia ×2, Calmer ×1, Zephyr ×2, Sequoia ×2)
**Voice specs:** all four found and used
**Per-char examples:** none (global thematic examples only — critique grounded in voice specs)
**Total flags:** 21 across 7 sections

| Section | Narrator | Flags | Top issue |
|---------|----------|-------|-----------|
| The Scalding Battlefield | Zinnia | 3 | "files a formal complaint" — bureaucratic metaphor in a tradecraft voice |
| Confrontation with the Wraith | Calmer | 5 | Stock temperature-drop opening; "calculating odds" is Zephyr's vocabulary |
| Ambush by Ghouls | Zephyr | 3 | "identity drift" — clinical vocabulary |
| Descent into the Second Level Corridors | Sequoia | 5 | Too-literary wraith observation; "aesthetic details"; "designed for" |
| The Hall of Trophies and Elemental Strife | Zinnia | 3 | "information asymmetry" — academic economics, not tradecraft |
| The Prisoner's Bargain | Sequoia | 3 | Mostly mechanical (em-dashes, one table-voice slip) |
| Beckoned | Zephyr | 3 | "chain of command" + generic closing simile "lit coal" |

## Recurring theme

**Register-wrong vocabulary** is the primary pattern throughout. The LLM defaulted to analytical, institutional, or academic vocabulary — "structural damage," "recalibration," "files a formal complaint," "aesthetic details," "information asymmetry," "identity drift," "chain of command" — where each character has a specific cognitive register: Zinnia's spy tradecraft, Calmer's clerical conviction, Zephyr's economic ledger, Sequoia's practical staccato. The off-register words stand out precisely because the surrounding prose is otherwise well-calibrated to those registers.

**Em-dashes** appear 9 times at narration level (not in dialogue or italic spans). Most are appositive uses that convert cleanly to commas or colons; none are severe. The frequency is worth noting for future narration runs — a style pass setting em-dash → comma/period as default would clean most of these automatically.

## Priority rewrites

**1. Calmer scene, opening paragraph** (lines 53–55 in source):
The temperature-drop + headache-simile + "calculating odds" cluster is the worst voice-drift in the document: stock haunted-dungeon prose followed by Zephyr's probability vocabulary in Calmer's mouth. This is the only flag that feels systemic rather than isolated. Highest priority for a manual rewrite or scene re-run with an updated voice prompt emphasizing "divine revulsion, not ambient horror."

**2. Zephyr (Ghouls), "identity drift"** (line 127):
One clinical term that breaks Zephyr's vocabulary cleanly. Single-sentence fix.

**3. Zinnia (Hall), "information asymmetry"** (line 235):
Academic economics in a tradecraft voice. Single-phrase fix.

**4. Zephyr (Beckoned), closing simile** (line 363):
"Lit coal" is generic; a ledger-vocabulary image closes the document in Zephyr's actual voice.

---

*All critiques are review-only. For flagged sentences, manual spot-edits in gm-assist-doc.md are the fastest path. For priority #1 (Calmer opening), if the problem reads as more than an isolated sentence, consider re-running that scene with the voice spec emphasis on theological revulsion over ambient horror cues.*
