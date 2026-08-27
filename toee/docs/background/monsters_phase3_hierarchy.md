# Phase 3 — Monster Boss Hierarchy (CR-Difference Classification)

**Purpose:** For every unnamed-monster *tribe* in the Temple of Elemental Evil (T1-4, 5e), identify its **bigger bad** (the boss who commands that tribe) and classify that boss as **NOMINAL** or **HARD** using the rule specified below.

**THE RULE (verbatim):**

> Δ = CR(boss) − CR(rank-and-file). Use the HIGHEST rank-and-file CR for the conservative (smallest-gap) comparison when a tribe has multiple tiers.
> - Δ < 4 → NOMINAL boss (a leader in name; threat within ~3 CR of rank-and-file).
> - Δ > 4 → HARD boss (genuinely more dangerous threat than rank-and-file).
> - Δ == exactly 4 → NOMINAL+ (borderline-hard) — flag for review, NEVER silently call "hard".
> Edge cases: tribes whose boss is a NAMED module NPC keep that name (do NOT rename). Truly leaderless tribes get either a NOMINATED boss (an unnamed commander named in Phase 2) or "NO BOSS — ambient/independent". Apex creatures that command no tribe (e.g. Zuggtmoy, a node prince) are marked apex/HARD threat but not a "tribe boss".

**Boss-tier edge conventions applied here:**
- Where a boss CR is given as a *range*, I pick a central value, show the range in the entry, and compute Δ against the **highest** rank-and-file CR (most conservative). If the top of the range yields Δ = 4, that tribe is flagged **NOMINAL+ (borderline-hard)**.
- A negative Δ (boss *weaker* than an elite subordinate) is reported honestly as a **NOMINAL / peer** finding — never forced positive.
- Module-named NPCs are **never renamed**; only classified. Counts are unchanged from Phase 1/2.

**CR source note:** All CRs are taken from `monsters_cr_reference.md` (source-of-truth). The Greater Temple leadership levels come from `_leadership_flattened.txt`. **Hedrack's CR is taken as 6 from his embedded statblock ("Challenge 6 (2,300 XP)")** — *not* the CR-reference estimate of ~11 (the appendix note's "L11 → CR~11" is overridden by the actual printed stat). A footnote on this appears in Section A13/29/30. Node princes (Crushing Wave, etc.) and Zuggtmoy are apex NAMED creatures, excluded from renaming, treated as apex/HARD over their tribes.

**Legend:** CR(rank) = rank-and-file Challenge Rating · CR(boss) = boss Challenge Rating · Δ = CR(boss) − CR(rank).

---

## A. Tribes with a NAMED MODULE boss

### A1. Trading Post garrison — the Eyes of the Temple (Key to the Village, Area 13)
- Rank-and-file CR: Groom (L0) 1/4, Man-at-arms (L1 Fighter) 1/2. Highest rank CR = **1/2**.
- Named-module boss(es): **Rannos Davl** (L10 Thief → CR 3 per CR-ref "Thief (ToEE) 3") and **Gremag** (L7 Assassin → CR 8). Both preserved verbatim, NOT renamed.
- Δ (Gremag CR8 − rank1/2) = **7.5** → **HARD boss** (Gremag is the physical threat). Δ (Rannos CR3 − rank1/2) = 2.5 → NOMINAL if Rannos were the sole boss.
- **Verdict:** **HARD boss** (Gremag, the assassin, is the decisive bigger bad). Rannos is a NOMINAL co-leader. Meta-chain: the post reports to an unnamed Temple brigand courier → ultimately **Hedrack**.

### A3. Guard Tower garrison — Burne's Watch (Area 31)
- Rank-and-file CR: Guard (L2 Fighter) 1/2. Highest rank CR = **1/2**.
- Named-module boss: **Burne** and **Rufus** (tower owners; Rufus = "overall commander of the village troops"). Preserved verbatim, NOT renamed.
- CR ambiguity: Burne/Rufus are not in the CR table; estimated **CR ~9** (high-level fighter-wizard types, L9-equivalent; range ~8–11). Δ (~9 − 1/2) ≈ **8.5** → **HARD boss**.
- **Verdict:** **HARD boss.** (Good-aligned village wardens, outside the Temple chain — but by CR they are a massive leap over their guards.) Flagged CR ambiguity noted below.

