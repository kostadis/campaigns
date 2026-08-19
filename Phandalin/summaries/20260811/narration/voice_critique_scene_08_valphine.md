# Voice Critique — Valphine, scene 08: Cullen Sharpe at the Quay

**Narration:** `session_doc_scene_08_cullen_sharpe_at_the_quay.md`
**Input shape:** per-scene

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record (post-#276); 61 lines, 7547 chars |
| Rulebook vs run record | match | recomputed `sha256(stripped)[:12]` identical |
| HARD BANS | `base.md` | 4221 chars |
| Voice spec | `valphine_new_pipeline.md` | rule (c) — unique key beginning `valphine_` |
| Per-char examples | `valphine.md` | stem == first name; 12750 chars |
| Global examples | none | — |
| Party doc | `docs/party.md` | roster 4/4 PCs |
| voice_lint | ran | 0 errors, 0 warns, 1 skipped check |

## Budget ledger

**Scope: single scene — doc-level budgets NOT evaluable here.** See `voice_critique_summary.md`.

Scene-local: 14 em-dashes, **all inside verbatim dialogue**, 0 in narration prose. First-person present throughout. This is the longest section of the session and it holds tense and POV without a slip.

## Flags

### [1] Rulebook conflict — behavioral taxonomy (profession as explanation)

> Cullen is not intimidated. Cullen is enjoying himself, the way a fencing master enjoys an enthusiastic student.

**Why:** `base.md` HARD BAN — "class, or profession as the explanation for what one person just did", banned "whatever shell it arrives in." *A fencing master* is a profession supplying the read in place of what Valphine actually watched Cullen's face and body do, and it is the third instance of this move in her two sections.
**Suggested rewrite:** `Cullen is not intimidated. Cullen is enjoying himself; he lets the pat land, and he does not step back from it.` — spec: "She narrates with cool precision, as if cataloging a specimen"; the observed detail is already in the scene, since Brewbarry has just patted him twice.

## Cleared on inspection

- `Margaster Logistics Operations occupies its stretch of waterfront the way a well-bred predator occupies a clearing` — a simile for a *place*, not an explanation of a person's behaviour by their class. It is close to the family and worth watching, but the colon that follows (`nothing out of place, nothing wasted, nothing accidental`) immediately renders the specifics, which is what the ban asks for.
- `I know the taste of a forgery the way a vintner knows a corked bottle` — the narrator's own inherited skill, not a third party's behaviour, and grounded in the specific tells that follow (`the seal a fraction too crisp, the ink aged in the wrong order`).
- `They mistake restraint for kindness up here, all of them.` — **spec-licensed**, `valphine_new_pipeline.md` line 46 ("Her recurring read on surface religiosity… they mistake restraint for kindness"). Not a finding.

The closing paragraph — `The dawn is not kind. The dawn is inexhaustible power arriving on schedule, and everything that cannot bear it withers.` — is spec line 45's faith register almost to the word (radiant, indifferent, inexhaustible; never sentimental consolation), and `In Menzoberranzan we had a shorter word for it: *survival*.` is the spec's controlled, unsentimental use of her past.

## Reclassified table speech

One hatch, twenty-eight spans — the largest in the session, and correctly scoped. It pulls all the roll-calling (`"Valphine, roll your insight."`, `"So you failed your intimidation check, so…"`, `"Roll your… roll your deception, bro."`, `"Alright, a 6, awesome."`, `"11."`, `"You got two ones."`), the GM's adjudication (`"He doesn't notice the lie. He thinks you're just being a barbarian who doesn't know what he's talking about."`), and the session-planning line at the end.

**Two spans in this hatch carry GM-side weight and should be read before accepting:**

> `"I have a feeling I know who the gnome is."`

This is Dave speaking out of character. `campaign_state.md` records it explicitly as **player knowledge only — Vukradin does not know who KP is**, and the party has connected nothing to the manifold sabotage. Pulling it from the fiction is not merely a style call; leaving it in would have leaked the Bimble Nackle irony trap. **The reclassification is correct and load-bearing — accept.**

> `"Valphine, I think you have a special ability now related to your character, where you can detect lies or cause people who are lying."`

Also correctly pulled, and the prose renders the beat in-fiction instead (`Something in me settles into the stillness Lathander has been teaching me, the quiet that lets a lie ring against the ear like a cracked bell`).

## Render defect

Line 79, inside verbatim dialogue: `"It's much safer withus."` — missing space. Extraction artifact, not a voice issue.

## Verdict

One instance of the banned profession-as-explanation move, the third across Valphine's two sections this session — a single-sentence spot edit, but the recurrence is the reason her spec is where any re-narration budget should go.
