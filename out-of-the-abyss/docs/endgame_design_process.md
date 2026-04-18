# Debugging a D&D End-Game with an LLM: A Walkthrough

*How a two-hour conversation with Claude moved my modified Out of the Abyss climax from "mostly works but something is off" to an airtight architecture — and what the shape of that conversation tells you about where LLMs help with design work and where they don't.*

---

## Why I'm writing this

I run a modified *Out of the Abyss* where the end-game is called "The Fall of the City of Spiders." It replaces the published module's Chapter 17 finale (Vizeran's lonely Araj tower, fetch-quest components, party-watches-demon-slugfest) with a political thriller set inside Menzoberranzan: Vizeran hiding in the city, a party running noble-cover infiltration under a Heat clock, a three-node ritual ("Tripod of Ruin") anchored at Narbondel, the Pool of Baenre, and the Great Rift, and a finale where demon lords arrive *into* the city rather than being gathered *to* the party.

It was written across five canon docs (master plan, canon guardrails, risk levers, decision ladders, NPC profile). It felt coherent when I wrote it. It didn't feel coherent a few weeks later — something was off. I couldn't name what.

So I asked Claude to audit it. What happened over the next two hours is a case study in what LLMs can and can't do for design work. The end-state is a locked, mechanically honest end-game with deliberate branches. The path there is what's interesting.

The short version: **the LLM's job was to put articulation pressure on the design. My job was to supply the two structural insights that actually closed the gaps. Neither half works alone.** This walkthrough is about how that division of labor showed up turn by turn.

---

## The starting state

What I had written:

- Vizeran lives hidden in the city (DeVir ruins), anti-divination shielded. Can't leave — "Living Circuit" mechanical constraint.
- Party arrives via purple-worm mounts, parks worms outside the wards, runs a Social Masquerade (Daz as "Master"). Heat clock: Ghost → Rumors → Purge → Lockdown → Extermination.
- Tripod of Ruin with three distinct site functions: Narbondel = beacon, Great Rift = pheromone drop for worm stampede, Pool of Baenre = demon portal.
- Vizeran dies with the city by design.
- Optional post-arc: Vhaerun cult holds Blink authorship proof, epic-tier continuation.

What felt wrong: I couldn't say exactly what the ritual *did* to the demon lords after they arrived. The master plan's apocalypse paragraph was about Menzoberranzan being torn apart. The demons were plural but the mechanisms were singular. The kill-Vizeran branch said "demons bound back weakly" and I couldn't have defended that clause under questioning.

But I didn't know if this was a real architectural problem or if I was just re-reading my own work too closely.

---

## Turn 1: the open-ended audit

I asked: *"Can you give me a view of the end-game for this campaign in Menzoberanzan, and whether the end-game plot and Vizeran Devir's motivations are consistent and there are no plot holes."*

Open-ended. No steering. I wanted to see what the design defended itself as, viewed from outside.

Claude pulled the master plan, Vizeran's dossier, and the surrounding docs, and returned a ranked list of five issues:

1. **The demon problem is never actually solved.** (Load-bearing.) The Tripod summons demon lords to Menzoberranzan and lets them destroy it. There is no written mechanism by which demons are then banished, bound, or depleted.
2. **Multiple demon lords, one portal.** The Pool of Baenre specifically invokes Demogorgon. Zuggtmoy has a wedding in Neverlight Grove and no reason to leave; Juiblex wants Zuggtmoy's domain, not Menzoberranzan.
3. **Dark Heart topology.** The ritual description mixed "one receiver" and "three wired sites" without an explicit architecture paragraph.
4. **Vizeran's mobility history is unstated.** Daz was vaulted pre-Velkynvelve; purple-worm infrastructure exists in the Wormwrithings. Present-tense Living Circuit means Vizeran couldn't have set any of it up recently. When did he become the anchor?
5. **Purple-worm double-use.** Vizeran provides bound mount-worms. Pheromones summon worms. If he already controls worms, why does he need pheromones?

It also said, correctly, that the political-thriller spine was airtight — Masquerade, Heat, DeVir reveal, Daz's three-way choice, Vizeran's anti-recurrence doctrine all consistent. The weakness was the demonological spine.

### What was valuable here

