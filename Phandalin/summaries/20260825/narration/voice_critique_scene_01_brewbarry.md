# Voice Critique — Brewbarry, scene 01: A Banker's Revelation

**Narration:** `session_doc_scene_01_a_banker_s_revelation.scrubbed.md`
**Input shape:** per-scene, targeted (single scene)
**Supersedes:** the critique of the codex-cli render, preserved as `voice_critique_scene_01_brewbarry.md.codex-cli.bak`.
**Doc-level budgets:** a single-scene critique cannot evaluate them. The doc-wide ledger is in `voice_critique_summary.md`; where this scene contributes to a doc-level row it is said so explicitly below.

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | `paths.genre_file`; 61 lines, 7,595 chars |
| Rulebook vs run record | match — unedited since render | recomputed `sha256(text.strip())[:12]` |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4.1K |
| Voice spec | `voice/brewbarry_new_pipeline.md` | declared `voice:` in `config/party.yaml` |
| Per-char examples | `examples/brewbarry.md` | declared `examples:`; 1.8K, two full POV sections from ch3 and ch5 |
| Global examples | none | no `shared_examples:` declared |
| voice_lint | ran (exit 0) | 0 errors, 0 warnings, 1 skipped check |

**Render provenance:** `--backend claude-code --model claude-fable-5`, 2026-08-31, replacing the `codex-cli` render of 2026-08-30. The `.knobs.json` sidecar still read `"backend": "codex-cli"` after the re-render — `sd_narrate` does not write it, the editor does — and was corrected by hand. See the amendment in `scrub_manifest_20260825.md`.

## What changed

| | codex-cli | fable | |
|---|---|---|---|
| narration prose | 244 w (31%) | **477 w (48%)** | now inside the 52–67% band of the other seven scenes |
| quoted lines | 66 | 52 | |
| attributed quoted lines | **0** | **26** | the defect that made the old render a transcript |
| connective em-dashes in prose | 0 | 0 | |
| taxonomy constructions | 0 | 0 | |

The old critique's single finding — "the section does not narrate" — **is resolved.** The forty-line untagged block is gone; every beat now has a POV holding it.

## Scene-scoped ledger

| Check | Observed | Rule | Verdict |
|---|---|---|---|
| connective em-dash | 0 (10 in file, all inside verbatim quotes) | rulebook: interruption only | ok |
| `the shape of` / portable portrait | 0 | banned | ok |
| `the way X …` taxonomy | 0 | banned | ok |
| first-person present tense | throughout | always | ok |
| POV — no narrator third person | clean | always | ok |
| recap framing | 0 | 0 | ok |
| generic fantasy reach | 0 | 0 | ok |
| event order follows the extraction | yes — spot-checked L79, L89 against `scene_extractions_smoothed/01_*.md` | always | ok |
| bookkeeping / filing caps | — | — | *not checked — rulebook declares no ```yaml voice_lint``` block* |
| doc-level budgets | — | — | *not evaluable from one scene — see the summary* |

## Flags

### [1] `Then Vukradin himself:` — broken construction — CONFIRMED

> "Enough," Vukradin says. Then Vukradin himself: "We wrote the name down. It says here, Bimble." Then, louder: "Bimbo the Gnome!"
> — L79

**Why:** "Then Vukradin himself" directly after "Vukradin says" reads as a botched edit — *himself* as opposed to whom? It looks like a misattribution, which is why I checked it against the source, and it is not one: `scene_extractions_smoothed/01_a_banker_s_revelation.md` L135–151 credits **Vukradin** with "Enough." (marked *interrupting*), with "We wrote the name down.", and with "Bimbo the Gnome!". All three attributions are correct. Only the connective prose is broken.

**Suggested rewrite:** the beat is three Vukradin lines escalating, so name him once and let the rhythm carry the rest — *"Enough," Vukradin says. Then: "We wrote the name down. It says here, Bimble." Then, louder: "Bimbo the Gnome!"*

### [2] `A small-business woman knows how food moves in a city.` — wrong syntax for this narrator, and a doc-level frame — CONFIRMED

> A small-business woman knows how food moves in a city. Who buys too much for one mouth. Lim might have a bead on how a hidden man gets fed.
> — L139

**Why, first on its own terms:** this is a fluent, well-formed English aphorism, and Brewbarry does not produce those. His spec: "short, declarative sentences… He does not build arguments, justify himself, or hedge. He states what is true and moves." His examples file makes the register unmistakable — when he generalises about a class of people he does it in his own broken grammar:

