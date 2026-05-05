# VTT transcription corrections — campaign name glossary

Misspellings found in Zoom/Otter VTT transcripts and the canonical
forms they should be corrected to. Use this as a reference for
future VTT cleanup passes.

First catalogued during the cleanup of
`summaries/20260427/GMT20260428-005729_Recording.transcript.vtt`.

## PCs

| Wrong | Right |
|---|---|
| Zaltir, Zalter, Zaltier, Zeltar | **Zalthir** |
| Gergam, Gregam, Greg, Grigam | **Grygum** |
| Thorne, Thornton, Thurren, Or Torin | **Thorin** |
| Adaz, Das, Dez, Dazz, Jazz | **Daz** |

## NPCs and creatures

| Wrong | Right |
|---|---|
| Glavagul, Glavagul's, Glabogul, Glavo, Glavacle, Glavable, Glavigal, Glavagol, Glabagul, Glabigle, Lavagul, Lavagul's, Miklabogul, Globul, Globagool, Gobblegool, Glabugul, Gladbagul, Globagul, Glabagool | **Glabbagool** |
| Jam Jar, Jim Jar | **Jimjar** |
| Kel'Vire, Kel Vire, Calvir, Kel Veer | **Khell-Vire** |
| Asha Vandri, Ashe Vandri, Ashas | **Asha Vandree** |
| Elvara, Olvara | **Ilvara** |
| Ebum Mir's, Ebum Mir, Ebonir, Princess Ebonir, Ebonheir, Princess Ebonheir | **Ebonmire** (Princess Ebonmire) |
| Muhammed, Buhammad's, Buhammad, Bahamad, Muhammad, Baham, Baumont | **Bahamut** |
| Melfire | **Malfire** |
| Zuggtomy, Zugtmoy, Zugtomy, Zuggotmoy, Zugatami, Sugadami, Zagotami | **Zuggtmoy** (confirmed via 5etools: MTF + OotA) |
| Plinky,Plenke | **Plinki** |
| Loth | **Lolth** |
| Lawthans | **Lolthians** |
| Lister | **Whistler** |
| Ardagorn, Artagon | **Ardragon** |
| Goodbarrell | **Goodbarrel** |
| Protanthor | **Protanther** |
| Straub | **Stroud** |
| Kessler | **Kestler** |
| Stroudian | **Stroudite** |
| Stroudians | **Stroudites** |
| Eldith, Aldath | **Eldeth** |
| Bahamian, Bahamatian | **Bahamutian** |
| Rishal | **Rishaal** |

## Items / artifacts

| Wrong | Right |
|---|---|
| Don Bringer, John Brenner, Dawn, Von Wigger | **Dawnbringer** |
| Vault Master | **Vaultmaster** |

## Houses / factions

| Wrong | Right |
|---|---|
| House Terran, Terran, House Turan, House Tsaran | **House T'sarran** |
| Embryograph | **Ember Grapple** (alt. name for the party) |
| Blatwork | **Black Network** |
| Zantarum | **Zhentarim** |
| Uthgart, Utgartian | **Uthgardt** |

## Locations

| Wrong | Right |
|---|---|
| Vulking Valve, Velcan-developed | **Velkynvelve** |
| Whirlstone | **Whorlstone** |
| Candle Keep, Candleep | **Candlekeep** |
| Mithril Hall | **Mithral Hall** |
| Whirlstone Caverns | **Whorlstone Caverns** |
| Castle Candlekeep | **Candlekeep Library** |
| Revil | **Toril** |
| Tribor | **Triboar** |
| Waterdeeps | **Waterdeep** |
| Silvery Marches | **Silver Marches** |
| Blindenson, Blingdonston | **Blingdenstone** |
| Sunbar | **Sundabar** |
| Ferrun | **Faerûn** |
| Mountain Mouth | **Mountain's Mouth** |
| The Night Beneath the Night | **The Knight Beneath the Knight** |
| Page Turners | **Pageturner** |
| And Richel | **and Rishaal** |
| Bahamut Stride | **Bahamut shrine** |
| Tempest Shrine, Defaced Tempest Shrine | **Tempus shrine** |
| North Sword Coast | **Northern Sword Coast** |

## Races / mechanics

| Wrong | Right |
|---|---|
| half-pork, Hawthorcs | **half-orc** |
| Dro, Drau | **Drow** |
| Lecanthropy | **lycanthropy** |
| Faye | **Fey** |

## Real-world / table

| Wrong | Right |
|---|---|
| costatis, Stottis, Kostat, Castadas, Costatas, Casados, Cristonis, Quesada, Costatus | **Kostadis** (pronounced "koh-stAH-dis", rhymes loosely with "toh-STA-dah") |

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

## Phrase fixes

| Wrong | Right |
|---|---|
| Braun Stroud bus | **bronze Stroud-bust** |