Articulation pressure. The LLM didn't find anything I hadn't vaguely sensed. But it *named* five discrete issues, ranked them, and explained why each one mattered. That's the move that made the next hour of work possible. You can't attack "something feels off"; you can attack "the Tripod imports demons but doesn't terminate them."

The ranking was also valuable — not because it was right (it wasn't, as we'll see), but because it forced a single load-bearing hypothesis to the top where I could react to it.

### What was already wrong, though

The top-ranked "plot hole" was not introduced by my extension. It's inherited from the published module. The LLM didn't know that yet because it hadn't read Chapter 17. Its confidence in the ranking was unearned.

Also, issue #4 (Vizeran's mobility history) is a real documentation gap, but it's not a plot hole — Vizeran became the anchor recently (post-Blink), and the work Daz-in-Velkynvelve etc. predated that. One sentence of canon closes it. The LLM ranked it as a plot hole because it hadn't distinguished "underwritten but coherent" from "coherent only if you stretch."

These kinds of confident-but-wrong rankings are the first thing to watch for. The LLM's output reads as authoritative. It isn't — it's a structured first draft of a critique, no more trustworthy than any other unverified first draft.

---

## Turn 2: "it's in the original"

I corrected: *"Okay — you identified a key plot hole that is in the original module. if you look it up you will see it."*

One line. Not a debate. Claude consulted *Out of the Abyss* via the 5etools MCP server and quoted Chapter 17's "Enacting the Plan" verbatim:

> "The ritual causes the dark heart to radiate a summons throughout the Underdark using the faerzress… All the demons and demon lords in the Underdark are drawn through those portals, appearing together in the area around the dark heart talisman. Enraged by being forcibly summoned yet again by a ritual, the demons fly into a frenzy once they see each other, beginning a battle to the death. As each demon's material form is destroyed, its essence is banished back into the Abyss."

It also found the "Lingering Evil" sidebar in Loose Threads ("one or more of the demon lords might remain") and the "Lesser of Two Evils" option that lets the DM decide whether the blood-sacrifice clause is real, a test, or Vizeran's madness.

Its revised take: the original module has a fig leaf — forced-rage combat → auto-banishment on death — and the fig leaf is openly flawed. The demons haven't been killing each other on sight during the campaign; Zuggtmoy is running a wedding; the "they see each other and fight" trigger is narrative fiat. My modified version *removes* the fig leaf entirely. Original = "end the demons" was half-true. Modified = the claim is entirely a lie.

### What was valuable here

Accuracy correction. The LLM retrieved and quoted primary source. Its new position was narrower and better-grounded than its first.

### What was still wrong

The "forced-rage handwave" framing was overconfident. The LLM was now claiming the original's mechanism was mechanically weak — that the demons fight each other because the module says so, not because of any rule. It was about to get corrected again.

The pattern worth noticing: the LLM's confidence level did not drop after being wrong once. It wrote the second answer with the same authority as the first. Calibration is not something these systems do reliably on their own.

---

## Turn 3: "check the Monster Manual"

I corrected: *"there is an implicit truth about demons if you check the monster manual bestiary, that when they die, they go back to the abyss."*

Claude pulled the relevant MM pages and revised again:

> "Demons (and all non-native fiends) on the Material Plane / Underdark have bodies that are essentially vessels. When the body is destroyed anywhere other than the Abyss, the essence is forced back to the Abyss automatically. Permanent destruction requires killing them on their home plane. This is MM canon for fiends and the Planescape-era rule 5e carried forward."

This reframed everything. Chapter 17's auto-banishment clause isn't the ritual's special effect — it's the module reminding the DM of the default rule. The ritual only has to do two things: gather the demons, force them to fight each other. Banishment is **free**. It's the automatic consequence of killing a fiend on the Prime.

With that rule in hand, the original module is mechanically tighter than the LLM had given it credit for. The crisis ("demon lords loose on the Prime") resolves because banishment resolves it by default. "Lingering Evil" isn't a hole — it's a DM option to carry specific demons forward as sequel hooks.

The remaining issue was now narrower: *my* modified version still doesn't guarantee demons die in Menzoberranzan. The original forces mutual combat (by narrative fiat). Mine has demons tearing the city apart and then — what?

