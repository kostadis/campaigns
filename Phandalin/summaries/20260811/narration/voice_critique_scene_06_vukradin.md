# Voice Critique — Vukradin, scene 06: Title Insurance at the Notary

**Narration:** `session_doc_scene_06_title_insurance_at_the_notary.md`
**Input shape:** per-scene

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record (post-#276); 61 lines, 7547 chars |
| Rulebook vs run record | match | recomputed `sha256(stripped)[:12]` identical |
| HARD BANS | `base.md` | 4221 chars |
| Voice spec | `vukradin_new_pipeline.md` | rule (c) — unique key beginning `vukradin_` |
| Per-char examples | `vukradin.md` | stem == first name; 15936 chars |
| Global examples | none | — |
| Party doc | `docs/party.md` | roster 4/4 PCs |
| voice_lint | ran | 0 errors, 0 warns, 1 skipped check |

## Budget ledger

**Scope: single scene — doc-level budgets NOT evaluable here.** See `voice_critique_summary.md`.

Scene-local: 8 em-dashes, **all inside verbatim dialogue**, 0 in narration prose. First-person present throughout.

## Flags

None.

`*Scandalous.*` is a spec verdict word (`vukradin_new_pipeline.md` line 42) landing exactly where the spec says it should — case closed in his head. `The cleanest room in their whole operation, and that is exactly the point.` and `Not the crime. The laundering of the crime into penmanship.` name the specific corruption rather than "the system", which is spec line 55. The long paragraph at line 85 (`the true ledger sits open in front of me…`) is the spec's clause-stacking moral-case register resolving into a verdict, and it keeps him sincere rather than sardonic — failure-prevention rules 1 and 2.

## Not flagged — spec-licensed

> The paperwork is beautiful. That is precisely what worries me. I own a fourth-level slot that can turn a man into a different man; this is not paranoia, this is professional knowledge.

`base.md`'s soft AVOID list includes "Mechanical detail (rolls, HP, spell slots)", but the campaign rulebook explicitly overrides it — "Drop hit points, distances, spell names directly into prose. Mechanics are not separate from feeling" — and `vukradin_new_pipeline.md` line 44 makes clean procedural mechanics his precision register specifically. Correct as written, and the campaign-specific rulebook is the authority here.

## Reclassified table speech — **MISS**

**No hatch is present in this file, and six spans of dice-mechanics table talk are live in the narration as in-fiction dialogue.** Scene 08 correctly pulled exactly this class of line, so the pass is inconsistent between sections of the same session.

The spans, lines 25–35:

> `"You know, 13 investigations. Maybe Valphine could look, too?"`
> `"20 insights, and then…"`
> `"20… wait, what? I think double rolls."`
> `"You got a 9 perception?"`
> `"Looks like I had a 9 perception."`

…plus the narration sentence built on top of them: `"We're going with the Insight roll." That's not favoritism, that's methodology.`

These are roll results and roll adjudication, not in-fiction speech — distinct from the spell-slot line above, which is a character reasoning about a capability. `base.md` names *rolls* separately from HP and slots in its AVOID list for this reason.

**GM decision required.** This is the last point at which it is reviewable: `assemble.py` strips reclassification comments, and there is no comment here to strip. If these should have been pulled, the beat still survives in the prose without them — `So I look.` … `My eyes only carry me so far.` … `And here is what Valphine's read comes back with` carries the scene cleanly.

## Verdict

No voice findings; the section is in spec throughout. The finding is a scope call the pass did not make — six lines of dice-roll table speech remain in the fiction, in the one scene of the session that emitted no reclassification hatch at all.
