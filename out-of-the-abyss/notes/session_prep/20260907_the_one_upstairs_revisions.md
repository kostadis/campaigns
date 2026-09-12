# The One Upstairs — table revisions, carried to next session

Staging, not canon. Supersedes the matching sections of
`20260830_the_one_upstairs.md` where the two disagree, because these were
ruled at the table. Everything below is `[TABLE]` unless marked `[OVERLAY]`.

---

## What actually happened

- **Manshoon A died in round 2.** Rounds 1 and 2 only. Act 1 was short.
- **Echo 3 (the Keeper Prophecy) never fired at round 4.** It played at the
  end of Act 1 instead, into a quiet room, over snow going grey and water
  running toward the stairs.
- **Edvaldo never reached the stairs.** He is trapped downstairs with the
  corpse, the robe, the staff, and the warm metal hand. Still unexposed.
- **Only two rounds of A's spells were spent** — `globe of invulnerability`
  (6th) and `wall of force` (5th), plus the pre-spent `mirror image` (2nd).
  Check what he burned in Legendary Resistances before Act 3.

---

## The stone count, as ruled

**Four played, six on the tray unplayed.** Not the doc's 5-then-tick schedule.

| Stone | What | Status |
|---|---|---|
| 1 | ⭐ **The door instruction** — Alaundo's terms | Played by B **alone, before dawn**. The party never heard it whole and never will |
| 2–3 | Atmospheric | Played |
| 4 | ⭐ **Echo 3 — the Keeper Prophecy** (Thorin, Zalthir, Daz, Dawnbringer) | **Heard whole by the party** |
| 5–10 | ⭐ **Six unplayed prophecies** | On the tray. Each plays in full exactly once |

⭐ **The six are the hostage.** Somewhere in them: Echo 1 (surface
contamination), Echo 2 (the Zuggtmoy wedding), Echo 4 (the Witness /
knucklebone marker), and Echo 5 (Daz — see below). The party does not know
what is in them.

---

## Manshoon B — as ruled at the table

⛔ **The doc's "never threatens, never mentions the books" is superseded.**

- ⭐ **He sent A downstairs because he did not want to share.** They were
  identical at dawn. B worked out what was behind the door, decided not to
  split it, and spent his twin. A agreed to fight because he thought he could
  win. **The party removed B's only rival, for free, and do not know it.**
- ⭐ **He knows the answer is `candle`.** He is not coy about it. The **eleven
  scorch marks are eleven times he said the right word and the door declined.**
  Knowing was never the obstacle.
- **He has given the party the door prophecy's terms.** They have to take his
  word for it — the stone that carried them is spent and they never heard it.
- ⭐ **He needs Gyrgum to walk in, and Gyrgum did.** He will not initiate
  combat, will not risk an AoE, and will physically stop anything that moves
  on the cleric.
- ⭐ **And then he loses patience.** *"Open the door or I destroy the
  prophecies."*

> ⭐⭐ **THE TRAP, and it is the climax: a threat is a demand.** Alaundo's terms
> require the word be offered **as a gift**. Coerced, it fails — twelve scorch
> marks, one wasted word, nothing opens. **Manshoon has just made the thing he
> wants impossible in order to get it faster**, in the last hour of a six-hour
> lesson in patience.
>
> **Gyrgum has to tell an archmage a thing the archmage already knows, while
> being threatened, and be believed.**
>
> > *"You can make me say it. You cannot make me give it. Those are different
> > words and the door knows the difference. You told me so yourself."*

### The three branches

1. **He backs down and actually asks.** Nothing behind it. A copy admitting it
   needs something — the one thing he has avoided all night.
2. **He does not, Gyrgum says it coerced, and nothing happens.** Then they are
   in a small room with a man who has lost his last option.
3. **Gyrgum refuses outright.** ⚠️ **Decide before play whether he really does
   it.** If you are not willing to let the six burn, do not have him threaten it.

---

## ⭐ Echo 5 — the Debtor Prophecy (Daz) `[OVERLAY]` — draft, unapproved

Daz's arc is the patron: someone in Menzoberranzan is paying Menzoberranzan
rates to keep a nobody alive, and he cannot name them. It is the one entry in
his accounts he cannot reconcile.

