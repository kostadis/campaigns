# Prompt v2 results — Vukradin and Valphine

The result is mixed. The targeted changes help Vukradin's Common Chord scene and remove specific problems from Valphine's narration, but Valphine also loses important dialogue and the scene's closing event. I would not replace v1 wholesale with this candidate.

[Read the three new scenes](v2_scenes.md), [compare v1 and v2 side by side](v2_comparison.html), or inspect the [tested brief](prompt_v2.md) and [pre-run proposal](v2_proposal.md). Each scene received one gpt-6-astra medium generation. The outputs and tested prompt have not been revised after seeing the results.

## Vukradin, Scene 1: a useful improvement, with tradeoffs

The astronomy discussion is substantially better edited. The moon question, Selûne, tides, Soma's underwater advantage, and the practical time window remain; intermediate arithmetic corrections become a short account of his reasoning. This is the intended distinction between preserving a player's contribution and replaying every transcription fragment.

Vukradin remains sincere about building the studio. His refusal to pressure the patron, insistence on donor recognition, openness to Wick's music-school interpretation, refund guarantee, and response to Old Hesp all survive. This new interior passage develops his actual outlook:

> His donation is not an entrance fee to being a fan. If his giving is finished, it is finished, and we can still have a perfectly good conversation about music.

The narration is less dependent on sardonic comments about his name doing better business without him. Remembered events now use natural past tense. The critical amounts and obligations remain: twenty gold collected, Petra's five hundred pending, one-year donor credits, and performance two days later.

It is not uniformly tighter. The closing reflections about affordability repeat a point already established, and the “room beneath the city” closing flourish still sounds writerly. Valphine's “huge in Japan” contribution disappears, although the Brewbarry-size joke remains. That is a voice-selection tradeoff, not a necessary correction established by the review.

## Valphine, Scene 2: specific fixes, significant regression

The third-person announcement “Vukradin is gonna stick around” becomes his intended action in narration. “Vukradin will pursue stealthily” similarly becomes movement. The construct no longer supplies the three invented negative observations about examining boxes, searching for a mark, and hesitating. Her distinction between rank and useful knowledge remains recognizably hers; the scene still contains the wet approach, separate ninth crate, carriers' conspicuous separation, construct, split pursuit, and solitary breakfast.

However, it stops at breakfast. The entire closing exchange about the magical disinterest is missing. The text establishes the Sending Stones as a means of communication, but does not use that connection for the later dialogue. It also drops Vukradin's “Or you promised them,” Soma's “Thank you so much,” and Valphine's “Good times.” V1's distinctive interpretation of who owns the promise is gone with the exchange. The promise itself survives as a fact, but that does not preserve the players' interaction.

This is not successful correction of the overstatement “He remembers where he is”: the draft avoids that sentence by omitting the event. Scene 3 still renders the disinterest in Vukradin's own perspective, so the event is not lost across these three files, but the planned Scene 2 coverage and its shared conversation are reduced.

My inference is that the stricter information-access instruction overcorrected, alongside the stronger compression guidance. One sample with several prompt edits cannot establish which instruction caused which omission. The observable result is enough to reject this as an unqualified improvement. The user's goal is preserving player voice, not achieving the lowest quotation percentage.

There is still some table-shaped wording at the opening (“very high stealth”). The cleanup is selective, not complete. Modern references that remain still need the normal register review.

## Vukradin, Scene 3: still strong, not a decisive win over v1

“Because I'm not over there,” the wrong-turn joke, Rsolk's recognition, autograph exchange, safety compliment, mine connection, paid-work offer, and limited promise to ask for tickets all remain. Vukradin is pleased by fans and looks for honest work; he does not congratulate himself on manipulating Rsolk. The distinction between remembering the mission and losing interest in the route is intact. He does not identify the spiders beyond the reported resemblance or fabricate an earlier encounter location.

The dialogue is grouped more naturally in places, but v1 already handled this encounter well. V2 is slightly longer, with a little more explanation of sentiments the action conveys. Its opening adds “By the time I want to ask someone about it, my friends are no longer beside me,” which misleadingly suggests they accompanied him until his wandering. Scene 2 establishes that he pursued alone. That transition needs correction in any reviewed draft.

## Checks and limits

| Scene / narrator | v1 total words | v2 total words | v1 quoted words | v2 quoted words |
|---|---:|---:|---:|---:|
| 1 / Vukradin | 2,315 | 2,235 | 707 | 590 |
| 2 / Valphine | 1,792 | 1,330 | 503 | 282 |
| 3 / Vukradin | 1,669 | 1,712 | 588 | 566 |

Counts use the same normalization as the earlier review. In Valphine's case, the reduction includes meaningful loss; these are not quality scores.

Lexical matching found 68/68 source-supported quotation spans in Scene 1 and 28/28 in Scene 2. Scene 3 matched 56/62 directly. The six flagged spans all join source lines from the same speaker in their existing order: three lost/directions fragments, the safety compliment, Rsolk's agreement and explanation, and his survivor description. Some joins cross omitted incidental interjections. No invented quoted wording was found against the supplied smoothed extractions. This does not certify every attribution or new narrative claim.

The normal style checks, with an in-memory heading adaptation, found no standard errors or warnings in unquoted prose. The four campaign-specific extra patterns and first-person filing were checked separately and had no matches. These narrow checks cannot detect the lost scene ending or judge voice quality.

All three source payloads are byte-identical to the preceding experiment. Character specifications and examples are unchanged. System-prompt differences are restricted to the new brief and one genre-reference tense paragraph. The brief grew from 575 to 761 whitespace-delimited words; assembled system prompts grew by 148 words because the tense paragraph was also shortened. Model and effort are explicitly recorded as gpt-6-astra and medium in each run. Input hashes remained unchanged through rendering and verification.

No production narration, campaign source, shared voice/genre file, or CampaignGenerator implementation was edited. This is one generation per scene, not a statistical comparison. Brewbarry's doorway staging, Soma's timing, and Valphine's broader theological range were not retested.

## Recommendation after the test

Keep the natural-tense clarification and the distinctions between action declarations, observations, and inferences. Keep permission to compress intermediate clarification. Do not adopt the v2 access paragraph unchanged, and do not treat a plot-bearing or character-defining exchange as disposable merely because its physical framing is underspecified.

For a future candidate, I would narrow that paragraph's communication rule to:

> When the source establishes a shared communication link for a split party, interpret subsequent exchanges in that scene in light of that link; it need not be reannounced before every line. Distinguish what the narrator witnesses from what is communicated. Do not invent a new channel, convenient proximity, or an unsupported debrief. Preserve consequential exchanges supported by the established connection; missing line-by-line transmission directions alone are not a reason to omit them.

That wording is a post-test proposal, not part of the prompt that produced these drafts, and it has not been tested. If a scene truly requires inaccessible events, its POV plan or source framing needs an explicit decision rather than either fabricated access or silent loss. I have not run another generation or promoted any version to production.
