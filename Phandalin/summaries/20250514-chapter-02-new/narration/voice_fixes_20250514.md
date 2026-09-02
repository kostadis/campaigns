# Voice fixes — 20250514-chapter-02-new, 2026-09-02

**49 hand edits applied across 6 scenes**, from the GM's blanket ACT on both triage pages.

## ⚠️ These fixes are not durable. Read this before running /scrub.

`/scrub` regenerates `.scrubbed.md` from the raw `.md`. **Every edit below that landed in a
`.scrubbed.md` will be silently destroyed by the next scrub run on that scene.** They are not
in `.scrub_state.json` and nothing else remembers them. This file is the only replay record.

Which file each scene's fixes landed in — **it is not uniform**:

| Scene | Fixes landed in | Why |
|---|---|---|
| 02, 03 | `session_doc_scene_NN_*.md` (raw) | no `.scrubbed.md` exists for these scenes |
| 04, 05, 07 | `session_doc_scene_NN_*.scrubbed.md` only | scrubbed variant exists and is what assembles; **the raw still carries the old prose** |
| 01, 06, 08 | — | no fixes; no action was required |

For 04, 05 and 07 the raw and scrubbed have now diverged in prose as well as residue. A
re-run of `sd_narrate` on those scenes discards both layers.

## Backups taken

| File | What it is |
|---|---|
| `session_doc_scene_04_*.prior-render.md.bak` | the pre-10:39 render (superseded, kept for reference) |
| `session_doc_scene_07_*.prior-render.md.bak` | **the render now in use** — scene 07 was rolled back to this |
| `session_doc_scene_08_*.prior-render.md.bak` | the pre-10:41 render (superseded) |
| `session_doc_scene_02_*.prior-render.md.bak` | **the render now in use** — scene 02 was rolled back to this |
| `session_doc_scene_02_*.render-1110.md.bak` | the 11:10 re-render, rejected as worse (35.9% prose vs 49.5%) |

## Two rollbacks

**Scene 07** — the 10:39 re-render lost 22% of its narration, grew a 16-line unattributed run
where the previous render had speaker beats, and doubled its closers including the one line the
critique had asked to preserve. Restored from `.prior-render.md.bak`, then the one GM-approved
scrub decision that applies to that text was replayed (`the 50 gold pieces` → `the fifty gold
pieces`, 3 occurrences on 2 lines). Verified clean of the other residue classes.

**Scene 02** — re-rendered at 11:10 under G1 to move it onto the committed rulebook. The result
was worse (prose 49.5% → 35.9%, runs 6 → 7), so it was rolled back and the current-rulebook
rules were applied by hand instead. **Scene 02 therefore still records an older rulebook**;
that is a provenance gap, not a rules gap.

## Edits by scene

### Scene 02 — `session_doc_scene_02_the_gray_begins_at_the_wall.md` (raw) — 5 edits

| # | Old | New | Finding |
|---|---|---|---|
| 1 | `…neither can be eaten unless a merchant accepts moral conviction in place of payment.` | `…I have counted my coins. Twice, in case the first count was pessimistic.` | G2 closer |
| 2 | `It is an extraordinary legal theory. Property remains property inside Neverwinter, ceases to belong…` | `I look at the wall behind him. It is the same stone on both sides.` | G2 closer |
| 3 | `“Do you bring their scalps? Seems vile.”` | `+ “,” Soma says.` | G3 attribution |
| 4 | `“Like a cat delivering a dead mouse.”` | `+ “,” Soma says.` | G3 attribution |
| 5 | `“I just want you to know that is the — …”` | `The guard spreads his hands. + quote` | G3 attribution |

Kept deliberately: **02:95** *“Everyone benefits except the dead people whose possessions are
sitting in a monster's chest.”* and **02:143** *“…a retirement fund wearing the hat of an
orphaned-property office.”* Vukradin therefore sits at **2 closers against a budget of 1** — a
deliberate breach, approved as G2.

### Scene 03 — `session_doc_scene_03_first_sight_of_phandalin.md` (raw) — 1 edit

