# VTT transcription corrections — obelisk

**Single source of truth** for Zoom/Otter/Whisper proper-noun garbles in this
campaign's session transcripts. Wrong→right; the canonical (right) is **bolded**.

- The `vtt-spell-pass` skill reads and appends here
  (`add_to_glossary.py --glossary notes/vtt_transcription_corrections.md`).
- `docs/ensemble/aliases.json` is **generated** from this file (plus the
  bundling-only short forms in `docs/ensemble/build_aliases.py`) — never hand-edit
  aliases.json; re-run the generator.
- This file holds **only true garbles** — forms that are safe to substitute into
  transcript text. Entity short-forms, titles, and player→character mappings
  (e.g. `Sildar`→`Sildar Hallwinter`, `Nikhil Reddy`→`Zenvon`) must **not** be
  substituted into text (the word-boundary applier would double-expand them), so
  they live in the generator's `BUNDLING_ALIASES`, not here.

Canonical spellings are verified against `docs/background/name_glossary.md` and `characters/`.

## PCs

| Wrong | Right |
|---|---|
| Xenophon, Xenobon, Zenovon, Xenovon, Xenomon, Cinnamon, Zenomon, Zenon, Zenotic, Zenovan, Xenovan, Xenowalt, Zalthir, Zalthamir, Zenbon, Xenobod, Zen Von, Xenobun, Xenoons, Zanoan, Zenmon, Zenoven, Zenvan, Zenobun | **Zenvon** |
| Zenoan | **Zenvon** (session 5: more ASR variant of the PC "Zenvon") |
| Zanabon, Zenimon, Xenob | **Zenvon** (session 7: more ASR variants of the PC "Zenvon") |
| Foreput, Forput, Forepaw | **Forepot** (surname of the PC Zenvon; canonical per GM ruling 2026-08-03 — every other spelling is a misspelling, including the one that was in `name_glossary.md`) |
| Vera, Azvera, Rivera, Maya, Maia, Zerabira, Bera, Zira, Zvera, Vena, Farrah, Barah, Avera, Bayraz, Vaira | **Veyra** |
| Sister Vera | **Veyra** (session 5: ASR gave Veyra the cleric's title. The applier sorts longest-first, so this beats the bare "Vera" row and yields "Veyra", not "Sister Veyra") |
| Sister Mela, Mela, Mila, Myla, Mil, Myra, Nela, Mele, Sister Bela, Sister Meela, Sturmela, Sister Mele, Tell Sister Meila, Sister Neela, Sister Vayle, Sister Vela, Sister Maella, Sister Mala, Sister Merla, Stormylla, Sister Melis | **Sister Maela** (session 7: "Mila"/"Myla"/"Mil" also = Maela, the Turn-Undead cleric) |
| sister male | **Sister Maela** (session 7: ASR split the name into two real words — safe because the two-word sequence never occurs legitimately) |
| veera | **Veyra** (session 7: doubled-vowel variant, cf. the "Vera" row) |
| Foreput | **Forepot** (session 8 rule REVERSED 2026-08-21: the D&D Beyond sheet spells the surname "Forepot", so the corpus was corrected to match and this row now runs the other way — it exists to undo the old rule's output in already-cleaned VTTs) |
| Neela,Neila,Neera,Mayla | **Maela** (session 8) |

## NPCs and creatures

| Wrong | Right |
|---|---|
| Clarg | **Klarg** |
| Glastaff, Glass Staff, Glassdaff, Glass Tap, Glastap, Glassstaff, Blast Staff, Gastav, Blackstaff, Blastaff, Glassap, Lasa, Glastath | **Glasstaff** (session 4: "Clarg"→Klarg; session 5/7: two-word "glass staff" / "Glassdaff" / "Glass Tap" = Glasstaff, Iarno Albrek's alias) |
| Toblin, Hoblin, Talbot, Poglin, Stoblin, Tobel, Tobin | **Toblen** |
| Tobelin, Tublin | **Toblen** (session 4: more ASR variants of "Toblen Stonehill") |
| Glastaff | **Glasstaff** |
| Darren Edermeth | **Daran Edermath** |
| Oren Voss, Orrin Voss | **Orryn Voss** |
| Ruth exceeds | **Ruxithid** (garbled whispered name in "You're not what Ruxithid wants") |
| Soldar, Siddhar, Solgar, Syldar, Soldora, Sildur | **Sildar** (session 4: ASR garbles of "Sildar Hallwinter") |
| Silar, Silvar | **Sildar** (session 4: ASR garbles of "Sildar" — verify vs. other names) |
| Gundran, Gundrin, Gundrum, Gundrun, Gundrund, Wundren | **Gundren** (session 4: ASR garbles of "Gundren Rockseeker") |
| Goodrin, Dundrum | **Gundren** (session 4: more ASR variants of "Gundren") |
| Gunther, Kissandar | **Gundren** (session 5: only these two are Gundren — "Gunther" = Sildar's old mentor; "Kissandar miner" = the Wave Echo Cave miner. All other Rondar/Rudar/Randar/Rondor/Rundar/Rondart/Brandar/Gundrid are the NPC Rondar, NOT Gundren) |
| Thardin | **Tharden** (session 4: Rockseeker brother "Tharden") |
| Barthin | **Barthen** (session 4: "Barthin's prov[isions]" = Elmina Barthen's shop) |
| Linen Lanain | **Linene Graywind** (session 4: "Linen Lanain … Lionshield coster" = Linene Graywind; both tokens garbled) |
| Linen, Lanain | **Linene** (session 4: single-token garbles of "Linene") |
| Yarno, Yorno, Jano, Yano, Jarno, Vekov, Evoko, Yarna, Jarl | **Iarno** (session 4: ASR garbles of "Iarno Albrek"/Glasstaff) |
| Quip | **Pip** (session 4: Nikhil's sidekick Pip, ASR garble) |
| Pimp, Pippa, Pips | **Pip** (session 7: more ASR garbles of the sidekick "Pip") |
| Albrecht, Albright | **Albrek** (session 4: "Jarno/Larno Albrecht" = Iarno Albrek) |
| Ruxothid, Ruxathid | **Ruxithid** (session 4: Veyra repeating the goblin's name) |
| Melavera | **Veyra** (session 4: fused "Maela"+"Veyra" garble of the tiefling) |
| Xinavan | **Zenvon** (session 4: more ASR variant of the PC "Zenvon") |
| Dendars, The Ten Doves | **Dendrars** (session 7: variant of the Dendrar family, cf. session 1 "Dendar") |
| Dendar, Dendra, Dandrar, Drendrar | **Dendrar** (session 1: ASR mishearing of the family name. Moved here from `docs/entity_registry.yaml` on 2026-08-01 — garbles are transcription errors, not identity aliases, so they belong in this glossary and never in the registry) |
| Tell Dendar | **Thel Dendrar** (early session: ASR heard "Thel" as "Tell", cf. the "Tell Sister Meila" row. Evidenced by a `docs/ensemble/merged.json` source_quote; that session's VTT is not retained. Longest-first ordering makes this beat the bare "Dendar" row) |
| Dessa | **Dosa Rook** (session 7: Redbrand-handled bandit, full name confirmed from retranscription) |
| Black Sparta, Black Jeff, Black Spire, Blackspur | **Black Spider** (Nezznar's known alias) |
| Karimi, Redbrand Moravian, Redbrand Muffian, Redbrand muffin | **Redbrand Ruffian** |
| Rhondar, Prandar, Rudar, Randar, Rondor, Brandar, Randa, Randor, Rhonda, Rondart, Rundar, Gundrid, Arnold, Brandor | **Rondar** |
| Gnothic, Gnostic | **Nothic** |
| Orman, Bormann, Ormon, Urman | **Urmon** (session 6: "Urman" added 2026-08-01 — journal-author NPC) |
| Dvarvish | **Dwarvish** |
| Carbon Wester,Harbren Wester,Pardman Wester | **Harbin Wester** (session 5: ASR garbles of the townmaster's first name, correct surname retained) |
| Iarno Ulbrecht,Larno Albrek,Giano Albrand | **Iarno Albrek** (session 5: ASR garbles of Glasstaff's real name) |
| Harvin | **Harbin** (session 5: bare first-name garble, paired with the Harbin Wester row) |
| Holly, Talia, Aalia, Alia | **Halia** (session 5: DM pulling up Halia Thornton's notes, ASR garble) |
| Red Brad Muffin Ruffians | **Redbrand Ruffians** (session 5: Halia's 'shocked, shocked' line, 4-word garble not caught by the 2-word 'Redbrand muffin' rule) |
| Bogenistel, Bogentle, Bo Gentle, Bao Gentle, Bow Gentle | **Bowgentle** (session 8) |
| Dru | **Droop** (session 8) |
| Breda | **Freda** (session 8) |
| Lord's Alliance | **Lords' Alliance** (session 8) |
| Namira Drendra | **Mirna Dendrar** (session 8) |
| Gnart,Nark | **Narth** (session 8) |
| The Lord's Alliance | **The Lords' Alliance** (session 8) |
| Talan, Theo, Tella, Tel, Thale | **Thel** (session 8) |
| Temora,Tamura | **Tymora** (session 8) |
| Yola,Una | **Mirna** (session 8: the map-pin cue "Treasure — according to Mirna" at 00:43:39, after Mirna gives up the Thundertree necklace; "Una" was never a person) |
| Sarnak, Cessnak | **Ssarnak** (session 8: the nothic guarding the Crevasse Cave, PaBTSO ch.2 R8 — module spells it with a double S) |
| Sawplee (when it refers to Droop's clan) | **Scraptops** (session 8: 5etools `adventure-pabtso.json` R9 — "He is a member of the Scraptops, a goblin clan known for its scavenging and tinkering." Scraptops occurs exactly once in the module; Sawplee is Ruxithid's separate psionic-goblin faction, 29 occurrences. The DM said "Sawplee" at the table; this row repairs the clan, not the faction.) |
| Sildar Hillipwinter | **Sildar Hallwinter** |
| Sister Grail, Sister Garayel, Sister Grailie | **Sister Garaele** |
| Amund Cost | **Hamun Kost** |
| Harmon, Haman, Hammond | **Hamun** |
| Carsus | **Karsus** |

## Locations

| Wrong | Right |
|---|---|
| Tresender Manor, Tressander Manor, Tressender Manor, Tressendor Manor, Tressendur Manor, Tresander Manor, Trickndaw Manor, Trissinyr Manor, Tresenter Manor | **Tresendar Manor** |
| Eldermath Orchard | **Edermath Orchard** |
| Nethrel, Netherland, Netherlands | **Netheril** |
| Tribor Trail, Triborg Trail | **Triboar Trail** (also matches "Tribor Trails" plural) |
| Fandelin, Fandalin, Fandele, Fendolin, Panelin, Phanalyn, Fandeliever, Phandelin, Candolin, Pandathim, Fandal, Pandalam, Thanduil, Tangal, Tanglin, Fandalan, Bamburgh, Pandora, Vandaaram, Fandalyn, Fandland | **Phandalin** (session 4: ASR garbles of "Phandalin") |
| Nevermember, Nevermber, Neverwin, Nightwinter, Never Never | **Neverwinter** (session 4: ASR garbles of "Neverwinter") |
| Weiwe Vekov Cave, wake of Evoko Cave | **Wave Echo Cave** (session 4: "Vekov"/"Evoko" in cave context = ASR garble of "Echo", NOT the Glasstaff character Iarno — semantic disambiguation) |
| Fandele Verpakt, Phandalin Verpakt | **Phandelver Pact** (session 4: ASR garbles of "Phandelver Pact") |
| Kragmaw, Kragma, Kragmars | **Cragmaw** (session 4: "Kragmaw Hideout" = Cragmaw Hideout) |
| Zentarim | **Zhentarim** (session 4: ASR garble of "Zhentarim") |
| Tresander Crypts, Tresandar Crypts, Tresandar | **Tresendar Crypts** |
| Phandelever | **Lost Mine of Phandelver** |
| Town Master's Hall, Town Master Hall | **Townmaster's Hall** (session 5: spacing variant) |
| Wyvern Tour, Raven Tower, Wyvernor, Torb, Weaventor, Wivorn, Wventh | **Wyvern Tor** (session 5: ASR garble of the Wyvern Tor quest location) |
| Agathys Lair, Gotham's Lair | **Agatha's Lair** (session 8) |
| Cragma Castle, Crack Maw Castle, Crag Maw Castle, Grasma Castle, Krogmall Castle, Kragmakasm | **Cragmaw Castle** (session 8) |
| Kragma Hideo | **Cragmaw Hideout** (session 8) |
| Midas exchange, Miners Exchange | **Miner's Exchange** (session 8) |
| Stone Hill Inn, Stonehill Tavern | **Stonehill Inn** (session 8) |
| The Crag Mars | **The Cragmaw** (session 8) |
| Casinder,Crescendar | **Tresendar** (session 8) |
| Coneybury, Connie Berry, Coney Berry, Connberry | **Conyberry** |
| Old Alvwell, Old Dwell Hall, Oldwell Owl, Old Abel | **Old Owl Well** |
| Netherbese Empire, Netherreese Empire | **Netherese Empire** |
| Netherreal Empire | **Netheril Empire** |
| Thunder Tea | **Thundertree** |
| Faye | **Thay** |
| Taryn's Orchard | **Daran's Orchard** |

## Module terms (lower-case / compound — semantic pass)

| Wrong | Right |
|---|---|
| red brand, red brands, Red Rand, Red Bran, Red Ran, red-brand | **Redbrand** (session 4: the Phandalin bandit gang; "Red Brand Ruffian" = "Redbrand Ruffian"; session 5: "Red Bran" truncated ASR form) |
| Red Browns, Red Rans, Red Rands, Red Runes, Red Plance, Red Rats | **Redbrands** (session 5: "Red Browns" = Redbrands, 'w' ASR slip. Session 8: bare "Rands" was tried and reverted — it fires inside "The Red Rands" and yields "The Red Redbrands", so the two-word form is the only safe one) |
| Forward Giants | **Redbrands** (session 5: player garbled the gang name twice — "Forward Giants, Red Brands?") |
| notar | **dwarf** (session 5: ASR garble of "dwarf", lower-case) |
| Roxiga | **Rockseeker** (session 4: "Gundren Roxiga" = Gundren Rockseeker) |
| frock-seeker, frock seeker | **Rockseeker** (session 4: "old frock-seeker" = old Rockseeker) |
| Shub | **shove** |
| Thwax | **thwacks** |
| slids | **lids** (session 7: sarcophagus lids — "slids" is not a word, safe to substitute) |
| Curley wounds, Akir wounds | **Cure Wounds** (session 7: the spell, two-word garble) |
| red blank | **red cloak** (session 7: the Redbrand cloaks the party wears as disguise) |
| help bar | **health bar** (session 7: the VTT token HP bar) |
| points of denture | **points of damage** (session 7: phrase-scoped — bare "denture" is a real word and must NOT be substituted alone) |
| D10 during | **D10 damage** (session 7: phrase-scoped — bare "during" is a real word and must NOT be substituted alone) |
| Flambay | **flambé** (session 8: the Nothic's word, which the markdown spells correctly two lines later. "Serith" is the markdown's garble of the same word but is NOT in this row — it also occurs at 00:22:45 in the Dendrar scene, where it is something else entirely, so it is applied as a targeted edit instead) |
| Goblin Plan | **goblin clan** (session 8) |
| Prasinder | **I presume** (session 8: not a name at all — ASR garble of the GM's spoken phrase. Nonsense token, zero collision risk, and a recurring verbal tic) |

## Notes for future passes

Rows that are safe today but could bite later. Grep the transcript for these
before every apply.

- **`Talan` → `Thel`** (added session 8). The party took the magic longsword
  **Talon** out of the crevasse chest at the end of session 8 (PaBTSO ch.2:
  "Talon was lost here until Ssarnak found it"). `Talon` and `Talan` differ by
  one letter, and the applier matches case-insensitively. The row is safe only
  while ASR never renders the *sword* as "Talan". From session 9 on, grep for
  `Tal[oa]n` and check each hit is the murdered woodcarver and not the weapon
  before applying.
- **`Tel` → `Thel`** (added session 8). Three letters, case-insensitive. Zero
  lowercase hits across sessions 5–8, but it is short enough to watch.
- **`Serith` is deliberately NOT a row.** It garbles to `flambé` in the Nothic
  exchange (~01:42) but is something else entirely at 00:22:45 in the Dendrar
  scene. Context-dependent — apply as a targeted edit, never as a rule.
- **`Rands` is deliberately NOT a row.** It fires inside "The Red Rands" and
  yields "The Red Redbrands". Only the two-word `Red Rands` form is safe.
- **Split sections:** `Veyra` and `Zenvon` each have rows in both `## PCs` and
  `## NPCs and creatures` (from session 4's `Melavera` / `Xinavan`).
  `add_to_glossary.py` searches one section only, so the next append will make
  a third row. Consolidate into `## PCs` when convenient.

## Houses / factions

| Wrong | Right |
|---|---|
| Res Wizards | **Red Wizards** |
| Uthgarts | **Uthgardt** |

## Real-world / table

| Wrong | Right |
|---|---|
| Kostatis | **Kostadis** |