> *"A crow will fly out of the spider's city, and the city will not call it
> back. It will be paid for, and it will not know the buyer. The debt will be
> honest and the purpose will not. When the crow learns whose coin kept it
> alive, it will have to decide whether it was worth the price."*

- Stays in his own vocabulary — *paid for, buyer, debt, price* — without using
  his words. He audits; Alaundo audited him first.
- ⛔ **Do not let them reach for it first.** Late, or let it be the one that
  burns — a prophecy about a debt you cannot see is worse unfinished.
- ⭐ **Keep it among the six.** Thorin's already landed and is safe; Daz's is in
  Manshoon's hand. That makes the threat cost a *player*, not just the campaign.

---

## Open, for the GM

1. **Did stone 9 / Echo 4 play on the stairs?** If not, the Witness Prophecy is
   still on the tray and is the only *asset* among the six — a guaranteed
   audience with a god, spendable once.
2. ⭐ **Did A and B diverge enough to un-share the pool?** If they are two
   creatures now, B has spent nothing and the three Legendary Resistances are
   his alone. Harder fight than the 0830 doc assumed. **Rule it before Act 3.**
3. **Edvaldo's timing.** He is downstairs with the loot. Does he come up during
   the negotiation, wait, or hold the corpse? He is still the fifth person in a
   four-person decision and nobody has counted.
4. **The two metal hands.** Two rooms, two numbers in Thorass on the inner
   wrist-cup, and they do not match. One sentence, no follow-up.

⛔ **Still never cut:** stone 10 / the door terms read whole · the offer · the
choice about the Book. **Cut on the choice, then level to 10.**

---

## ⚠️ Balance findings — `tools/combat_sim.py`, 5000 trials each

**Confirmed at the table 2026-09-09: the Manshoon B fight ran, and it was
"not too bad." The simulator predicted exactly that.**

### Manshoon B alone is not a fight, and no dial fixes it

| Variant | Win | Rounds | ≥1 PC drops | TPK |
|---|---|---|---|---|
| As written (AC 15, 95 HP) | 100% | 1.9 | 0.0% | 0.0% |
| AC 19, HP 130 | 100% | 2.8 | 0.0% | 0.0% |
| Six Legendary Resistances | 100% | 1.8 | 0.0% | 0.0% |
| Ward-Eater recharge 4–6 | 100% | 1.8 | 0.0% | 0.0% |
| Banishment on Zalthir, round 1 | 100% | 1.8 | 0.0% | 0.0% |
| **All buffs stacked** | 100% | 2.8 | 0.0% | 0.0% |

⛔ **Do not buff his statblock.** The party deals ~91 damage/round vs AC 15
against his 95 HP. Zalthir alone is 42 of it. **Every stat lever only makes the
fight longer, never dangerous** — which is the 0810 design contract working
exactly as written, just never intended for a *solo*.

### ⭐ The only thing that moves the needle is a second body

| Scenario | ≥1 PC drops | TPK |
|---|---|---|
| Edvaldo allied with Manshoon | 43.7% | 0.0% |
| ⭐ **Edvaldo turns on his own, after** | **~70%** | **0.0%** |

⭐ **He is more dangerous as Manshoon's rival than as his ally** — a fresh
104 HP / 5d6 sneak-attack creature against a party that has just spent
everything. **And it is stable across every path:**

| Party state at the pedestal | ≥1 PC drops | TPK |
|---|---|---|
| Fresh (they negotiated) | 69.0% | 0.0% |
| Spent (they fought Manshoon) | 71.9% | 0.0% |
| Either, **with** a surprise round | +2 pts | 0.0% |

⛔ **Skip the surprise round** — worth two percentage points and the 0830 doc
already warns against it. **He targets lowest AC**: Daz (15), then Zalthir (16).
⛔ Not Gyrgum (18) or Thorin (22).

> ⭐ **He is tied up downstairs `[TABLE]` — and that does not take him off the
> board.** Rope holds a Medium humanoid; it does not hold a shapechanger that
> becomes Small as an action with Cunning Escape as a bonus action. **That is
> his statblock, not a fudge.** Place him on story timing alone — the numbers
> are the same wherever you put him.
>
> **Best moment: Act 4, at the pedestal, the instant the Book decision goes
> against him.** The 0830 doc already names it.

### ⭐⭐ The real threat in the library was never Manshoon — it's the glyphs