> Order is bullies. They bully barbarians.
> — `examples/brewbarry.md`, ch5

The *content* of L139 is fine and the deduction is his to make. The syntax belongs to somebody else.

**Why it is also a doc-level finding:** the frame `A [class] [verb]s [general truth]` now appears six times across three narrators — Brewbarry (this scene), Vukradin (`A performer knows the difference between a joke that failed and a room that wasn't listening`, `A being who counts your days deserves to be addressed properly`), Valphine (`A tortle who counts what leaves a building is a tortle worth listening to`, `A merchant whose costs do not twitch when the artery is severed was never drinking from the artery`). Same shape as the `the way X …` finding: one frame, every POV, the noun swapped. In the earlier pass I had this as PLAUSIBLE and confined to Valphine; the new scene 01 is what makes it cross-narrator and confirmed.

**Suggested rewrite, in his grammar:** *Lim feeds people. She buys the food. She would see who buys too much for one mouth.*

## Not flagged

### `A warrior checks his straps before battle. Same thing.` (L31) — same frame, and I would keep it

Structurally this is flag [2]'s construction, but it is doing the opposite work. Brewbarry's spec says "He is still learning surface-world norms and asks honest questions that reveal how much he does not know" — here he is mapping an unfamiliar surface behaviour (a banker fussing his coat straight) onto the only frame he has. And `Same thing.` is his syntax, not an essayist's. This is the character reaching, not the narrator reaching.

### The rest, which is the strongest short-form Brewbarry in the session

> Cullen Sharpe and House Margaster still sit in my teeth like gristle. (L9)
> Small lungs, big hurry. Aurelan Vance. My banker. (L13)
> Mine, is which one. The man holding my bathrobe money. (L17)
> A banker's small name. He hands it to me like a coin from his own pocket, not the bank's. (L57)
> Real anger in him. Not blood-anger like mine. Paper-anger. (L99)
> Kept. Fed. Or. (L103)
> Find the food, find the man. That is good hunting. Ori is a hunter after all. Just on paper. (L111)
> Soup first. Then the gnome. (L143)

`Kept. Fed. Or.` is the best thing in the section — a one-word sentence carrying a whole suspicion, which is exactly what his spec means by "very little space between feeling and acting." The `paper-anger` / `paper hunter` pair at L99 and L111 is earned reuse rather than repetition: it is set up, then paid off eighty lines later.

**Four similes** (L9 gristle, L51 checking for cracks, L57 the coin, L99 blood/paper-anger) is on the high side for a narrator whose spec forbids building arguments — but every one is bodily or material, which is his declared lens, and none is a workshopped fantasy simile. Noting, not flagging.

`huffy-puffy` (L31) reads oddly against his register but it is lifted from the GM's own words at the table, and it is the kind of word he would repeat back.

`maintenance roll` (L91, L105) is a payroll register, not a die roll. Not residue. The scrub's scanner returned **0 candidates** on this scene for the second time running.

## Reclassified table speech

**One hatch, 2 spans** — down from ~25 in the codex render:

> "He struggles to say Mr. Brewbarry, but then realizes we're on friendly terms. Brew — that is how a contract is abandoned!"
> "And because he's a banker, and this is the only kind of question he's any good at: he has drawn nothing since. He has not banked, he has not borrowed, and he has not left. Your Harper friends would tell you the same if you had any — so somebody is keeping him. Find who feeds a man, and you have found the man."

Both are GM narration *about* a character rather than speech *by* one, which is the documented tell, and both survive in the narration — the first rendered at L97, the second at L101 and L111. Correct calls, and a much smaller scope decision than the 25-span hatch it replaces.

## Scrub apparatus

One `*Marginal note in a later hand: "Bimbo" … — Kostadinious the Sage*` paragraph at L131, GM-confirmed. Apparatus, not narration — not critiqued against the narrator's voice. The companion `Bingo` note from the first pass was **not** re-added: fable drops the word entirely, so it would have glossed a term the scene never uses.

## Verdict

The transcript problem is gone — 0 → 26 attributed quoted lines and prose from 31% to 48% — and `Kept. Fed. Or.` is the best single beat in the document. Two things left: `Then Vukradin himself:` at L79 is a broken connective, not the misattribution it looks like; and `A small-business woman knows how food moves in a city` is a well-formed English aphorism in the mouth of a narrator whose own examples say *Order is bullies. They bully barbarians.*
