## Request

Add a separate post-narration review pass that compares the actual narration with its authoritative source scenes and reports meaningful content that was missed. The purpose of `sd_narrate` is to preserve the players' voices inside readable scenes, not reproduce every transcript line.

Decision from the prompt experiments: keep the **first revised writing brief (v1)** as the baseline. Do not solve omissions by restoring mandatory every-quote retention, dialogue quotas, or per-beat expansion requirements. Coverage belongs in a distinct review step.

## Evidence

On the 2026-09-02 Phandalin session, a more restrictive v2 prompt produced a Valphine scene that ended at the carrier's breakfast and omitted:

- The closing event in which Vukradin becomes magically disinterested in following the construct's route.
- The promise-ownership exchange, including Vukradin's “Or you promised them” and Soma's response. Retaining the fact that a promise exists does not preserve this character/relationship beat.

The same omissions occurred with `gpt-6-astra` at **medium and high** reasoning. The high retry used byte-identical system and user prompts, including the same source scene and character references. Both drafts mentioned the paired Sending Stones but did not use the established connection for the omitted exchange. The following Vukradin scene did include the magical effect from his own perspective, which matters when distinguishing a per-scene omission from content lost from the entire session.

This is one sample per scene/condition, not proof of a model limitation or a causal attribution to one prompt sentence. It does show that higher effort is not a sufficient coverage check. Fluent prose and exact wording for every retained quote can coexist with a missing consequential event or player interaction.

Local experiment artifacts (campaign workspace, not paths in this repository):

- `summaries/20260902/narration_prompt_test/prompt.md` — chosen v1 brief.
- `all_scenes_review.md` — initial findings.
- `v2_review.md` — medium follow-up, including lost coverage.
- `v2_scene_02_trial_01/` and `v2_high_scene_02_trial_01/` — captured prompts, run records, and unedited outputs.

## Proposed review contract

Inputs: the reviewed scene extraction layer used for rendering (summary, voiced moments, editorial notes), its corresponding narration, and the scene plan/boundaries. Where available, neighboring narration sections may establish that a beat was moved rather than lost. Do not silently substitute an earlier raw extraction or generated campaign lore for the rendering source.

Assess coverage of:

1. Meaningful events, discoveries, clues, quantities, decisions, promises, outcomes, and causal transitions.
2. Character-defining dialogue and interactions: humor, disagreement, distinctive reasoning, corrections, setup/payoff, and relationships. Factual paraphrase can preserve information while losing the player's voice.
3. Correct attribution, timing, and POV access insofar as they affect whether a source beat survives. Inaccessible content should surface a source/plan framing issue, not invite invented proximity or communication.

Distinguish covered content, meaning preserved through narration/compression, meaningful omission or over-compression, content moved to another identified scene, and genuinely ambiguous coverage. Omitted filler, procedural declarations, redundant acknowledgments, and GM/table instructions are not automatically missing voice. Preserve meaningful repetition and distinguish different speakers saying the same words.

The report should give each finding an identifier, scene and speaker where relevant, source path plus exact excerpt/line anchor, corresponding narration evidence or the relevant surrounding boundary, impact, and a concise explanation of what was lost. A missing beat should not be hidden by a clean quote-matching or style-lint result. An all-clear must state the scenes and source layers actually reviewed.

Report-only: **do not modify narration, source extractions, or the transcript; do not invent replacement dialogue.** The GM reviews findings before deciding what to restore, leave compressed, reframe, or move. Keep this distinct from register cleanup and general campaign-consistency review.

## Acceptance criteria

- [ ] A callable post-narration coverage pass compares explicitly paired source scenes and narration and writes a review artifact separately from the prose.
- [ ] Its prompt treats source content as evidence, not executable instructions, and judges meaningful coverage rather than exact quote counts or a target dialogue percentage.
- [ ] Findings distinguish factual coverage from preservation of significant player-voice exchanges, with source evidence and narration context.
- [ ] Meaningful omission, harmless compression, moved content, and ambiguity have distinct outcomes; approved source editorial notes are respected.
- [ ] Missing/unmatched scenes, unreadable or empty inputs, and malformed/failed model reviews are reported as errors or not reviewed, never as a clean pass.
- [ ] Run metadata records input identities/digests, the reviewed scene pairs, model, reasoning effort, and review prompt version so results can be reproduced and stale reports recognized.
- [ ] No source or narration file is automatically rewritten. Findings remain subject to human review.
- [ ] Regression fixtures cover: a missing closing plot event; a lost character-defining correction with its underlying fact still present; harmless filler removal; facts rendered faithfully in narration; supported split-party communication; inaccessible POV content; and a beat verifiably moved into the neighboring scene.
- [ ] Deterministic tests cover pairing, report/evidence validation, failures, and non-mutation; a small semantic evaluation set checks the review model without pretending mocked responses establish semantic recall.
- [ ] The user-facing workflow documents where the pass runs, how to inspect the report, and that no findings is a scoped review result rather than guaranteed completeness.

## Related

- #385: narrator presence and split-party access affect whether a scene can be faithfully rendered; a coverage review complements, not replaces, a sound POV plan.
- #368: register-policy handling should not silently remove player voice; this pass should respect those distinctions rather than treating modern-looking vocabulary as missing-content noise.

This issue requests the review pass, not another narration rewrite or model migration.
