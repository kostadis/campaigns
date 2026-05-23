# Voice Critique — Brewbarry, scene 1: The Spoils of War

**Narration:** `gm-assist-doc.md` (lines 6–66)
**Voice spec:** `voice/brewbarry_new_pipeline.md`
**Per-char examples:** `examples/brewbarry.md`

## Flags

### [1] Voice spec conflict — extended literary observation

> Dark oak, black-oiled, banded in iron. Someone had taken care of it once. You could tell by the carving — concentric rings of standing stones cut into the face, old work, the kind that takes patience.

**Why:** Brewbarry's spec is "short, declarative sentences. He feels something and then he acts. There is very little space between the two." The examples bear this out — his narration is bodily and immediate ("My rage consumes me. And yet…"), not slow archaeological inventory of a shield. A four-clause description of *the kind that takes patience* is the literary-fiction narrator, not Brewbarry.
**Suggested rewrite:** *Dark oak. Iron bands. Carving on the face — stones in rings, old work. Someone had cared about it once. Then someone hammered a Talos bolt over the middle. Different hands.*

### [2] Banned tic — "the shape of X"

> The shape of belief doesn't always match the thing it's built around.

**Why:** `_genre.md` lists "the shape of X" as a banned Claude tic — "gesturing at pattern without naming it." Brewbarry especially does not abstract this way; his spec says "Do not give him complex moral arguments about systems, factions, or ideology." This is exactly that.
**Suggested rewrite:** Cut the sentence. If something is needed: *They called Talos holy. He wasn't.*

### [3] Voice spec conflict — extended philosophical reflection on past

> I thought about what a god looks like to someone who was told, for years, that the wrong thing was holy. The Uthgardt have their own version of Talos — storms, power, the thing you can't argue with. I was sober when I was found guilty. I was drunk by the time I understood what that meant.

**Why:** Spec: "Do not make him narrate his own shame at length. He references it briefly when it surfaces; he does not return to it." Also: "Do not over-explain his interior. The reader infers from his actions and his short sentences. If a paragraph of inner monologue is needed, it is too long." This is a paragraph of inner monologue about his exile. The examples never do this — when his past comes up, it's one line and gone.
**Suggested rewrite:** *Valphine talked about Lathander. I thought about my Talos. The Uthgardt one. Storms. The thing you don't argue with. I was sober when they found me guilty. That was a long time ago.*

### [4] Generic prose — hedging mid-paragraph

> Probably dead. Probably not going to come asking for it back. But Vukradin's right about the principle, even when the principle costs nothing — especially then, maybe, because the habit has to go somewhere.

**Why:** Spec: "He does not build arguments, justify himself, or hedge. He states what is true and moves." The "even when… especially then, maybe, because…" structure is exactly the hedging-argument the spec forbids. Brewbarry agrees with Vukradin in one sentence and moves.
**Suggested rewrite:** *Probably dead. Probably won't come asking. Vukradin's right anyway.*

### [5] Generic prose — tell-not-show on the halberd

> The halberd sat against my leg, waterlogged and lethal. Some things don't need more words than that.

**Why:** "Some things don't need more words than that" is a *narrator* commenting on the prose's own brevity — meta-commentary the spec doesn't want. Brewbarry simply stops talking when there's nothing to say; he doesn't announce that he is stopping. Compare the examples: he ends sections on action or a one-line verdict, not on a meta-observation about his own laconism.
**Suggested rewrite:** Drop the second sentence. The halberd line lands harder alone.

### [6] Generic prose — Vukradin's cover story narrated twice

> "You're mistaken," Vukradin said, to no one in particular. "This is the halberd you've had all along. You just sharpened it on a sharpening stone. And it just looks more lethal. That's totally fine. You can sharpen your halberd as much as you want. No problem with that."
>
> I said nothing.

**Why:** Not a flag against the prose; flagging because the two Vukradin paragraphs ("This is the halberd you've had all along…") are nearly identical and one looks like an extraction duplicate. Worth checking the VTT to see whether Vukradin actually repeated himself or whether the second block is a duplicate the GM-assist pulled twice. (Voice-neutral, but the artifact is suspect.)
**Suggested rewrite:** Verify against transcript; if duplicate, drop the second.

## Verdict

The scene is doing too much reflective interior for Brewbarry — he philosophizes about belief, lingers on his exile, and hedges through full subordinate clauses. The "shape of belief" line and the closing exile meditation are the highest-leverage cuts; both directly violate the spec. Worth a re-run with the voice file in scope, or a tight manual edit cutting the contemplative paragraphs.
