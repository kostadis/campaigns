# Scrub manifest — session 20260825 (Chapter 50)

Produced by `/scrub` on 2026-08-31. Every change below was confirmed by the GM
one candidate at a time (Phase 2). Two things this file exists to record:

1. **These spans deliberately diverge from the VTT.** Any future fidelity or
   consistency check will flag them as transcription errors. They are not.
   They are GM-authored.
2. **Anything invented here is now canon** (`provenance: on_the_fly` — authored
   in narration, not played or prepped).

## GM-authored divergences from the tape

| Scene | Line | Tape / prior narration | Scrubbed | Class |
|---|---|---|---|---|
| 01 | 27 | `"That's not an intimidation."` | `"That was no such thing."` | mechanical (skill-as-noun) |
| 01 | 83 | `spelling bee` | `spelling fairy` | anachronism |
| 01 | 131 | — | one Kostadinious marginal note appended (`"Bimbo"`) | annotation |
| 01 | 139 | `"Aww — when you're here, you're family?"` | `"Aww — a home away from home?"` | anachronism (ad slogan) |
| 02 | 77 | `Oh, God,` | `Oh, gods,` | setting (monotheism) |
| 02 | 93 | `"Stranger's just a friend you haven't met."` | `"A stranger is only a friend the tide hasn't brought in yet."` | anachronism (Will Rogers) |
| 04 | 85 | `at 3 AM.` | `at the third hour after midnight.` | internal consistency |
| 05 | 95 | `Roll for initiative.` | `Draw steel.` | **mechanical (table speech)** |
| 06 | 57 | `listening device` | `listening stone` | anachronism (modern jargon) |
| 06 | 111 | `"You had me at tea,"` | `"The tea alone would have done it,"` | anachronism (Jerry Maguire) |
| 07 | 117 | `the quest tracker!` | `the quest list!` | metagame (game-log tool) |
| 08 | 21 | `a 10 out of 10` | `a ten out of ten` | numeral normalisation |
| 08 | 51 | `"Start a Kickstarter campaign, you know,"` | `"Sell subscriptions, you know,"` | anachronism (named platform) |
| 08 | 141 | `that is where Hollywood,` | `that is where the theatres,` | anachronism (named place) |
| 08 | 271 | `"There's bad beer, there's Bud Light,"` | `"There's bad beer, and there's Common Chord ale,"` | anachronism (brand) |
| 08 | 311 | `Blue Oyster Cult` | `the Nine Hells Chorale` | anachronism (real band) |

## New canon authored in narration (`provenance: on_the_fly`)

- **Kostadinious the Sage** — used as the campaign's marginal-note persona for
  the first time in this session (scene 01, two notes). Established device, per
  the ch3 precedent.
- **"Bimbo" as a Dock Ward coinage** — glossed in the scene 01 note as dockside
  slang for one pleasant to look upon and empty behind the eyes. NOT an alias of
  Bimble Nackle; it is a mishearing/insult, and must not be registered as one.
  The canonical entity remains **Bimble Nackle**.
- **Bingo, the elven fate-game** — players sit at a long table and wait for their
  fates to be called, one at a time, until a life is complete. Scene 01 note.
- **The spelling fairy** — a Faerûnian spelling competition (scene 01 L91).
- **Tortle proverb** — "A stranger is only a friend the tide hasn't brought in
  yet." Soma's coastal idiom (scene 02 L93), consistent with `shell sprout` and
  `shells don't hurry`.
- **Listening stone** — a magic item purchasable in a Neverwinter magic shop
  (scene 06 L57).
- **The Nine Hells Chorale** — a famous band, known well enough that Soma can
  cite its arrangements (scene 08 L311).

## GM rulings on what is NOT residue (do not re-flag)

- **Real-world economics vocabulary is the campaign's central conceit**, not
  anachronism: Vukradin is deliberately importing real-world economic ideas into
  Faerûn, and KP's planar-efficiency project is the same premise from the other
  side. Kept: `fair trade`, `organic`, `farm-to-table`, `locally sourced`,
  `supply chain`, `marketing`/`advertising`, `revenue share`, `front-end points`,
  `net`/`gross`, `image and likeness`, `perpetuity`, `pre-orders`, `merchandise`.
