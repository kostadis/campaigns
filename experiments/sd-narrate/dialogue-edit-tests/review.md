# Three editing approaches — review

[Selected passages](passages.md) · [Compare all complete drafts](index.html)

## Finding

The broader permissions did not produce a wholesale voice rewrite in these nine tests. All three approaches made modest edits. The most useful distinction was where they spent their attention: B improved dialogue more consistently; C improved surrounding prose and tense, but sometimes left obvious dialogue roughness intact.

**I would start with B as the dedicated dialogue-editing pass.** It kept the inner narration unchanged in all three cases while making useful, source-supported edits to speech. For an overall finished passage, C produced attractive results for Valphine and Zenvon. There is no single clean winner across the three voices, and the combined A→B→C pipeline has not been tested or recommended.

This is one response per approach per scene, reviewed by the same assistant that designed the prompts. It is a small qualitative experiment, not a blinded or repeated reliability evaluation, and it does not establish that a model generation is categorically safe to rewrite dialogue.

## Design

Nine independent calls: three approaches applied to each existing v1 draft. Every call used **gpt-6-astra, medium reasoning**, through the existing CampaignGenerator Codex CLI adapter. The user payload was the same within each narrator's A/B/C set; only the editing instruction changed. No arm consumed another arm's output.

Inputs: the complete existing draft, complete source extraction, and character references. The Phandalin cases received the character-perspective sections for all four PCs used in the earlier experiment; the Obelisk case received Zenvon's full voice notes, the confirmed supporting notes including Veyra and Pip, and its local register policy. No new narrator examples or plot context were added. The separate editing brief explicitly superseded verbatim-copy restrictions for the permitted edits, while retaining distinctive diction and source grounding.

| Approach | Permission | Observed result |
|---|---|---|
| A — light copyedit | Edit inside existing quotes; preserve surrounding prose | Kept voice and stayed within scope, but left substantial transcript awkwardness. |
| B — contextual dialogue edit | Reshape dialogue using context; minimal adjacent attribution changes permitted | Best dialogue improvements; in practice, all three responses left surrounding narration unchanged. Some cadence edits deserve scrutiny. |
| C — integrated line edit | Edit dialogue and inner/descriptive prose together | Useful tense and flow repairs without flattening the inner voice; less consistent at cleaning the dialogue itself. |

## Zenvon: C narrowly preferred as a whole scene

All three fix the interrupted “What do you… guys want to do?” and the duplicate “I can… can,” while keeping “yeah, yeah,” “I guess you're right,” and his formal phrasing. None replaces him with a generic fantasy rogue.

C also changes “he has told me” / “I have weighed his warning aloud” into ordinary retrospective tense. It trims a few redundant narrative clauses but keeps his assessments, the unknown enemy count, the distance problem, and the distinction between intending Pip's movement and completing it.

B makes one edit I would reject or ask the player about:

> Original / A / C: “I feel using the mage hand is more effort. For the same output.”
>
> B: “I feel using the mage hand is more effort for the same output.”

The words and meaning survive, but the separate landing is part of the performance. B also changes “At the ravine?” into a statement; the self-correction remains, but the confirmatory quality is weakened. Permission to smooth still requires attention to prosody and conversational intent.

All arms leave the inherited pike/bike problem untouched: the earlier narrator converted the spoken misunderstanding into an internal thought. These are not successful repairs of that interaction, and the experiment deliberately excluded missing-beat reconstruction.

## Vukradin: B clearly preferred for dialogue

B turns Valphine's unfinished “What… What do I?” into “What… what am I expected to know?” The extraction explicitly labels her question as asking what she is expected to know, so this is a context-supported completion rather than a new question.

B also reduces the repeated tide calculation to:

> “High to low is three hours. Yeah, no, high to low… High to low is six hours. Six.”

It preserves the wrong first answer, correction, and emphatic settling on six. A leaves two consecutive full “High to low is 6 hours” sentences inside one quote; C leaves the original longer repetition untouched. B is genuinely more readable here.

The inner prose remains intact, including his pleasure in the studio, refusal to pressure a donor, and the long reflection that he cannot ask Old Hesp for an opinion and then reject it because he wanted a compliment. The repeated “We're gonna get it back” also survives. This is not readability purchased by stripping out the sincere bard.

C's prose trims are mostly reasonable, but it leaves “But, oh, but,” the incomplete Valphine question, and the repeated calculation. Broader editing permission did not automatically produce better dialogue editing.

## Valphine: C narrowly preferred as a whole scene

C keeps her long analytical sentences, reading of the carriers' deliberate separation, uncertainty about rank, and private interpretation of Vukradin. It corrects “the one he raises himself a short while ago” to “raised,” and similarly fixes the past actions at the end.

The promise exchange becomes one connected paragraph: Vukradin's reminder, his narrowing of whose promise it was, and “Or you promised them.” Her following observation about imposing a promise while accounting for whose neck it rests upon remains untouched. The dialogue, relationship beat, and inner voice coexist.

B does some useful local cleanup but otherwise mainly changes number formatting. Its removal of “over. Yeah” from the walkie-talkie line merits a human look: “over” could be a dangling fragment or radio-play texture. The edit is plausible, not demonstrably necessary. Both B and C leave several rough planning fragments, so neither is a finished universal solution.

Crucially, all arms retain the end-of-scene magical-disinterest exchange, the Sending Stone connection, uncertainty about the spell, and the distinction between remembering the purpose and losing the willingness to pursue that tunnel. None repeats the omission seen in the earlier v2 narration experiment.

## What the checks do and do not establish

| Narrator | Baseline words | A | B | C |
|---|---:|---:|---:|---:|
| Zenvon | 977 | 974 | 973 | 943 |
| Vukradin | 2311 | 2305 | 2304 | 2276 |
| Valphine | 1789 | 1787 | 1787 | 1780 |

These are whitespace word counts, including the narrator heading. They are not quality scores: spelling out a number can increase the count while otherwise tightening a sentence.

- All nine calls completed with the requested model and effort, recorded in each `run.json`.
- All hashed inputs remain unchanged. Raw responses are preserved exactly, with hashes and unified diffs; no human edits were applied.
- A stayed inside existing quoted spans for all three cases. A and B's outside-dialogue comparison is identical after replacing quoted spans and ignoring outer whitespace; this is not a claim of raw-byte equality including the final newline.
- The consecutive-quote detector flags the two “Yes” replies in Valphine, but those are attributed to different speakers agreeing to the plan. Conversely it misses repeated sentences *within* Vukradin's quoted calculation. This is why the mechanical check is not the editorial judgment.
- Reviewing the full diffs against the baseline and affected source passages found no newly introduced events or removed load-bearing narrative beats. This is a manual finding, not an automated semantic guarantee. Existing source-to-draft issues remain separate.
- The experiment runner's five tests pass: accepted-prompt hash, frontmatter handling, refusal to overwrite different snapshots, no model calls/source mutation during preparation, and failure rather than success for a mismatched backend identity.

## Next decision

The test supports allowing contextual dialogue editing while retaining explicit source and voice constraints. B is the cleanest starting point for that separate pass; C is a useful optional scene-level edit, especially where the prose has tense or attribution friction. Keep before/after review, preserve the source archive, and judge cadence as part of fidelity—not merely words and facts.

Do not stack extra passes automatically. First let the GM read these passages and choose the degree of editorial latitude. No production prompt, pipeline stage, campaign source, or voice file has been changed by this experiment.
