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

> ## ⚠ Recomputed 2026-08-22
>
> Every Δ in this file is derived from `monsters_cr_reference.md`, and **28 of that file's 95 CRs were wrong**.
> The table has been regenerated deterministically from the 5etools canonical bestiary and every Δ below has
> been recomputed against it. **Three verdicts flipped:**
>
> | Section | Boss | Was | Is | Why |
> |---|---|---|---|---|
> | **A7** | Nezznar the Spider | HARD | **NOMINAL** | He has his own PaBTSO block at **CR 2**; the old figure was the MM *drow mage*, CR 7 |
> | **A9** | Qunbraxel | NOMINAL+ | **HARD** | CR **9**, not 7 — clears the gap-4 line by two |
> | **B20** | Encephalon Cluster | NOMINAL | **HARD** | Cluster **10**, gemmules **3** — Δ 7, not 3 |
>
> **Two boss CRs here were invented rather than looked up**, and both are corrected in place:
> **Brughor Axe-Biter** (was "~CR 2 as a leader"; the module says "an orc with 18 hit points" — MM Orc, **CR 1/2**)
> and **Chalaag** (was CR 3; the module says "the gray slaad explorer," so MM Gray Slaad, **CR 9**). Both verdicts
> survive, but the *reasoning* in A4 and A11 inverted — in each case the file had the boss on the wrong side of
> its own troops.
>
> **Verified correct, against expectation:** Ghaluzesh at CR 23. He carries no PaBTSO stat block because he is
> simply a kraken (A13).
>
> **The pattern.** Nothing was wrong with the *classification logic* — the rule was applied consistently every
> time. The errors all entered as unchecked inputs and were then amplified into verdicts. Regenerate the CR
> table first, re-run the Δ math second; never hand-edit a CR in either file.

---

## A. Tribes with a NAMED MODULE boss

### A1. Cragmaw band (goblins / goblin bosses / wolves / hobgoblins / bugbears)
- Rank-and-file CR: Goblin 1/4, Goblin Boss 1, Hobgoblin 1/2, Wolf 1/4. Highest rank CR = **1** (goblin boss).
- Bosses in module: **King Grol** (bugbear, CR 1) is the supreme chief; **Klarg** (bugbear, CR 1) runs the hideout; Yeemik/Errk/Yegg/Lhupo are named sub-bosses (goblin boss, CR 1).
- Δ (Grol CR1 − rank1) = **0** → **NOMINAL boss**.
- Δ (Klarg CR1 − rank1) = **0** → **NOMINAL boss**.
- **Verdict:** The Cragmaws are top-heavy with nominal bosses — every "boss" is the same CR as the rank-and-file. King Grol is the biggest bad, but by CR he is only a nominal step up. (The real power over the Cragmaws is **Nezznar the Spider** — who pays them, and who is only **CR 2**; see A7.)

### A2. Sawplee goblins (generic goblins / psi brawlers / psi commanders / feral & psionic ashenwights / goblin psi minions at Illithinoch)
- Rank-and-file CR: Goblin 1/4, Psi Brawler **2**, Psi Commander **4**, Feral Ashenwight **5**, Psionic Ashenwight **7**. Highest rank CR = **7** (psionic ashenwight).
- Boss in module: **Ruxithid the Chosen** (psionic goblin, own Appendix A block → CR **5**).
- Δ (Ruxithid CR5 − rank7) = **−2** → the boss is genuinely *below* his own psionic ashenwights; against plain goblins (5 − 1/4) Δ = **4¾**, which is HARD.
- **Verdict:** **NOMINAL boss** (Δ < 4). Ruxithid is a leader by psychic authority, not by raw CR — fitting, since he is a puppet of the mind flayer fanatics (A7).
- True chain-of-command: Sawplees → Ruxithid (nominal) → **mind flayer fanatics** (Chishinix/Hashutu/Voalsh, mind flayer clairvoyant, CR **11**; Δ 7 vs the psi commanders) = **HARD bosses** (see A14).

### A3. Redbrands (Redbrand ruffians / human bandits / crypt skeletons)
- Rank-and-file CR: Redbrand Ruffian **1/2**, Bandit 1/8, Skeleton 1/4. Highest rank CR = **1/2**.
- Boss in module: **Glasstaff** = Iarno Albrek (own PaBTSO block → CR **1**).
- Δ (Glasstaff CR1 − rank1/2) = **½** → **NOMINAL boss** (Δ < 4).
- **Verdict:** NOMINAL, and far more so than this file used to say. Glasstaff is barely above his own ruffians — which is exactly how he played at the table in Ch. 6: wounded by a *Firebolt* and a javelin, and gone. His master **Nezznar** is CR **2**, not 7 — see A7.