- **`cosplaying` is an in-canon word** (GM ruling). s04 L27/L29, s08 L53.
- Kept comedic references: the `#NotAllMen` were-rats bit (s06 L65–71), `Yoko`
  (s07 L57/59/63), the Matrix `deja vu`/cat (s07 L67–69), the Godfather line
  (s05 L35), `Always be closing` (s08 L43–45), `more cowbell`/`heavy metal`
  (s08 L309/313), `Pearls before swine` (s08 L281), `avant-garde` (s08 L207),
  `Hammock District` (s03 L25), `Blue Light`/`Red light` (s03 L11–15).
- The line the GM drew: **named real-world entities go** (a platform, a place,
  a brand, a band); **economic ideas stay**.

## Notes

- Scene 03 was reviewed and produced **no** `.scrubbed.md` — every candidate was
  ruled keep. This is correct; `assemble.py` falls back to the raw file per scene.
- The only scanner-generated candidate all session (s03 L109, `I have one`) was a
  false positive and was rejected per-instance. It was deliberately NOT written to
  the campaign ignore list — the fragment is too generic and would have disabled
  roll-result detection campaign-wide.
- `--party-md` loaded only 3 of 4 players; Stéphane Bourdeaud's roster line in
  `docs/party.md` lacks the `Player:` prefix that `load_player_names` requires,
  so the player with 204 cues was invisible to `player_name` detection. All four
  real names were checked by hand across the narration — none present.

## Amendment — scene 01 re-narrated on fable, 2026-08-31

Scene 01 was **re-rendered and re-scrubbed** after the voice critique found it
was the one scene of the eight that did not narrate (27% narration prose against
a 52–67% band; ~40 consecutive untagged quoted lines).

**Cause, from the run logs:** the GM tried `--backend codex-cli` on scenes 01, 02
and 03, switched to `--backend claude-code --model claude-fable-5`, and re-ran
02–08 — but never went back for 01. The surviving file was a leftover from the
abandoned attempt.

**What was re-run** — the scene-02 invocation with scene 01's parameters, identical
in every other argument (`--party`, `--party-config`, `--players-config`,
`--voice-dir`, `--examples`, `--narrate-tokens 32000`, `--prose-mode`,
`--reflections`, `--narration-genre-file`):

```
sd_narrate … --scene 1 \
  --scene-extraction-file …/scene_extractions_smoothed/01_a_banker_s_revelation.md \
  --backend claude-code --model claude-fable-5
```

**Result:** narration prose 244 → 477 words (31% → 51%); quoted lines 66 → 52;
attributed quoted lines 0 → 26.

**The codex-cli render is preserved** beside the new one as
`session_doc_scene_01_a_banker_s_revelation.{md,scrubbed.md,knobs.json}.codex-cli.bak`.
None of those names match the `session_doc_scene_*.md` glob, so `assemble.py`
cannot pick them up.

### Two provenance notes

- **`sd_narrate` does not write the `.knobs.json` sidecar — the editor does**
  (`server/routers/scene_editor.py::_knobs_snapshot`). A CLI render therefore
  leaves whatever the editor last wrote. Scene 01's sidecar still read
  `"backend": "codex-cli"` after the fable render; it has been corrected by hand
  to `claude-code`. Any future CLI-driven re-render has the same trap.
- **The knobs schema has no `model` field at all.** It records `backend` from
  `cfg.backends.active` and nothing else about the model, so *no* scene in this
  session records that it ran on `claude-fable-5` — that fact exists only in
  `logs/2026-08-30_*_sd_narrate.md` and here.

### Scrub decisions on the re-render (GM-confirmed 2026-08-31, one at a time)

The fable pass restored three spans from the tape that the first scrub had
already ruled on. All three rulings were re-confirmed unchanged. Scanner output
was **0 candidates**, as on the first pass — every finding came from reading.

| Line | From | To | Class |
|---|---|---|---|
| 27 | `"That's not an intimidation."` | `"That was no such thing."` | mechanical (skill-as-noun) |
| 83 | `spelling bee` | `spelling fairy` | anachronism |
| 139 | `"…when you're here, you're family?"` | `"…a home away from home?"` | anachronism (Olive Garden slogan) |
| 131 | — | the `"Bimbo"` marginal note, re-added | annotation |

**The `Bingo` marginal note was NOT re-added.** The fable render drops the word
`Bingo` entirely, so the note would have glossed a term the scene never uses. The
canon it established — *Bingo, the elven fate-game* — **remains valid and logged
above**; it simply has no anchor in this scene any more. The `"Bimbo"` note was
kept because that word still appears five times.

One note rather than two also sits better with the skill's "a spice, not a
default" rule.
