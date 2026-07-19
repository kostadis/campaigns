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
| Xenophon, Xenobon, Zenovon | **Zenvon** |
| Zenoan | **Zenvon** (session 5: more ASR variant of the PC "Zenvon") |
| Vera | **Veyra** |
| Sister Mela, Mela | **Sister Maela** |

## NPCs and creatures

| Wrong | Right |
|---|---|
| Clarg | **Klarg** |
| Glastaff, Glass Staff, Glassdaff | **Glasstaff** (session 4: "Clarg"→Klarg; session 5: two-word "glass staff" / "Glassdaff" = Glasstaff, Iarno Albrek's alias) |
| Toblin | **Toblen** |
| Tobelin, Tublin | **Toblen** (session 4: more ASR variants of "Toblen Stonehill") |
| Glastaff | **Glasstaff** |
| Darren Edermeth | **Daran Edermath** |
| Oren Voss | **Orryn Voss** |
| Ruth exceeds | **Ruxithid** (garbled whispered name in "You're not what Ruxithid wants") |
| Soldar, Siddhar | **Sildar** (session 4: ASR garbles of "Sildar Hallwinter") |
| Silar, Silvar | **Sildar** (session 4: ASR garbles of "Sildar" — verify vs. other names) |
| Gundran, Gundrin, Gundrum, Gundrun, Gundrund | **Gundren** (session 4: ASR garbles of "Gundren Rockseeker") |
| Goodrin, Dundrum | **Gundren** (session 4: more ASR variants of "Gundren") |
| Gunther, Kissandar | **Gundren** (session 5: only these two are Gundren — "Gunther" = Sildar's old mentor; "Kissandar miner" = the Wave Echo Cave miner. All other Rondar/Rudar/Randar/Rondor/Rundar/Rondart/Brandar/Gundrid are the NPC Rondar, NOT Gundren) |
| Thardin | **Tharden** (session 4: Rockseeker brother "Tharden") |
| Barthin | **Barthen** (session 4: "Barthin's prov[isions]" = Elmina Barthen's shop) |
| Linen Lanain | **Linene Graywind** (session 4: "Linen Lanain … Lionshield coster" = Linene Graywind; both tokens garbled) |
| Linen, Lanain | **Linene** (session 4: single-token garbles of "Linene") |
| Yarno, Yorno, Jano, Yano, Jarno, Vekov, Evoko | **Iarno** (session 4: ASR garbles of "Iarno Albrek"/Glasstaff) |
| Quip | **Pip** (session 4: Nikhil's sidekick Pip, ASR garble) |
| Albrecht | **Albrek** (session 4: "Jarno/Larno Albrecht" = Iarno Albrek) |
| Ruxothid, Ruxathid | **Ruxithid** (session 4: Veyra repeating the goblin's name) |
| Melavera | **Veyra** (session 4: fused "Maela"+"Veyra" garble of the tiefling) |
| Xinavan | **Zenvon** (session 4: more ASR variant of the PC "Zenvon") |

## Locations

| Wrong | Right |
|---|---|
| Tresender Manor, Tressander Manor | **Tresendar Manor** |
| Eldermath Orchard | **Edermath Orchard** |
| Nethrel | **Netheril** |
| Tribor Trail | **Triboar Trail** (also matches "Tribor Trails" plural) |
| Fandelin, Fandalin, Fandele, Fendolin, Panelin, Phanalyn, Fandeliever | **Phandalin** (session 4: ASR garbles of "Phandalin") |
| Nevermember, Nevermber, Neverwin | **Neverwinter** (session 4: ASR garbles of "Neverwinter") |
| Weiwe Vekov Cave, wake of Evoko Cave | **Wave Echo Cave** (session 4: "Vekov"/"Evoko" in cave context = ASR garble of "Echo", NOT the Glasstaff character Iarno — semantic disambiguation) |
| Fandele Verpakt, Phandalin Verpakt | **Phandelver Pact** (session 4: ASR garbles of "Phandelver Pact") |
| Kragmaw | **Cragmaw** (session 4: "Kragmaw Hideout" = Cragmaw Hideout) |
| Zentarim | **Zhentarim** (session 4: ASR garble of "Zhentarim") |

## Module terms (lower-case / compound — semantic pass)

| Wrong | Right |
|---|---|
| red brand, Red Brand, red brands, Red Brands | **Redbrand** (session 4: the Phandalin bandit gang; "Red Brand Ruffian" = "Redbrand Ruffian") |
| Red Browns | **Redbrands** (session 5: "Red Browns" = Redbrands, 'w' ASR slip) |
| Forward Giants | **Redbrands** (session 5: player garbled the gang name twice — "Forward Giants, Red Brands?") |
| notar | **dwarf** (session 5: ASR garble of "dwarf", lower-case) |
| Roxiga | **Rockseeker** (session 4: "Gundren Roxiga" = Gundren Rockseeker) |
| frock-seeker, frock seeker | **Rockseeker** (session 4: "old frock-seeker" = old Rockseeker) |
