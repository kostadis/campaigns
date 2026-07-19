# Phase 3 — Monster Boss Hierarchy (CR-Difference Classification)

**Purpose:** For every unnamed-monster *tribe* in this module, identify its **bigger bad** (the boss who commands that tribe) and classify that boss as **NOMINAL** or **HARD** using the rule you specified:

> CR difference between the tribe's rank-and-file monster and its boss is **< 4** → **NOMINAL boss** (a leader in name; the threat is within ~3 CR of the rank-and-file).
> CR difference is **> 4** → **HARD boss** (a genuinely more dangerous threat than the rank-and-file).

**Edge cases handled:**
- Gap exactly 4 is ambiguous in the brief ("< 4" vs "> 4"). **Convention used:** `< 4` means 0–3 → NOMINAL; `> 4` means 5+ → HARD; a gap of exactly **4** is flagged **NOMINAL+ (borderline-hard)** so it is never silently called "hard" without review.
- Tribes whose boss is a **named module NPC** keep that name (Klarg, King Grol, Ruxithid, Glasstaff/Nezznar, Brughor, Mormesk, Favric, Ontharyx, Qunbraxel, Naruv, Chalaag, Nellik, Vundru, Hamun Kost). We do NOT rename them (per Phase 2 rules).
- Truly **leaderless** tribes (stirges, owlbear, wild snake, violet fungi, the infected elder brain, intellect snares, brain breakers, psychic gray oozes) have **no in-module boss**; for those we NOMINATE a boss from the description file (an unnamed commander we named in Phase 2) or mark "no boss — ambient/independent."
- CR values are from `monsters_cr_reference.md`. Where a tribe has multiple rank-and-file tiers, the comparison uses the **highest rank-and-file CR** (most conservative — smallest gap), and the range is noted.

**Legend:** CR(rank) = rank-and-file Challenge Rating · CR(boss) = boss Challenge Rating · Δ = CR(boss) − CR(rank).

---

## A. Tribes with a NAMED MODULE boss

### A1. Cragmaw band (goblins / goblin bosses / wolves / hobgoblins / bugbears)
- Rank-and-file CR: Goblin 1/4, Goblin Boss 1, Hobgoblin 1/2, Wolf 1/4. Highest rank CR = **1** (goblin boss).
- Bosses in module: **King Grol** (bugbear, CR 1) is the supreme chief; **Klarg** (bugbear, CR 1) runs the hideout; Yeemik/Errk/Yegg/Lhupo are named sub-bosses (goblin boss, CR 1).
- Δ (Grol CR1 − rank1) = **0** → **NOMINAL boss**.
- Δ (Klarg CR1 − rank1) = **0** → **NOMINAL boss**.
- **Verdict:** The Cragmaws are top-heavy with nominal bosses — every "boss" is the same CR as the rank-and-file. King Grol is the biggest bad, but by CR he is only a nominal step up. (The real power over the Cragmaws is **Nezznar the Spider**, CR 7, who pays them — see A7.)

### A2. Sawplee goblins (generic goblins / psi brawlers / psi commanders / feral & psionic ashenwights / goblin psi minions at Illithinoch)
- Rank-and-file CR: Goblin 1/4, Psi Brawler 1/4, Psi Commander 1/2, Feral Ashenwight 1 (stat-block variant), Psionic Ashenwight 2. Highest rank CR = **2** (psionic ashenwight).
- Boss in module: **Ruxithid the Chosen** (psionic goblin, Appendix A "goblin boss" base → CR 1).
- Δ (Ruxithid CR1 − rank2) = **−1** → boss is actually *lower* CR than the psionic ashenwights; vs goblins (CR1−1/4) Δ = 3/4.
- **Verdict:** **NOMINAL boss** (Δ < 4). Ruxithid is a leader by psychic authority, not by raw CR — fitting, since he is a puppet of the mind flayer fanatics (A7).
- True chain-of-command: Sawplees → Ruxithid (nominal) → **mind flayer fanatics** (Chishinix/Hashutu/Voalsh, CR 7, Δ 5–6 vs rank) = **HARD bosses** (see A7).