| Old | New | Finding |
|---|---|---|
| `It is quaint. This is rarely good.` | `It is quaint. Nothing about it is defended.` | G4 closer |

Kept: **03:61** *“Some places mistake that for a plan.”* Soma is now at exactly 1 for the session.

### Scene 04 — `.scrubbed.md` — 29 edits (2 taxonomy, 4 closers, 23 attribution)

Taxonomy (F3):
- `Surface politics remains committed to disguising paralysis as procedure.` → `Harbin has not decided. That is the whole of it.`
- `Surface morality can be remarkably efficient when no actual restitution is required.` → `Brewbarry said nothing and was forgiven anyway. Nobody asked him for anything.`

Closers (F2), keeping **153** (`My sisters would consider this an invitation`): trimmed at 53,
91, 165, 193.

Attribution (F1): 23 speaker tags and action beats added, sourced from
`scene_extractions_smoothed/04_arrival_at_the_stonehill_inn.md`. **No word inside any quote was
changed.** Orphan runs 12 → 5, longest 8 → 6.

### Scene 05 — `.scrubbed.md` — 6 edits

- 2 closers trimmed (`A clean exchange.`, `…becomes municipal inventory.`) — G2
- 2 attribution tags (Soma ×2) — G7
- 2 excisions completing the half-reclassified exchange — G6: `“No, that we're his favorite group
  of players.”` + its orphaned narration line, and `Soma pauses. / “Trying. Yes.”` whose question
  was reclassified as table speech. Blank runs collapsed.

**G6's excisions are scrub-class, not voice-class** — they belong in the scrub manifest as well,
recorded below.

### Scene 07 — `.scrubbed.md`, post-rollback — 13 edits

Taxonomy ×2:
- `Surface dwellers become exquisitely protective of differences once the similarities are spoken aloud.` → `He has told me my own liturgy and objected to the accent.`
- `A standard surface moral taxonomy: weapons become harmless when carried by agreeable strangers.` → `Norbus looks at my mace and decides it is furniture.`

Closers: kept **87** *“Convenient. The dead lose their rights when their theology becomes
distasteful.”* — the line the critique named as Valphine's single survivor. Trimmed 51, 125, 247.

Attribution: 8 tags. Orphan runs 8 → 6, longest 6 → 4.

## A collision I introduced and caught

While tagging scene 04 I wrote `Toblen recites it like a man who has said it before.` — that is
the **banned `like a man who` taxonomy shell**, one of the four the rulebook added in the ch40–48
sweep, and `voice_lint` would have failed on it. Replaced with `Toblen recites it without
pausing.` before finalising.

Recorded because it is the exact hazard the skill warns about: a fix pass can introduce the
defect the pass exists to remove, and a span-local applier cannot see it.

## Verification

- `voice_lint` across all 8 scenes: **0 errors, 0 warnings**, exit 0.
- Grep for every banned shell (`the shape of`, `with the X of a man`, `like a man/woman/person/someone`, `I file/filed`): **none**.
- Connective em-dashes in narration prose: **0**.
- Doc prose share: 53.7% (4,974 / 9,265 words).

| Scene | Orphan runs before → after | Longest before → after |
|---|---|---|
| 02 | 6 → **4** | 5 → **4** |
| 03 | 0 → **0** | — |
| 04 | 12 → **5** | 8 → **6** |
| 05 | 2 → **1** | 3 → **3** |
| 07 | 10 (pre-rollback) → **6** | 16 → **4** |

## Still outstanding

- **Scenes 02 and 03 have never been through `/scrub`** against their current text (G5). Scene 03
  carries `“How long have we been walking?”`, which reads as player-to-GM table speech.
- **Quote typography is still mixed** (G5): 01/02/04/07 curly, 05/06/08 straight, 03 mixed
  internally. To be normalised at assembly, not by hand-editing eight files.
- **Scene 02's rulebook provenance** — it records an older digest and was not re-rendered, by
  choice. See the rollback note above.