### A8. Moathouse dungeon garrison — the New Master's Legion (Dungeon Level, areas 18, 21, 27, 31, 30)
- Rank-and-file CR: Green Slime 1/4, Zombie 1/4, Bugbear 1, Ghoul 1, Giant Crayfish 1/2. Highest rank CR = **1** (bugbear/ghoul).
- Named-module boss: **Lareth the Beautiful** (the "New Master," room 35), preserved verbatim, NOT renamed. CR not in table; estimated **CR ~8** (L7–8 cleric of Lolth; range 7–8).
- Δ (Lareth ~8 − rank1) ≈ **7** → **HARD boss**.
- **Verdict:** **HARD boss.** Lareth is a genuine leap above his undead/bugbear legion. He also meta-commands Tribe 9 (Lubash), Tribe 10 (gnolls) and Tribe 11 (Temple Guards).

### A9. Blackthorn ogres — Lubash's Reavers (Dungeon Level, Area 24)
- Rank-and-file CR: a single named ogre, **Lubash**, CR 2. (Plus implied kitchen thralls — no separate combat rank.)
- Named-module boss: **Lubash** (explicitly named ogre), preserved verbatim, NOT renamed. The "tribe" is the ogre himself.
- Δ (Lubash CR2 − rank2) = **0** → **NOMINAL boss** (he *is* the rank-and-file).
- **Verdict:** NOMINAL. Lubash is a solo named monster, not a boss over a distinct rank-and-file; classified NOMINAL by definition. He is recruited by Lareth (A8).

### A11. Temple Guards — the Eyes of Fire (Dungeon Level, areas 33–34)
- Rank-and-file CR: Guardsman (L1 Fighter) 1/2, Sergeant (L2 Fighter) 1/2. Highest rank CR = **1/2**.
- Named-module boss: **Lareth the Beautiful** (the "New Master"), preserved verbatim, NOT renamed. CR ~8 (range 7–8).
- Δ (Lareth ~8 − rank1/2) ≈ **7.5** → **HARD boss**.
- **Verdict:** **HARD boss** (same boss as A8).

