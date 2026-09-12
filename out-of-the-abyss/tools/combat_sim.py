#!/usr/bin/env python3
"""
Act 3 balance tester -- the library fight, Out of the Abyss.

Four PCs (scaled to level 9) plus Glabbagool vs Manshoon Simulacrum B.
Monte Carlo. Answers: do they win, how often does someone drop, how often
is it a funeral, and does un-sharing B's spell pool break the encounter.

Sources:
  docs/party/{Thorin,Zalthir,Daz,Gyrgum}-level-08.md   -- PC sheets
  notes/session_prep/20260810_race_to_the_vile_door.md -- Manshoon statblock
  notes/session_prep/20260907_the_one_upstairs_revisions.md -- table rulings

EVERY assumption beyond those sources is tagged ASSUMPTION in ASSUMPTIONS
below and printed with the report. Correct them and re-run.
"""

import random
import argparse
from dataclasses import dataclass, field

# ----------------------------------------------------------------------------
# Assumptions, printed with every run. This is the part to argue with.
# ----------------------------------------------------------------------------

ASSUMPTIONS = [
    "Level 9 scaling: +1 hit die + Con to HP; proficiency 3 -> 4 for the three",
    "  casters, so Zalthir's Stunning Strike DC 13 -> 14, Gyrgum's DC 16 -> 17,",
    "  Daz's DC 16 -> 17. Thorin's sheet already lists PB +4 at level 8, which",
    "  looks like a sheet error; his to-hit is used verbatim and not bumped.",
    "Attack bonuses and damage dice are taken VERBATIM from the sheets. Zalthir's",
    "  listed 1d8+8 unarmed at +11 is unusually high for monk 8 and may include a",
    "  magic item the sim does not know about. If it is wrong, the party is",
    "  weaker than this reports.",
    "No area damage from Daz. The hundred glyph-warded tomes make fireball a",
    "  decision, not a button, so he plays single-target. This is the doc's rule.",
    "Manshoon B never targets Gyrgum. He needs the Reader alive. Canon, from the",
    "  table rulings. This measurably helps the party and is deliberate.",
    "B opens with mirror image, then fights defensively. He does not want this",
    "  fight and does not open with violence -- 0810 doc, tactics section.",
    "Magic Resistance does NOT apply to Stunning Strike (a focus effect, not a",
    "  spell). Flip with --mr-vs-stun if you rule the other way; it matters a lot.",
    "Legendary Resistance is spent on the first three failed saves that would",
    "  actually land a stun or a banish, not on trivial ones.",
    "Glabbagool acts on Zalthir's initiative as a sidekick: one pseudopod attack.",
    "Death saves are not modelled. A PC at 0 is out for the fight and counted as",
    "  'dropped'. A TPK is all five at 0.",
]

# ----------------------------------------------------------------------------
# Dice
# ----------------------------------------------------------------------------

def d(n):
    return random.randint(1, n)

def roll(dice, sides, mod=0):
    return sum(d(sides) for _ in range(dice)) + mod

def d20(adv=0):
    a, b = d(20), d(20)
    if adv > 0:
        return max(a, b)
    if adv < 0:
        return min(a, b)
    return a

# ----------------------------------------------------------------------------
# Combatants
# ----------------------------------------------------------------------------

@dataclass
class Combatant:
    name: str
    hp: int
    max_hp: int
    ac: int
    init_mod: int
    saves: dict = field(default_factory=dict)
    alive: bool = True
    stunned_until: int = -1
    banished: bool = False

    def save(self, stat, dc, adv=0):
        return d20(adv) + self.saves.get(stat, 0) >= dc

    def damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def heal(self, amount):
        if not self.alive:
            self.alive = True   # brought back up
            self.hp = 0
        self.hp = min(self.max_hp, self.hp + amount)


def make_party(level9=True):
    """Sheets from docs/party/, scaled per ASSUMPTIONS."""
    bump = 1 if level9 else 0
    thorin = Combatant(
        "Thorin", 84 + (9 * bump), 84 + (9 * bump), 22, -1,
        {"str": 8, "con": 7, "dex": 0, "wis": 1, "int": 2},
    )
    zalthir = Combatant(
        "Zalthir", 51 + (6 * bump), 51 + (6 * bump), 16, 4,
        {"str": 0, "con": 2, "dex": 8, "wis": 6, "int": 1},
    )
    daz = Combatant(
        "Daz", 50 + (6 * bump), 50 + (6 * bump), 15, 1,
        {"str": -1, "con": 2, "dex": 1, "wis": 6, "int": 9},
    )
    gyrgum = Combatant(
        "Gyrgum", 59 + (7 * bump), 59 + (7 * bump), 18, 1,
        {"str": -1, "con": 2, "dex": 1, "wis": 9, "cha": 6},
    )
    glab = Combatant(
        "Glabbagool", 63, 63, 12, 0,
        {"str": 2, "con": 4, "dex": -2, "wis": -1, "int": -4},
    )
    return [thorin, zalthir, daz, gyrgum, glab]