### A4. Brughor's Wyvern Tor raiders (orcs / bugbears / ogre)
- Rank-and-file CR: Orc 1/2, Bugbear 1, Ogre 2. Highest rank CR = **2** (ogre).
- Boss in module: **Brughor Axe-Biter** — the text says plainly "an orc with 18 hit points." No special block: MM **Orc, CR 1/2**, with bumped HP. *(The old CR 2 here was invented.)*
- Δ (Brughor CR1/2 − rank2) = **−1½** → **NOMINAL boss**.
- **Verdict:** NOMINAL — and inverted from what this file used to claim. Brughor is the **weakest thing in his own cave**: his ogre Gog is CR 2 and each of his four bugbears is CR 1. **Table note:** the module says the rest of the band *flees if Brughor is killed*, so the softest target in the room is also the off-switch for the encounter. Worth knowing before Wyvern Tor, which is both Harbin's 120-gp job and one of Hamun Kost's two favours.

### A5. Wave Echo Cave undead (zombies / dwarf & ogre zombies / ghouls / skeletons / flameskull / spectator / ochre jelly / giant octopus / giant constrictor / stirges)
- Rank-and-file CR: Zombie 1/4, Ghoul 1, Skeleton 1/4, Ogre Zombie 2, Flameskull 4, Spectator 3, Ochre Jelly 2. Highest rank CR = **4** (flameskull) — but the *combat rank-and-file* are the zombies/ghouls (CR 1/4–1). Use highest true-combat rank = **2** (ogre zombie) for the conservative check; note flameskull (4) separately.
- Boss in module: **Mormesk the Wraith** (wraith, CR 5 — leader of the mine's undead).
- Δ (Mormesk CR5 − rank2) = **3** → **NOMINAL boss** (Δ < 4).
- Δ (Mormesk CR5 − flameskull rank4) = **1** → NOMINAL.
- **Verdict:** NOMINAL. Mormesk is a clear leader but within 4 CR of his own undead — and he outclasses **Nezznar (CR 2)**, who nominally controls the mine. See A7.

### A6. Old Owl Well undead (zombies)
- Rank-and-file CR: Zombie 1/4.
- Boss in module: **Hamun Kost** — "a human mage," i.e. MM **Mage, CR 6**.
- Δ (Hamun CR6 − rank1/4) = **5¾** → **HARD boss**.
- **Verdict:** **HARD boss** (verdict unchanged; the old CR 7 was one step high). A CR-6 mage commanding CR-1/4 zombies is still a massive leap, and against a level-3 party he is not a fight — which is the whole reason `notes/hamun_kost_strategy.md` plays him as a man who talks on the first syllable. The zombies are set-dressing; **he** is the encounter, and the encounter is a conversation.

### A7. The Spider's web / Nezznar's forces (Cragmaws, Redbrands, bugbears, doppelgangers, WEC occupants)
> ⚠ **VERDICT FLIPPED 2026-08-22.** This section had Nezznar at CR 7 (the MM *drow mage*). PaBTSO gives him his **own** stat block at **CR 2**.

- This is the meta-tribe: **Nezznar the Spider** is the hidden master paying/commanding the Cragmaws (A1), the Redbrands (A3), and his own WEC bugbears and doppelgangers. PaBTSO stats him at **CR 2**.
- Compared to those tribes' rank-and-file (goblin 1/4, Redbrand ruffian 1/2, bugbear 1): Δ = **1 to 1¾** → **NOMINAL boss** over every one of them. His own doppelganger (CR 3) outranks him.
- **Verdict:** **NOMINAL boss.** The campaign's central antagonist is a schemer, not a wall of hit points — he is a peer of the bugbears he hires. **This matters for how chapter 4 is run:** if the party reaches him expecting a hard boss, the fight is over in two rounds. What makes Nezznar dangerous is the network, the ambush position, and everything standing between the party and him — not his stat block. Note: the module names him the "Spider"; do not rename.

### A8. Cult of the Obelisk (humanoid mutates, Talhundereth)
- Rank-and-file CR: Humanoid Mutate **4**.
- Boss in module: **Ontharyx Henlifel** — his entry inherits the Humanoid Mutate block, so CR **4**.
- Δ (Ontharyx CR4 − rank4) = **0** → **NOMINAL boss**.
- **Verdict:** NOMINAL, and exactly so — he is mechanically identical to his own followers. (His sons Nythalyn/Yanthdel use **Drow Elite Warrior, CR 5**, so they are marginally the harder fight.)

### A9. Qunbraxel's court (grimlocks / basilisks / ropers nearby / petrified victims)
- Rank-and-file CR: Grimlock 1/4, Basilisk 3. Highest rank CR = **3** (basilisk).
- Boss in module: **Qunbraxel** — own PaBTSO block, CR **9** (not 7).
- Δ (Qunbraxel CR9 − rank3) = **6** → **HARD boss**. Vs grimlocks (9 − 1/4 = 8¾) it is emphatically HARD.
- **Verdict:** ⚠ **HARD boss** — flipped 2026-08-22. This section previously sat on the exact gap-4 line and was flagged NOMINAL+ for review; the correct CR clears the line by two. Qunbraxel is a real leap above his court, not a borderline case.

### A10. Naruv's Feeder Trenches grells (grells, Far Realm F2/F4)
- Rank-and-file CR: Grell 3.
- Boss in module: **Feedkeeper Naruv** (grell, CR 3 — same stat block as her underlings).
- Δ (Naruv CR3 − rank3) = **0** → **NOMINAL boss**.
- **Verdict:** NOMINAL. Naruv is "host" by seniority, not by power.

### A11. Spawn Hollow slaadi (red/blue/gray slaadi, tadpoles)
- Rank-and-file CR: Red Slaad 5, Blue Slaad 7, Tadpole ~0. Highest rank CR = **7** (blue slaad).
- Boss in module: **Chalaag** — the text says "the gray slaad explorer who discovered Spawn Hollow," so MM **Gray Slaad, CR 9** (not 3), plus *glyph of warding* once a day.
- Δ (Chalaag CR9 − rank7) = **2** → **NOMINAL boss**.
- **Verdict:** NOMINAL — verdict unchanged, reasoning inverted. This file used to call Chalaag *weaker* than his own brood and "first-among-equals." He is in fact the **strongest thing in Spawn Hollow**, he opens with explosive-rune glyphs he set in advance, and he goes invisible to investigate. Run him as a prepared defender, not a figurehead.

### A12. Nellik's rebel mezzoloths (mezzoloths / umber hulk / brain-breaker squads in epilogue)
- Rank-and-file CR: Mezzoloth 5, Umber Hulk 5, Brain Breaker **12**. Highest rank CR = **12** (brain breaker, epilogue).
- Boss in module: **Nellik** (nycaloth, CR 9) with adjutant **Frevvik** (mezzoloth, CR 5, named).
- Δ (Nellik CR9 − rank12/brain breaker) = **−3** → boss well below the brain-breaker elite; vs mezzoloth (9 − 5 = 4) = exactly 4 → **NOMINAL+ (borderline-hard)**.
- **Verdict:** NOMINAL. Nellik leads by force of personality/rank; the brain breakers (CR **12**) she directs in the epilogue are a markedly harder threat than she is. (Epilogue brain-breaker squads are directed by **Ghaluzesh the kraken, CR 23** → HARD boss, see A13.)

### A13. Ilvaash's epilogue enforcers (brain breakers, mind flayer prophets)
- Rank-and-file CR: Brain Breaker **12**, Mind Flayer Prophet **8**.
- Boss in module: **Ghaluzesh** — "a kraken named Ghaluzesh," so MM **Kraken, CR 23**. *(Verified: correct as originally written. He has no PaBTSO block because he uses the MM one.)* He directs the brain-breaker squads in "Ilvaash's Revenge."
- Δ (Ghaluzesh CR23 − rank12) = **11** → **HARD boss** (still the most overwhelming CR gap in the module).
- **Verdict:** **HARD boss.**

### A14. Illithinoch fanatics' minions (goblin psi commander + brawlers at the lab; unspecified mind flayer servants; resident aberrant zealots)
- Rank-and-file CR: Psi Commander **4**, Psi Brawler **2**, Mind Flayer (servant) 7, Aberrant Zealot **8**.
- Boss in module: the three fanatics **Chishinix / Hashutu / Voalsh** (mind flayer clairvoyant, CR **11**).
- Δ (fanatic CR11 − aberrant zealot 8) = **3** → NOMINAL over the zealots; vs servant mind flayers (11 − 7) = **4** → NOMINAL+; vs the goblin psi commanders (11 − 4) = **7** → **HARD boss**.
- **Verdict:** **HARD boss** over the goblin psi minions they keep as expendable fodder; nominal over their own aberration peers. They answer to **Ilvaash** (godlet; final boss via the **Refraction of Ilvaash, CR 15** — not 16) → HARD.

### A15. Vundru's grell band (grells, J7 Scavengers' Nook)
- Rank-and-file CR: Grell 3.
- Boss in module: **Vundru** ("a grell psychic named Vundru" — Grell Psychic, CR **4**).
- Δ (Vundru CR4 − rank3) = **1** → **NOMINAL boss**.
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

### B7. Gibbering Mouthers (J9) + Flesh Meld — CR 2 / **7**
- No boss; they merge into a flesh meld. The meld is CR **7** (not 2), so Δ = **5** over the mouthers. **Verdict: NO BOSS — ambient brood, but the emergent flesh meld is a HARD step up from what spawns it.** Do not treat the merge as cosmetic.

### B8. Behir (J6) — CR 11
- Solo. **Verdict: NO BOSS — independent apex predator** (named in Phase 2). Note: a CR-11 behir is itself a HARD threat to a Level-5 party but has no tribe to command.

### B9. Cloaker Mutate (J8) — CR **10** *(was 8)*
- Solo (puppets Thorgran's corpse). **Verdict: NO BOSS — independent.**

### B10. Grick lair (Gibbet Crossing G8/G9: alpha + 6) — CR 2
- The **grick alpha** (CR 2) leads the 6 lair gricks (CR 2). Δ = 0 → NOMINAL. **Verdict: NOMINAL boss (the alpha, named in Phase 2).**

### B11. Ropers (Gibbet Crossing G10) — CR 5
- Two ropers, no leader. **Verdict: NO BOSS — paired ambush predators** (named in Phase 2).

### B12. Intellect Devourer in quaggoth (Tunnel Encounters) — CR 2
- Controls a quaggoth. Δ (devourer CR2 − quaggoth CR **2**) = 0 → NOMINAL over its host. **Verdict: NOMINAL boss (the devourer is the true mind).**

### B13. Quaggoths (Tunnel Encounters + statues) — CR **2**
- Led by a quaggoth thonot (CR **3**) in the encounter table. Δ = 1 → NOMINAL. **Verdict: NOMINAL boss (the thonot, named in Phase 2).**

### B14. Specters / Crypt Guardians / Revenants (Crypt of the Talhund) — CR 4 / 5
- Undead bound to the crypt; animated by the obelisk fragment's corruption, not a living boss. The **clay golem** (P7, CR 9) and **mummy** (P13, CR 6) are independent wardens.
- **Verdict:** The specters/revenants have **NO single boss** — they answer to the crypt's haunt (the obelisk fragment). The clay golem (CR 9) and mummy (CR 6) are **independent wardens**; vs the undead rank (CR 4–5) the golem is a **HARD** warden (Δ 4–5) and the mummy is **NOMINAL+** (Δ 1–2). Flag: the golem/mummy are guardians, not "bigger bads" of a tribe.

### B15. Infected Elder Brain (Illithinoch X15) — CR **11** *(was 14)*
- Unique apex creature; it *is* the boss of the illithid stronghold's lower functions but has no tribe of its own to command (it is served by the fanatics, not the reverse). **Verdict: apex creature, NO boss — it IS a bigger bad** (and a HARD threat at CR 11, though the named fanatics/Ilvaash sit above it).

### B16. Intellect Snares (Talhundereth / Endless Void / Nematode) — CR **8** *(was 3)*
- No boss; they float free. **Verdict: NO BOSS — ambient aberrations.**

### B17. Psychic Gray Oozes (Phandalin Town Green) — CR **1** *(was 1/4; the only stat block is 2024-MM — GM ruling needed for a 2014 table)*
- Spawned by Daisy the Cow (named, excluded). **Verdict: NO BOSS — spawned brood** (named in Phase 2).

### B18. Flumphs (Briny Maze B11 cloister) — CR **1/8**
- Led by **Wise Borblish** (named flumph, CR **1/8**) — but she is a NAMED individual, so by rule we keep her. Δ = 0 → NOMINAL. **Verdict: NOMINAL boss (Wise Borblish, named — kept as-is).**

### B19. Phase Spiders (B2) + Psionic Ashenwights (B2/B3) — CR 3 / **7**
- No single boss; they ally. **Verdict: NO BOSS — allied pack.**

### B20. Encephalon Cluster / Gemmules — CR **10 / 3**
> ⚠ **VERDICT FLIPPED 2026-08-22.** Both CRs were low: the cluster is **10**, the gemmules **3**.

- The cluster (CR **10**) is "parent" to the gemmules (CR **3**). Δ = **7** → **HARD** over its progeny. **Verdict: HARD boss (the cluster); the gemmules are its offspring, not a tribe.** A party that has been clearing gemmules is not calibrated for the thing that makes them.

### B21. Clay Golem (P7) / Shield Guardian (Indigo Sanctum P13, Zorzula) / Fiendish Auger (Z18, CR **5** — was 2) / Mummy (P13)
- Constructs; each bound to a maker/location, not a tribe. **Verdict: NO BOSS — independent wardens/constructs** (each named/designated in Phase 2).

### B22. Unnamed drow thieves (Gibbet Crossing G25) — CR 1/4
- Dead/scavengers; no boss. **Verdict: NO BOSS — corpses/independent.**

---

## C. Hierarchy tree (boss → tribe), with classification

```
ILVAASH (godlet; final boss via Refraction of Ilvaash, CR 15)  [apex — HARD over all]
└─ the three mind flayer fanatics: CHISHINIX / HASHUTU / VOALSH (mind flayer clairvoyant, CR 11)
   ├─ HARD over: goblin psi minions (A14), Sawplee goblins (A2, via Ruxithid), Illithinoch residents
   ├─ NOMINAL over aberrant zealots (CR 8); NOMINAL+ over peer servant mind flayers (CR 7)
   ├─ Ghaluzesh the kraken (CR 23) → HARD over brain-breaker squads (CR 12) (A13)
   ├─ Ahooshathan / Gulguush / Oshundo / Duoro etc. (named) — kept as-is
   └─ Infected Elder Brain (CR 11) [apex creature, B15]

NEZZNAR THE SPIDER (own PaBTSO block, CR 2)  [NOMINAL boss over ch1–4 — ⚠ FLIPPED]
├─ Cragmaw band → King Grol (CR 1) → NOMINAL (A1); Grol → Klarg (CR 1) NOMINAL
├─ Redbrands → Glasstaff / Iarno (CR 1) → NOMINAL (A3)
├─ WEC bugbears / doppelgangers (Vyerith, Vhalak named) — the doppelganger (CR 3) OUTRANKS him
└─ Wave Echo Cave undead → Mormesk (CR 5, also outranks him) → NOMINAL (A5)

BRUGHOR AXE-BITER ("an orc with 18 hit points" — MM orc, CR 1/2)  [NOMINAL] (A4)
└─ Wyvern Tor raiders: four bugbears (CR 1) + the ogre Gog (CR 2) — every one of them
   tougher than Brughor, and the band FLEES if Brughor is killed

RUXITHID THE CHOSEN (psionic goblin, own block, CR 5)  [NOMINAL over his own elite] (A2)
└─ Sawplee goblins (1/4) / psi brawlers (2) / psi commanders (4) / ashenwights (5–7)

ONTHARYX HENLIFEL (humanoid mutate, CR 4)  [NOMINAL — mechanically identical to his cult] (A8)
└─ Cult of the Obelisk humanoid mutates (CR 4)

QUNBRAXEL (own block, CR 9)  [HARD over grimlocks AND basilisks — ⚠ FLIPPED] (A9)
└─ grimlocks (1/4) / basilisks (3), Gibbet Crossing

HAMUN KOST (Red Wizard — "a human mage", MM mage, CR 6)  [HARD boss] (A6)
└─ Old Owl Well zombies (CR 1/4)

ENCEPHALON CLUSTER (CR 10)  [HARD over its own gemmules (CR 3) — ⚠ FLIPPED] (B20)
└─ encephalon gemmules

FEEDKEEPER NARUV (grell, CR 3)      [NOMINAL] (A10)  └─ Feeder Trenches grells
CHALAAG (gray slaad, CR 9)          [NOMINAL — strongest thing in Spawn Hollow] (A11)
                                                     └─ slaadi (blue 7 / red 5)
NELLIK (nycaloth, CR 9)             [NOMINAL+] (A12) └─ rebel mezzoloths (→ Ghaluzesh HARD, epilogue)
VUNDRU (grell psychic, CR 4)        [NOMINAL] (A15)  └─ J7 grell band
WISE BORBLISH (flumph, CR 1/8)      [NOMINAL, named] (B18) └─ flumph cloister

INDEPENDENT / AMBIENT (no boss):  stirges, owlbear, wild wolves, giant snake, violet fungi,
  gibbering mouthers (→ flesh meld CR 7: a HARD emergent step up, not cosmetic), behir,
  cloaker mutate (CR 10), ropers, intellect snares (CR 8), psychic gray oozes (CR 1 — 2024-MM
  block only, needs a GM ruling), phase spiders, drow thieves, constructs (clay golem /
  shield guardian / fiendish auger CR 5 / mummy), quaggoth thonot (NOMINAL), grick alpha
  (NOMINAL), intellect devourer (NOMINAL over host)
```

---

## D. Summary table

| Tribe | Boss (module name) | Rank CR | Boss CR | Δ | Classification |
|---|---|---|---|---|---|
| Cragmaw band | King Grol (bugbear) | 1 | 1 | 0 | NOMINAL |
| Cragmaw hideout | Klarg (bugbear) | 1 | 1 | 0 | NOMINAL |
| Sawplee goblins | Ruxithid the Chosen | 7 | 5 | −2 | NOMINAL |
| Redbrands | Glasstaff / Iarno | 1/2 | 1 | 0.5 | NOMINAL |
| Wyvern Tor raiders | Brughor Axe-Biter | 2 | 1/2 | −1.5 | NOMINAL |
| WEC undead | Mormesk the Wraith | 2 | 5 | 3 | NOMINAL |
| Old Owl Well undead | Hamun Kost | 1/4 | 6 | 5.75 | **HARD** |
| Nezznar's forces (meta) | Nezznar the Spider | 1 | 2 | 1 | **NOMINAL** ⚠ *flipped* |
| Cult of the Obelisk | Ontharyx Henlifel | 4 | 4 | 0 | NOMINAL |
| Qunbraxel's court | Qunbraxel | 3 | 9 | 6 | **HARD** ⚠ *flipped* |
| Naruv's grells | Feedkeeper Naruv | 3 | 3 | 0 | NOMINAL |
| Spawn Hollow slaadi | Chalaag | 7 | 9 | 2 | NOMINAL |
| Nellik's mezzoloths | Nellik | 12 | 9 | −3 | NOMINAL+ |
| Ilvaash's enforcers | Ghaluzesh | 12 | 23 | 11 | **HARD** |
| Fanatics' goblin minions | Chishinix/Hashutu/Voalsh | 4 | 11 | 7 | **HARD** |
| Vundru's grells | Vundru | 3 | 4 | 1 | NOMINAL |
| Thornmaw wolves (nominated) | Vex (trainer) | 1/4 | 1/4 | 0 | NOMINAL |
| Grick lair (nominated) | grick alpha | 2 | 2 | 0 | NOMINAL |
| Quaggoth band (nominated) | quaggoth thonot | 2 | 3 | 1 | NOMINAL |
| Intellect devourer host | the devourer | 2 | 2 | 0 | NOMINAL |
| Encephalon cluster | the cluster | 3 | 10 | 7 | **HARD** ⚠ *flipped* |
| Flumph cloister | Wise Borblish (named) | 1/8 | 1/8 | 0 | NOMINAL |
| Infected Elder Brain | (apex, none) | — | 11 | — | apex/HARD threat |
| Independents (owlbear, behir, snake, stirges, etc.) | none | var | — | — | NO BOSS |

\* Gap exactly 4: flagged **NOMINAL+ (borderline-hard)** so it is never silently called "hard" without review.

**Bottom line:** By your rule, the module has **4 clear HARD bosses** (Hamun Kost, Nezznar the Spider, the fanatics over their goblin minions, Ghaluzesh over the epilogue enforcers) plus the apex godlet Ilvaash; **2 borderline NOMINAL+** (Qunbraxel's court, Nellik's mezzoloths); and the large majority of tribe bosses are **NOMINAL** — the module's rank-and-file and their named leaders sit within 3 CR of each other, with the real "hard" power concentrated in the mind flayer / archmage / kraken villains.

**Companion files:** `monsters_phase1_scan.md` (consolidated scan), `monsters_phase2_descriptions.md` (named tribes + individuals), `monsters_cr_reference.md` (CR source table). Temporary scanner partials: `_scan_A.md`, `_scan_B.md`, `_scan_C.md`.