Doc's rule run as written (once per **area spell or fire damage**, not per hit):

| Fireballs cast | Tomes lost **permanently** | ≥1 PC drops |
|---|---|---|
| 1 | 13.6 | 67.0% |
| 2 | 27.4 | 96.7% |
| 3 | 41.2 | 99.7% |

⭐ **One fireball costs ~14 irreplaceable books and drops a PC two times in
three.** Correctly calibrated — **do not change it.** The library is the most
dangerous room in the tower and the danger is entirely self-inflicted.

⚠️ **But a disciplined party pays nothing.** Daz plays single-target in there,
so zero books burn. If you want branch 3 to *always* cost something, the
trigger has to be wider than area damage. **GM call.**

### Caveats on the numbers

- Glyph figures assume every detonation catches all four PCs. The doc says a
  **20-ft radius centred on that shelf** — real losses are lower with spread
  positioning and Daz's Sculpt Spells.
- ⚠️ **Zalthir's sheet lists unarmed at +11 for 1d8+8**, which is high for
  Monk 8 and may include an item the sim doesn't know about. If it's wrong,
  the party is *weaker* than everything above reports.
- Death saves are not modelled; a PC at 0 is counted "dropped" and out.
- ⚠️ **Name:** `config/party.yaml` says **Gyrgum**; the spell-pass glossary says
  **Gyrgum** (bolded canonical, many rows). The canon chain favours party.yaml.
  **Unresolved — the sim uses `Gyrgum`, one line to change.**

---

# ⭐⭐ THE REDESIGN — ruled 2026-09-11

⛔ **This supersedes Acts 3 and 4 of the 0830 doc and the balance section
above where they disagree.** The night now has a *designed outcome*, not an
open one.

## The three goals

1. ⭐ **The party walks out with the artifacts** — **the ten Seer stones.**
2. ⭐ **Manshoon gets what he wants** — the Book.
3. ⭐ **Create a long-term enemy.**

> **All three land through the deal, and only through the deal.** The enemy you
> create is one the party *made themselves*, by agreement, from a man who kept
> every word he gave. ⭐ **That is a far better recurring antagonist than one
> who beat them** — every time he surfaces they have to sit with having helped.
>
> ⛔ **He does not betray them in that room.** The souring lands three sessions
> out, when they learn what he did with it, and the worst part is they cannot
> even say he lied.

## ⛔ Why he survives — and it is not the encounter math

**B holds the pair's only 7th-level slot: `teleport`.** Counterspelling it is a
DC 17 check and Daz has to have it prepared with a slot free. **He leaves
whenever he decides to, with or without the Book.** ⭐ **The long-term enemy is
guaranteed by that one slot, not by the fight being winnable** — and per the
sim it emphatically is not (100% party win, ~1.9 rounds, 0% drops).

## ⭐ The hostage, and the irony that makes the scene

- ⭐ **He holds the tray in his hands the whole scene.** Not on the far wall,
  not on the desk. Six unplayed stones, visible, held the way you hold
  something you have already said you are willing to break.
- ⭐ **He threatens to destroy the prophecies** — *"Open the door or I destroy
  the prophecies."* He believes this is a lever he controls.

> ⭐⭐ **HE IS WRONG, AND HE DOES NOT KNOW IT.** If the party kills him, the
> death-burst detonates the shelf wall **and the stones go with him.** His
> threat executes itself through his own corpse.
>
> ⭐ **He would be appalled.** He spent six hours learning that this vault
> punishes impatience and never worked out that it applied to him. **Alaundo
> built a room where the impatient destroy the thing they came for** — the door
> is only the last instance of it.
>
> ⛔ **Nobody in the room is lying and nobody is fully informed.** Do not let
> anyone explain the irony out loud, tonight or ever.

## ⭐⭐ The doppelganger knows — and this is the scene

`[TABLE]`: he was **exposed and tied up downstairs** after the round-2 fight.
⭐ **That does not take him off the board. It makes him the only informed
creature in the building.**

**He wants to be next to the Book when the door opens.** If the stones burn,
Manshoon dies, the door never opens, and **he gets nothing.** ⭐ **Warning them
is the most self-interested thing he can do, and it happens to be true.**

### The beat — ⭐ timing is everything

