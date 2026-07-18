# Voice Critique — gm-assist-doc.md (multi-narrator)

**Narration:** `summaries/20260614/gm-assist-doc.md`
**Voice specs:** `voice/zephyr_voice.md`, `voice/zinnia_voice.md`, `voice/sequoia_voice.md`, `voice/calmer_voice.md`
**Per-char examples:** `examples/` (global only — no per-character files matched)

---

## Mechanical Scan A — Em-dashes

Em-dashes throughout are used as parenthetical markers and pivot punctuation. The usage is characterful and consistent with established voice patterns in prior sessions — no blanket conversion recommended. Two specific instances are flagged under the scene-level critique below where the em-dash introduces content that should be reconsidered on other grounds.

## Mechanical Scan B — Register-wrong vocabulary

Two hits outside verbatim dialogue:

- **Line 86 (Zinnia):** `filed` — see flag [2] below.
- **Line 232 (Zephyr, italicized internal):** `executive structure` — see flag [8] below.

---

## Structural Issues

**[S1] Misspelled narrator heading**

`## sequioa — The Discovery of Frostbrand`

Should be `## sequoia`. One-character fix; correct in gm-assist.md but the narration file has its own copy.

**[S2] Duplicate heading — Zephyr scene 5**

Lines 196–198 have:
```
## zephyr — Maeris Dorn's Surrender

## Zephyr — Maeris Dorn's Surrender
```
The first line is a leftover artifact. Delete it; keep the second.

---

## Scene 1 — Zephyr: The Battle in the Fire Temple Continues

### [1] Cliché simile

> Restrained. Held. Pinned like a moth to a stone wall

**Why:** "Moth to a stone wall" is generic captivity imagery — it breaks the staccato rhythm Zephyr's voice has been building ("Restrained. Held.") and substitutes a stock visual. Zephyr's simile vocabulary runs economic and operational, not nature-metaphor.

**Suggested rewrite:** Cut the simile entirely. "Restrained. Held. Pinned." lands harder and stays in register. Or replace with something Zephyr-specific: "Pinned the way a deal goes wrong — fast, and too late to walk back."

---

### [2] Generic prose

> Every instinct I own went still and cold and very, very awake.

**Why:** "Went still and cold" is stock threat-response language — the body going quiet in danger. The voice file shows Zephyr's response to threat is *reading*, not feeling: "This man is calculating something, but I do not know what it is." He processes externally, not through somatic sensation. The sentence that follows (reasoning about why creatures surrender) is the correct Zephyr register; this line is the wrong approach to that beat.

**Suggested rewrite:** "Every instinct I own started doing the math." Or cut to: "I stayed where the coils had left me and I watched." The watching IS the instinct — no need to name it.

---

## Scene 2 — Zinnia: The Infernal Contract

### [3] Register-wrong vocabulary

> I filed it where I file all his tells.

**Why:** Mechanical scan B hit. "Filed" is bureaucratic/administrative diction — filing-cabinet metaphor. Zinnia's spy vocabulary runs to "infiltration," "operational security," "leverage," "the mouse." She doesn't file tells; she holds them, reads them, or stores them in the way a body stores a reflex.

**Suggested rewrite:** "I noted it and kept moving." Or: "I held it where I hold everything — still, waiting, not yet useful."

---

### [4] Factual error

> *Gotcha.* I took the cold sword and said nothing.

**Why:** Zinnia did not take Frostbrand. Sequoia did — the entire next scene is narrated from his perspective as the one who claimed it. This is the most load-bearing error in the file: it contradicts the following scene and misattributes the central item of the session.

**Suggested rewrite:** The "*Gotcha.*" is correct — it's Zinnia's perceptive arrival at the cold anomaly. But the action that follows should be observation, not acquisition: "*Gotcha.* The cold came off it even here. I noted it and said nothing." Or even just: "*Gotcha.*" and stop — the anomaly has landed; Sequoia's scene picks up from there.

---

## Scene 3 — Sequoia: The Discovery of Frostbrand

*Note: heading reads `## sequioa` — see structural flag [S1].*

### [5] Voice spec conflict — Zephyr register

> I will say this plainly. We assassinated Romag. We started a three-faction war from the inside and let it eat the people running it. I have moved treasure into my own pile when no one was counting.

**Why:** This is Zephyr's internal narrator, not Sequoia's. Sequoia's voice file is explicit: "Forward calculation in internal monologue (always oriented toward next move)." He does not do retrospective self-narration of crimes. That theatrical backward-looking accounting — "another notch in my victory belt," narrating the arc of what the party has done — belongs to Zephyr's theatrical self-aware inner voice. Sequoia processes things as evidence, not narrative.

