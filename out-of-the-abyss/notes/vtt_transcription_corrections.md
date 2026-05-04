# VTT transcription corrections — campaign name glossary

Misspellings found in Zoom/Otter VTT transcripts and the canonical
forms they should be corrected to. Use this as a reference for
future VTT cleanup passes.

First catalogued during the cleanup of
`summaries/20260427/GMT20260428-005729_Recording.transcript.vtt`.

## PCs

| Wrong | Right |
|---|---|
| Zaltir, Zalter, Zaltier | **Zalthir** |
| Gergam, Gregam, Greg | **Grygum** |
| Thorne, Thornton | **Thorin** |
| Adaz, Das, Dez | **Daz** |

## NPCs and creatures

| Wrong | Right |
|---|---|
| Glavagul, Glavagul's, Glabogul, Glavo, Glavacle, Glavable, Glavigal, Glavagol, Glabagul, Glabigle, Lavagul, Lavagul's, Miklabogul, Globul, Globagool, Gobblegool | **Glabbagool** |
| Jam Jar, Jim Jar | **Jimjar** |
| Kel'Vire, Kel Vire | **Khell-Vire** |
| Asha Vandri, Ashe Vandri, Ashas | **Asha Vandree** |
| Elvara, Olvara | **Ilvara** |
| Ebum Mir's, Ebum Mir, Ebonir, Princess Ebonir, Ebonheir, Princess Ebonheir | **Ebonmire** (Princess Ebonmire) |
| Muhammed, Buhammad's, Buhammad, Bahamad, Muhammad | **Bahamut** |
| Melfire | **Malfire** |
| Zuggtomy, Zugtmoy, Zugtomy, Zuggotmoy, Zugatami, Sugadami, Zagotami | **Zuggtmoy** (confirmed via 5etools: MTF + OotA) |
| Plinky,Plenke | **Plinki** |
| Loth | **Lolth** |
| Lawthans | **Lolthians** |

## Items / artifacts

| Wrong | Right |
|---|---|
| Don Bringer, John Brenner, Dawn | **Dawnbringer** |

## Houses / factions

| Wrong | Right |
|---|---|
| House Terran, Terran, House Turan, House Tsaran | **House T'sarran** |
| Embryograph | **Ember Grapple** (alt. name for the party) |

## Locations

| Wrong | Right |
|---|---|
| Vulking Valve, Velcan-developed | **Velkynvelve** |
| Whirlstone | **Whorlstone** |
| Candle Keep | **Candlekeep** |
| Mithril Hall | **Mithral Hall** |
| Whirlstone Caverns | **Whorlstone Caverns** |
| Castle Candlekeep | **Candlekeep Library** |
| Revil | **Toril** |

## Races / mechanics

| Wrong | Right |
|---|---|
| half-pork | **half-orc** |
| Dro | **Drow** |

## Real-world / table

| Wrong | Right |
|---|---|
| costatis, Stottis, Kostat, Castadas, Costatas, Casados, Cristonis | **Kostadis** (pronounced "koh-stAH-dis", rhymes loosely with "toh-STA-dah") |

## Non-name fixes (recorded for context, not a glossary entry)

- "Marie" stray word in "Yeah, Marie, Glabbagool" — removed (transcription artifact, no NPC by that name).
- "Melba" in "the Kostadis is Melba" — corrected to "mellow" (table-chatter mishearing).
- "taught San to think" — corrected to "taught sand to think" (the "we taught sand to think" meme; not a campaign name).

## Notes for future passes

- **Stroud** transcribes correctly. Don't auto-correct it.
- **Eldeth** transcribes correctly.
- Speaker labels at line starts (e.g. `Thorin (Joe):`) are stable; mistranscriptions appear inside dialogue, not labels.
- Whisper-style transcribers tend to anglicize fantasy names into English/proper nouns (Thorin → Thorne/Thornton, Dawnbringer → Don Bringer, T'sarran → Terran). Grep for the anglicized forms before each cleanup.
- Possessive `'s` can be lost in regex replacement when a variant is matched as `Name's` and replaced with bare `Name` — eyeball the diff after a sweep.