### What was valuable here

A second revision, this time converging. The LLM now had the right frame: the problem is not "demon problem not solved in general," it's specifically "termination not guaranteed in the Tripod version."

### The pattern so far

Three turns. I've supplied: (a) "the original module has this hole too" — a source correction; (b) "MM canon says fiends banish on Prime death" — a rules correction. The LLM has supplied: structured articulation, primary source retrieval, ranking, and repeated revision under correction.

Neither of my corrections was clever. They were just things I happened to know that the LLM didn't initially apply. The LLM's job wasn't to know them; it was to write clearly enough that I could see *exactly* where my knowledge needed to enter the conversation.

---

## Turn 4: the keystone

I said: *"Vizeran is too clever to not understand this. So the reason he is essential for the ritual, is that his life acts as the forcecage that traps the demons in Menzoberanzan until only one is alive."*

This is the turn where the design locked.

The insight is one sentence. The Living Circuit is not a tether preventing Vizeran from leaving — it is a *containment field*. His lifeforce, projected through the Dark Heart into Menzoberranzan's ley architecture, seals demons **inside** the city. Demons cannot leave until the anchor drops. The anchor drops when he dies. He dies when the last demon falls.

Once I said it, the LLM immediately wrote back the downstream consequences — and this is the turn where it *did* contribute real thinking, because the implications of the cage insight ramify into every previous issue:

- **Why Menzoberranzan specifically?** The cage topology is welded to Menzoberranzan's ley lines. "Put the Dark Heart anywhere else" = no cage = demons arrive, wreck the place, walk out alive. The original module's "talisman can be placed in any location" is precisely what Vizeran cannot allow. The modified version's site specificity becomes mechanically required, not aesthetic.
- **Why must Vizeran die with the city?** Because the cage only ends when its power source does. His death isn't tragic exhaustion — it's the seal resolving. Intended, not incidental.
- **Why do the demons fight instead of just destroying the city?** Captivity + mutual hatred + no exit. The original module's "rage-trigger narrative fiat" now has a mechanical driver: demon lords locked in a room with their rivals and no way out have exactly one optimal strategy.
- **What does the Tripod actually do, cleanly?** Narbondel = beacon (calls them). Pool of Baenre = portal (lets them in). Great Rift = worm stampede (physical destruction of the clerical order; the cage handles demons, not priestesses). Three non-overlapping functions.
- **What happens in the kill-Vizeran branch?** Cage drops. Surviving demons escape. The party's choice to kill Vizeran becomes a genuine trade — faster end for him, more loose demon lords after.
- **Anti-recurrence absolutism becomes philosophically precise.** Vizeran makes himself the last prison. The ultimate Gift-of-Choice act is choosing to be the cage that contains both tyrannies until they annihilate each other inside him.

Every one of the five original plot-hole-ranked issues now either resolves or clarifies under the cage frame. Issues #2 (multiple demons), #3 (Dark Heart topology), and #5 (worm double-use) all collapse into "the cage demands it." Issues #1 (demon termination) and #4 (mobility history) close with single sentences.

### What the LLM actually contributed here

Not the keystone — that came from me. But once the keystone landed, the LLM traced the downstream consequences faster and more exhaustively than I would have working alone. It connected the cage concept to the "why Menzoberranzan" question, to the slugfest driver, to the Tripod's three functions, to the reconstruction branch's sharp consequences, all in one response.

This is what LLMs do well: given a locked architectural constraint, propagate it fast across a known corpus. The constraint has to come from somewhere — it came from me — but the propagation is a real labor savings.

### The asymmetry worth remembering

The keystone was the *simplest* contribution in the whole conversation. One sentence. Twenty-five words. It's the cheapest input in terms of text generated, and it's the only input that closed the architecture.

The LLM's outputs were orders of magnitude larger. They were also, individually, wrong more often than right until the keystone landed. The LLM cannot produce the keystone because the keystone requires believing one specific thing about Vizeran's intelligence and character, and then asking what mechanism his intelligence would have demanded. That's a character-logic move, not a structure-traversal move.

---

## Turn 5: the sharpening

