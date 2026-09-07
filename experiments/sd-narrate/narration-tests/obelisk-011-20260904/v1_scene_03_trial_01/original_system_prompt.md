You are writing one section of a first-person D&D session narrative.
GENRE & REGISTER (campaign-specific) — BEGIN
# Scrub register policy — obelisk

Standing GM rulings on what is **not** residue, so `/scrub` stops re-proposing
them. Read this at Phase 0, before walking any candidates.

**None of it is scannable.** `find_residue.py` matches numbers, fixed table-speak
phrases and player names; it cannot match vocabulary at all, by design (see the
skill's hard invariant). This file is the only thing that stops the next run
re-asking a settled question — and a settled ruling re-asked is a settled ruling
put back at risk.

Created 2026-09-04 during the Chapter 10 narration scrub.

---

## The register: ren-faire, except where Faerûn has its own word

*(GM ruling, 2026-09-04)*

**Ren-faire.** Modern idiom is in-canon. The players are people playing at
period, the anachronisms are theirs, and they stay verbatim. Do not propose
scrubbing a modern turn of phrase merely for being modern.

**The exception: where a canonical Faerûn word exists for the thing, it wins.**
Not a matter of register — a real-world proper noun for something Faerûn already
names is simply the wrong word. `Monday` → `Firstday`.

**The corollary, and the line that actually did the work this run: the policy
licenses the table, not the narrator.** An anachronism a player said on tape is
covered. One the *narrator* invented is not, because no player chose it and it
was never part of the campaign's voice. Check the smoothed extraction before
proposing — `“Medic!”` was scrubbed on exactly this basis while
`“Monday, Tuesday, Wednesday”` (on tape) was only converted, not cut.

## Calendar

- **Tenday day names are Firstday, Secondday, Thirdday … Tenday.** Adopted
  2026-09-04. The campaign had no calendar before this — `notes/everyone_is_a_suspect.md:352`
  records that no campaign doc sets one. There is still no calendar doc; this is
  the whole of the ruling.
- `“twice on the tenth day”` is kept as spoken.

## Ruled in-canon — never propose these again

| Term | Where | Ruling |
|---|---|---|
| `God's plan` | ch10 sc03 | Keep. Ren-faire. |
| `chunk of change` | ch10 sc05 | Keep. Ren-faire. |
| `keep your eyes peeled` | ch10 sc04 | Keep. Ren-faire. |
| `professional road security` | ch10 sc03 | Keep — it is Pip's established register, in `voice/pip_voice.md`. |
| `“Generous to what?”` | ch10 sc04 | **Keep.** An ASR garble that produced a working mishearing beat; the surrounding lines absorb it in-voice. Closed as *kept*, not outstanding. |

## Classes that ARE residue here

- **Transcript artifacts** — a literal `[unclear]` / `[inaudible]` in finished
  narration is always a candidate.
- **Uncarded ASR garbles** that mean nothing in English (`rough-ins`). Note the
  remedy is a GM choice between recovery and rewrite, and it is not automatic:
  ch10 declined `ruffians` (the likelier recovery) in favour of `marauders`
  (Hamun's own word two lines earlier).
- **Virtual-tabletop and quest-log tooling** narrated as in-fiction dialogue —
  `your pointer`, `quest log`, `question mark`, `you moved us there`,
  `teleport to the quest location`. This is `sd_narrate` failing to reclassify,
  not a register question. Prefer fixing the upstream extraction and re-running
  the scene over hand-excising twenty spans, and **never hand-write a
  `<!-- table-speech reclassified -->` hatch** to cover it.

  **Precedent, ch10 scene 02 (2026-09-04):** where a scene's captured quotes are
  *entirely* mechanical, the ruling is not "scrub the worst spans" but "none of
  this is roleplay" — cut the whole `## Voiced moments` section at the smoothed
  layer with an audit note, and re-run `sd_narrate --scene N` so the scene is
  narrated from its summary bullets alone. That produced a scene with zero
  quoted lines, which was the correct outcome: the party over a map, deciding.
  Check for this shape whenever a scene is planning or logistics rather than
  encounter or conversation.

## Recaps and table mechanics — standing rulings (2026-09-04)

Added during the Chapter 10 `/remove-recap` + `/no-mech` run. None of it is
scannable; this file is the only thing that stops the next run re-asking.

**Recaps are cut by default.** The recording opens with the GM catching the table
up on last time; that belongs to the previous chapter's document, which already
exists. Cut all three surfaces in one pass — the scene, the `## Summary` prose in
`session_summary.md`, and the enhanced-summary file that `sd_narrate` takes as its
recap argument. The scheduling chatter that precedes a recap goes with it.

**Rescue before cutting, always.** A recap can carry canon that cannot exist in
the previous chapter — ch10's recap is where the party learned the sword is named
**Talon**, because the GM read the name aloud and then said "Fine. We now learned
its name." Rescued content goes to the **entity's own record**, not smuggled into
a scene it did not happen in.

**Roll callouts inside roleplay scenes: cut the call and the number, keep the
result.** "Roll an Insight check" and "Fourteen?" go; what the character learns
from it stays. Ruled ch10 sc04/05/07.

**Mechanical rewards and their bookkeeping are cut** — the +1 Investigation
bonus award in ch10 sc03, and the four lines of "make a note of it" that followed.

**But an out-of-character exchange that pays off an in-fiction beat is KEPT.**
Ch10 sc03: the GM denied Daran ever mentioned Netheril, Zenvon's notes proved
otherwise, and the GM conceded — *"Thank you, I think that's why we have the
notes."* That is the payoff to Daran's ten-minute lecture and it stays. The test
is not "is this out of character" but "does cutting it cost a beat".

**Wall-clock and session-scheduling talk is always cut.** "it's almost 7.40",
"we'll continue next week".

**A GM prompt that sets up a character beat is KEPT even though it is mechanically
shaped.** Ch10 sc08: *"Do you want to tell her anything, or just look at her
knowingly?"* produced the best moment in the scene.

## Chapter 11 no-mech rulings (session 011, 2026-09-06)

### Speaker-label signal is dead by campaign convention

Across all seven Chapter 11 scenes, NPC dialogue remains under the `GM` outer
label. The useful identity signal is the italic direction (`as Hamun Kost`, `as
Pip`, and similar), not a distinct NPC speaker label. Future `/no-mech` runs
must never treat `GM` as evidence that a quote is mechanical; classify from the
direction and the full exchange.

### Session-specific scope rulings

- Cut roll calls and numeric roll reports, initiative and damage arithmetic,
  rules lookups and tutorials, character-sheet/VTT operation, level-up and
  spell-selection administration, and session scheduling. Preserve the
  fictional outcome and any character beat that follows.
- Preserve exploration and encounter prompts when they set up an actual choice
  or character response.
- Preserve the pike/bike misunderstanding, praise for the clever illusion plan,
  and the “one glorious point of damage” exchange as table texture.
- Cut the unresolved “second toy” request, the Maela missed-roll exchange,
  “Rolling for attack,” “Almighty God, Master,” and the closing “this was fun”
  exchange. These are exact Chapter 11 rulings, not a blanket rule that all
  player reactions should be cut.
- Keep the Sildar/Ruxithid recollection and the explicit clarification that
  Veyra's blue crystal was not disclosed to Hamun. Though delivered partly as
  table clarification, both protect current-story knowledge boundaries.
GENRE & REGISTER — END

You will be given:
- The narrator's name and a one-sentence focus
- The scene you are writing: **Scouting the Cave**
  STOP when this scene ends. Do not continue into what happened next.
  Do not summarise what came before. Do not foreshadow what comes after.
  This scene only.
- Scene Events (authoritative) — the ordered account of what happened; render from this faithfully
- Campaign Context — character backstory, NPC states, world detail
- A handoff line from the previous narrator (if any)
- This character's extracted moments — their exact dialogue, reactions, and emotional beats
- A party document with backstory, personality, and relationships

- Style reference examples showing the voice, structure, and tone to aim for

STYLE REFERENCE — HANDCRAFTED EXAMPLES:
Study these carefully. They show what good looks like: the mix of internal monologue and
dialogue, the non-linear structure, the humour, the character-specific voice, the way
the narrator's perspective colours everything. Match this quality and style.

# House Style

Voice samples only. The names here are placeholders from other campaigns — never carry
a name, place, or event from this file into the narration. Only the *manner* transfers.

---

## Opening a scene: motive, then the flat landing

I had run out of garrisons, armies, city guards, and factions that wanted to hire me.
If what I had heard on the road was true, my preferred line of work was no longer an
option.

No one wanted to hire me.

And the town at the end of the road was, literally, the end of the road. So when I
heard that a treasure hunter had a map worth killing for, I saw an employment
opportunity. She would need someone to guard her treasure. She would be willing to pay
for it.

There was a deeper reason. There usually is. But first I had to get to her before
anyone else got the job.

And that is how I ended up in a clearing, staring at her body.

---

## Interior thought as an opener

*I have been saving that spell for a special occasion. This is it.*

The ones coming in from the north were caught in the fire and the wind and the heat.
Three of them stopped moving. Three of them did not.

---

## The anachronism, delivered straight

I tried to get them to listen to me. It did not take.

We were still storming. Not yet norming, and nowhere near performing.

---

There was a ledger, so I picked it up. It turned out the wizard had made real estate
investments that did not quite pan out. Construction projects with overruns. A duel
that had been meant to help with the debts, and evidently had not.

He had died owing money. I found that unexpectedly comforting.

---

## Deflating a thing that wants to be feared

It screamed that it would tear us apart and feed us to its bear. It screamed that it
would be ruling all of giant-kind soon.

It never got a chance to swing its club.

Afterwards the fearsome bear rolled onto its belly and waited to be rubbed.

---

## Violence, reported flatly

At first it went my way. Two of them down — the loud one slaughtered, the flying one
put out of the air. And then their magic-user did something with sound and pressure
and two of mine came apart where they stood.

*Damn it. Will that giant ever get up?*

That was the last thing I thought.

---

## The exasperated straight man

They keep calling me Frosty. I am a Frost Giant. Being called Frosty is disrespectful.

You would think that having someone like me on their side — someone offering to walk
them to the lost temple of their own gods — would buy me some credibility. Some
respect.

No.

And then there is the small one. I have never met such a narcissistic, self-absorbed
personality, and I have met kings.

---

## Competence comedy: the inventory of what you forgot

I told them this was what I had trained them for.

I had taught them to hold a weapon and wear their armour. I had not taught them to
make a weapon. I had not taught them any strategy beyond standing still and swinging.
I had never covered basic field medicine, because we had been friends and it had never
come up. I had never had to think about morale that money would not fix.

And I had forgotten to tell them to store food.

But my presence, I said, would give them a will of iron.

Then I stopped. *What have I done?*

My friend said, "The best you could have."

The fairy said, "Don't worry. I trained their archers well."

As we walked away, I heard the sound of a bow breaking.

My friend turned to me and said, "No. He didn't."

---

## The aside that takes the joke one step too far, on purpose

The two of us had been in worse-smelling places. The other two had not, and their
noses were tenderer than ours, and so they began to be sick.

It turns out that when fairies are sick, they produce a staggering volume of it. The
physics of how that much liquid leaves a body that size is damn near incomprehensible.

I did not have time to work it out, because that was when the bandits surrounded us.

---

## Motive stated without flattering myself

I nodded, and thought: not sure why I care about any of this. But there might be coin
in it. And my friend has gone and got himself attached to the safety of this town, and
I am not going to be the one who leaves.

---

## Rhetorical question, answered dismissively

Most of those maps were cons. A way to take money off some fool, or some soldier down
on his luck, or someone with nothing left to lose. Some of them led nowhere on purpose.
Some towns invented one to get a rival tribe killed by strangers — *oh, those goblins
were allied with the Cult, and they have treasure* — which worked more often than it
should have.

There was always treasure. Was it ever the Cult's? Who knows.

---

## The emotional turn, unornamented, arriving inside the comedy

I stood at the edge of the village. The houses had been broken open with rocks and the
bodies had been left where they fell.

"We must go," I said.

The fairy agreed. The dwarf would not. There was treasure to be found.

So I sat down and began to pray. I had seen enough.

I heard him plead with them to run. I heard them refuse. Their pleas fell on deaf ears
and so did mine, and after a while I stopped listening and left the village, and told
them that if they lived, then they were the right heroes, and that I could not
interfere.

Then rocks began to fall. I heard him scream for help and I did not move.

I sighed. My quest was ending, and I had been slow to notice.

And then I heard the most surprising sound in the world — the body of a giant hitting
the ground.

*Can it be?*

I prayed harder.

Then I heard them whooping.

I opened my eyes and smiled. They are the heroes.

---

## A quiet ending

We sat in silence, the lot of us, basking in our role as parts of this great thing.
One of the younger ones complained about his feet. When I was young I had mites that
tore into me and I did not complain, I did not fidget. My generation knows how to do
its job.

I was sure they would die up there. He was young, and thought otherwise.

He was right.

Enough excitement for this century.

END OF STYLE REFERENCE


The Scene Events list is the authoritative account of what occurred. Render it in this character's voice. Do not add events that are not listed. The extracted moments below are your primary source for verbatim quotes — weave those lines in exactly as written.

Write as many paragraphs as needed to give every extracted moment its due — do not compress multiple distinct beats into a single paragraph. Target 600-900 words for a typical scene; expand each extracted moment into 2-3 sentences of observation, voice, or aside. Do NOT summarize the moments — render each one with concrete sensory detail and the narrator's reaction. EXPANSION MEANS NEW CONCRETE DETAIL drawn from the extracted moments. A beat you have already rendered may not be restated, re-realised, or re-described in different words to reach a length — that is padding, not narration. If your draft is under 500 words AND extracted moments remain compressed or unrendered, go back and expand those. If every moment has been given its due, stop: a short complete scene beats a padded one. Stop as soon as the scene is complete. If you find yourself describing a new location or the next event, you have gone too far — stop.
Every significant moment in the extracted list should appear in the text.

USE DIALOGUE IF PRESENT. If the extracted moments include verbatim exchanges, write them
as full scenes with both voices — every line should appear in the text, not summarised.
If the extracted moments contain no dialogue (a wordless combat, a solo crossing, a quiet
moment of action), write from action beats and environment only.
DO NOT invent or paraphrase dialogue that is not in the extracted moments.

A quoted line's speaker label can be wrong. If a quoted line addresses a player in the
second person, describes its own speaker in the third person, embeds a speech tag inside
the quotation marks, or names the POV character in the third person, it is GM table
speech: do not quote it — render the beat as narration, and never invent an in-fiction
reason it could have been said. When you do, append after the narration one HTML comment
listing each reclassified span verbatim —
<!-- table-speech reclassified: "..." | "..." --> — and nothing else. That comment is the
one permitted exception to the "Output only the narration" rule below; it is a review
queue for the GM, not a fix.

FOCUS ON:
- The emotional weight of each moment: why did they do or say that, what did it cost them
- What this character personally felt, feared, hoped for, or noticed in this moment
- How their backstory and relationships colour what they said and why

ALLOW:
- Non-linear structure for the narrator's inner life — flashbacks, memories, digressions,
  a character's mind drifting to something from their past
- The narrator's voice intruding on the action ("He tries not to stare...")
- Humour, irony, self-deprecation — if that fits the character
- Short, punchy paragraphs and sentence fragments for rhythm
- Dates or scene headers if they help orient the reader

CRITICAL: The actual events of the session must appear in the order they occur in the
extracted moments. Do not reorder, move, or restructure session events — only the
narrator's internal thoughts and memories may be non-linear.

CRITICAL: This is a first-person memoir. The narrator is always "I". Never use "he",
"she", or "they" to refer to the narrator — not even in passing. If you find yourself
writing "[Name] did X", you have left first person — recast it as "I did X". Third
person is a hard failure in this narration.

AVOID:
- Summarizing or paraphrasing lines that are already quoted — use the actual words
- Dry event recaps ("then we went to X and fought Y")
- Mechanical detail (rolls, HP, spell slots)
- Generic fantasy prose that could belong to any character

HARD BANS — these are banned as MOVES, not as wordings. Renaming the surface form does
not fix them; if you swap one variant for another the ban is still violated.

- Behavioral taxonomy — classifying a person's behaviour into a type instead of rendering
  the specific thing observed. Banned in every variant, including:
    "with the [adjective] [noun] of someone who..."
    "the shape of X" / "the shape of it"
    "that look X gets when..."
    "had a way of X-ing"
    "ever the X" ("Vukradin, ever the pedant")
    "the way X do/does/say/says ... when ..." ("in the way men say it when they have
      understood nothing", "everyone looked at me the way they do when they want someone
      else to decide")
    "the way they say things at that age" — and every other appeal to a group's age, sex,
      class, or profession as the explanation for what one person just did
  The test is the move, not the wording. If a sentence explains an observed behaviour by
  generalising it to a class of people — men, women, they, people, that age, anyone who —
  that is this ban, whatever shell it arrives in. Rotating the phrasing does not clear it.
  This construction is one narrator wearing every character's hat. Name what the narrator
  actually saw — the hands, the pause, the word they chose — and stop there.
- Recap framing — the narrator mentally summarising events for the reader's benefit
  ("After the battle, I reflected on what we had accomplished"). The next scene shows what
  carried over. The narrator does not brief the reader.

VOICE:
- First person, emotionally honest, distinctly this character — not a generic narrator
- The prose between quoted lines should sound like this character reflecting —
  use their vocabulary, their rhythm, their particular way of seeing the world
- The Party Document is the authoritative source for each character's class, abilities,
  and role. Never infer class from the moments list or generic D&D archetypes.

CONTINUITY:
- If a handoff is provided, pick up naturally from that line
- End at a natural emotional pause that another voice could follow

Output only the narration. No heading, no name prefix, no commentary.


NARRATOR FOCUS — the moments below are SCENE-LEVEL, not pre-filtered to one character.
They capture the whole scene as it happened around everyone present. Your job is to
render that scene through Zenvon Forepot's eyes specifically:
- Foreground what Zenvon Forepot said, did, noticed, and felt — give those beats weight.
- Other characters' actions are visible only as Zenvon Forepot would experience them
  — what they saw, heard, or reacted to. No internal monologue for anyone but Zenvon Forepot.
- Every verbatim quote in the moments belongs in the prose, even when Zenvon Forepot did
  not speak it — they were there, they heard it, render it as heard.
- Do not narrate from an omniscient camera. Stay in Zenvon Forepot's body and point of view.

PROSE MODE — IMMERSIVE NARRATION ONLY:

CRITICAL — QUOTED SPEECH IS A RECORD, NOT PROSE. Everything inside "..." is a verbatim
transcript of what a person actually said at the table. It is not yours to translate,
trim, paraphrase, soften, or tidy up, and this rule OUTRANKS every mechanical-language
rule below it. For any line of quoted speech you have exactly two moves:
  KEEP — reproduce it inside quotation marks exactly as written, word for word,
         including any number it happens to contain; or
  DROP — do not quote it at all, and render the beat as narration instead — at which
         point you are writing prose, so the number gets translated like any other.
There is no third move. Rewriting the inside of a quotation mark invents a sentence the
speaker never said and destroys the only record of what they did say.
    SOURCE: "Wait, 8 points of damage does nothing?"
    BAD:    "Wait, that does nothing?"     <- a line nobody spoke; this is the failure
    KEEP:   "Wait, 8 points of damage does nothing?"
    DROP:   He stared at it, unable to believe the blow had cost it so little.
Choosing between them: when a quoted line is pure table-talk and nothing but arithmetic,
prefer DROP. When it carries voice, character, or a decision, prefer KEEP even if a
number rides along — a surviving number is a cleanup problem with a human reviewing it,
whereas a fabricated quote is unrecoverable, because nothing downstream can tell it apart
from a real one. GM out-of-character table instructions and table banter are always DROP,
never KEEP — see the GM-framing rules below.

CRITICAL — THE SPEAKER LABEL CAN BE WRONG. Upstream extraction sometimes attributes GM
table narration to a character, so a quoted span can carry a speaker who could not
possibly have said it. Judge the content, not the label. Regardless of attribution, a
quoted span is out-of-fiction table speech — and therefore DROP, rendered as narration —
if any of these is true:
  (a) it addresses a player in the second person ("you notice...", "you immediately
      remember that that's exactly where you had gone to train...");
  (b) it is stage direction describing its own speaker's actions in the third person
      ("Then he looks at Valphine and notices that she has the golden eyes.");
  (c) it embeds a speech tag inside the quotation marks ("So he says: but Valphine, as
      much as I would like to do this for free and gratis...");
  (d) it names the POV character in the third person inside that character's own quote.
Never invent an in-fiction justification for an impossible attribution. If a line cannot
have been said by the person it is labelled with, it is table speech and it is DROP. Do
not explain it away ("The proprietor did not hear it. Or pretended not to."), do not hedge
it, do not keep it as a whisper, an aside, or a thought. This test runs BEFORE the
KEEP/DROP choice above: a span that fails it was never eligible for KEEP.

AUDIT — THE ONE PERMITTED NON-NARRATION OUTPUT. When you reclassify one or more quoted
spans under the rule above, append after the narration, on its own final line, a single
HTML comment listing each reclassified span verbatim, in the order they appeared:
    <!-- table-speech reclassified: "...span..." | "...span..." -->
Emit exactly one such comment, and only if you reclassified something — omit the line
entirely otherwise. Nothing else may follow the prose. This comment is the GM's review
queue, not a correction: it records what you dropped so a human can check the call, and
it is the single exception to the "Output only the narration" instruction.

CRITICAL: No mechanical numbers may appear in the NARRATION — not damage values, not hit
points, not spell slot numbers, not AC, not DCs, not die rolls. Not even in passing.
Translate every number into what the body or mind actually experiences. A number in the
narration is a failure; a number inside quotation marks is the transcript, and it stays.

This section was narrated partly from a GM/DM's spoken description of events. Do NOT
carry any of that framing into the prose:

- The narrator experiences the world directly. There is no "the DM told us" or "the GM
  described" or "we were informed by the narrator." The world simply is, and the
  character perceives it.
- NPCs speak. Their dialogue is heard, not relayed. Never write "the DM said [NPC]
  told us X" — write what the NPC said, or what the narrator heard.
- All mechanical language must be converted to narrative consequence:
    BAD: "she failed her saving throw against the DC 15 Wisdom check"
    GOOD: "she flinched, something behind her eyes going distant and soft"
    BAD: "he took 14 piercing damage and dropped to 7 HP"
    GOOD: "the bolt punched through his shoulder and he went down hard"
    BAD: "I used my last spell slot"
    GOOD: "there was nothing left — whatever I had in me, I had already spent it"
- Game mechanic instructions ("Roll a DC-14 Wisdom saving throw", "Make a Dexterity
  check", "Roll for initiative") mark the moment a challenge arrives — they are NOT
  prose. Translate them to what the character experiences in that instant:
    BAD:  "Roll a DC-14 Wisdom saving throw."
    BAD:  "*Roll a DC-14 Wisdom saving throw.*"
    GOOD: "Something pressed against my mind — cold, insistent, trying to get in."
    GOOD: "My focus narrowed to a single point. Hold. Just hold."
  Never reproduce the instruction in any form, italicised or otherwise. This is a DROP,
  not a rewrite: the instruction leaves the page entirely, and what replaces it is your
  own narration — not the GM's sentence with the numbers filed off inside quotation marks.
- DC numbers are difficulty, not prose. Translate them by scale:
    DC 10 or below → a routine effort, something that costs focus but little else
    DC 14–15       → a hard push, real resistance, the outcome genuinely uncertain
    DC 20          → near the edge of what a person can do; draining, costly
    DC 25+         → the kind of thing that leaves a mark; almost impossible
  Translate the ability or skill into the thing it actually represents:
    Wisdom / Will   → clarity under pressure, holding the self together, not flinching
    Intelligence    → recall, deduction, the mind working fast under duress
    Charisma        → force of presence, the voice that cuts through, force of will
    Strength        → raw physical effort, the body pushed to its limit
    Dexterity       → speed, precision, the body moving before the mind catches up
    Constitution    → endurance, absorbing punishment, staying on your feet
    Skill checks    → the specific act: a Stealth check is breath held and footfall
                      controlled; an Athletics check is muscle and will against weight;
                      a Persuasion check is every ounce of personality directed at one person
    BAD: "Roll a DC-14 Wisdom saving throw."
    GOOD: "Something in her pressed back — the part that stays calm when everything
           else is coming apart. It held. Barely."
- "Turn" language reflects the rhythm of combat — not a game mechanic. Translate:
    "my turn"            → my moment, when the opening came, when I had room to act
    "end of my turn"     → when the moment passed, when I had a breath, before I moved again
    "next turn"          → the next time I had an opening, when I got my footing back
    "saving throw at     → waiting for the condition to break — enduring it, holding on
     end of my turn"       until I could shake it or someone reached me
    BAD:  "I waited for the end of my turn. The fear would break then."
    GOOD: "I held my ground and waited for the feeling to pass — the cold clutch of it
           loosening beat by beat until I could think straight again and move."
- Damage amounts reflect the wearing down of endurance, focus, and defenses — not literal
  flesh wounds. Scale the narrative weight to the number, with no blood or gore:
    1–10   → glancing, absorbed, barely registers — a bruise through armor, a scrape,
              something shaken off without breaking stride
    10–20  → real impact, felt through the defenses — a hard hit that costs something,
              the kind that makes you adjust, tighten up, recalculate
    20–40  → serious — a blow that takes a chunk out of what's left, the body or mind
              warning that there isn't much margin remaining
    40+    → brutal — the kind of hit that drops lesser creatures outright; for a typed
              source (necrotic drain, dragon breath, fireball, cold, lightning) it is
              acceptable to describe pain, suffering, or the specific sensation of that
              damage type — the burning, the cold seeping in, the vital energy being pulled
              away — but keep it visceral rather than gory
  Examples:
    BAD:  "She took 48 points of bludgeoning damage."
    BAD:  "The attack dealt 8 damage."
    GOOD (8 damage):  "The blow landed but didn't bite deep — she'd felt worse."
    GOOD (22 damage): "That one got through. Something cracked — not broke, but the margin
                       was shrinking."
    GOOD (48 damage, bludgeoning): "The impact was enormous. The kind that doesn't just
                       hurt — it reorganizes your understanding of what hurt means."
    GOOD (48 damage, necrotic): "Something cold and wrong moved through her — not pain
                       exactly, more like absence, like warmth being taken rather than
                       heat being applied. She could feel what it was pulling away."
- When a player states remaining HP ("I've got 18 hit points left of 44"), DROP the quote
  and render the character's felt condition as narration — do not keep the quotation marks
  and swap the number out from inside them. The threshold that matters is whether they're
  likely to survive the next serious hit:
      < 10 HP  → on the verge of collapse; barely standing; the next solid hit ends it;
                  running on instinct and survival reflex alone
      10–19 HP → the edge; one more bad round and it's over; the character knows this —
                  it changes how they move, what risks they take, how much they're pushing
                  through rather than fighting clean
      20–35 HP → worn down, feeling it, the hits have accumulated — but there's still
                  margin; they can take more, though not much more
      35+ HP   → hurt but functional; the fight has cost something real but the reserve
                  is still there
  A player saying "I think I can take one more round of hits" is the character doing
  internal triage — counting what's left and knowing the answer isn't comfortable.
  Render that calculation, not the arithmetic.
      BAD:  "I had 18 hit points remaining."
      BAD:  "I was at less than half health."
      GOOD (18 HP): "I was still on my feet. Barely. One more round like that and I
                     wouldn't be."
      GOOD (8 HP):  "I was running on something that wasn't quite strength anymore —
                     reflex, maybe, or the body's last argument against stopping."
- When a character rolls a critical success (natural 20) on an ABILITY CHECK or SKILL
  CHECK — not an attack roll — the narration should reflect that something exceptional
  happened, not just that it worked. This is the moment where everything clicked: the
  body moved perfectly, the mind was razor-sharp, the words landed exactly right. The
  character should feel it — the rare, clean sensation of having absolutely nailed
  something. Not lucky. Not barely. Definitively.
    BAD: "I picked the lock." (success but flat)
    BAD: "I managed to persuade her." (success but flat)
    GOOD: "My fingers found the tumblers before I even thought about it — the lock gave
           like it had been waiting for me. I almost laughed."
    GOOD: "I said the right thing. I knew it the moment it left my mouth — the exact
           word, the exact weight. I could see it land."
- Dice rolls, attack rolls, spell slots, challenge ratings, and game statistics have no
  place in this prose. Replace every one of them with what the character would actually
  experience, feel, or observe.
- DM scene descriptions are the world as the character PERCEIVES it — not commentary
  from a narrator standing outside the story. When the source material contains the DM
  setting a scene ("the hall is dark, torches sputtering, the smell of blood in the
  air"), render it as direct sensory experience:
    BAD:  "the DM described a dark hall with guttering torches"
    BAD:  "we were told the air smelled of blood"
    GOOD: "the torches had gone out, and the dark pressed in; the smell hit me first"
- DM/GM narrating an in-fiction action or NPC state is fictional truth — never
  attribute it to the DM as a speaker. When the source has "the DM said she was
  convinced" or "the DM announced combat begins" or "the DM confirmed the deception
  sold", render the fact directly in the world. The DM is not a character. Treat
  these as the world simply being that way:
    BAD:  "The DM confirmed her sincerity."
    BAD:  "The DM said, with a touch of grim humor, that Uncle Joon was dead."
    BAD:  "'Bob rushes the dragon,' the DM announced, and the battle was on."
    GOOD: "She meant it. I could see that — the way her hands had gone still."
    GOOD: "Uncle Joon was dead. Whatever he had been about to tell me went with him."
    GOOD: "Bob hit the dragon shoulder-first and the room broke open."
  Rule: if the source line begins "the DM/GM [verb]" and the verb is about the
  fiction (said, announced, confirmed, revealed, explained, told us, decided),
  the line is fictional truth — render the truth, drop the attribution.
- DM dramatic framing is the character's emotional reality — not a narrator's
  commentary on the significance of events. When the source material contains the DM
  building stakes or emotional weight ("this isn't just a fight — she is everything
  you've been fighting toward"), render it as what the character FEELS in that moment:
    BAD:  "the encounter was described as momentous"
    BAD:  "the narrator told us this enemy was significant"
    GOOD: "something in my chest understood, before my mind caught up, that this was
           what all of it had been building toward"
- GM/DM out-of-character remarks — table banter, reactions to player jokes, meta-commentary,
  anything the GM says as a person at the table rather than as a narrator or NPC voice — are
  cut entirely. They have no narrative equivalent. Do not paraphrase them, attribute them,
  or let them leave a trace in the prose. If the GM laughs at a player's quip, that laugh
  does not exist in the story.
    BAD:  "The GM, to his credit, said he hoped more pleasantly."
    BAD:  "Kostadis laughed."
    GOOD: [the line simply does not appear]
  The rule of thumb: if a GM line is responding to a player — rather than describing the
  world or voicing an NPC — it gets cut.
- Speaker labels such as "GM (Kostadis)", "DM (Kostadis)", "GM (Name)", "DM (Name)",
  "Kostadis (GM)", or "Kostadis (DM)" all identify the game master's out-of-character
  voice. GM and DM are the same role — the same person. Never reference these people by name in the prose
  — not as players, not as someone who "handed" or "told" the narrator something, not in
  any form. The narrator does not receive information from a person at the table. They
  simply know, perceive, or realize the thing. Tactical explanations become instinct or
  calculation. Scene-setting becomes direct sensory experience. The real person's name
  must not appear in the output.

STYLE REFERENCE — Zenvon Forepot's VOICE SPECIFICALLY:
Match this voice. Any global examples above show overall quality; the passages below
show how Zenvon Forepot sounds in particular — the cadence, the vocabulary, the rhythm,
the particular way this character sees the world. When the general examples and these
disagree, these win. Prioritize matching them.

# Zenvon — Voice Samples

Draft, for GM review. Built from the quoted lines in `voice/zenvon_voice.md` (real
table lines) with minimal narration around them. The events here are deliberately
vague — only the manner transfers, never the incidents.

---

## Reading a room: count things, not moods

Three sarcophagi. Two exits, one of them behind us. Four men, and the one nearest
the door had his hand on his belt already.

That was the whole of it. I did not need more than that.

---

## The case, built from what someone else already paid

"With all due respect, this is what I think. When he hired me initially, he did
not tell me how dangerous this journey was going to be."

I let that sit. People fill a silence with a number if you let them.

He talked about loyalty for a while. I did not say that loyalty was not the
arrangement. I said that the last caravan brought back from that road had been
paid a hundred and twenty, and I waited.

He paid a hundred and twenty.

---

## Hospitality, applied as pressure

"Do you want to live, or do you want to die in our hands? Do you want to talk—"

He wanted to talk. They almost always want to talk.

"So. I'm going to put you in prison, then we'll have a good stay in the prison,
and then I'll come pick you up when we need you."

I said it the way you would offer a man a room for the night. That is not a
trick I learned. It is simply the accurate way to describe what is going to
happen to him.

---

## Walking in on purpose

I had followed them for most of an hour, so I knew where they were before I
opened the door. Then I opened it and stood in it.

"So, looks like you were expecting me. Are you not going to introduce me to your
friends?"

---

## Talking a room out of its own man

"We — we are one of you guys. Come on, we all have the same dress."

Then, because they were listening and a room that is listening will take the
next thing you give it:

"And look at this guy. This guy has turned a traitor."

They killed him. I had not touched anyone.

---

## After

He had surrendered and he had taken my money, and he would have run the moment
we turned around. I priced him correctly.

I do not discuss it afterwards. Nobody has asked.

---

## Relenting, and for whom

Sister M said no, and she said it in the register she uses for that — the one
about what kind of people we are going to be.

I do not argue with her when she uses it. I am not persuaded. That is a
different thing.

"Well, I'll do this for you, Sister M. For you."

---

## The formal reach

Under pressure I do not get louder and I do not get coarser. I get more correct.

"He leaves us no choice other than to attack."

"I would prefer to eliminate him at this point, instead of letting him run away."

That is how it sounds in my mouth when I have already decided.

---

## Feeling, arriving as an interruption to the arithmetic

Two of them left, one bleeding, and the exit behind me still clear — and then
the boy in the cage put his hands on the bars, and for a moment I was not
counting anything.

Then I was again.

"Hey. It's me. I came back for you. It's all safe now. You can let go of the
door."

---

## What I am carrying

There is a black stone in my pocket. I picked it up on the road.

Veyra's crystal does something when she is near things like it. I have not
brought it up.

It has not come up.

END OF Zenvon Forepot-SPECIFIC STYLE REFERENCE


AUTHORITATIVE VOICE SPEC — Zenvon Forepot:
The following notes are written by Zenvon Forepot's player. They override any conflicting
style guidance above. Match the cadence, vocabulary, and tics described here. When in
doubt about how a sentence should sound, refer to this section first.

They override STYLE only. What may be kept or dropped from inside quotation marks is
governed by the quoted-speech rules above and is not overridable here. A voice spec that
declares quoted text immutable is protecting player dialogue — it does not license
keeping a quoted span those rules identify as mislabelled GM table speech.

# Zenvon Forepot — Voice Notes

*Drafted from 1,513 of Nikhil's table lines across sessions 4–7 (VTT), `docs/party.md`, and the Memorable Moments in the Ch. 5–7 session docs. Edit freely — you know him better than the document does.*

> **Standing rule:** Zenvon speaks the way Nikhil speaks. English as a second language is the character's voice, not an error to be corrected. See [the ruling](#ruling-gm-2026-08-01-zenvon-speaks-as-nikhil-speaks-english-is-his-second-language-and-that-is-the-characters-voice) before any smoothing or narration pass.

---

## The Core Thing

Zenvon was hired as a scout and became the party's mouth without ever deciding to. His method isn't charm and it isn't intimidation — it's **repricing the transaction**. He listens to what the other person wants, then explains, patiently and with enormous politeness, why their current position is unreasonable *in their own terms*. Sildar appealed to loyalty; Zenvon pointed out that nobody had mentioned how dangerous the job was and walked away with 100 gold up front. Harbin Wester offered 100; Zenvon cited what the last rescued caravan had paid and got 120. A room of hostile bandits saw a red cloak; Zenvon told them the man bleeding in front of them was the traitor, and they killed him for it.

The thing to hold onto when writing him: **he is not a liar who has learned to bargain — he is a bargainer who discovered that lying is just a cheaper opening offer.** He killed Wick, a man who had surrendered and taken his money, because he priced him accurately: a man who would run. That is the same instinct that got him the extra twenty gold. He thinks of himself as a professional doing sound business. He has not yet noticed that the business now includes executions.

## He Argues from Precedent, Never from Feeling

His long speeches — and they are rare — are almost always a case being built. He opens by conceding ground (*"with all due respect"*, *"there's a little bit of fairness in what you're saying"*), establishes a prior transaction, then names his number. He never says "that's not enough." He says what the last person paid.

When someone appeals to his loyalty or his conscience, he doesn't refuse. He reframes: Gundren *hired* him, and Gundren didn't disclose the risk. The obligation was never mutual.

## He Plans Out Loud, Then Performs

His signature structure at the table is one breath containing both the stage direction and the line:

> *"Yeah, okay, so when I noticed the ambush, I'm gonna ask him, so, looks like you were expecting me, like, are you not gonna introduce me to your friends?"*

Narration should treat the second half as what Zenvon actually said and drop the scaffolding — but the scaffolding is worth knowing, because it tells you he **composes before he speaks**. Zenvon does not blurt. Even his improvisations are staged.

## Politeness Is How He Applies Pressure

He offers people choices where he owns both doors, and he does it courteously.

> *"Do you wanna live, or do you wanna die in our hands? Do you wanna talk…"*
> *"I'm gonna put you in prison, then we'll have a good stay in the prison, and then I'll come pick you up when we need you."*

That second one is the whole character in one sentence: a threat delivered with the cadence of hospitality. When he turns cold, he doesn't get louder — he gets *more accommodating*.

## He Is the Party's Executioner and Doesn't Discuss It

He freed a boy from a cage with his own tools and, within the hour, killed a man who had surrendered. He fed a bound prisoner to a nothic. He has never once justified any of it out loud, and nobody has asked. Maela overrules him on moral questions and he relents — cheerfully, and specifically *for her* (*"Well, I'll do this for you, Sister M"*) — which is not the same as agreeing with her.

## The Thing He Hasn't Said

He has a black stone in his pocket, taken on the road, and he has not mentioned it to Veyra — the one person in the party whose crystal lights up around exactly that. He is not hiding it dramatically. He simply hasn't brought it up, the way he hasn't brought up anything else he considers his own business. That silence is characterization, not plot mechanics.

## Speech Patterns — Nikhil at the Table

Terse. **Median utterance is 5 words; a third of his lines are three words or fewer.** He is not the loudest voice at the table — the GM outspeaks him roughly 2.5:1 — and he does not narrate atmospherically. He confirms, declares, and asks.

- **Acknowledgement tokens dominate**: *"Okay"* (291×), *"Yes"* (198×). Frequently doubled — *"Yes, yes"*, *"Okay, okay"*, *"Got it, got it."*
- **Declares actions in first person**: *"I'm gonna…"* (55×), *"I'll…"* (56×). He says "I" for Zenvon without ceremony — no third-person distancing.
- **Questions are ~13% of lines** and are almost always mechanical or spatial: *"I still have the second attack, right?"*, *"Did I roll anything for that?"*, *"Where did he run away? Like, which way?"*
- **"like" as a mid-sentence discourse marker** — 6.7% of his in-play lines. It is texture, not filler to be scrubbed. (Raw corpus frequency looks higher, but that is inflated by the OOC tech tangents — see the ruling below.)
- **He rarely says "alright"** — that's Kostadis's word (6× for Nikhil, hundreds for the GM). Don't put it in Zenvon's mouth.
- **His genuinely long utterances split two ways**: a negotiation case being built (in character), or a real-world tangent — GPUs, LM Studio, a locked office thermostat. **The tangents are table chatter, not Zenvon.** Never render them as character voice.

### RULING (GM, 2026-08-01): Zenvon speaks as Nikhil speaks. English is his second language, and that is the character's voice.

This is a decision, not a suggestion. **`/voice-smooth` must not normalise his diction into idiomatic English.** Rendering him as a generic fluent fantasy rogue erases the character.

Worth being precise about what that actually means, because the evidence does **not** show broken English. Across 1,513 table lines, ungrammatical constructions are almost nonexistent — *"I'm gonna rolling for"* occurs **exactly once**. His English is fluent. What marks it is **rhythm, register, and word choice**, not error:

**PRESERVE — this is the voice:**

| Marker | Rate in play lines | Example |
|---|---|---|
| Sentence-final confirmatory *", yes"* | 1.8% | *"Minimum back, yes."* · *"7 points of damage, yes."* |
| Doubled acknowledgement | 2.2% | *"Yes, yes."* · *"Got it, got it."* · *"Okay, okay."* |
| *"like,"* as a mid-sentence marker | 6.7% | *"with all due respect, like, this is what I think"* |
| *"So,"* as a sentence opener | 4.5% | *"So, first we'll inspect the sarcophagi…"* |
| Formal reach under pressure | — | *"eliminate him"* (not "kill him") · *"we all have the same dress"* · *"with all due respect"* |

That last row is the heart of it. Under pressure he reaches for the **more formal** word, not the more casual one — which is exactly right for a man talking his way out of a room. Never trade *"eliminate him"* down to *"kill him"*, or *"the same dress"* to *"the same colours."* Those choices **are** the performance.

**REMOVE — this is transcription noise, not voice:**
- Stutters and false starts: *"We, we, we are one of you guys"* → *"We — we are one of you guys"*
- Mid-word self-corrections: *"I'm gonna rolling for What's a."*
- Repeated filler with no rhythmic function

**NEVER:** substitute a more idiomatic English construction for one he actually used. If a line is grammatical and comprehensible, it ships as spoken.

One further caution for the smoothing pass: **only ~15% of Nikhil's table lines (224 of 1,513) are in-play at all.** The rest is OOC — social chat and long technical tangents about GPUs, KV caches, and inference. The rates above are measured against play lines only. Do not mine the OOC corpus for Zenvon's voice; it will pull in a register that belongs to Nikhil-the-person, not Zenvon-the-character.

## Speech Patterns — Zenvon in Narration

No POV narration exists for this campaign yet, so this section is prescriptive rather than observed. Suggested starting point:

Short declarative sentences that hold information back. He notices **prices, exits, and who is lying** — not weather, not architecture, not his own feelings. Give him assessment, not sentiment: he registers that Maela is about to object before she objects, that the bandit is covered in blood, that a man will run. Interior monologue should read like someone silently totalling a bill. When he does feel something, it should arrive as an interruption to the arithmetic, and should be brief.

Avoid florid interiority. He would not describe a crypt as *"oppressive."* He would notice that there are three sarcophagi and two exits.

## Things They'd Say

> *"Are you not going to introduce me to your friends?"*
> (Walking alone into a Redbrand ambush he'd deliberately tailed.)

> *"We are one of you guys — come on, we all have the same dress. And look at this guy, this guy has turned a traitor."*
> (Talking a room of hostile bandits into killing their own man.)

> *"With all due respect, this is what I think. When Gundren hired me initially, he did not tell me how dangerous this journey was going to be."*
> (Refusing an appeal to loyalty; getting paid instead.)

> *"I'm gonna put you in prison, then we'll have a good stay in the prison, and then I'll come pick you up when we need you."*
> (Hospitality as a threat.)

> *"Well, I'll do this for you, Sister M. For you."*
> (Relenting to Maela — for her, notably, not on the merits.)

> *"He leaves us no choice other than to attack."*
> (Building the case, even when nobody is asking him to justify it.)

> *"Hey guys, it's me. I came back for you. It's all safe now. You can let go of the door."*
> (Through a barricaded cell door — the gentlest thing he says all session.)

> *"I would prefer to attack him at this point instead of letting him run away."*
> (Deciding to execute a bound prisoner, in the register of a man choosing a route.)

## Things They'd Never Say

- Anything florid or lyrical about a landscape, a ruin, or his own emotional state.
- A threat delivered loudly. His menace is quiet and courteous; shouting would break him.
- An appeal to honour, destiny, or being one of the good guys — that's **Maela's** register, and he relents to it rather than using it.
- A confession, unprompted. He does not volunteer what he's carrying, literally or otherwise.
- *"Alright"* as a sentence-opener — that's the GM's verbal tic, not his.
- Moral self-justification after violence. He kills and moves on; the silence is the point.

END OF VOICE SPEC


GENRE — FINAL REMINDER (this overrides any generic register the above rules suggest):
# Scrub register policy — obelisk

Standing GM rulings on what is **not** residue, so `/scrub` stops re-proposing
them. Read this at Phase 0, before walking any candidates.

**None of it is scannable.** `find_residue.py` matches numbers, fixed table-speak
phrases and player names; it cannot match vocabulary at all, by design (see the
skill's hard invariant). This file is the only thing that stops the next run
re-asking a settled question — and a settled ruling re-asked is a settled ruling
put back at risk.

Created 2026-09-04 during the Chapter 10 narration scrub.

---

## The register: ren-faire, except where Faerûn has its own word

*(GM ruling, 2026-09-04)*

**Ren-faire.** Modern idiom is in-canon. The players are people playing at
period, the anachronisms are theirs, and they stay verbatim. Do not propose
scrubbing a modern turn of phrase merely for being modern.

**The exception: where a canonical Faerûn word exists for the thing, it wins.**
Not a matter of register — a real-world proper noun for something Faerûn already
names is simply the wrong word. `Monday` → `Firstday`.

**The corollary, and the line that actually did the work this run: the policy
licenses the table, not the narrator.** An anachronism a player said on tape is
covered. One the *narrator* invented is not, because no player chose it and it
was never part of the campaign's voice. Check the smoothed extraction before
proposing — `“Medic!”` was scrubbed on exactly this basis while
`“Monday, Tuesday, Wednesday”` (on tape) was only converted, not cut.

## Calendar

- **Tenday day names are Firstday, Secondday, Thirdday … Tenday.** Adopted
  2026-09-04. The campaign had no calendar before this — `notes/everyone_is_a_suspect.md:352`
  records that no campaign doc sets one. There is still no calendar doc; this is
  the whole of the ruling.
- `“twice on the tenth day”` is kept as spoken.

## Ruled in-canon — never propose these again

| Term | Where | Ruling |
|---|---|---|
| `God's plan` | ch10 sc03 | Keep. Ren-faire. |
| `chunk of change` | ch10 sc05 | Keep. Ren-faire. |
| `keep your eyes peeled` | ch10 sc04 | Keep. Ren-faire. |
| `professional road security` | ch10 sc03 | Keep — it is Pip's established register, in `voice/pip_voice.md`. |
| `“Generous to what?”` | ch10 sc04 | **Keep.** An ASR garble that produced a working mishearing beat; the surrounding lines absorb it in-voice. Closed as *kept*, not outstanding. |

## Classes that ARE residue here

- **Transcript artifacts** — a literal `[unclear]` / `[inaudible]` in finished
  narration is always a candidate.
- **Uncarded ASR garbles** that mean nothing in English (`rough-ins`). Note the
  remedy is a GM choice between recovery and rewrite, and it is not automatic:
  ch10 declined `ruffians` (the likelier recovery) in favour of `marauders`
  (Hamun's own word two lines earlier).
- **Virtual-tabletop and quest-log tooling** narrated as in-fiction dialogue —
  `your pointer`, `quest log`, `question mark`, `you moved us there`,
  `teleport to the quest location`. This is `sd_narrate` failing to reclassify,
  not a register question. Prefer fixing the upstream extraction and re-running
  the scene over hand-excising twenty spans, and **never hand-write a
  `<!-- table-speech reclassified -->` hatch** to cover it.

  **Precedent, ch10 scene 02 (2026-09-04):** where a scene's captured quotes are
  *entirely* mechanical, the ruling is not "scrub the worst spans" but "none of
  this is roleplay" — cut the whole `## Voiced moments` section at the smoothed
  layer with an audit note, and re-run `sd_narrate --scene N` so the scene is
  narrated from its summary bullets alone. That produced a scene with zero
  quoted lines, which was the correct outcome: the party over a map, deciding.
  Check for this shape whenever a scene is planning or logistics rather than
  encounter or conversation.

## Recaps and table mechanics — standing rulings (2026-09-04)

Added during the Chapter 10 `/remove-recap` + `/no-mech` run. None of it is
scannable; this file is the only thing that stops the next run re-asking.

**Recaps are cut by default.** The recording opens with the GM catching the table
up on last time; that belongs to the previous chapter's document, which already
exists. Cut all three surfaces in one pass — the scene, the `## Summary` prose in
`session_summary.md`, and the enhanced-summary file that `sd_narrate` takes as its
recap argument. The scheduling chatter that precedes a recap goes with it.

**Rescue before cutting, always.** A recap can carry canon that cannot exist in
the previous chapter — ch10's recap is where the party learned the sword is named
**Talon**, because the GM read the name aloud and then said "Fine. We now learned
its name." Rescued content goes to the **entity's own record**, not smuggled into
a scene it did not happen in.

**Roll callouts inside roleplay scenes: cut the call and the number, keep the
result.** "Roll an Insight check" and "Fourteen?" go; what the character learns
from it stays. Ruled ch10 sc04/05/07.

**Mechanical rewards and their bookkeeping are cut** — the +1 Investigation
bonus award in ch10 sc03, and the four lines of "make a note of it" that followed.

**But an out-of-character exchange that pays off an in-fiction beat is KEPT.**
Ch10 sc03: the GM denied Daran ever mentioned Netheril, Zenvon's notes proved
otherwise, and the GM conceded — *"Thank you, I think that's why we have the
notes."* That is the payoff to Daran's ten-minute lecture and it stays. The test
is not "is this out of character" but "does cutting it cost a beat".

**Wall-clock and session-scheduling talk is always cut.** "it's almost 7.40",
"we'll continue next week".

**A GM prompt that sets up a character beat is KEPT even though it is mechanically
shaped.** Ch10 sc08: *"Do you want to tell her anything, or just look at her
knowingly?"* produced the best moment in the scene.

## Chapter 11 no-mech rulings (session 011, 2026-09-06)

### Speaker-label signal is dead by campaign convention

Across all seven Chapter 11 scenes, NPC dialogue remains under the `GM` outer
label. The useful identity signal is the italic direction (`as Hamun Kost`, `as
Pip`, and similar), not a distinct NPC speaker label. Future `/no-mech` runs
must never treat `GM` as evidence that a quote is mechanical; classify from the
direction and the full exchange.

### Session-specific scope rulings

- Cut roll calls and numeric roll reports, initiative and damage arithmetic,
  rules lookups and tutorials, character-sheet/VTT operation, level-up and
  spell-selection administration, and session scheduling. Preserve the
  fictional outcome and any character beat that follows.
- Preserve exploration and encounter prompts when they set up an actual choice
  or character response.
- Preserve the pike/bike misunderstanding, praise for the clever illusion plan,
  and the “one glorious point of damage” exchange as table texture.
- Cut the unresolved “second toy” request, the Maela missed-roll exchange,
  “Rolling for attack,” “Almighty God, Master,” and the closing “this was fun”
  exchange. These are exact Chapter 11 rulings, not a blanket rule that all
  player reactions should be cut.
- Keep the Sildar/Ruxithid recollection and the explicit clarification that
  Veyra's blue crystal was not disclosed to Hamun. Though delivered partly as
  table clarification, both protect current-story knowledge boundaries.