### A12. Nulb brigands — the Shattered Tower Brotherhood (Nulb, River Pirates, Broken Tower)
- Rank-and-file CR: Nulb Militia (Warrior) 1/4, Mercenaries 1/4, River-Pirate crew (Bandit/Thug) 1/2, Broken Tower bandits 1/8. Highest *pirate-crew* rank CR = **1/2** (the named-boss core).
- Named-module boss: **Tolub** (Pirate Leader, L8 Fighter → CR 8) and **Grud Squinteye** (Pirate Lieutenant, L6 Fighter → CR 6). Preserved verbatim, NOT renamed. (The Broken Tower's L6 Leader and the Upper-Works L5/L3 leaders are *unnamed* stat-blocks — covered in the note below.)
- Δ (Tolub CR8 − rank1/2) = **7.5** → **HARD**; Δ (Grud CR6 − rank1/2) = **5.5** → **HARD**.
- **Verdict:** **HARD boss** over the pirate crews. *Sub-note:* the Broken Tower L6 Leader (unnamed, CR 2) over his bandits (1/8) is only NOMINAL (Δ ≈ 1.9); the militia/merc contingents are leaderless in-module. The whole Nulb sink ultimately answers to **Madame Selentis** (Hedrack's agent).

### A13. Greater Temple Brigands — the Moathouse Raiders (Dungeon L1/L2, areas 240–244, 243)
- Rank-and-file CR: Bandit 1/8, Guard (raider) 1/2, Bandit Captain (serjeant) 2, Veteran (raider leader) 3. Highest rank CR = **3** (veteran).
- Named-module boss: **Feldrin** (Commander, uses Assassin stats, qtr 243a), preserved verbatim, NOT renamed. CR guidance: **CR 5–7** (assassin). Central value **6**; range shown.
- Δ (Feldrin CR6 − rank3) = **3** → **NOMINAL** at the central value. **Borderline flag:** at the *top* of his range (CR 7), Δ = 7 − 3 = **4 exactly → NOMINAL+ (borderline-hard)**.
- **Verdict:** **NOMINAL** (central CR 6), **flagged NOMINAL+ (borderline-hard)** should Feldrin sit at CR 7. He answers to **Hedrack**.

### A14. Earth Temple — the Black Earth Brotherhood (Dungeon L1, areas 121–145)
- Rank-and-file CR: Gnoll 1/2, Hobgoblin 1/2, Ogre 2, Earth Elemental 5. Highest rank CR = **5** (earth elemental).
- Named-module boss: **Romag** (High Priest of Earth), preserved verbatim, NOT renamed. CR guidance: **CR 7–8** (L7 cleric); central 7.5. Also **Hartsch** (Acolyte, named) and the named Earth Prince (Black Earth, apex) — excluded as monster.
- Δ (Romag ~7.5 − rank5) = **2.5** → **NOMINAL boss**.
- **Verdict:** NOMINAL. Romag's authority is real, but his toughest troops (the earth elementals, ogres) sit within 3 CR of him. He answers to **Hedrack** and secretly to **Zuggtmoy**.

### A15. Temple Guards — the Black-Triangle Watch (Dungeon L1, areas 133–149)
- Rank-and-file CR: Guard 1/2, Veteran 3, Gladiator (commander) 5. Highest rank CR = **5** (gladiator).
- Named-module boss: **Romag** (Earth Temple High Priest, ultimate authority), preserved verbatim, NOT renamed. Immediate field commanders (Veteran lieutenant, Gladiator commander) are *unnamed*.
- Δ (Romag ~7.5 − rank5) = **2.5** → **NOMINAL boss**.
- **Verdict:** NOMINAL. Same boss as A14; the gladiator-commander rank-and-file nearly matches Romag's CR.

### A16. Water Temple — the Crushing Wave's Drowned (Dungeon L2, areas 213–221)
- Rank-and-file CR: Bugbear 1, Ogre 2, Under-Priest 2, Zombie/gargoyle 2, Juggernaut 5, Owlbear 3, Troll 5. Highest rank CR = **5** (juggernaut / troll).
- Named-module boss: **Belsornig** (High Priest of Water), preserved verbatim, NOT renamed (CR 7–8; central 7.5). Also **Oohlgrist** the troll chief (area 219, named) — CR 5 troll over the temple's trolls (CR 5) → NOMINAL/peer.
- Δ (Belsornig ~7.5 − rank5) = **2.5** → **NOMINAL boss**. Δ (Oohlgrist CR5 − troll rank5) = 0 → NOMINAL.
- **Verdict:** NOMINAL. Belsornig is a real high priest but his trolls/juggernaut are within 3 CR. Answers to **Hedrack** / **Zuggtmoy**.

### A17. Fire Temple — the Flamebound Zealots (Dungeon L2, areas 202–212)
- Rank-and-file CR: Troll 5, Werewolf 3, Bugbear 1, Gladiator 5, **Hydra 8**, Salamander 5, Cult Fanatic 2. Highest rank CR = **8** (the bound five-headed hydra).
- Named-module boss: **Alrrem** (Prefect of Fire), preserved verbatim, NOT renamed (CR 7–8; central 7.5).
- Δ (Alrrem ~7.5 − rank8/hydra) = **−0.5** → **NOMINAL boss (peer / NEGATIVE Δ)**. The hydra is actually *harder* than Alrrem.
- **Verdict:** **NOMINAL (peer).** This is a real finding — Alrrem is *weaker* than his own bound hydra; he leads by cult authority, not raw CR. (Per rule, the negative Δ is reported, never forced positive.) Answers to **Hedrack** / **Zuggtmoy**.

### A18. Air Temple — the Greywind Devotees (Dungeon L2, areas 225–226)
- Rank-and-file CR: Bugbear 1, Goblin 1/4. Highest rank CR = **1** (bugbear).
- Named-module boss: **Kelno** (Prefect of Air), preserved verbatim, NOT renamed (CR 7–8; central 7.5).
- Δ (Kelno ~7.5 − rank1) = **6.5** → **HARD boss**.
- **Verdict:** **HARD boss.** Unlike the other three elemental priests, Kelno's contingent is only bugbears/goblins (no CR-5 elemental), so he is a genuine CR leap above them. Answers to **Hedrack** / **Zuggtmoy**.

### A19. Bugbear Guards — the Blackplate Wardens (Dungeon L2, areas 204, 231, 232)
- Rank-and-file CR: Bugbear 1. Highest rank CR = **1**.
- Boss: no *in-module named* bugbear chief; the tribe "obeys only the central Temple command." By the meta-chain the commander is **Hedrack** (Supreme Commander, named, CR 6), preserved verbatim, NOT renamed.
- Δ (Hedrack CR6 − rank1) = **5** → **HARD boss**.
- **Verdict:** **HARD boss** (via Hedrack's authority). These neutral muscle are a distinct tribe but their bigger bad is Hedrack. (Listed in Section A because Hedrack is a named-module NPC and the authority.)

### A25. Zuggtmoy's Menagerie (Dungeon L3, areas 301–320)
- Rank-and-file CR: Troll 5, Ettin 4, Leucrotta 5, Gargoyle 2, Jackalwere 1/4, Will-o'-Wisp 2, Lamia 4, Bugbear 1, Gnoll 1/2, Ogre 2. Highest rank CR = **5** (troll / leucrotta).
- Named-module boss: **Zuggtmoy** (Demoness of Fungi, mistress of the Interdicted Prison), preserved verbatim, NOT renamed. Apex creature, CR ~23 (unique, 49 HD).
- Δ (Zuggtmoy 23 − rank5) = **18** → **HARD boss (apex)**.
- **Verdict:** **HARD / apex.** Zuggtmoy commands this brood directly; she is the mistress, not merely a patron.

### A26. Prison Shadows (Dungeon L3, areas 323–332)
- Rank-and-file CR: Shadow 1/2, Banshee 4, Lurker Above 5. Highest rank CR = **5** (lurker above).
- Named-module boss: **Zuggtmoy** and **Iuz** (Abyssal patrons the shadows "await the return of"), preserved verbatim, NOT renamed. Zuggtmoy CR ~23; Iuz is a demigod (apex).
- Δ (Zuggtmoy 23 − rank5) = **18** → **HARD boss (apex)**.
- **Verdict:** **HARD / apex.**

### A27. Fungal Brood — Interdicted Prison, North Halls (areas 341–350)
- Rank-and-file CR: Violet Fungus 1/4, Lesser Hooting Fungus 0, Animated Armor 1, Gray Ooze 1/2, Ochre Jelly 2, Black Pudding 4, Shrieker 0. Highest rank CR = **4** (black pudding).
- Named-module boss: **Zuggtmoy** (creator and mistress of the entire Brood), preserved verbatim, NOT renamed. CR ~23.
- Δ (Zuggtmoy 23 − rank4) = **19** → **HARD boss (apex)**.
- **Verdict:** **HARD / apex.**

### A29. Greater Temple — Troop & Guard Positions, the Temple Host (Garrison table, areas 401–430)
- Rank-and-file CR: Troll 5, Gargoyle 2, Ogre 2, Bugbear 1, Hill Giant 5, Ettin 4. Highest rank CR = **5** (hill giant / troll).
- Named-module boss: **Hedrack** (Supreme Commander, CR 6) with **Barkinar** (Troop cmd, CR 7–9), **Deggum** (Guard cmd, CR 5–8), **Senshock** (Lord Wizard, CR 9–11) — all preserved verbatim, NOT renamed.
- Δ (Hedrack CR6 − rank5) = **1** → **NOMINAL boss** (over his elite garrison troops). *(Δ vs the bugbear/ogre rank would be HARD; the conservative comparison uses the hill-giant/troll top tier.)*
- **Verdict:** NOMINAL. Hedrack is only a step above his hill giants and trolls, though a HARD leap above the bugbear rank. *(Hedrack's printed CR is 6, not the ~11 the appendix note implies — see CR-source note.)* Ultimate authority: **Iuz**.

### A30. Hedrack's Inner Sanctum — Detailed Room Garrisons (Room Key 401–435)
- Rank-and-file CR: Troll 5, Gargoyle 2, Ogre 2, Bugbear 1, Hill Giant 5, Ettin 4, Doppelganger 4, Commoner 0. Highest rank CR = **5** (hill giant / troll).
- Named-module boss: **Hedrack** (CR 6), **Barkinar**, **Deggum**, **Senshock** — preserved verbatim, NOT renamed. (Kella the spy is excluded as named.)
- Δ (Hedrack CR6 − rank5) = **1** → **NOMINAL boss**.
- **Verdict:** NOMINAL (same as A29 — the per-room detail of the same Host).

### A31. Air Node natives — the Stormwrack Brood
- Rank-and-file CR (conservative highest): Cloud Giant 9 (young white dragon 6, air elemental 5, hieracosphinx 3, etc.). Highest rank CR = **9**.
- Named-module boss: **Whispering Wind** (Prince of Evil Air, apex), preserved verbatim, NOT renamed. CR guidance: **17–21**; central 19.
- Δ (Whispering Wind 19 − rank9) = **10** → **HARD boss (apex)**.
- **Verdict:** **HARD / apex.** (Above him: the Elder Elemental Eye; secretly Zuggtmoy.)

### A32. Earth Node inhabitants — the Stone-Choir
- Rank-and-file CR (conservative highest): Stone Giant 7. Highest rank CR = **7**.
- Named-module boss: **Black Earth** (Prince of Evil Earth, apex), preserved verbatim, NOT renamed. CR 17–21; central 19.
- Δ (Black Earth 19 − rank7) = **12** → **HARD boss (apex)**.
- **Verdict:** **HARD / apex.**

### A33. Fire Node inhabitants — the Cinder Court
- Rank-and-file CR (conservative highest): **Adult Red Dragon 17** (efreeti 11, fire giant 9, bodak 6, fire elemental 5, salamander 5). Highest rank CR = **17**.
- Named-module boss: **Eternal Flame** (Prince of Evil Fire, apex), preserved verbatim, NOT renamed. CR 17–21; central 19.
- Δ (Eternal Flame 19 − rank17/red dragon) = **2** → **NOMINAL boss (apex, peer with the red dragons)**.
- **Verdict:** NOMINAL. The Fire Node's red dragons are nearly as dangerous as the prince himself — a real peer finding. (The efreeti, fire giants, etc. are well below him.)

### A34. Water Node inhabitants — the Drowned Choir
- Rank-and-file CR (conservative highest): **Dragon Turtle 17** (frost giant 8, water elemental 5, floating eye 2). Highest rank CR = **17**.
- Named-module boss: **Crushing Wave** (Prince of Evil Water, apex), preserved verbatim, NOT renamed. CR 17–21; central 19.
- Δ (Crushing Wave 19 − rank17/dragon turtle) = **2** → **NOMINAL boss (apex, peer with the dragon turtle)**.
- **Verdict:** NOMINAL. The dragon turtle is the node's near-equal.

### A35. Wandering humans — the Bargent's Road Brigands (Nodes-wide)
- Rank-and-file CR: Bandit 1/8 (×7). Highest rank CR = **1/8**.
- Named-module boss: **Grank** (cleric-captain, Priest stat → CR 2), preserved verbatim, NOT renamed.
- Δ (Grank CR2 − rank1/8) = **1.875** → **NOMINAL boss**.
- **Verdict:** NOMINAL. Grank is a modest step up over his desperate bandits.

---

## B. Leaderless / ambient tribes — NOMINATED boss or "no boss"

These tribes have **no in-module named boss of their own**. Where the module leaves an *unnamed* field commander, we NOMINATE the commander named in Phase 2; where the tribe is truly wild/vermin/random, it is ambient/independent.

### B2. Welcome Wench lodgers — the Watching Guests (Inn, rooms 16 & 114)
- Zert (L2 Fighter), Kobort (L2 Fighter), Turuko (L3 Monk) are *module-named individuals* preserved verbatim, but **none leads the others** — a loose knot of spies/opportunists, no boss.
- **Verdict: NO BOSS — independent individuals** (named, kept as-is, not renamed).

### B4. Burne's Badgers — the Tower Free-Company (Area 31, GT 8–9)
- Rank-and-file CR: Men-at-arms 1/2; the two leaders (captain, lieutenant) are *unnamed* in module (L1–2 fighter → CR 1/2). Overall owners **Burne & Rufus** are named but are not the field boss.
- Nominated boss (Phase 2): **Captain Halla Broadshield** (mercenary captain, CR 1/2). Δ (Halla 1/2 − rank1/2) = **0** → NOMINAL.
- **Verdict: NOMINAL boss (nominated — Halla Broadshield).** The true patrons (Burne/Rufus) are HARD over the whole company but are not its field commander.

### B5. Moathouse brigand garrison — the Black Chamber Company (Ruins UL, area 7)
- Rank-and-file CR: Brigand 1/2, Leader (L2 Fighter) 1/2, Aide 1/4. Highest rank CR = **1/2**.
- Nominated boss (Phase 2): **Varl "Black-Jack"** (the unnamed L2 leader, CR 1/2). Δ (Varl 1/2 − rank1/2) = **0** → NOMINAL.
- **Verdict: NOMINAL boss (nominated — Varl).** Independent of Lareth (the dungeon "New Master"); the upper-level garrison has no named-module boss.

### B6. Moathouse ruins fauna — the Ruin-Dwellers (Ruins UL: Pool, Tower, Random, Corner Room)
- Wild beasts/vermin: giant frog 1/4, huge spider 1, giant rat 1/4, giant tick 1/2, huge adder 1/2. No leaders.
- **Verdict: NO BOSS — ambient/independent wildlife.**

### B7. Hommlet village dogs — the Hounds of Hommlet (Areas 1, 15, 18, 19, 25)
- Beasts: farm/watch/war dogs 1/4. No leaders (Jaroo's bear excluded as a named-NPC companion).
- **Verdict: NO BOSS — ambient guardian beasts.**

### B10. Gnoll warband — the Dust-Manes (Dungeon L1, area 29)
- Rank-and-file CR: Gnoll 1/2. Highest rank CR = **1/2**.
- Nominated boss (Phase 2): **Snarl-tooth** (the unnamed gnoll leader, CR 1/2). Δ (Snarl-tooth 1/2 − rank1/2) = **0** → NOMINAL. Overall force serves **Lareth** (A8, HARD).
- **Verdict: NOMINAL boss (nominated — Snarl-tooth).** Meta-boss Lareth is HARD over them.

### B20. Dungeon Jailers — the Iron-Lemma Wardens (Dungeon L2, areas 152, 228)
- Rank-and-file CR: Ogre 2, Bugbear 1, Gladiator (turnkey) 5. Highest rank CR = **5** (gladiator turnkey).
- Nominated boss (Phase 2): **Turnkey Varl** (the gladiator turnkey, CR 5; unnamed in module). Δ (Varl 5 − rank5) = **0** → NOMINAL. Orders "from below" (Hedrack's command) via an ettin courier.
- **Verdict: NOMINAL boss (nominated — Turnkey Varl).**

### B21. Lower Warren — Dungeon L1 Undead & Vermin (areas 103–150)
- Faction-less infestation: ghoul 1, ghast 2, giant rat 1/8, harpy 1, gelatinous cube 2, gray ooze 1/2, zombie 1/4. No leader.
- **Verdict: NO BOSS — ambient/independent warren** (predates and ignores the cults).

### B22. Deep Scavengers — Dungeon L2 Random/Wandering (RE 02–10)
- Opportunist wanderers: bugbear 1, carrion crawler 2, ochre jelly 2, ogre 2, troll 5. No leader; the trolls trail **Oohlgrist** (named troll chief, CR 5 → NOMINAL over trolls).
- **Verdict: NO BOSS — ambient scavengers** (troll sub-group answers to Oohlgrist, NOMINAL).

### B23. Relic Wardens — Dungeon Misc Room Guardians (areas 120–146, 230, 232)
- Room-trap guardians/beasts: skeleton 1/4, giant rat 1/8, giant snake 1/4, stirge 1/8, otyugh 5. Unaligned, no leader.
- **Verdict: NO BOSS — ambient room-guardians** (triggered by intrusion, not commanded).

### B24. Pit Spawn — Dungeon L3 Random Encounters (RE 01–12)
- Leaderless wanderers: black pudding 4, ettin 4, gargoyle 2, hill giant 5, ogre 2, troll 5. No named leader.
- **Verdict: NO BOSS — ambient/independent random menagerie.**

### B28. Sealed Patrol — Interdicted Prison Random Encounters (RE 01–16)
- Prison patrols/pass-throughs: black pudding 4, ettin 4, troll 5, gargoyle 2, hill giant 5, ogre 2, bugbear 1. No specific boss; ogres/bugbears "head back to area 405" (Hedrack/Barkinar); patrons Zuggtmoy & Iuz.
- **Verdict: NO BOSS — ambient patrol traffic** (answers to Hedrack / Zuggtmoy above).

---

## C. Hierarchy tree (boss → tribe), with classification

```text
ZUGGTMOY (Demoness of Fungi — apex, CR ~23)            [apex / HARD over all her brood]
├─ IUZ (demigod patron, Old One)                        [apex]
├─ Fungal Brood (A27)                                   HARD (Δ 19)
├─ Prison Shadows (A26)                                 HARD (Δ 18)
├─ Menagerie (A25)                                      HARD (Δ 18)
└─ the four NODE PRINCES (apex, named, CR 17–21):
   ├─ WHISPERING WIND (Air)   → Stormwrack Brood (A31)  HARD (Δ 10)
   ├─ BLACK EARTH (Earth)      → Stone-Choir (A32)      HARD (Δ 12)
   ├─ ETERNAL FLAME (Fire)     → Cinder Court (A33)     NOMINAL (Δ 2 — peer w/ red dragon)
   └─ CRUSHING WAVE (Water)    → Drowned Choir (A34)    NOMINAL (Δ 2 — peer w/ dragon turtle)

HEDRACK (Supreme Commander — CR 6, NOT ~11)            [NOMINAL over giants/trolls; HARD over bugbears]
├─ Barkinar (Troop cmd, CR 7–9) · Deggum (Guard cmd, CR 5–8) · Senshock (Lord Wizard, CR 9–11)
├─ Greater Temple Brigands → FELDRIN (CR 6)            NOMINAL (Δ 3) · flagged NOMINAL+ at CR 7
├─ Blackplate Wardens (A19)                            HARD (Δ 5 over bugbears)
├─ Dungeon Jailers (B20, nominated Turnkey Varl)       NOMINAL (Δ 0)
├─ Temple Host (A29)                                    NOMINAL (Δ 1)
├─ Inner Sanctum (A30)                                  NOMINAL (Δ 1)
└─ the FOUR HIGH PRIESTS (each CR 7–8):
   ├─ ROMAG (Earth)   → Earth Temple (A14)             NOMINAL (Δ 2.5)
   │                   → Black-Triangle Watch (A15)    NOMINAL (Δ 2.5)
   ├─ KELNO (Air)     → Air Temple (A18)               HARD (Δ 6.5 over bugbears)
   ├─ ALRREM (Fire)   → Fire Temple (A17)              NOMINAL (Δ −0.5 — PEER w/ hydra)
   └─ BELSORNIG (Water)→ Water Temple (A16)            NOMINAL (Δ 2.5)
                       → Oohlgrist troll chief (CR5)   NOMINAL (Δ 0 over trolls)

LARETH THE BEAUTIFUL (New Master — CR ~8)              [HARD]
├─ Moathouse dungeon garrison (A8)                      HARD (Δ 7)
├─ Temple Guards / Eyes of Fire (A11)                   HARD (Δ 7.5)
├─ Gnoll warband (B10, nominated Snarl-tooth)           NOMINAL (Δ 0)
└─ (Lubash's ogres, A9, separate — NOMINAL solo)

TOLUB (CR 8) & GRUD SQUINTEYE (CR 6)  [Nulb pirate captains]   [HARD]
└─ Nulb brigands (A12)                                   HARD (Δ 7.5 / 5.5)

BURNE & RUFUS (Guard Tower — CR ~9, Good, independent)  [HARD]
├─ Guard Tower garrison (A3)                             HARD (Δ ~8.5)
└─ Burne's Badgers (B4, nominated Halla Broadshield)    NOMINAL (Δ 0)

RANNOS DAVL (CR 3) & GREMAG (CR 8)  [Trading Post]      [HARD via Gremag]
└─ reports to Temple brigand courier → Hedrack

GRANK (cleric, CR 2)  [Bargent's Road Brigands]         NOMINAL (Δ 1.875)

INDEPENDENT / AMBIENT (NO BOSS):
  Welcome Wench lodgers (B2, named individuals), Moathouse ruins fauna (B6),
  Hommlet dogs (B7), Lower Warren (B21), Deep Scavengers (B22, trolls→Oohlgrist),
  Relic Wardens (B23), Pit Spawn (B24), Sealed Patrol (B28),
  Moathouse brigand garrison (B5, nominated Varl — NOMINAL)
```

---

## D. Summary table

| Tribe | Boss (module name) | Rank CR | Boss CR | Δ | Classification |
|---|---|---|---|---|---|
| A1 Trading Post | Gremag (assassin)¹ | 1/2 | 8 | 7.5 | **HARD** |
| A3 Guard Tower | Burne & Rufus | 1/2 | ~9 | ~8.5 | **HARD** |
| A8 Moathouse dungeon | Lareth the Beautiful | 1 | ~8 | ~7 | **HARD** |
| A9 Blackthorn ogres | Lubash (named ogre) | 2 | 2 | 0 | NOMINAL |
| A11 Temple Guards (Eyes of Fire) | Lareth the Beautiful | 1/2 | ~8 | 7.5 | **HARD** |
| A12 Nulb brigands | Tolub / Grud Squinteye | 1/2 | 8 / 6 | 7.5 / 5.5 | **HARD** |
| A13 Greater Temple Brigands | Feldrin | 3 | 6 (5–7) | 3 (→4 at 7) | NOMINAL · **NOMINAL+ flagged** |
| A14 Earth Temple | Romag | 5 | 7.5 (7–8) | 2.5 | NOMINAL |
| A15 Black-Triangle Watch | Romag | 5 | 7.5 (7–8) | 2.5 | NOMINAL |
| A16 Water Temple | Belsornig | 5 | 7.5 (7–8) | 2.5 | NOMINAL |
| A17 Fire Temple | Alrrem | 8 | 7.5 (7–8) | −0.5 | NOMINAL (peer) |
| A18 Air Temple | Kelno | 1 | 7.5 (7–8) | 6.5 | **HARD** |
| A19 Blackplate Wardens | Hedrack (meta-chain) | 1 | 6 | 5 | **HARD** |
| A25 Zuggtmoy's Menagerie | Zuggtmoy (apex) | 5 | 23 | 18 | **HARD (apex)** |
| A26 Prison Shadows | Zuggtmoy / Iuz (apex) | 5 | 23 | 18 | **HARD (apex)** |
| A27 Fungal Brood | Zuggtmoy (apex) | 4 | 23 | 19 | **HARD (apex)** |
| A29 Temple Host | Hedrack | 5 | 6 | 1 | NOMINAL |
| A30 Inner Sanctum | Hedrack | 5 | 6 | 1 | NOMINAL |
| A31 Air Node | Whispering Wind (apex) | 9 | 19 (17–21) | 10 | **HARD (apex)** |
| A32 Earth Node | Black Earth (apex) | 7 | 19 (17–21) | 12 | **HARD (apex)** |
| A33 Fire Node | Eternal Flame (apex) | 17 | 19 (17–21) | 2 | NOMINAL (apex, peer) |
| A34 Water Node | Crushing Wave (apex) | 17 | 19 (17–21) | 2 | NOMINAL (apex, peer) |
| A35 Bargent's Road Brigands | Grank (cleric) | 1/8 | 2 | 1.875 | NOMINAL |
| B4 Burne's Badgers (nominated) | Halla Broadshield | 1/2 | 1/2 | 0 | NOMINAL |
| B5 Moathouse brigand garrison (nominated) | Varl "Black-Jack" | 1/2 | 1/2 | 0 | NOMINAL |
| B10 Gnoll warband (nominated) | Snarl-tooth | 1/2 | 1/2 | 0 | NOMINAL |
| B20 Dungeon Jailers (nominated) | Turnkey Varl | 5 | 5 | 0 | NOMINAL |
| B2 Welcome Wench lodgers | none (named individuals) | — | — | — | NO BOSS |
| B6 Moathouse ruins fauna | none | var | — | — | NO BOSS |
| B7 Hommlet dogs | none | 1/4 | — | — | NO BOSS |
| B21 Lower Warren | none | var | — | — | NO BOSS |
| B22 Deep Scavengers | none (trolls→Oohlgrist) | var | — | — | NO BOSS |
| B23 Relic Wardens | none | var | — | — | NO BOSS |
| B24 Pit Spawn | none | var | — | — | NO BOSS |
| B28 Sealed Patrol | none | var | — | — | NO BOSS |

¹ Rannos Davl (CR 3) is Gremag's co-leader; he alone would be NOMINAL (Δ 2.5). Gremag is the decisive HARD boss.

---

## Bottom line

- **HARD bosses: 12** — Trading Post (Gremag), Guard Tower (Burne/Rufus), Moathouse dungeon garrison (Lareth), Temple Guards (Lareth), Nulb brigands (Tolub & Grud), Air Temple (Kelno), Blackplate Wardens (Hedrack), and Zuggtmoy's three tribes (Menagerie, Prison Shadows, Fungal Brood) plus the two "hard" node princes (Whispering Wind, Black Earth). Of these, **7 are named mortal bosses** and **5 are apex creatures** (Zuggtmoy ×3, 2 node princes).
- **NOMINAL+ (borderline-hard): 1** — Greater Temple Brigands under **Feldrin** (NOMINAL at his central CR 6; flagged NOMINAL+ if he sits at CR 7, where Δ = 4 exactly). Never silently called "hard."
- **NOMINAL bosses: 14** — Lubash (solo), Romag (Earth Temple + Black-Triangle Watch), Belsornig (Water Temple), Alrrem (Fire Temple, *peer/negative Δ vs the hydra*), Hedrack (Temple Host + Inner Sanctum, NOMINAL over his giants/trolls), the two "peer" node princes (Eternal Flame, Crushing Wave, *near-equals of their red dragons/dragon turtle*), Grank, and the four NOMINATED commander tribes (Burne's Badgers, Moathouse brigand garrison, Gnoll warband, Dungeon Jailers).
- **NO BOSS (ambient/independent): 8** — Welcome Wench lodgers, Moathouse ruins fauna, Hommlet dogs, Lower Warren, Deep Scavengers, Relic Wardens, Pit Spawn, Sealed Patrol.

**Key finding:** The four Elemental High Priests are **mostly NOMINAL** over their *own* cult troops — Romag, Belsornig and Alrrem each sit within 3 CR of their hardest soldiers (earth elementals/trolls/juggernaut at CR 5; Alrrem is actually *weaker* than his bound CR-8 hydra). Only **Kelno** is HARD, purely because the Air Temple's rank-and-file are merely bugbears/goblins (no CR-5 elemental to close the gap). The genuine **HARD** power in the Temple is concentrated at two levels: (1) the **apex layer** — Zuggtmoy (CR 23) and the node princes (CR 17–21) — and (2) the **surface/Outer** bosses who command weak humanoid rank-and-file — Gremag, Burne/Rufus, Lareth, Tolub/Grud, and Hedrack over his bugbears. **Hedrack himself is only NOMINAL over his elite garrison** (hill giants/trolls at CR 5, Δ = 1) despite being the Supreme Commander — his printed CR is 6, *not* the ~11 the appendix note estimates.

**Borderline NOMINAL+ flagged:** Feldrin (Greater Temple Brigands) — NOMINAL at central CR 6, becomes NOMINAL+ (Δ = 4) at the top of his 5–7 CR range. Review before finalizing his stat.

**Companion files:** `monsters_phase1_scan.md` (consolidated scan), `monsters_phase2_descriptions.md` (named tribes + individuals), `monsters_cr_reference.md` (CR source table), `_leadership_flattened.txt` (Greater Temple chain of command), `_nulb_flattened.txt` (Nulb relationships).