I followed up: *"what if the party kills Vizeran — in that case the attraction spell works, and the demons do arrive, but they don't all fight to the death. Demon lords loathe each other and the satisfaction of killing one another and given that for the last little bit they have been trying to kill each other is too much of an optimal thing to pass up. Furthermore, they all know that anyone who escapes will be 10x harder to kill and keep getting in their way, so they would fight in the absence of the tether, but some of them would flee rather than die. So if the party kills Vizeran, the city still falls, the demons still rage, and the party has to deal with more than 1 demon at the very end. In fact, part of what they must accomplish is killing the fleeing demons who would be weakened..."*

This is the second architectural insight. It sharpens what the cage does and doesn't do.

My initial framing had the cage *causing* the slugfest. The sharpened frame: the cage doesn't cause the slugfest. Mutual hatred and game-theoretic necessity cause the slugfest — demon lords know that every rival who escapes wounded today is exponentially harder tomorrow. Killing each other now, weakened, is rational. They would fight without the cage.

What the cage prevents isn't fighting — it's **flight**. In the cage, losers either win or die. Outside the cage, losers break contact when the outcome becomes clear.

This gives the kill-Vizeran branch a clean mechanical shape:

1. Tripod fires (components are anchor-independent: beacon, portal, stampede all ignite whether Vizeran is alive or dead).
2. Demons arrive. City falls.
3. Demons engage each other. Some die → banished by MM default.
4. Wounded losers flee rather than fight to the death.
5. Party endgame converts from "kill the weakened sole survivor" to a **hunt**: pursue multiple wounded demon lords through the falling city and the surrounding Underdark before they reach a redoubt and recover.
6. Each killed = one fewer loose thread. Each escaped = a permanent post-campaign threat. Faerzress keeps escapees Prime-bound — they cannot self-plane-shift home.

Now the kill-Vizeran branch isn't a "bad ending." It's a *messier* success. More combat. More aftermath. Deliberate trade. And it strongly motivates the Vhaerun post-arc, because the Blink-authorship archive becomes the only lever left on the lingering demon presence.

### What the LLM contributed here

Accepted the sharpening, built a clean comparison table, and caught one consequence I hadn't stated explicitly: the Faerzress trap (the same condition that made OotA's premise work) keeps escaped demon lords Prime-bound. They can't self-banish. They go to ground in the Underdark and become aftermath threats. This connected the modified end-game back to OotA's own premise in a way that tightened both.

### The two insights together

Insight 1 (cage): the design's *primary* branch works mechanically. Insight 2 (flee vs die): the design's *secondary* branch — kill Vizeran — works mechanically, and is a trade, not a fail state.

Neither insight came from the LLM. Both came from me thinking about what a character as smart as Vizeran would have planned, and about how demon lords would actually behave under specific pressure conditions. These are character-logic and game-theory moves, both rooted in domain expertise.

---

## Turn 6: propagation

I said *"yes"* to the proposal to propagate the locked architecture across five canon docs. Claude executed coordinated edits to:

- `docs/campaign_master_plan.md` — rewrote Section VI ("The Final Payout: The Apocalypse") with explicit cage mechanics and a fully specified kill-Vizeran branch.
- `docs/canon_guardrails.md` — updated the Living Circuit hard constraints section with cage semantics; split the Recovery Pattern for Vizeran death into two cases (before Tripod activation = reconstruction branch; during/after = cage collapse and hunt phase).
- `docs/risk_levers.md` — narrowed Ritual Collapse to pre-activation scope only; entirely rewrote Living Circuit Failure to own cage-collapse semantics, with trigger, warnings, immediate and downstream consequences, mitigation, and ownership all consistent with the new architecture.
- `docs/decision_ladders.md` — updated the Vizeran Disclosure Stage 4 proof condition (cage visibility) and expanded the required decision to three mechanically distinct options (Complete / Break / Kill Vizeran), each with explicit downstream consequences.
- `docs/npcs/vizeran_devir.md` — rewrote the Hidden Truths line to state Vizeran is the cage (not just the battery) and that death is the seal resolving.

This took the LLM maybe five minutes to execute. It would have taken me two hours to do by hand, and I would have introduced inconsistencies — a clause in one doc that contradicts a clause in another — because coordinated multi-doc edits are where humans get sloppy and LLMs (given a locked design) are precise.

### This is where LLMs genuinely earn their keep

