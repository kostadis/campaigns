# Voice Critique — Vukradin, scene 03: The Universal Basic Treasure Proclamation

**Narration:** `summaries/20260623/narration/session_doc_scene_03_the_universal_basic_treasure_proclamation.scrubbed.md` (re-rendered 2026-08-09, 2661 words — up from 1986)
**Voice spec:** `voice/vukradin_new_pipeline.md` (authoritative)
**Supplementary spec:** `voice/v1/vukradin_voice.md`
**Per-char examples:** `examples/vukradin.md` (162 lines, four passages)
**Genre:** `voice/_genre.md`

*Second pass. Critiques the re-rendered and scrubbed text, not the version reviewed on 2026-08-08.*

## Resolved since the previous render

The two structural findings from the first pass are **fixed**:

- **POV collapse resolved.** The previous render had ~60 lines (95–135, 163–195) carrying no narrator at all. Vukradin is now present throughout the charter debate — reframing, pressing, editorialising in his own register.
- **Unattributed dialogue resolved.** Lines that previously floated with no speaker are now attributed: `"That's why we need to build a wall"` → Soma (153), `"Landed gentry"` → Soma (141), `"I would say property owners…"` → Brewbarry (139). This was the finding I said could not be fixed by re-running, because the source extraction had lost the speakers — the re-render recovered most of them. Worth spot-checking against the VTT that the attributions are *correct* and not confabulated; see flag [4].
- Mechanical residue removed by the scrub pass (`did you roll a 28`, `The roll came up short`, the advantage paragraph, `ask the GM`).

## Flags

### [1] Canon error — Brewbarry's stature, line 139

> Brewbarry stepped forward, all five and a half feet of immediate presence. "I would say property owners within the bounds of Phandalin."

**Why:** Brewbarry is a **Goliath** — `docs/party.md:46` ("Barbarian 6 (Path of the Giant) | Goliath"), `characters/brewbarry.md:5` ("**Species:** Goliath"). Goliaths stand seven to eight feet. Five and a half feet is shorter than an average human. This also contradicts **scene 01 of the same session**, line 57, which calls him "A giant of a man." His entire subclass is Path of the Giant, which grows him larger in combat. This is not a voice problem — it is a factual error that will read as wrong to every player at the table.
**Suggested rewrite:** `Brewbarry stepped forward, and the crowd made room the way crowds do for a goliath. "I would say property owners within the bounds of Phandalin."`

### [2] Banned tic — "the look of a woman who…," line 169

> Linene Graywind stepped forward then, and I saw the glint in her eye — the look of a woman who has been waiting for this argument her whole life.

**Why:** `voice/_genre.md` line 44 bans this construction by name. Vukradin's lens per the genre doc is *specific corruption* — he names Tibor Wester, House Margaster, Adabra, Falcon, not behavioural categories. The first half (`the glint in her eye`) already renders what he saw; the second half taxonomises it.
**Suggested rewrite:** `Linene Graywind stepped forward with a glint in her eye, and I understood that she had been waiting years for someone to say this out loud.`

### [3] Voice spec conflict — verdict register still absent, third scene running

**Why:** A mechanical scan finds none of the spec's signature landings — `Foolish!` / `Scandalous.` / `Phonies!` / `Nope.` / `Done.` — in this scene, as in scenes 03 and 05 of the previous render. Failure-prevention rule 9 names the verdict register as one of three things that "must all be present." Rule 8: "Do not let long building sentences drift without landing in a clear verdict." This scene now has several long builds and all of them resolve into abstraction. Line 55 is the obvious site — Jenna smugly calling wealth "the dialectics of the financials" in front of poor people is exactly the corruption trigger the spec describes.
**Suggested rewrite:** Line 57 → `*The dialectics of the financials.* As if wealth were a scholarly abstraction and not bread on a table. Phonies.`

### [4] Narrator editorialising and recap framing — lines 249–253

> …I looked at that fused mass of impossible gold and felt, for the first time, that I had a rival in noble schemes. (249)

> The Universal Basic Treasure wasn't just a handout. It was a promise that the world could be better than the people who ran it. That we could take the ugly machinery of plunder and make it feed the villagers instead of the wolves. (251)

> Now all we had to do was unfuse the gold, find the expert, and make good on the promise. (253)

**Why:** Three problems stacked. `voice/_genre.md` line 30: "The narrator never editorializes… no winking at the reader. Conclusions belong to the character; the reader is trusted to weigh them." Line 49 bans recap framing outright — line 253 is a to-do list written for the reader's benefit. Line 251 states the scene's theme in plain declarative, which line 209 (`a machine that fed the people who fed us`) already dramatised better.

