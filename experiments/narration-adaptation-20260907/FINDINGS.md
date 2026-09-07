# Finding: keep the simple adaptation brief as the starting point

Recorded 2026-09-07. Design/evidence tracking:
[CampaignGenerator #408](https://github.com/kostadis/CampaignGenerator/issues/408).

## The goal clarified in the discussion

The narrative began with a larger responsibility for preserving the campaign's
record. Better session summaries and consistency work have reduced that burden.
The user now wants campaign fan fiction: fun to read, appropriate to the game,
faithful to what happened, and recognizable as these players and characters.

Events, material facts, decisions, promises, outcomes, and knowledge boundaries
remain constrained by the record. Dialogue can be reconstructed into readable
exchanges. Interior thoughts can be invented within character and circumstance;
they do not automatically become canonical motives or history.

Provenance can connect multiple authorities—the VTT, reviewed summary,
corrections, and reviewed extractions. This does not require inventing another
single authoritative document. For these tests, the existing smoothed
extractions already provided the factual preparation.

The user also explained the historical pressure toward quotes: early summaries
were dry and lost the players' dialogue. Preserving the quotes restored life,
but that protection eventually became too strong for the desired adaptation.

## What was tested

| Experiment | Question | Observed result | Limit |
|---|---|---|---|
| [Five-scene adaptation](experiments/20260907-phandalin-adaptation/README.md) | Can the existing reviewed smoothed layer support freer narration? | Major events checked survived and obvious transcript debris disappeared. Fragmentation remained; a comic promise-ownership qualification was lost. | One generated chapter versus an edited historical chapter; multiple prompt/reference changes; historical model not attested. |
| [Single-scene A/B](experiments/20260907-phandalin-scene-composition/README.md) | Does replacing general composition guidance with a scene-specific assignment improve the result? | The user preferred **B**, the general brief. Both drafts preserved the consequential facts checked. The paragraph rhythms were similar. | One stochastic pair; the added block combined planning and a specific scene interpretation. |

The comparison's B is the first experiment's general adaptation contract with a
single-scene output wrapper. It is **not** the unchanged production pipeline, nor
automatically equivalent to earlier archived prompts called v1.

Exact candidate baseline:
[B/control system prompt](experiments/20260907-phandalin-scene-composition/control/system_prompt.md).
It works with the [shared source/reference message](experiments/20260907-phandalin-scene-composition/user_prompt.md),
including cleaned character descriptions and the synthesized campaign style.
Do not attribute the entire result to the system prompt alone.

## The user's preference is the decisive new evidence

The user said “i like b more,” then identified this passage in A as an irritating
narrative structure:

> Nothing has happened to him. I have found a symbol, not a knife at his back.
> I make myself keep that distinction too.

They clarified:

- “my prose is straightforward and simple.”
- Habitual narration of “oh i thought x, and then corrected it” annoys them.
- These are adventurers—“creatures of action.”
- The original/general adaptation prompt was a good starting point.

The positive target is direct, characterful adventure prose: what the characters
notice, say, decide, and do. The criticism is not a new blanket prohibition on
uncertainty, contrast, private thoughts, or genuine changes of mind in the game.
The adjacent simple wish to have Brewbarry close enough to hear already conveys
Soma's concern without the elaborate self-correction.

The assistant's initial, slight preference for A's ending is preserved in the
[pre-reveal reading notes](experiments/20260907-phandalin-scene-composition/blind_review.md).
It is separate from the user's preference. The fuller
[review](experiments/20260907-phandalin-scene-composition/review.md) records both.
The treatment's instruction not to invent immediate danger may have contributed
to the disliked passage; this remains a hypothesis, not a causal finding.

## What this does and does not justify

Use B and the first general adaptation brief as a candidate baseline for future
work. This trial does not support adding the tested scene-specific guidance as
a mandatory production stage. It also does not support another paragraph quota,
automatic ban, or model migration. More explicit reflection did not establish
better writing for the intended reader.

Keep factual review distinguishable from literary judgment. Missing consequential
events and lost interactions still matter; exact quote counts and successful
lint checks cannot substitute for reading the scene. The prompt's factual limits
should not require the character to narrate those limits as self-correction.

The [pipeline audit](docs/design/NarrationPipelineAudit.md) separately records
historical design drift, competing instructions, downstream uses of narration,
and specific implementation defects at the inspected snapshot. In particular,
the earlier successful experiment removed editing wrappers from voice references
and changed genre guidance. Production's use of whole voice files meant that
installing the brief alone did not reproduce those conditions.

Implementation remains a user decision. Revalidate the relevant current code and
effective prompt before changing it; these archived results are not a fresh
assessment of every later fix. No draft is promoted by saving this preference.

## Design and test references

- [SkillPipelineOrder](https://github.com/kostadis/CampaignGenerator/blob/d9c5de87a0ec4831c1cdc999b26491851b1f7c01/docs/design/SkillPipelineOrder.md): post-recording skill flow and stage boundaries. This is the filename found for the design described in conversation as SkillFlow.
- [TheFlow](https://github.com/kostadis/CampaignGenerator/blob/d9c5de87a0ec4831c1cdc999b26491851b1f7c01/docs/design/TheFlow.md): the larger loop, including narration's historical grounding role.
- [VoiceCriticAlignment proposal](https://github.com/kostadis/CampaignGenerator/blob/d9c5de87a0ec4831c1cdc999b26491851b1f7c01/docs/design/VoiceCriticAlignment_proposal.md): duplicated rules and review/input alignment.
- [Earlier narration/dialogue experiments](https://github.com/kostadis/campaigns/tree/0355cdd28179650cf11ecb4435e4841fbe61d54c/experiments/sd-narrate): predecessor evidence, distinct from these trials.
- [CG #386](https://github.com/kostadis/CampaignGenerator/issues/386): meaningful event and interaction coverage.
- [CG #397](https://github.com/kostadis/CampaignGenerator/issues/397): conflicting quote contracts; this preference informs which contract is wanted.
- [CG #395](https://github.com/kostadis/CampaignGenerator/issues/395): already-fixed tense-policy conflict, not the cause of the rejected structure.
- [CG #366](https://github.com/kostadis/CampaignGenerator/issues/366): preserving narration iteration evidence.

The archive contains three actual generation calls: one chapter and two
independent single-scene drafts, all attested Astra/medium. There were no rerolls
or post-generation prose edits. File hashes and the portable verifier make the
archived evidence inspectable without calling a model.