Propagation tasks have two features that make them LLM-suitable:

1. **The architectural decision has already been made.** The LLM is not choosing anything structural; it's expressing a chosen structure across multiple surfaces.
2. **Consistency across surfaces matters.** The same constraint expressed five different ways is exactly what humans tend to drift on.

Under those conditions, the LLM's weaknesses don't matter (it's not architecting anything) and its strengths dominate (fast, consistent, exhaustive expression).

---

## Turn 7: the rationale doc

After propagation, I asked for a long document explaining the original module, the extension's changes, and the rationale, for sharing with other DMs running the same campaign.

Claude wrote `docs/endgame_extension_rationale.md` — roughly 3000 words, structured as: orientation (what the original does), seven structural changes, what's preserved, why (root problems addressed), tradeoffs and costs, seven open questions for DM feedback, comparison table.

This is another rendering task. Given a locked design and a locked critique of the original, produce a polished comparison document. The LLM does this well because there are no architectural decisions left — only expression decisions.

I reviewed the output line by line. It was accurate. It didn't need re-architecting. It needed (in principle) light editing for tone and some reordering for emphasis, which I could do directly in the text.

---

## What I take from this

### 1. LLMs are renderers, not architects

Every time the conversation needed an architectural insight — the MM rule, the cage, the flee-vs-die distinction — it came from me. The LLM's contribution was to expose the design to pressure so I could see where the gaps were, and then to propagate my insights once I supplied them.

This maps directly to a principle I try to work from: **LLMs are good at taking verified structure and making it expressive. They are unreliable at scope decisions, temporal ordering, and respecting boundaries they can see past.** "What is Vizeran's mechanism of containment?" is a structural question. The LLM can critique answers to it (five plot holes, ranked). It cannot generate the right answer.

### 2. The value of the first pass is articulation, not discovery

When I asked the open-ended audit question, I didn't learn anything I hadn't sensed. What I got was a clear, ranked, defensible articulation of what I had sensed. That articulation is what made the next five turns possible. You can't attack "something's off." You can attack "the Tripod imports demons but does not terminate them."

I'd use this pattern again. Not to find bugs — to force the design to defend itself in concrete terms so I can see where to push.

### 3. Correct, don't argue

I never debated the LLM. When it was wrong, I said one line of redirection ("it's in the original," "check the MM"). Debate is expensive; correction is cheap. The LLM is going to be confident in its wrong answers because it doesn't have the concept of "I might be wrong about this specific thing." You don't need to negotiate with the confidence — just redirect.

The LLM took the redirections well. It revised, retrieved primary source, and converged. It never doubled down. This is a strength of the interaction model.

### 4. Keystone insights compound; mid-sized critiques don't

The cage insight closed five separate issues at once. That's not luck. That's the shape of architectural insights — they are load-bearing, and when they land, everything downstream clicks.

The LLM's five ranked plot holes were mid-sized critiques. Individually, they were fixable, but fixing them individually would have produced five local patches without the unifying frame. The cage insight is the frame. It wasn't in the LLM's list because the LLM can't generate keystones; it can only react to them.

If I'm using an LLM for design critique going forward: I should take its output as a **map of where to think**, not a to-do list. The right move isn't "fix plot hole #1 then plot hole #2." It's "stare at the ranked list until I see the architectural frame that makes them all dissolve simultaneously."

### 5. Propagation is the cleanest LLM win

Once the architecture was locked, the five-doc coordinated edit was fast, consistent, and accurate. This is the task where LLMs are unambiguously useful — verified structure in, expressive rendering out, no architectural judgment required.

I try to set up work so that propagation is a separate step from architecture. Don't ask the LLM to architect and propagate in the same pass; errors compound silently. Architect (with human judgment), lock the design, then propagate. The rationale doc is the same pattern at a different altitude: locked critique in, polished expression out.

### 6. The LLM's errors were informative

The sequence of wrong answers — "the demon problem isn't solved" → "the original has a fig leaf" → "MM rule makes it work, modified still has gap" — traced the shape of *my own* blind spots. I hadn't explicitly applied the MM banishment rule. I hadn't explicitly articulated what specifically was missing in my modified version versus the original. The LLM's wrong answers made those absences legible.

This is the most subtle win and the one I didn't expect. Being wrong *specifically and concretely* is more useful than being right vaguely. A vague right answer ("this is mostly fine") would have let me keep my blind spots. Specific wrong answers forced me to articulate why they were wrong, and that articulation closed the gaps.

---

## Honest failure modes

I want to be specific about what went wrong, not just what went right.

**The first-pass ranking was wrong.** The top-ranked issue was inherited from the source module. Issue #4 (mobility history) was a documentation gap, not a plot hole. Issue #5 (worm double-use) was already implicitly answered in the text (bound mounts are a small handful; pheromones summon wild populations). A reader who took the ranked list at face value and tried to fix issues in order would have introduced a fix to a non-problem (binding demons to collapsing ley lines) and potentially broken the module's canonical mechanism in the process.

**The "fig leaf" framing of the original was overconfident.** In Turn 2, the LLM claimed the original module's rage-trigger was narrative fiat. It was, sort of — the module says the demons "see each other and fight" — but the underlying banishment mechanic is canon (MM default), so the fiat only covers one step. A better LLM answer would have said "I don't know if this mechanism is load-bearing or if it's leaning on canon I'm not seeing — can you verify?" But calibrated uncertainty is not something these systems produce reliably on their own.

**The LLM never volunteered the MM rule.** It knew the rule (it could retrieve and apply it once I pointed to it). It didn't apply it proactively. This is a general failure mode: LLMs reason forward from what's in the prompt more reliably than they reason outward from what they know but wasn't mentioned. If your question doesn't gesture at the right canon, you won't get the canon applied.

**Once the cage insight landed, the LLM moved very fast.** That's a mixed blessing. It produced the comparison table, the propagation plan, and the five-doc edits in quick succession, and they were correct. But "very fast and correct" in this context means I had to review carefully — the same system that produced the wrong ranked list in Turn 1 is producing the locked propagation in Turn 6, with no shift in its confidence level. I can't tell from the output which turn is which. I have to trust my own review, every time.

---

## If I were running this again

Prep differently. Before asking the open-ended audit, gather the canon touchpoints I know are relevant — MM rules on fiends, Chapter 17 of the source module, the specific mechanical claims in my extension. Put them in the prompt. The LLM's first pass would be better-grounded; the two correction turns would be unnecessary.

Ask for uncertainty explicitly. Something like *"for each plot hole, rate how confident you are that it's a real problem versus a documentation gap versus a possible misreading of canon."* Forcing the LLM to express calibration surfaces the overconfidence that otherwise hides in clean prose.

Architect alone; propagate together. Once I had the keystone insight, the propagation step was clean. If I'd tried to co-architect with the LLM — "help me think about what Vizeran is" — I'd have gotten more of the same kind of five-bullet structural critique, not the cage. Architecture needs silence and character-logic reasoning. Propagation needs the LLM.

Review every propagation output line by line. The LLM will not tell you when it drifted. You have to read the diffs.

---

## Closing

What I have now is an end-game I couldn't have written in isolation and the LLM couldn't have designed for me. Five canon docs are consistent. The primary branch has a mechanically honest demon-termination path: Tripod fires → cage seals demons inside the city → captivity and rivalry drive mutual combat → party kills the last weakened survivor → MM-default banishment resolves everything. The kill-Vizeran branch is a deliberate trade with sharp mechanical consequences: cage drops, demons still fight but losers flee, finale converts to a hunt, Faerzress keeps escapees Prime-bound as aftermath threats. Vizeran's motivations ladder cleanly from his doctrine (anti-recurrence absolutism) through his method (synchronized collapse) to his mechanism (make himself the last prison). The whole architecture is load-bearing in a way I can now defend under player questioning.

The thing I most want other DMs using LLMs for design work to take from this: **the LLM is not your co-designer. It is a fast first-draft partner for articulation and propagation. The architectural work is still yours. When the LLM is wrong, correct in one line and move on. When it's right, verify before trusting. When you get a keystone insight, give the LLM the chance to propagate it — that's where the leverage is.**

The two-hour conversation produced a locked design across five docs plus two long-form documents (this one and the rationale). I could not have done it in two hours alone. The LLM could not have done it at all. The division of labor is the whole lesson.