Separately, **`a rival in noble schemes` at line 249 has no referent I can find.** Nobody in this scene is presented as a rival schemer, noble or otherwise — Harbin claims credit, Linene wants a subcommittee, Jenna leaves. If this is meant to gesture at KP (`docs/KP.md`), Vukradin has no in-world knowledge of him, and the planar-anomaly reveal two lines earlier is Soma's, not his. Flagging as probable invention rather than asserting it.
**Suggested rewrite:** End the scene at line 249's first half and cut 251–253 entirely: `The slag sat there, quiet and wrong, a knot in the fabric of the world that we were only beginning to understand. And as the town cheered behind us, Harbin Wester congratulated himself on a plan he'd never had.`

### [5] Attribution plausibility — lines 155–157

> Brewbarry nodded. "You have to live within Phandalin's boundary for at least 50-plus percent of the year."
>
> "Primary residence, I mean…"

**Why:** The re-render fixed the unattributed-dialogue problem by assigning speakers — but assigned tax-code English to the character least able to produce it. `50-plus percent of the year` and `primary residence` are statutory drafting. Brewbarry's spec: "He thinks in short, declarative sentences… Do not give him complex moral arguments about systems." His own line four beats earlier is `"I need to get myself a house in Phandalin, by the way"`, which is the register. This is worth checking against the VTT — if the tape has someone else saying it, the attribution is simply wrong; if it *is* Brewbarry, the narration should render it in his words.
**Suggested rewrite:** If it stays with him: `Brewbarry nodded. "You have to actually live there. Most of the year. Your real home, not a room you keep."`

### [6] Voice spec conflict — "worthless," line 65

> My abilities, my convictions, my whole worthless silver tongue finally doing what it was meant to do.

**Why:** Failure-prevention rule 1: "Do not make Vukradin sound cynical, smirking, or sardonic. He is sincere." Rule 6: "the world keeps disappointing him, and he has not concluded that disappointment is its nature." Calling his own defining gift *worthless* is self-contempt he does not carry — the spec has him believe "that, given enough words, any room will resolve into harmony." The sentence wants "the thing everyone treats as worthless," not "my worthless thing."
**Suggested rewrite:** `My abilities, my convictions, the silver tongue everyone treats as a party trick — finally doing what it was meant to do.`

### [7] Cliché simile and cross-scene convergence — line 63

> Soma's voice, dry as old leaves: "UBT…"

**Why:** Scene 05 has `Soma asked, dry as old parchment` (line 43). Same construction, same character, same session, different noun — one narrator reaching for the same shelf twice. `voice/_genre.md` line 38 asks for "the sensory specific… before the metaphor," and Soma is a tortle with a body available to the description.
**Suggested rewrite:** `Soma tasted the word. "UBT…"`

### [8] Mechanical scan A — 20 narration-level em-dashes

Lines 9, 23, 29, 31, 55, 65, 71, 111, 115, 169, 209, 235, 241, 245. Down from 30 in the previous render despite the scene being 675 words longer — a real improvement in rate.

**Why:** The remaining concentration is in the long interior builds (65, 209, 235), which is where flag [3] bites: the em-dash parenthetical is what lets a build defer its landing indefinitely.
**Suggested rewrite:** Line 235 `And it turned out — of course it turned out — that this wasn't conventional magic.` → `And it turned out this wasn't conventional magic. Of course it did.`

## Also present

- **Line 199** — `And when the noise died down, someone said it plainly. "That was totally not expected. Take your treasure gift. That was a very clever solution to the problem."` This is still GM reward-narration in the fiction; the scrub pass removed the `The DM` attribution, and the re-render assigned it to `someone`. `Take your treasure gift` is not a thing a Phandalin townsperson says.
- **Line 87 and 129** — the two `sidebar` lines you protected on 2026-08-08 survive the re-render intact and remain in the ignore list.
- **Line 29** — `Even Spider-Man — Toblen, I mean` correctly uses the canon nickname from `voice/vukradin_new_pipeline.md` line 45.

## Verdict

Line 139 puts a seven-foot goliath at five and a half feet, contradicting both the character sheet and scene 01 of the same session — fix that before anything stylistic. The structural problems from the first pass are genuinely resolved; what remains is the missing verdict register and a closing that explains the scene instead of trusting it.