@dataclass
class Manshoon:
    name: str = "Manshoon B"
    hp: int = 95
    max_hp: int = 95
    ac: int = 15               # mage armor only, no robe, no staff
    init_mod: int = 2
    legendary_resistance: int = 3
    save_dc: int = 17
    to_hit: int = 9
    ward_eater_ready: bool = True
    mirror_images: int = 0
    slots: dict = field(default_factory=lambda: {
        1: 4, 2: 2, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1
    })
    alive: bool = True
    stunned_until: int = -1
    saves: dict = field(default_factory=lambda: {
        "int": 13, "wis": 9, "con": 7, "dex": 4, "str": 2, "cha": 6
    })

    def save(self, stat, dc, magical=True, is_stun=False, mr_vs_stun=False):
        """Magic Resistance: advantage on saves vs spells and magical effects."""
        adv = 0
        if magical and (not is_stun or mr_vs_stun):
            adv = 1
        return d20(adv) + self.saves.get(stat, 0) >= dc

    def damage(self, amount):
        # mirror image soaks whole attacks, handled at attack time
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.alive = False


# ----------------------------------------------------------------------------
# The fight
# ----------------------------------------------------------------------------

def run_fight(mr_vs_stun=False, level9=True, max_rounds=20, log=None):
    party = make_party(level9)
    boss = Manshoon()

    stun_dc = 14 if level9 else 13
    order = sorted(
        [(d20() + c.init_mod, c) for c in party] + [(d20() + boss.init_mod, boss)],
        key=lambda x: -x[0],
    )
    order = [c for _, c in order]

    lr_spent = 0
    stun_rounds = 0
    ward_eater_hits = 0

    for rnd in range(1, max_rounds + 1):
        for actor in order:
            if not getattr(actor, "alive", False):
                continue
            if actor.stunned_until >= rnd:
                continue

            # ---------------- Manshoon's turn ----------------
            if isinstance(actor, Manshoon):
                targets = [p for p in party if p.alive and p.name != "Gyrgum"]
                if not targets:
                    targets = [p for p in party if p.alive]
                if not targets:
                    break

                if boss.mirror_images == 0 and boss.slots.get(2, 0) > 0 and rnd == 1:
                    boss.slots[2] -= 1
                    boss.mirror_images = 3
                    if log is not None:
                        log.append(f"R{rnd} B: mirror image")
                    continue

                # Ward-Eater when it would catch two or more
                if boss.ward_eater_ready and len(targets) >= 2:
                    boss.ward_eater_ready = False
                    for t in targets:
                        if t.save("con", 17):
                            t.damage(roll(5, 8) // 2)
                        else:
                            t.damage(roll(5, 8))
                            ward_eater_hits += 1
                    boss.hp = min(boss.max_hp, boss.hp + 25)
                    if log is not None:
                        log.append(f"R{rnd} B: Ward-Eater, heals to {boss.hp}")
                else:
                    # banishment on the monk if he is stunning, else Metal Fist
                    tgt = max(targets, key=lambda t: t.max_hp - t.hp)
                    if boss.slots.get(4, 0) > 0 and any(
                        t.name == "Zalthir" and t.alive for t in targets
                    ) and stun_rounds > 0:
                        boss.slots[4] -= 1
                        z = next(t for t in targets if t.name == "Zalthir")
                        if not z.save("cha", 17, adv=0):
                            z.banished = True
                            z.alive = False
                            if log is not None:
                                log.append(f"R{rnd} B: banishment lands on Zalthir")
                        continue
                    if d20() + boss.to_hit >= tgt.ac:
                        tgt.damage(roll(1, 4, 3))
                    if not boss.ward_eater_ready and d(6) >= 5:
                        boss.ward_eater_ready = True
                continue

            # ---------------- PC turns ----------------
            def attack(bonus, dice, sides, mod, adv=0):
                """One attack. Mirror image eats whole attacks."""
                if boss.mirror_images > 0:
                    # 3 images: 1 in 4 chance to hit the real one, etc.
                    if d(boss.mirror_images + 1) != 1:
                        if d20() + bonus >= 10:      # AC 10 to pop an image
                            boss.mirror_images -= 1
                        return 0
                nat = d20(adv)
                if nat == 20:
                    dmg = roll(dice * 2, sides, mod)
                    boss.damage(dmg)
                    return dmg
                if nat + bonus >= boss.ac:
                    dmg = roll(dice, sides, mod)
                    boss.damage(dmg)
                    return dmg
                return 0

            if actor.name == "Thorin":
                attack(9, 1, 8, 6)
                attack(9, 1, 8, 6)

            elif actor.name == "Zalthir":
                landed = False
                for _ in range(2):                       # Extra Attack
                    if attack(11, 1, 8, 8) > 0:
                        landed = True
                for _ in range(2):                       # Flurry of Blows
                    if attack(11, 1, 8, 8) > 0:
                        landed = True
                if landed and boss.alive:                # Stunning Strike
                    if not boss.save("con", stun_dc, magical=True,
                                     is_stun=True, mr_vs_stun=mr_vs_stun):
                        if boss.legendary_resistance > 0:
                            boss.legendary_resistance -= 1
                            lr_spent += 1
                        else:
                            boss.stunned_until = rnd + 1
                            stun_rounds += 1
                            if log is not None:
                                log.append(f"R{rnd} STUNNED")

            elif actor.name == "Daz":
                # magic missile upcast: no attack roll, ignores mirror image
                lvl = max((l for l in (5, 4, 3) if boss.alive), default=3)
                darts = 3 + (lvl - 1)
                boss.damage(sum(roll(1, 4, 1) for _ in range(darts)))

            elif actor.name == "Gyrgum":
                hurt = [p for p in party if p.alive and p.hp < p.max_hp * 0.4]
                down = [p for p in party if not p.alive and not p.banished]
                if down:
                    down[0].heal(roll(1, 8, 5))
                elif hurt:
                    hurt[0].heal(roll(2, 8, 5 + 2 + 3))   # Disciple of Life
                else:
                    attack(4, 1, 8, 1)

            elif actor.name == "Glabbagool":
                attack(6, 3, 6, 3)

        # ---------------- legendary actions ----------------
        if boss.alive and boss.stunned_until < rnd:
            live = [p for p in party if p.alive and p.name != "Gyrgum"]
            if live:
                t = random.choice(live)
                if not t.save("str", 17):
                    pass  # Ward-Pull: repositioning only, no damage

        if not boss.alive:
            return dict(win=True, rounds=rnd, party=party, lr=lr_spent,
                        stuns=stun_rounds, we=ward_eater_hits, boss_hp=0)
        if not any(p.alive for p in party):
            return dict(win=False, rounds=rnd, party=party, lr=lr_spent,
                        stuns=stun_rounds, we=ward_eater_hits, boss_hp=boss.hp)

    return dict(win=False, rounds=max_rounds, party=party, lr=lr_spent,
                stuns=stun_rounds, we=ward_eater_hits, boss_hp=boss.hp)


# ----------------------------------------------------------------------------
# Reporting
# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=5000)
    ap.add_argument("--mr-vs-stun", action="store_true",
                    help="rule that Magic Resistance applies to Stunning Strike")
    ap.add_argument("--level8", action="store_true", help="do not scale to 9")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--sample", action="store_true", help="print one narrated fight")
    ap.add_argument("--sweep", action="store_true", help="dial sweep: AC x HP grid")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.sweep:
        sweep()
        return

    if args.sample:
        log = []
        r = run_fight(args.mr_vs_stun, not args.level8, log=log)
        print("\n".join(log))
        print(f"\nResult: {'party wins' if r['win'] else 'party loses'} "
              f"in {r['rounds']} rounds")
        for p in r["party"]:
            state = f"{p.hp}/{p.max_hp}" if p.alive else "DOWN"
            print(f"  {p.name:<12} {state}")
        return

    wins = rounds = lr = stuns = 0
    dropped_any = tpk = 0
    drops_by_name = {}
    for _ in range(args.trials):
        r = run_fight(args.mr_vs_stun, not args.level8)
        wins += r["win"]
        rounds += r["rounds"]
        lr += r["lr"]
        stuns += r["stuns"]
        downs = [p.name for p in r["party"] if not p.alive]
        if downs:
            dropped_any += 1
        for n in downs:
            drops_by_name[n] = drops_by_name.get(n, 0) + 1
        if len(downs) == len(r["party"]):
            tpk += 1

    n = args.trials
    print("=" * 62)
    print(f"  ACT 3 -- Manshoon B alone, {n} trials")
    print(f"  party level {'8' if args.level8 else '9'} + Glabbagool")
    print(f"  Magic Resistance vs Stunning Strike: "
          f"{'YES' if args.mr_vs_stun else 'no'}")
    print("=" * 62)
    print(f"  Party wins            {wins/n:6.1%}")
    print(f"  Median rounds         {rounds/n:6.1f}")
    print(f"  >=1 PC drops          {dropped_any/n:6.1%}")
    print(f"  TPK                   {tpk/n:6.1%}")
    print(f"  Leg. Resistances used {lr/n:6.2f} / 3")
    print(f"  Rounds B was stunned  {stuns/n:6.2f}")
    print("-" * 62)
    print("  Who goes down:")
    for name, c in sorted(drops_by_name.items(), key=lambda x: -x[1]):
        print(f"    {name:<12} {c/n:6.1%}")
    print("=" * 62)
    print("ASSUMPTIONS -- argue with these, then re-run:")
    for line in ASSUMPTIONS:
        print("  " + line)




# ----------------------------------------------------------------------------
# Sweep: what dials turn this into an actual fight?
# ----------------------------------------------------------------------------

def sweep(trials=1500):
    print("=" * 68)
    print("  DIAL SWEEP -- what makes Act 3 a fight?")
    print("  win% / median rounds / >=1 PC drops")
    print("=" * 68)
    print(f"  {'AC':>4} {'HP':>5}   {'win':>7} {'rounds':>7} {'drops':>7}")
    for ac in (15, 17, 19, 21):
        for hp in (95, 130, 170, 190):
            w = rr = dr = 0
            for _ in range(trials):
                import copy
                party = make_party(True)
                boss = Manshoon(hp=hp, max_hp=hp, ac=ac)
                res = _fight_with(party, boss)
                w += res[0]; rr += res[1]; dr += res[2]
            print(f"  {ac:>4} {hp:>5}   {w/trials:6.1%} {rr/trials:7.1f} "
                  f"{dr/trials:7.1%}")
    print("=" * 68)


def _fight_with(party, boss, max_rounds=20):
    """Stripped fight used by the sweep. Returns (win, rounds, any_drop)."""
    order = sorted(
        [(d20() + c.init_mod, c) for c in party] + [(d20() + boss.init_mod, boss)],
        key=lambda x: -x[0])
    order = [c for _, c in order]
    for rnd in range(1, max_rounds + 1):
        for actor in order:
            if not getattr(actor, "alive", False):
                continue
            if actor.stunned_until >= rnd:
                continue
            if isinstance(actor, Manshoon):
                tg = [p for p in party if p.alive and p.name != "Gyrgum"] \
                     or [p for p in party if p.alive]
                if not tg:
                    break
                if boss.mirror_images == 0 and rnd == 1 and boss.slots.get(2, 0):
                    boss.slots[2] -= 1; boss.mirror_images = 3; continue
                if boss.ward_eater_ready and len(tg) >= 2:
                    boss.ward_eater_ready = False
                    for t in tg:
                        t.damage(roll(5, 8) // 2 if t.save("con", 17)
                                 else roll(5, 8))
                    boss.hp = min(boss.max_hp, boss.hp + 25)
                else:
                    t = max(tg, key=lambda x: x.max_hp - x.hp)
                    if d20() + boss.to_hit >= t.ac:
                        t.damage(roll(1, 4, 3))
                    if not boss.ward_eater_ready and d(6) >= 5:
                        boss.ward_eater_ready = True
                continue

            def atk(bonus, dice, sides, mod):
                if boss.mirror_images > 0 and d(boss.mirror_images + 1) != 1:
                    if d20() + bonus >= 10:
                        boss.mirror_images -= 1
                    return
                n = d20()
                if n == 20:
                    boss.damage(roll(dice * 2, sides, mod))
                elif n + bonus >= boss.ac:
                    boss.damage(roll(dice, sides, mod))

            if actor.name == "Thorin":
                atk(9, 1, 8, 6); atk(9, 1, 8, 6)
            elif actor.name == "Zalthir":
                for _ in range(4):
                    atk(11, 1, 8, 8)
                if boss.alive and not boss.save("con", 14, is_stun=True):
                    if boss.legendary_resistance > 0:
                        boss.legendary_resistance -= 1
                    else:
                        boss.stunned_until = rnd + 1
            elif actor.name == "Daz":
                boss.damage(sum(roll(1, 4, 1) for _ in range(7)))
            elif actor.name == "Gyrgum":
                dn = [p for p in party if not p.alive]
                hu = [p for p in party if p.alive and p.hp < p.max_hp * 0.4]
                if dn:
                    dn[0].heal(roll(1, 8, 5))
                elif hu:
                    hu[0].heal(roll(2, 8, 10))
            elif actor.name == "Glabbagool":
                atk(6, 3, 6, 3)

        if not boss.alive:
            return (1, rnd, int(any(not p.alive for p in party)))
        if not any(p.alive for p in party):
            return (0, rnd, 1)
    return (0, max_rounds, int(any(not p.alive for p in party)))


if __name__ == "__main__":
    main()
