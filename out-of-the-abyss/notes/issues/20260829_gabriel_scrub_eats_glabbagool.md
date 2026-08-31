# ISSUE — the `Gabriel → Zalthir` player-name scrub silently eats Glabbagool

**Status: OPEN.** Filed 2026-08-29 from the `/staged-consistency` re-run on
`summaries/20260809` (Chapter 63). GM approved filing it.

## The collision

Zoom's ASR renders **Glabbagool** as **"Gabriel"** — one of dozens of garbles it
produces for that name. "Gabriel" is also the real first name of Zalthir's player.

`notes/vtt_transcription_corrections.md:236` carries the player-name scrub:

| Wrong | Right |
|---|---|
| Gabriel Tarasuk-Levin, Gabriel, Gabe | **Zalthir** |

Longest-first ordering means a bare **"Gabriel"** is claimed by the player scrub
before anything else can look at it. The `Glabbagool` row (line 24) has a
`Gabriel Ghoul` variant, but nothing for `Gabriel` alone — so every in-text
"Gabriel" becomes "Zalthir", whether it meant the player or the ooze.

## What it did to Chapter 63

Three in-text hits in `summaries/20260809`, all silently rewritten in the
cleaned VTT. Raw line numbers, `GMT20260804-005646_Recording.transcript.vtt`:

| Raw | ASR text | Cleaned as | Should be |
|---|---|---|---|
| `:3491` | Joe Beda: "I don't know, we should find out, Gabriel." | "…find out, **Zalthir**" | **Glabbagool** |
| `:3711` | Daz: "sticking in the middle of **Gabriel**" | "…middle of **Zalthir**" | **Glabbagool** |
| `:3767` | Gabriel Tarasuk-Levin: "You mean **Gabriel**?" | "You mean **Zalthir**?" | **Glabbagool** |

`:3711` is settled by the GM's own next cue — *"Glabbagool, I mean, as long as
Glabbagool… somebody tells Glabbagool to not talk about it."* `:3767` is settled
by the GM's answer — *"Yeah, yeah, Glabbagool, sorry"* — which only parses as a
self-correction if the player asked about Glabbagool.

**`:3491` was settled 2026-08-29 by the sibling transcript.** It sits inside the
Glabbagool-eats-the-wizard exchange (Thorin: *"Can we, like, let Glabbagool have
his way with him?"* → GM as Glabbagool: *"do they dissolve like other people?"* →
Thorin: *"I don't know, we should find out, Gabriel."*), and read either as Thorin
addressing the ooze in fiction or as Thorin addressing Gabe out of character. The
independent transcription `session_20260809_transcript.vtt` at `01:28:39.139`
renders it *"We should find out, **Glabbagool**."* — **so all three hits are the
ooze, not the player.** Corrected in
`scene_extractions/02_the_surrender_and_ambush.md:487`.

**The general lesson:** the sibling speakerless transcript is the cheapest way to
break this specific tie, because it has no speaker-name scrub applied to it at
all — the collision cannot occur there. Check it before asking the GM.

## Why the glossary already knowing this was not enough

`vtt_transcription_corrections.md:344–347` diagnosed exactly this ordering
problem during the 20260824 pass, for the string `Gabriel Ghoul`. The fix that
was applied was a row for that *compound* form. A bare "Gabriel" was left
uncovered, so the failure recurred one session earlier in the archive without
anyone noticing.

## Why it is worth a standing note

The rewrite is **invisible downstream**. "Zalthir" is a real PC name, so it
reads as ordinary text in every derived document — nothing flags it, and the
`verify_quotes.py` sweep passes it because the cleaned VTT *is* the corpus it
checks against. It surfaced this run only because the sentence it produced
("hiding the key inside Glabbagool… Daz: sticking in the middle of Zalthir")
contradicted itself in a single bullet.

## Options, none applied

The GM has not chosen a fix; this note only records the trap.

1. **Do nothing** — catch it per-session as targeted edits, as 08-19 and this
   run both did. Cheapest, and it has now failed to hold twice.
2. **Order the glossary so Glabbagool wins** — risks the opposite error, since
   the players do address Gabe by name at the table.
3. **Scrub player names last**, after every entity row has run. Structural, and
   would need a change wherever the spell pass orders its replacements.
4. **Never auto-scrub a bare first name that collides with an entity garble** —
   flag it for review instead of substituting.

## Cross-references

- `notes/vtt_transcription_corrections.md:24` — the Glabbagool wrong-form row
- `notes/vtt_transcription_corrections.md:236` — the player-name scrub
- `notes/vtt_transcription_corrections.md:344–347` — the 20260824 diagnosis
- `notes/vtt_transcription_corrections.md:469–473` — the 08-19 targeted edits,
  including *"sticking in the middle of Zalthir" → **Glabbagool***, which was
  ruled and logged but never applied to `session-summary.md` until this run
