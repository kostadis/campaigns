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
| Xenophon, Xenobon, Zenovon, Xenovon, Xenomon, Cinnamon, Zenomon, Zenon, Zenotic, Zenovan | **Zenvon** |
| Zenoan | **Zenvon** (session 5: more ASR variant of the PC "Zenvon") |
| Zanabon, Zenimon, Xenob | **Zenvon** (session 7: more ASR variants of the PC "Zenvon") |
| Vera, Azvera, Rivera, Maya, Maia, Zerabira | **Veyra** |
| Sister Vera | **Veyra** (session 5: ASR gave Veyra the cleric's title. The applier sorts longest-first, so this beats the bare "Vera" row and yields "Veyra", not "Sister Veyra") |
| Sister Mela, Mela, Mila, Myla, Mil, Myra, Nela, Mele, Sister Bela, Sister Meela, Sturmela, Sister Mele, Tell Sister Meila | **Sister Maela** (session 7: "Mila"/"Myla"/"Mil" also = Maela, the Turn-Undead cleric) |
| sister male | **Sister Maela** (session 7: ASR split the name into two real words — safe because the two-word sequence never occurs legitimately) |
| veera | **Veyra** (session 7: doubled-vowel variant, cf. the "Vera" row) |

## NPCs and creatures

| Wrong | Right |
|---|---|
| Clarg | **Klarg** |
| Glastaff, Glass Staff, Glassdaff, Glass Tap, Glastap, Glassstaff, Blast Staff, Gastav | **Glasstaff** (session 4: "Clarg"→Klarg; session 5/7: two-word "glass staff" / "Glassdaff" / "Glass Tap" = Glasstaff, Iarno Albrek's alias) |
| Toblin | **Toblen** |
| Tobelin, Tublin | **Toblen** (session 4: more ASR variants of "Toblen Stonehill") |
| Glastaff | **Glasstaff** |
| Darren Edermeth | **Daran Edermath** |
| Oren Voss | **Orryn Voss** |
| Ruth exceeds | **Ruxithid** (garbled whispered name in "You're not what Ruxithid wants") |
| Soldar, Siddhar | **Sildar** (session 4: ASR garbles of "Sildar Hallwinter") |
| Silar, Silvar | **Sildar** (session 4: ASR garbles of "Sildar" — verify vs. other names) |
| Gundran, Gundrin, Gundrum, Gundrun, Gundrund, Wundren | **Gundren** (session 4: ASR garbles of "Gundren Rockseeker") |
| Goodrin, Dundrum | **Gundren** (session 4: more ASR variants of "Gundren") |
| Gunther, Kissandar | **Gundren** (session 5: only these two are Gundren — "Gunther" = Sildar's old mentor; "Kissandar miner" = the Wave Echo Cave miner. All other Rondar/Rudar/Randar/Rondor/Rundar/Rondart/Brandar/Gundrid are the NPC Rondar, NOT Gundren) |
| Thardin | **Tharden** (session 4: Rockseeker brother "Tharden") |
| Barthin | **Barthen** (session 4: "Barthin's prov[isions]" = Elmina Barthen's shop) |
| Linen Lanain | **Linene Graywind** (session 4: "Linen Lanain … Lionshield coster" = Linene Graywind; both tokens garbled) |
| Linen, Lanain | **Linene** (session 4: single-token garbles of "Linene") |
| Yarno, Yorno, Jano, Yano, Jarno, Vekov, Evoko | **Iarno** (session 4: ASR garbles of "Iarno Albrek"/Glasstaff) |
| Quip | **Pip** (session 4: Nikhil's sidekick Pip, ASR garble) |
| Pimp, Pippa, Pips | **Pip** (session 7: more ASR garbles of the sidekick "Pip") |
| Albrecht | **Albrek** (session 4: "Jarno/Larno Albrecht" = Iarno Albrek) |
| Ruxothid, Ruxathid | **Ruxithid** (session 4: Veyra repeating the goblin's name) |
| Melavera | **Veyra** (session 4: fused "Maela"+"Veyra" garble of the tiefling) |
| Xinavan | **Zenvon** (session 4: more ASR variant of the PC "Zenvon") |
| Dendars, The Ten Doves | **Dendrars** (session 7: variant of the Dendrar family, cf. session 1 "Dendar") |
| Dendar | **Dendrar** (session 1: ASR mishearing of the family name. Moved here from `docs/entity_registry.yaml` on 2026-08-01 — garbles are transcription errors, not identity aliases, so they belong in this glossary and never in the registry) |
| Tell Dendar | **Thel Dendrar** (early session: ASR heard "Thel" as "Tell", cf. the "Tell Sister Meila" row. Evidenced by a `docs/ensemble/merged.json` source_quote; that session's VTT is not retained. Longest-first ordering makes this beat the bare "Dendar" row) |
| Dessa | **Dosa Rook** (session 7: Redbrand-handled bandit, full name confirmed from retranscription) |
| Black Sparta | **Black Spider** (Nezznar's known alias) |
| Karimi, Redbrand Moravian, Redbrand Muffian, Redbrand muffin | **Redbrand Ruffian** |
| Rhondar, Prandar, Rudar, Randar, Rondor, Brandar, Randa, Randor, Rhonda, Rondart, Rundar, Gundrid, Arnold, Brandor | **Rondar** |
| Gnothic | **Nothic** |
| Orman, Bormann, Ormon, Urman | **Urmon** (session 6: "Urman" added 2026-08-01 — journal-author NPC) |
| Dvarvish | **Dwarvish** |
| Carbon Wester,Harbren Wester,Pardman Wester | **Harbin Wester** (session 5: ASR garbles of the townmaster's first name, correct surname retained) |
| Iarno Ulbrecht,Larno Albrek,Giano Albrand | **Iarno Albrek** (session 5: ASR garbles of Glasstaff's real name) |
| Harvin | **Harbin** (session 5: bare first-name garble, paired with the Harbin Wester row) |
| Holly | **Halia** (session 5: DM pulling up Halia Thornton's notes, ASR garble) |
| Red Brad Muffin Ruffians | **Redbrand Ruffians** (session 5: Halia's 'shocked, shocked' line, 4-word garble not caught by the 2-word 'Redbrand muffin' rule) |

## Locations

| Wrong | Right |
|---|---|
| Tresender Manor, Tressander Manor, Tressender Manor, Tressendor Manor, Tressendur Manor, Tresander Manor, Trickndaw Manor | **Tresendar Manor** |
| Eldermath Orchard | **Edermath Orchard** |
| Nethrel | **Netheril** |
| Tribor Trail | **Triboar Trail** (also matches "Tribor Trails" plural) |
| Fandelin, Fandalin, Fandele, Fendolin, Panelin, Phanalyn, Fandeliever, Phandelin | **Phandalin** (session 4: ASR garbles of "Phandalin") |
| Nevermember, Nevermber, Neverwin, Nightwinter | **Neverwinter** (session 4: ASR garbles of "Neverwinter") |
| Weiwe Vekov Cave, wake of Evoko Cave | **Wave Echo Cave** (session 4: "Vekov"/"Evoko" in cave context = ASR garble of "Echo", NOT the Glasstaff character Iarno — semantic disambiguation) |
| Fandele Verpakt, Phandalin Verpakt | **Phandelver Pact** (session 4: ASR garbles of "Phandelver Pact") |
| Kragmaw | **Cragmaw** (session 4: "Kragmaw Hideout" = Cragmaw Hideout) |
| Zentarim | **Zhentarim** (session 4: ASR garble of "Zhentarim") |
| Tresander Crypts, Tresandar Crypts, Tresandar | **Tresendar Crypts** |
| Phandelever | **Lost Mine of Phandelver** |
| Town Master's Hall | **Townmaster's Hall** (session 5: spacing variant) |
| Wyvern Tour, Raven Tower | **Wyvern Tor** (session 5: ASR garble of the Wyvern Tor quest location) |

## Module terms (lower-case / compound — semantic pass)

| Wrong | Right |
|---|---|
| red brand, red brands, Red Rand, Red Bran | **Redbrand** (session 4: the Phandalin bandit gang; "Red Brand Ruffian" = "Redbrand Ruffian"; session 5: "Red Bran" truncated ASR form) |
| Red Browns | **Redbrands** (session 5: "Red Browns" = Redbrands, 'w' ASR slip) |
| Forward Giants | **Redbrands** (session 5: player garbled the gang name twice — "Forward Giants, Red Brands?") |
| notar | **dwarf** (session 5: ASR garble of "dwarf", lower-case) |
| Roxiga | **Rockseeker** (session 4: "Gundren Roxiga" = Gundren Rockseeker) |
| frock-seeker, frock seeker | **Rockseeker** (session 4: "old frock-seeker" = old Rockseeker) |
| Shub | **shove** |
| Thwax | **thwacks** |
| slids | **lids** (session 7: sarcophagus lids — "slids" is not a word, safe to substitute) |
| Curley wounds | **Cure Wounds** (session 7: the spell, two-word garble) |
| red blank | **red cloak** (session 7: the Redbrand cloaks the party wears as disguise) |
| help bar | **health bar** (session 7: the VTT token HP bar) |
| points of denture | **points of damage** (session 7: phrase-scoped — bare "denture" is a real word and must NOT be substituted alone) |
| D10 during | **D10 damage** (session 7: phrase-scoped — bare "during" is a real word and must NOT be substituted alone) |
