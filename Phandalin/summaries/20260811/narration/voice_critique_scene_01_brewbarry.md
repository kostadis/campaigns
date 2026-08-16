# Voice Critique — Brewbarry, scene 01: Bathrobe Speech to Empty Room

**Narration:** `session_doc_scene_01_bathrobe_speech_to_empty_room.md`
**Input shape:** per-scene

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record (post-#276); 61 lines, 7547 chars |
| Rulebook vs run record | match | recomputed `sha256(stripped)[:12]` identical |
| HARD BANS | `base.md` | 4221 chars |
| Voice spec | `brewbarry_new_pipeline.md` | rule (c) — unique key beginning `brewbarry_` |
| Per-char examples | `brewbarry.md` | stem == first name; 1851 chars |
| Global examples | none | — |
| Party doc | `docs/party.md` | roster 4/4 PCs |
| voice_lint | ran | 0 errors, 0 warns, 1 skipped check |

## Budget ledger

**Scope: single scene — doc-level budgets NOT evaluable here.** See `voice_critique_summary.md` for the ledger computed across scenes 01–08.

Scene-local observations only: 5 em-dashes, **all inside verbatim dialogue**, 0 in narration prose. First-person present throughout; the `Last night I stood in front of the glass` passage is a memory, which `base.md` explicitly allows.

## Flags

None.

The section is short declaratives with almost no gap between feeling and action, which is `brewbarry_new_pipeline.md`'s first spec line. `My words go up into the rafters and come back down with nothing on them.` and `He starts choosing them. I can see him choosing. Then Vukradin steps in front of the choosing.` are specific rather than generic, and the costume beat executes spec line 43's rage/mercy structure — `My rage stirs. And yet.` — verbatim in form, including the pause the spec asks to be left standing.

`he carries it the way I carry the halberd` was checked against the behavioral-taxonomy ban and **cleared**: it compares against the narrator's own handling of his own weapon, not a class of people, and weight-and-carry is exactly Brewbarry's observational lens per the rulebook.

## Reclassified table speech

One hatch, three spans:

> `"So I walk into the counting house."` | `"Booming voice, and I say: Hello, good folks, I am Brewbarry Rootsmasher, Ogolo… no, sorry. OG… Ogonakanu. Yes."` | `"He goes: oh, what are you making again?"`

All three describe their own speaker in the third person or narrate the action rather than speak it. The reclassification looks correct; the beats survive in the prose (`I fill my chest and I boom the greeting I built last night`, `I trip on the tribe part, back up, take it again, land it`, `He asks what it is I'm making again`). **GM: accept or reject.**

## Render defect

Line 77, inside verbatim dialogue: `"Okay. Alright, this is Brewbarry'smoment. Go for it."` — missing space. Extraction artifact, not a voice issue.

## Verdict

No voice findings. The scene holds Brewbarry's register without reaching for a single portable construction.
