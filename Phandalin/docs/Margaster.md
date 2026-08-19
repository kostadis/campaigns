# House Margaster — knowledge boundary and dossier

**Hand-authored. Not a pipeline output — do not regenerate.** Created 2026-08-15 during the
ch48 `/voice-smooth` pass. Lives at `docs/` top level per `Phandalin/CLAUDE.md`, because the
generated grounding docs (`world_state.md`, `campaign_state.md`, `planning.md`, `party.md`)
are clobbered on every pipeline run.

## WHAT THE PARTY ACTUALLY KNOWS (GM ruling 2026-08-15, as of ch48)

| | Witnessed extortion & forgery | Suspects Margaster sabotaged the manifold | Knows Margaster are **cambion-blooded** |
|---|---|---|---|
| **The party (in-fiction)** | **Yes** | **Yes — as a hypothesis, this session** | **No** |
| **Vukradin (character)** | Yes | Yes — he spelled the hypothesis out | **No** |
| **Soma (character)** | Yes | Yes | **No** |
| **Valphine (character)** | Yes | Yes | **No** |
| **Brewbarry (character)** | Yes | Yes — "No shit, Sherlock" | **No** |
| **Wade, Gary (players, out-of-fiction)** | — | — | **Yes**, from a different adventure |

### The rule

The cambion connection to House Margaster is **player knowledge carried in from another
adventure**. No character in this campaign has encountered it, been told it, or deduced it.

Two lines in ch48 say the word out loud, and both are out-of-character table talk:

- **Soma** — *"Were they Cambions?"* (`scene_extractions/04_the_margaster_hypothesis.md`)
- **Valphine** — *"Yeah, they're, they're, they're Cambions."* (same scene)

Both are captured in the transcript under the characters' labels, because the VTT labels by
speaker and cannot distinguish IC from OOC. **They are not in-fiction claims.**

**Do not narrate any character as suspecting, asserting, or acting on House Margaster having
fiendish blood.** If the party is to learn it, that is a scene yet to be played.

Transcription note: Zoom captured the word as `Cambians` both times; the re-transcription
heard the second one as `Kenyans`. Canonical spelling for the creature is **cambion**.

### A third leak — and it was the GM's own line (ruling 2026-08-16, ch48 stage 3)

The two lines above are players talking over the table. The third is not, which is why it
survived every earlier pass: **the GM said it, in character, while narrating an investigation
result.**

Tape (Zoom l.1055–1056), the GM delivering what Valphine's search of the notary house turns up:

> "It is, in fact, just a notary. It doesn't have any of the usual, you know.
> Margaster, you know, **demonic**…"

It reached `scene_extractions/06` L85 as a verbatim GM quote and rendered in the ch48 narration
as *"No hidden sigils, no **demonic trappings**, none of the usual Margaster stink on the
premises."*

**GM ruling: this was a slip**, spoken minutes after the players' out-of-character cambion riff
in the same session, and it does not create character knowledge. The narration was corrected to
*"No hidden sigils, no forger's back room, none of the stink of the writ racket on the
premises"* — extortion and forgery being what the party has actually witnessed.

**The reusable lesson is the shape of the leak.** A line describing what an investigation did
**not** find still asserts what the searcher was *looking for*. "No demonic trappings" puts the
expectation of demonic trappings inside the character's head just as surely as finding them
would. So the rule above extends:

> Do not narrate any character as suspecting, asserting, acting on, **or scanning for** House
> Margaster having fiendish blood — including in the negative.

Note also that `check_consistency.py` flagged this correctly but for the wrong reason: it cited
this file and called it a narration error, having never read the tape. The narration was
faithfully rendering a GM line. Only the tape shows that the *source* was the thing to rule on.

### Why this file exists

This is the second player-vs-character knowledge boundary found in ch48. The first — Dave
knowing who KP is while Vukradin does not — is recorded the same way in [`KP.md`](KP.md).
Both were caught only because a human read the transcript against the characters' actual
information state; neither is visible to `check_consistency.py`, which has no model of who
knows what.

## What the party DOES know about House Margaster (in-fiction, as of ch48)

- They extorted the rightful owner of the lighthouse statue — **witnessed firsthand**
  (the Elara Seasong Meliamne quest, crossed out as complete in the shared quest journal).
- They extorted money out of Elara's brother — witnessed.
- Forgery — witnessed.
- They made an offer to Vukradin as "a more efficient redistributor of lost goods."
- They have the cheapest distribution network in Neverwinter right now. **The banker
  volunteered this; it was not a Margaster approach to Brewbarry** — the GM corrected the
  party's recollection on exactly this point during the scene.
- The Commission's displacement manifold went dark some time ago, and Lionshield Coster
  shipping costs rose sharply as a result.
- **Hypothesis formed this session (not confirmed):** Margaster sabotaged the manifold to
  knock out a competitor and monopolize shipping.
- Ser Kaelen warned Vukradin to stay away from them.
- **Out of character**, the GM confirmed to the table that House Margaster is a recurring
  villain across these campaigns. The characters did not hear this.

## Open threads

- Aurelan Vance promised to make inquiries into House Margaster **by the next day** (ch48).
- The party resolved to visit House Margaster to intimidate, not attack — Brewbarry's
  barbarian principle: "I let my enemy know that I am there."
- Registry: `docs/entity_registry.yaml` has House Margaster as a faction — noble house that
  filled the distribution gap after the Manifold went dark, connected to the Commission's
  Harbor authority, killed Elara.
