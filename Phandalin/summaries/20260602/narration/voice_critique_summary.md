# Voice Critique Summary — Session 20260602

**Session:** Ch. 44 — "The Unfated Routine of Rimardo and Corrin"
**Scenes critiqued:** 6 (scenes 01–06)

| Scene | Narrator | Flags | Report |
|---|---|---|---|
| 01 | Vukradin | 3 | voice_critique_scene_01_vukradin.md |
| 02 | Valphine | 4 | voice_critique_scene_02_valphine.md |
| 03 | Soma | 2 | voice_critique_scene_03_soma.md |
| 04 | Brewbarry | 4 | voice_critique_scene_04_brewbarry.md |
| 05 | Valphine | 3 | voice_critique_scene_05_valphine.md |
| 06 | Soma | 3 | voice_critique_scene_06_soma.md |

**Total: 19 flags across 6 scenes**

---

## Recurring themes

### 1. Valphine's conversion is framed as involuntary (scenes 02 and 05 — 2 flags)

Two Valphine scenes, two lines that read the conversion as something that overcame her:

- Scene 02: "hooked me, deep and unwilling"
- Scene 05: "once mistook for the sun"

Both contradict the voice spec: the conversion was a power calculation, not a surrender. She became *clearer*. She recognized the larger power and allied with it. "Unwilling" and "mistook" both say she got it wrong first, which is the drow-redeemed-by-the-light cliché the spec explicitly rejects. These two flags share a root cause; fix both or neither — leaving one risks the inconsistency reading as intentional.

### 2. Stock similes replacing narrator-specific image vocabulary (scenes 04, 05, 06 — 4 flags)

- "like a hand on the shoulder before the gate opens" (Brewbarry)
- "like a dropped cup" (Valphine)
- "faster than a frightened squirrel" (Soma)
- "like a snuffed candle" (Soma)

All four are evocative-but-generic. The pattern suggests the narration pass defaults to literary stock when no image from the specific character's vocabulary is available. Each narrator has a distinct image register: Brewbarry's is bodily-declarative, Valphine's is drow-tactical-aristocratic, Soma's is coastal-natural-world-specific. These similes don't belong to any of them.

### 3. Vocabulary bleed between narrators (scene 04 — 1 flag)

"Bright and a little bit like a wound" is Valphine's theological register (pain as proof of contact with Lathander) appearing in Brewbarry's narration. Single instance, but the clearest case of the narration pass not maintaining narrator distinctiveness.

---

## Priority

1. **Fix both Valphine conversion lines (scenes 02 and 05)** — same root problem, two sentences, high precision impact on a load-bearing character backstory.
2. **Fix Brewbarry's Valphine-vocabulary bleed (scene 04, flag [3])** — narrator distinctiveness issue.
3. **Simile audit (scenes 04, 05, 06)** — low priority, spot-editable; stock similes don't break the voice, they flatten it.

---

## Reminder

These reports are review-only. Apply fixes in the `.scrubbed.md` files — that's what `assemble.py` reads. For the Valphine conversion pattern, two targeted edits across two files. For Brewbarry's scene, spot edit only — "Something in my chest went very simple and very loud." and "Who's responsible for the destruction of the wine." are exactly right and a re-narration would likely lose them.