**Suggested rewrite:** Same beat, Sequoia's register: "We killed Romag. Ran a three-way war and let it eat itself. I have taken things when no one was counting. That is the file." Short, declarative, evidence-based, forward-pointing — the last phrase sets up the surprise of the sword's choice without belaboring it.

---

### [6] Voice spec conflict — etiquette register

> Then, to the sword, because manners cost nothing

**Why:** "Manners cost nothing" is Calmer's moral register (authority and protocol) or Zephyr's operational politeness-as-technique. Sequoia's voice file: "Practical vocabulary; no metaphors, no flourish." His reason for talking to the sword would be information-gathering, not courtesy. He doesn't rationalize pleasantness — he acts and moves.

**Suggested rewrite:** Cut the "because" clause entirely: "Then, to the sword: 'Hey. How's it going?'" The greeting is already characterful; the justification dilutes it.

---

## Scene 4 — Calmer: Confronting the Fallen Commander

### [7] Unclear referent / cliché

> I have seen this man levy taxes on the act of breathing; two seemed thin.

**Why:** "Levy taxes on the act of breathing" is a stock hyperbole for a greedy or extractive character. It's not established Zephyr behavior — his pattern is economic reframing and strategic extraction, not taxation-for-existing. The referent "this man" requires a beat to parse (it means Zephyr, but the last person named before it was the commander). Calmer is allowed hyperbole, but it should be specific to what Zephyr actually does.

**Suggested rewrite:** Something anchored to established behavior: "I have seen this man charge the ferryman for the oar. Two gold seemed thin." Or if the taxonomy matters more: "I have watched this man quantify every breath someone else takes. Two gold seemed like he was being sentimental."

---

## Scene 5 — Zephyr: Maeris Dorn's Surrender

*Note: duplicate heading — see structural flag [S2].*

### [8] Register-wrong vocabulary (internal monologue)

> *We ran a three-way war that filled these corridors with bodies, and now I am explaining executive structure inside a hug.*

**Why:** "Executive structure" is corporate register. The voice file shows Zephyr using economic framing ("We're gonna bankrupt it"), not management-speak. "Executive structure" is the word an MBA reaches for; Zephyr is a tiefling assassin who ran a temple war.

**Suggested rewrite:** "*...and now I am explaining the chain of command inside a hug.*" Or: "*...and now I am explaining who outranks whom inside a hug.*" Same dry beat, correct vocabulary.

---

### [9] Cliché simile

> Asking her why she was running from the ashes was like asking the corpse why it had stopped breathing.

**Why:** Corpse/stopped breathing is a stock mortality simile — it doesn't carry Zephyr's voice. The surrounding lines ("the whole burning enterprise," "that isn't a corpse. That's a hire.") are much sharper. The simile is the weakest sentence in a paragraph that otherwise does the job correctly.

**Suggested rewrite:** Cut the simile. "It was the wrong question. I knew it the moment her face changed. We had killed everything that mattered to her." The next sentence carries the weight without needing the comparison.

---

## Scene 6 — Calmer: The Water Temple Ambush

### [10] Generic prose

> something opened up in my chest, clean and hot.

**Why:** "Something opened up in my chest" is stock excitement-in-combat language. Calmer's warrior-priest joy in battle has specific coloring in his voice file: his response to finally destroying the wraith was "*Who's the man? Who is the man?*" — outward, declarative, triumphant. He doesn't render combat excitement as interior sensation; he announces it. The internal register is wrong for this character.

**Suggested rewrite:** "And something in me said *yes.*" Or: "I will not dress it up — I wanted blood, and the room had just handed me permission." Or simply let the quoted dialogue carry it and cut the sensation line: "He told me, fine, let's kill them. 'Good! I want to kill them! I want them dead!'"

---

## Verdict

The file is strong in its structural bones — each narrator has a distinct setup, and the Calmer sections in particular are on-voice throughout. The top recurring issue is **register bleed**: Sequoia's scene contains two passages in Zephyr's theatrical retrospective voice (flag 5 and 6), and Zephyr's scenes contain one instance of Calmer's corporate diction (flag 8). These are single-scene patch jobs, not systemic re-narration problems. The one flag requiring an immediate fix before this file feeds anything downstream is **flag [4]**: Zinnia taking the cold sword is a factual error that contradicts the next scene.

**Recommended action:** Fix flag [4] and [S1]/[S2] immediately (one-line edits). Apply flags [5] and [6] as the next priority (Sequoia's scene is otherwise the strongest in the file and worth getting right). The simile flags [1], [9] are optional cleanup.
