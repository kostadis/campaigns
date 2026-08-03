# Voice Critique — Brewbarry, scene 5: The Siege of Falcon's Hunting Lodge

**Narration:** `gm-assist-doc.md` (lines 296–362)
**Voice spec:** `voice/brewbarry_new_pipeline.md`
**Per-char examples:** `examples/brewbarry.md`

## Flags

### [1] Particular-X tic

> Gorthok first. You feel something like that before you see it — a mass, a wrongness, the particular way large violent things displace the air in front of them.

**Why:** Same gestural-categorization tic flagged across the document. Brewbarry's spec is short declaratives and bodily render. He *feels* a thing displace the air; he doesn't taxonomize "the particular way large violent things displace the air." The first half ("a mass, a wrongness") is excellent Brewbarry — the genericization at the end is the Claude voice.
**Suggested rewrite:** *Gorthok first. You feel something like that before you see it. A mass. A wrongness. The air going wrong in front of him.*

### [2] Voice spec conflict — analytical paragraph about Valphine

> Valphine moved through us without hurrying — she does everything without hurrying, which I have always found either admirable or unsettling depending on the situation.

**Why:** Spec: "Do not have him justify himself at length. One sentence, then act." And: "Do not over-explain his interior." The "either admirable or unsettling depending on the situation" qualifier is the kind of multi-clause hedge the spec forbids. The examples never reach for "I have always found either X or Y depending on Z" — Brewbarry feels one thing and names it. He'd just notice that she doesn't hurry, and move on.
**Suggested rewrite:** *Valphine moved through us without hurrying. She never hurries.*

### [3] Voice spec conflict — philosophizing about Vukradin

> This is what I mean when I say I like Vukradin's music. Most people hear *music* and think: gentle thing, careful thing, the thing that stops the fight. When Vukradin hears it, he hears *kill them all* as an opening position and agrees wholeheartedly. We have always understood each other on the important points.

**Why:** Spec, explicit failure-prevention rule #9: "Do not make him philosophize about Vukradin. He likes Vukradin's music. He likes Vukradin. That is all the explanation he needs." This whole paragraph is exactly the philosophy the spec forbids — a three-sentence essay on what "music" means in his and Vukradin's grammar. The example from chapter 5 shows the right register: *"Drink good."* End of analysis.
**Suggested rewrite:** *I like Vukradin's music. Most people don't understand what I mean by that. Today they would.*

### [4] Generic prose — meta-aside about who is speaking

> At this point someone — from the direction it came, I think it was meant to be my voice, my thinking, some approximation of what I would say — offered the core strategic wisdom: *they are savages, we kill them all.*

**Why:** This reads as the GM-assist pipeline confessing it doesn't know whose line this was. Even if the intent was a Brewbarry beat, the meta-framing ("from the direction it came, I think it was meant to be my voice, my thinking, some approximation of what I would say") is the AI editorializing about its own attribution problem — exactly the "narrator editorializing" `_genre.md` bans. If the line is Brewbarry's, he just says it. If it isn't, attribute it to the actual speaker.
**Suggested rewrite (if Brewbarry's):** *I said the obvious thing. "They are savages. We kill them all."*
**Action item:** Cross-check the VTT — this looks like an unresolved attribution from extraction.

### [5] Tell-not-show — "That part didn't bother me"

> I thought about the Uthgardt stories of the Great Boar — a thing conjured out of storm and lightning, older than the gods that claimed to own it. I thought about how you stop something like that. I thought: *probably you don't stop it. Probably you just get in front of it.*
>
> That part didn't bother me.

**Why:** The italicized thought lands perfectly — that's exactly the register the spec calls for ("italics for direct thought… short phrases"). But the standalone closer "That part didn't bother me" names the absence of fear instead of demonstrating it. Brewbarry shows lack-of-fear by *acting* — checking the grip, flexing the hands, sword in hand. The previous paragraph already did that work. The four-word verdict-after-thought is one beat too many.
**Suggested rewrite:** Cut "That part didn't bother me." The Great Boar thought + the next combat beat carry it.

### [6] Generic prose — generic combat-stage description

> The lightning came from well beyond the palisade.
>
> A bolt, not from the sky but from the darkness beyond the wall — aimed, deliberate, the kind that doesn't happen by accident. It hit the gate.

**Why:** "The kind that doesn't happen by accident" is the same gestural tic as "the particular way" — categorizing a thing instead of letting Brewbarry render it. His combat prose is bodily and procedural per spec: "the swing, the hit points dealt, the rage active or not, the protective move." A targeted lightning bolt is a thing he'd describe by *what it did* (came aimed, hit the gate, threw the logs), not by classifying it as "the kind that doesn't happen by accident."
**Suggested rewrite:** *Lightning from beyond the palisade. Not from the sky — from the dark past the wall. Aimed. It hit the gate.*

## Verdict

Scene 5 is meaningfully closer to Brewbarry's voice than scene 1 — the boars-panic, the Dread Helm beat, the *probably you just get in front of it* italics, and the closing *My sword was already in my hand* all hold. The Vukradin-music philosophical paragraph and the meta-attribution aside are the two highest-cost cuts. Spot-edit, don't re-run.
