# Scrub manifest — 20260902 narration3

Run approved by the GM on 2026-09-06 using batch review. The five scenes selected
by `narration3/plan.md` were scrubbed; the unselected alternate renders for scenes
01 and 05 were not part of the effective narration set.

## GM-authored divergences

These changes deliberately diverge from the tape and must not be reverted by a
later fidelity pass.

| Scene | Line | Tape / source text | Scrubbed text | Class |
|---|---:|---|---|---|
| 01 | 29 | `keeps it on the DL` | `keeps it discreet` | modern phrasing |
| 01 | 39 | `keeps it on the DL` | `keeps it discreet` | modern phrasing |
| 01 | 41 | `double entendres in these modules` | `double entendres in these noble names` | out-of-fiction reference |
| 01 | 103 | `by 3 AM` | `by the third hour after midnight` | Faerûn time register |
| 01 | 129 | `Awesome, there's a GoFundMe…` | `Excellent. We need a patronage purse ordinary people can reach.` | named modern platform |
| 01 | 131 | `QR code, Venmo account` | `Sending-stone pledges, temple drafts, portal transfers` | modern technology and named platform |
| 01 | 133 | `the obvious Faerun equivalent` | `the obvious Faerûnian answer` | table-facing phrasing |
| 01 | 135 | `All the Faerun equivalents` | `All the local equivalents` | table-facing phrasing |
| 01 | 137 | `Google Pay, Apple Pay, Portal Pay` | `coin, temple drafts, or portal transfers` | named modern platforms |
| 01 | 181 | `Jesus` | `Gods` | named real-world reference |
| 01 | 211 | `3 AM` | `The third hour after midnight` | Faerûn time register |
| 01 | 237 | `10 gold pieces` | `Ten gold pieces` | numeric money dialogue |
| 01 | 245 | `10 gold` | `Ten gold` | numeric money dialogue |
| 01 | 259 | `Patreon` | `patronage` | named modern platform |
| 01 | 261 | `Patreon` | `patronage` | named modern platform |
| 01 | 285 | `huge in Japan sometimes` | `famous from here to Kara-Tur` | named real-world place |
| 02 | 9 | `I have a very high stealth` | `I can move very quietly` | character-sheet talk |
| 02 | 17 | `I have an actual character` | `I have actual training` | player-level speech |
| 02 | 21 | `bards got high stealth` | `bards moved that quietly` | character-sheet talk |
| 02 | 23 | `it's just because I have boots of elvenkind` | `It's the Boots of Elvenkind` | character-sheet talk; magic item retained |
| 02 | 29 | `within one hundred feet` | `within reach of her magic` | numeric spell-range residue |
| 02 | 49 | `you said you got your high stealth` | `You said you were the quiet one` | character-sheet talk |
| 02 | 133 | `Only a 1 in 400 chance of disaster` | `The chance of disaster is negligible` | numeric table joke |
| 02 | 149 | `little walkie-talkies` | `speak back and forth through them` | modern technology |
| 02 | 151 | `We have walkie-talkies` | `We have Sending Stones` | modern technology |
| 02 | 173 | `doesn't seem kosher` | `doesn't seem wise` | real-world cultural reference |
| 03 | 43 | `left at Albuquerque` | `left at Leilon` | named real-world place |
| 03 | 97 | `applause or the sale of records` | `applause or a crowded hall` | modern technology |
| 04 | 11 | `dinner at 4 a.m.` | `dinner at the fourth hour after midnight` | Faerûn time register |
| 04 | 113 | `has entered the chat` | `has joined us` | modern technology |
| 04 | 187 | `Denvar, Colorado` | `Denvar, Daggerford` | named real-world place |
| 04 | 205 | `weekly settlements` | `settlements at each tenday's end` | Faerûn calendar register |
| 04 | 295 | `the Jesse Jackson of turtles` | `the Open Lord of turtles` | named real-world person |
| 05 | 15 | `local wererat mafia` | `local wererat gang` | modern phrasing |
| 05 | 33 | `two-way doctor's-office window` | `two-way moneylender's counter hatch` | modern analogy |
| 05 | 117 | `It is five o'clock somewhere` | `It is drinking hour somewhere` | modern table joke |
| 05 | 119 | `clock somewhere` | `Somewhere` | coupled callback repair |
| 05 | 163 | `Porque no los dos` | `Why not both?` | real-world language reference |
| 05 | 281 | `Truth, justice, and the American Way` | `Truth, justice, and the Neverwintan way` | named real-world reference |

## New canon (`provenance: on_the_fly`)

None. Kara-Tur, Leilon, Daggerford, Sending Stones, and the Open Lord are
pre-existing setting references. The remaining replacements are ordinary
descriptions rather than new proper nouns, institutions, or aliases.

## GM rulings on what is NOT residue

- `passive charm` is an in-world description of a magical effect, not a roll
  callout. Keep it; the exact phrase is protected in `notes/.scrub_state.json`.
- `passive confusion` is an in-world description of a magical effect, not a
  roll callout. Keep it; the exact phrase is protected in
  `notes/.scrub_state.json`.
- Existing campaign rulings continue to protect imported economics,
  adventuring vocabulary, spell names, magic vocabulary, and relaxed modern
  idiom that names neither modern technology nor a real-world entity.

## Notes

- Deterministic scan: three candidates. One accepted rewrite (`one hundred
  feet`) and two protected magical-effect false positives.
- Full-scene reading supplied the remaining accepted changes, including the
  cross-scene modern-register census.
- Post-apply deterministic scan: zero candidates in all five scrubbed scenes.
- All 39 exact line decisions applied successfully. Neighbouring paragraphs
  were reread for stranded grammar, pronouns, and callbacks; no follow-up edit
  was required.
- `docs/party.md` loaded David Mendenhall, Gary Young, and Wade Brown. Its
  Stéphane Bourdeaud roster line lacks the literal `Player:` marker and remains
  invisible to the scanner; the narration eligibility record marks him absent
  from this session, and a manual name search found no participant-name leak in
  the five selected scenes.
- No pass-through `.scrubbed.md` files were created for the two unselected
  alternate renders.