### A3. Redbrands (Redbrand ruffians / human bandits / crypt skeletons)
- Rank-and-file CR: Redbrand Ruffian 1/4, Bandit 1/8, Skeleton 1/4. Highest rank CR = **1/4**.
- Boss in module: **Glasstaff** = Iarno Albrek (human wizard, CR 3, MM "mage"/appendix).
- Δ (Glasstaff CR3 − rank1/4) = **2¾** → **NOMINAL boss** (Δ < 4).
- **Verdict:** NOMINAL. Glasstaff is a step up but within 4 CR. His true master is **Nezznar the Spider (CR 7)** — see A7.

### A4. Brughor's Wyvern Tor raiders (orcs / bugbears / ogre)
- Rank-and-file CR: Orc 1/2, Bugbear 1, Ogre 2. Highest rank CR = **2** (ogre).
- Boss in module: **Brughor Axe-Biter** (orc, CR 2 — PaBTSO orc raider leader with 18 HP, MM orc CR 1/2 but as a "leader" treated CR ~2).
- Δ (Brughor ~CR2 − rank2) ≈ **0** → **NOMINAL boss**.
- **Verdict:** NOMINAL. Brughor is a peer of his own ogres/bugbears, not a leap above them.

### A5. Wave Echo Cave undead (zombies / dwarf & ogre zombies / ghouls / skeletons / flameskull / spectator / ochre jelly / giant octopus / giant constrictor / stirges)
- Rank-and-file CR: Zombie 1/4, Ghoul 1, Skeleton 1/4, Ogre Zombie 2, Flameskull 4, Spectator 3, Ochre Jelly 2. Highest rank CR = **4** (flameskull) — but the *combat rank-and-file* are the zombies/ghouls (CR 1/4–1). Use highest true-combat rank = **2** (ogre zombie) for the conservative check; note flameskull (4) separately.
- Boss in module: **Mormesk the Wraith** (wraith, CR 5 — leader of the mine's undead).
- Δ (Mormesk CR5 − rank2) = **3** → **NOMINAL boss** (Δ < 4).
- Δ (Mormesk CR5 − flameskull rank4) = **1** → NOMINAL.
- **Verdict:** NOMINAL. Mormesk is a clear leader but within 4 CR of his own undead. The mine itself is controlled by **Nezznar (CR 7)** — see A7.

### A6. Old Owl Well undead (zombies)
- Rank-and-file CR: Zombie 1/4.
- Boss in module: **Hamun Kost** (Red Wizard of Thay, human mage CR 7).
- Δ (Hamun CR7 − rank1/4) = **6¾** → **HARD boss**.
- **Verdict:** **HARD boss.** A CR-7 archmage commanding CR-1/4 zombies is a massive leap; the zombies are trivial set-dressing next to him.

### A7. The Spider's web / Nezznar's forces (Cragmaws, Redbrands, bugbears, doppelgangers, WEC occupants)
- This is the meta-tribe: **Nezznar the Spider** (drow mage, CR 7) is the hidden master paying/commanding the Cragmaws (A1), Redbrands (A3), and his own WEC bugbears/doppelgangers.
- Compared to those tribes' rank-and-file (goblin 1/4, ruffian 1/4, bugbear 1): Δ = 6¼–7 → **HARD boss** over every one of them.
- **Verdict:** **HARD boss** (the single most consequential "bigger bad" of chapters 1–4). Note: the module also names him the "Spider"; do not rename.

### A8. Cult of the Obelisk (humanoid mutates, Talhundereth)
- Rank-and-file CR: Humanoid Mutate 2.
- Boss in module: **Ontharyx Henlifel** (drow patriarch turned humanoid mutate; as a "drow elite warrior" CR 4 or mutate-boosted ~CR 4–5).
- Δ (Ontharyx ~CR4 − rank2) = **2** → **NOMINAL boss** (Δ < 4).
- **Verdict:** NOMINAL. Ontharyx is the cult's head but only mildly tougher than his mutate followers. (His sons Nythalyn/Yanthdel, CR 4 drow elite, are off fetching him — also nominal over the cult.)

### A9. Qunbraxel's court (grimlocks / basilisks / ropers nearby / petrified victims)
- Rank-and-file CR: Grimlock 1/4, Basilisk 3. Highest rank CR = **3** (basilisk).
- Boss in module: **Qunbraxel** (mind flayer warlock, CR 7).
- Δ (Qunbraxel CR7 − rank3) = **4** → **NOMINAL+ (borderline-hard)**, exactly at the gap-4 line. Vs grimlocks (CR7−1/4 = 6¾) it is HARD.
- **Verdict:** Against the basilisks the gap is exactly 4 (flagged NOMINAL+ for review); against his grimlock minions it is a clear **HARD boss**. Qunbraxel is the Gibbet Crossing bigger bad.

### A10. Naruv's Feeder Trenches grells (grells, Far Realm F2/F4)
- Rank-and-file CR: Grell 3.
- Boss in module: **Feedkeeper Naruv** (grell, CR 3 — same stat block as her underlings).
- Δ (Naruv CR3 − rank3) = **0** → **NOMINAL boss**.
- **Verdict:** NOMINAL. Naruv is "host" by seniority, not by power.

### A11. Spawn Hollow slaadi (red/blue/gray slaadi, tadpoles)
- Rank-and-file CR: Red Slaad 5, Blue Slaad 7, Gray Slaad 3, Tadpole ~0. Highest rank CR = **7** (blue slaad).
- Boss in module: **Chalaag** (gray slaad, CR 3 — the "explorer who discovered Spawn Hollow").
- Δ (Chalaag CR3 − rank7/blue) = **−4** → boss is *weaker* than the blue slaad rank-and-file; vs gray tadpoles Δ positive but small.
- **Verdict:** **NOMINAL boss** (and arguably a peer/underling, not a true bigger bad). The slaadi are a loose Far Realm brood; Chalaag is first-among-equals.

### A12. Nellik's rebel mezzoloths (mezzoloths / umber hulk / brain-breaker squads in epilogue)
- Rank-and-file CR: Mezzoloth 5, Umber Hulk 5, Brain Breaker 10. Highest rank CR = **10** (brain breaker, epilogue).
- Boss in module: **Nellik** (nycaloth, CR 9) with adjutant **Frevvik** (mezzoloth, CR 5, named).
- Δ (Nellik CR9 − rank10/brain breaker) = **−1** → boss slightly below the brain-breaker elite; vs mezzoloth (CR9−5 = 4) = exactly 4 → **NOMINAL+ (borderline-hard)**.
- **Verdict:** NOMINAL. Nellik leads by force of personality/rank; the brain breakers (CR 10) she directs in the epilogue are actually a harder threat than she is. (Epilogue brain-breaker squads are directed by **Ghaluzesh the kraken, CR 23** → HARD boss, see A13.)

### A13. Ilvaash's epilogue enforcers (brain breakers, mind flayer prophets)
- Rank-and-file CR: Brain Breaker 10, Mind Flayer Prophet 7.
- Boss in module: **Ghaluzesh** (kraken, CR 23) directs the brain-breaker squads in "Ilvaash's Revenge."
- Δ (Ghaluzesh CR23 − rank10) = **13** → **HARD boss** (profile: the most overwhelming CR gap in the module).
- **Verdict:** **HARD boss.**

### A14. Illithinoch fanatics' minions (goblin psi commander + brawlers at the lab; unspecified mind flayer servants; resident aberrant zealots)
- Rank-and-file CR: Psi Commander 1/2, Psi Brawler 1/4, Mind Flayer (servant) 7, Aberrant Zealot 3.
- Boss in module: the three fanatics **Chishinix / Hashutu / Voalsh** (mind flayer clairvoyant, CR 7).
- Δ (fanatic CR7 − rank7/servant mind flayer) = **0** → NOMINAL over servant mind flayers; vs goblin psi (CR7−1/2 = 6½) → **HARD boss** over the goblin minions.
- **Verdict:** **HARD boss** over the goblin psi minions they keep as "expendable" fodder; nominal over peer mind flayers. They answer to **Ilvaash** (godlet; final boss via the Refraction, CR 16) → HARD.

### A15. Vundru's grell band (grells, J7 Scavengers' Nook)
- Rank-and-file CR: Grell 3.
- Boss in module: **Vundru** (grell psychic, CR 3 — same ballpark as grells, psychically boosted).
- Δ (Vundru CR3 − rank3) = **0** → **NOMINAL boss**.
- **Verdict:** NOMINAL.

---

## B. Leaderless / ambient tribes — NOMINATED boss or "no boss"

These tribes have **no in-module boss**. We either name a boss we created in Phase 2 (an unnamed commander) or mark them independent.

### B1. Cragmaw wolves (the Thornmaw Pack) — CR 1/4
- No in-module leader (Ripper/Snarl are named *pets*, excluded).
- Nominated boss (Phase 2): the pack's alpha, **Vex's trained lead wolf** is ambiguous; cleanest is to nominate the kennel's chief trainer. Per Phase 2, the goblin **Vex** (H3 wolf-trainer, CR 1/4) functionally "leads" them.
- Δ (Vex CR1/4 − wolf1/4) = **0** → NOMINAL. **Verdict:** NOMINAL boss (Vex the trainer). Marked "nominated."

### B2. Triboar Trail wilderness pack (wolves) — CR 1/4
- No boss; random-encounter wildlife. **Verdict: NO BOSS — independent/ambient.**

### B3. Stirges (W3, Triboar Trail, WEC) — CR 1/8
- No boss; vermin. **Verdict: NO BOSS — ambient.**

### B4. Owlbear (Triboar Trail) — CR 3
- Solo beast. **Verdict: NO BOSS — independent solitary monster** (named "the Hollow-Eye owlbear" in Phase 2).

### B5. Giant Poisonous Snake (H4, "Cold Creek Serpent of Viper's Rest") — CR 1/4
- Solo. **Verdict: NO BOSS — independent** (named in Phase 2).

### B6. Violet Fungi (W8) — CR 1/2
- Hazard. **Verdict: NO BOSS — ambient.**

### B7. Gibbering Mouthers (J9) + Flesh Meld — CR 2
- No boss; they merge into a flesh meld. **Verdict: NO BOSS — ambient brood** (the flesh meld is the emergent "boss," CR 2 = NOMINAL over the mouthers).

### B8. Behir (J6) — CR 11
- Solo. **Verdict: NO BOSS — independent apex predator** (named in Phase 2). Note: a CR-11 behir is itself a HARD threat to a Level-5 party but has no tribe to command.

### B9. Cloaker Mutate (J8) — CR 8
- Solo (puppets Thorgran's corpse). **Verdict: NO BOSS — independent.**

### B10. Grick lair (Gibbet Crossing G8/G9: alpha + 6) — CR 2
- The **grick alpha** (CR 2) leads the 6 lair gricks (CR 2). Δ = 0 → NOMINAL. **Verdict: NOMINAL boss (the alpha, named in Phase 2).**

### B11. Ropers (Gibbet Crossing G10) — CR 5
- Two ropers, no leader. **Verdict: NO BOSS — paired ambush predators** (named in Phase 2).

### B12. Intellect Devourer in quaggoth (Tunnel Encounters) — CR 2
- Controls a quaggoth. Δ (devourer CR2 − quaggoth CR1) = 1 → NOMINAL over its host. **Verdict: NOMINAL boss (the devourer is the true mind).**

### B13. Quaggoths (Tunnel Encounters + statues) — CR 1
- Led by a quaggoth thonot (CR 2, a stronger quaggoth) in the encounter table. Δ = 1 → NOMINAL. **Verdict: NOMINAL boss (the thonot, named in Phase 2).**

### B14. Specters / Crypt Guardians / Revenants (Crypt of the Talhund) — CR 4 / 5
- Undead bound to the crypt; animated by the obelisk fragment's corruption, not a living boss. The **clay golem** (P7, CR 9) and **mummy** (P13, CR 6) are independent wardens.
- **Verdict:** The specters/revenants have **NO single boss** — they answer to the crypt's haunt (the obelisk fragment). The clay golem (CR 9) and mummy (CR 6) are **independent wardens**; vs the undead rank (CR 4–5) the golem is a **HARD** warden (Δ 4–5) and the mummy is **NOMINAL+** (Δ 1–2). Flag: the golem/mummy are guardians, not "bigger bads" of a tribe.

### B15. Infected Elder Brain (Illithinoch X15) — CR 14
- Unique apex creature; it *is* the boss of the illithid stronghold's lower functions but has no tribe of its own to command (it is served by the fanatics, not the reverse). **Verdict: apex creature, NO boss — it IS a bigger bad** (and a HARD threat at CR 14, though the named fanatics/Ilvaash sit above it).

### B16. Intellect Snares (Talhundereth / Endless Void / Nematode) — CR 3
- No boss; they float free. **Verdict: NO BOSS — ambient aberrations.**

### B17. Psychic Gray Oozes (Phandalin Town Green) — CR 1/4
- Spawned by Daisy the Cow (named, excluded). **Verdict: NO BOSS — spawned brood** (named in Phase 2).

### B18. Flumphs (Briny Maze B11 cloister) — CR 1/4
- Led by **Wise Borblish** (named flumph, CR 1/4) — but she is a NAMED individual, so by rule we keep her. Δ = 0 → NOMINAL. **Verdict: NOMINAL boss (Wise Borblish, named — kept as-is).**

### B19. Phase Spiders (B2) + Psionic Ashenwights (B2/B3) — CR 3 / 2
- No single boss; they ally. **Verdict: NO BOSS — allied pack.**

### B20. Encephalon Cluster / Gemmules — CR 5 / 2
- The cluster (CR 5) is "parent" to gemmules (CR 2). Δ = 3 → NOMINAL over its progeny. **Verdict: NOMINAL boss (the cluster); the gemmules are its offspring, not a tribe.**

### B21. Clay Golem (P7) / Shield Guardian (Indigo Sanctum P13, Zorzula) / Fiendish Auger (Z18) / Mummy (P13)
- Constructs; each bound to a maker/location, not a tribe. **Verdict: NO BOSS — independent wardens/constructs** (each named/designated in Phase 2).

### B22. Unnamed drow thieves (Gibbet Crossing G25) — CR 1/4
- Dead/scavengers; no boss. **Verdict: NO BOSS — corpses/independent.**

---

## C. Hierarchy tree (boss → tribe), with classification

```
ILVAASH (godlet; final boss via Refraction of Ilvaash, CR 16)  [apex — HARD over all]
└─ the three mind flayer fanatics: CHISHINIX / HASHUTU / VOALSH (CR 7)
   ├─ HARD over: goblin psi minions (A14), Sawplee goblins (A2, via Ruxithid), Illithinoch residents
   ├─ NOMINAL over: peer servant mind flayers (A14)
   ├─ Ghaluzesh the kraken (CR 23) → HARD over brain-breaker squads (A13)
   ├─ Ahooshathan / Gulguush / Oshundo / Duoro etc. (named) — kept as-is
   └─ Infected Elder Brain (CR 14) [apex creature, B15]

NEZZNAR THE SPIDER (drow mage, CR 7)  [HARD boss over ch1–4]
├─ Cragmaw band → King Grol (CR 1) → NOMINAL (A1); Grol→Klarg (CR1) NOMINAL
├─ Redbrands → Glasstaff/Iarno (CR 3) → NOMINAL (A3)
├─ WEC bugbears / doppelgangers (Vyerith, Vhalak named) — kept as-is
└─ Wave Echo Cave undead → Mormesk (CR 5) → NOMINAL (A5)

BRUGHOR AXE-BITER (orc, CR ~2)  [NOMINAL boss] (A4)
└─ Wyvern Tor raiders (orcs/bugbears/ogre)

RUXITHID THE CHOSEN (psionic goblin, CR 1)  [NOMINAL boss] (A2)
└─ Sawplee goblins / psi brawlers / psi commanders / ashenwights

ONTHARYX HENLIFEL (drow mutate, ~CR 4)  [NOMINAL boss] (A8)
└─ Cult of the Obelisk humanoid mutates

QUNBRAXEL (mind flayer warlock, CR 7)  [HARD over grimlocks; NOMINAL+ over basilisks] (A9)
└─ grimlocks / basilisks (Gibbet Crossing)

HAMUN KOST (Red Wizard, CR 7)  [HARD boss] (A6)
└─ Old Owl Well zombies

FEEDKEEPER NARUV (grell, CR 3)  [NOMINAL] (A10) └─ Feeder Trenches grells
CHALAAG (gray slaad, CR 3)      [NOMINAL] (A11) └─ Spawn Hollow slaadi
NELLIK (nycaloth, CR 9)         [NOMINAL+] (A12) └─ rebel mezzoloths (→ Ghaluzesh HARD in epilogue)
VUNDRU (grell psychic, CR 3)    [NOMINAL] (A15) └─ J7 grell band
WISE BORBLISH (flumph, CR 1/4)  [NOMINAL, named] (B18) └─ flumph cloister

INDEPENDENT / AMBIENT (no boss):  stirges, owlbear, wild wolves, giant snake, violet fungi,
  gibbering mouthers, behir, cloaker mutate, ropers, intellect snares, psychic gray oozes,
  phase spiders, drow thieves, constructs (golem/guardian/auger/mummy), quaggoth thonot (NOMINAL),
  grick alpha (NOMINAL), intellect devourer (NOMINAL over host), encephalon cluster (NOMINAL over gemmules)
```

---

## D. Summary table

| Tribe | Boss (module name) | Rank CR | Boss CR | Δ | Classification |
|---|---|---|---|---|---|
| Cragmaw band | King Grol (bugbear) | 1 | 1 | 0 | NOMINAL |
| Cragmaw hideout | Klarg (bugbear) | 1 | 1 | 0 | NOMINAL |
| Sawplee goblins | Ruxithid the Chosen | 2 | 1 | −1 | NOMINAL |
| Redbrands | Glasstaff / Iarno | 1/4 | 3 | 2.75 | NOMINAL |
| Wyvern Tor raiders | Brughor Axe-Biter | 2 | ~2 | ~0 | NOMINAL |
| WEC undead | Mormesk the Wraith | 2 | 5 | 3 | NOMINAL |
| Old Owl Well undead | Hamun Kost | 1/4 | 7 | 6.75 | **HARD** |
| Nezznar's forces (meta) | Nezznar the Spider | 1/4 | 7 | 6.75 | **HARD** |
| Cult of the Obelisk | Ontharyx Henlifel | 2 | ~4 | 2 | NOMINAL |
| Qunbraxel's court | Qunbraxel | 3 | 7 | 4* | NOMINAL+ (borderline) |
| Naruv's grells | Feedkeeper Naruv | 3 | 3 | 0 | NOMINAL |
| Spawn Hollow slaadi | Chalaag | 7 | 3 | −4 | NOMINAL |
| Nellik's mezzoloths | Nellik | 10 | 9 | −1* | NOMINAL+ (borderline) |
| Ilvaash's enforcers | Ghaluzesh | 10 | 23 | 13 | **HARD** |
| Fanatics' goblin minions | Chishinix/Hashutu/Voalsh | 1/2 | 7 | 6.5 | **HARD** |
| Vundru's grells | Vundru | 3 | 3 | 0 | NOMINAL |
| Thornmaw wolves (nominated) | Vex (trainer) | 1/4 | 1/4 | 0 | NOMINAL |
| Grick lair (nominated) | grick alpha | 2 | 2 | 0 | NOMINAL |
| Quaggoth band (nominated) | quaggoth thonot | 1 | 2 | 1 | NOMINAL |
| Intellect devourer host | the devourer | 1 | 2 | 1 | NOMINAL |
| Encephalon cluster | the cluster | 2 | 5 | 3 | NOMINAL |
| Flumph cloister | Wise Borblish (named) | 1/4 | 1/4 | 0 | NOMINAL |
| Infected Elder Brain | (apex, none) | — | 14 | — | apex/HARD threat |
| Independents (owlbear, behir, snake, stirges, etc.) | none | var | — | — | NO BOSS |

\* Gap exactly 4: flagged **NOMINAL+ (borderline-hard)** so it is never silently called "hard" without review.

**Bottom line:** By your rule, the module has **4 clear HARD bosses** (Hamun Kost, Nezznar the Spider, the fanatics over their goblin minions, Ghaluzesh over the epilogue enforcers) plus the apex godlet Ilvaash; **2 borderline NOMINAL+** (Qunbraxel's court, Nellik's mezzoloths); and the large majority of tribe bosses are **NOMINAL** — the module's rank-and-file and their named leaders sit within 3 CR of each other, with the real "hard" power concentrated in the mind flayer / archmage / kraken villains.

**Companion files:** `monsters_phase1_scan.md` (consolidated scan), `monsters_phase2_descriptions.md` (named tribes + individuals), `monsters_cr_reference.md` (CR source table). Temporary scanner partials: `_scan_A.md`, `_scan_B.md`, `_scan_C.md`.