**After the swing is declared, before it resolves.** Thorin has called the
attack or Zalthir has announced the flurry and the dice are in somebody's hand.
Then a voice from the stairwell — from something that is supposed to be bound
two floors down.

> ### ***"DON'T KILL HIM!"***

⛔ **Stop everything. Do not let him finish yet.** Four people turn. **Manshoon
turns**, and does not understand what he is looking at either — this is a
scholar he has never met.

**Then the rest, breathing hard, and badly:**

> *"The stones. The stones are — if he dies in here it takes the shelves and it
> takes the stones, all of them, and then nobody opens anything, ever."*

⭐ **Give Manshoon one line into the silence, because he does not know either:**

> *"Is that true?"*

**It is the first question he has asked all night that he does not already know
the answer to.**

### Why this is the best version of the doppelganger

Everything about it has been composure — narrating other people's actions
admiringly from behind them, recusing itself from the owlbear's riddle rather
than risk a wrong answer, days of not being noticed. ⭐ **Here it burns all of
that, on a staircase, out loud.** Not brave — **a creature that has run the
numbers and found the disguise is now worth less than the outcome.**

⛔ **He never gets untied, never swings, never rolls initiative** — and he is
still the most consequential thing in the room. **One sentence from him changes
what four people do next.**

⛔ **Do not let him say the word *Alaundo*, and do not let him explain the
design.** He knows what the room does. He does not know why, and does not care,
and that gap is exactly what separates him from the man who spent six hours
learning it.

### 🟣 The three ways it goes — all good

| They… | Then |
|---|---|
| ⭐ **Believe him, take the deal** | All three goals land, **and the party was steered there by a prisoner** |
| **Don't believe him, kill Manshoon** | Stones burn, door stays shut, **and he watches from the floor with his hands tied. He told them. He was right. Nobody will ever thank him** |
| ⭐ **Believe him, then ask how he knows** | The honest answer costs him: he has been in this building since before dawn, reading their thoughts since the grove — **he came here to steal from the shelves too** |

> ⚠️ **The party has a correct warning from a source they have already caught
> lying.** Everything in their experience says it is working an angle. **It is.
> The angle is the truth.** ⛔ **No check resolves this.** Only whether they
> believe him.

## ⚠️ If they do it anyway — "screw it, Manshoon blows up"

**Run it straight.** ~14 tomes gone permanently · ≥1 PC drops ~93% · **real TPK
risk (~37%), which the GM has explicitly accepted** · ⭐ **and all ten stones
are destroyed.**

**They walk out of the deepest vault in Candlekeep with nothing.** No stones, no
Book, somebody down, and a number they have to say out loud to an Avowed in the
morning.

- ⛔ **Goal 2 still lands, deferred.** The door never opens; Candlekeep reseals
  a vault it now knows is reachable. ⭐ He does not need *this* Reader — he needs
  *a* Reader, in a building full of them, wearing a face nobody has seen.
  **"He eventually gets what he wants" becomes a name in a letter three sessions
  out.**
- ⭐ **Goal 3 gets STRONGER.** They blew up a man standing still, being polite,
  offering an honest trade, in a room he told them would detonate. **He kept his
  word right up until they killed him — and he was a copy.** The enemy they made
  is a wizard who now knows exactly what these four do when offered a reasonable
  deal, **and who has fourteen destroyed books to point at.**
- ⛔ **One line before the blast, and nothing clever after:**
  > *"That is a reasonable decision and I would probably make it."*

  Then snow, then water, then the room goes up.

> ⚠️ **Eyes open:** making the stones burn means the deal is not just the best
> option but **the only one that produces anything.** Branch 3 is now narrowed
> on purpose. **If a player argues afterwards that there was only one real
> answer, they are right** — and the honest response is that *Manshoon
> engineered it that way*, which is true and is the most frightening thing
> about him.

## Stage directions — the redesign

- ⭐ **He holds the tray the whole scene.** Never sets it down.
- ⛔ **He never gloats about the position he has put them in.** States where he
  is standing, what he is holding, what he wants. **Then waits.**
- ⭐ **When Gyrgum says the word, he hands over the tray FIRST, before the door
  opens** — because a man who meant to cheat them would not.
- ⛔ **The scream lands mid-swing, not before initiative and not after the
  damage.**
- ⭐ **Count to three after *"Is that true?"*. Do not fill it.**
