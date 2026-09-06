# Same prompt, four more scenes

My reading: the improvement extends beyond Soma. Both Vukradin scenes retain his sincerity and commercial ambition without making him a cynical salesman. Valphine's interpretation of events feels distinct from his. Brewbarry also gains a physical scene to inhabit, although his draft has the clearest unsupported staging. These are promising raw drafts, not publication-approved replacements.

Read the [side-by-side gallery](index.html) or the [complete experimental session](all_scenes.md). The accepted Soma result is included unchanged. The four new scenes use the same [writing brief](prompt.md), gpt-6-astra, and medium reasoning. No prompt tuning or hand-editing occurred between these four renders.

## Vukradin — scenes 1 and 3

In [Scene 1](scene_01_trial_01/session_doc_scene_01_patrons_of_the_common_chord.md), the studio is something he genuinely wants to build for people. A patron declining to contribute produces this interior response:

> He has given to charity. Good. The fact that it is not my charity does not undo that, and I am not going to make a person regret recognizing me because he has already helped somebody else.

That develops his actual “I'm not here to pressure anybody” instead of replacing it. His charitable purpose, donor credits, ticket prices, and promised money fit together. The donor names and the twenty gold actually collected remain distinct from Petra's pending five hundred. The refund guarantee and Old Hesp's criticism survive, with enough setting to explain why the old room matters.

There is still room to tighten the astronomy discussion. A few observations about the Chord trading on his name are more polished and sardonic than his best passages; I would watch that tendency, but it does not dominate his response to the patrons.

[Scene 3](scene_03_trial_01/session_doc_scene_03_lost_among_unexpected_fans.md) is the strongest Vukradin test. Rsolk's suspicion, recognition, enthusiasm, and offer of an escort become a continuous encounter. Vukradin is pleased to meet fans, not smug about manipulating them. His long reasoning about helping people and earning studio money lands in his actual offer of assistance. His promise about tickets stays limited to asking.

“Because I'm not over there” is restored as spoken dialogue; the extraction explicitly identifies it as his line. The draft also preserves the distinction between remembering his mission and losing interest in the route. It does not invent a specific location for the earlier strange-spider encounter.

## Valphine — scene 2

[Scene 2](scene_02_trial_01/session_doc_scene_02_the_ninth_crate_disappears.md) gives her something characteristic to do with description: distinguish evidence from conclusions about power. Watching the carriers, she thinks:

> One man completes a physical task. The other checks for its continuation.

> I cannot establish rank from a glance. I can identify which man expects something to emerge from the sewer.

Later she reads Vukradin's correction about who promised Lim as an exact allocation of obligation. That is a useful contrast with his sincere self-narration. She is controlled, skeptical, and attentive to leverage without importing an unrelated theological speech to signal her identity. The construct, wet approach, separate surveillance assignments, and uninformative breakfast now receive connected description.

The two consecutive “Yes” replies remain, but one is explicitly Vukradin and one Soma. They read as two people agreeing, not accidental duplication. The late charm/confusion guesses belong to Vukradin; the surrounding Sending Stone narration makes that reasonably clear, although one additional attribution would help.

Some procedural residue survives: Vukradin still refers to himself in the third person while announcing his plan. The narrative also over-specifies the construct's behavior with “no examination,” “no search,” and “no hesitation.” Those negative observations are not established as such in the source; they should not become additional evidence of its instructions. Near the end, “He remembers where he is” is stronger than the source's “remember where you were.” Preserve remembered route/purpose without asserting reliable present navigation, especially across the transition into Scene 3.

## Brewbarry — scene 5

[Scene 5](scene_05_trial_01/session_doc_scene_05_behind_the_thousand_faces.md) has short, bodily observations and an uncomplicated attachment to Vukradin's music: “Kill spiders. Get his studio built.” The couches, mirrors, old clothes, and properly drawing fire now matter to a man who previously could not afford the tavern. The rat's findings arrive as information, not as Brewbarry personally seeing through it. The Harper identification remains distinct from proving who commissioned the ninth crate.

The main fidelity problem is at line 111: “His voice reaches me through the entrance. I stay close enough to hear.” The source places Brewbarry inside and the others outside investigating the compartment, but does not establish that the entrance is within earshot of that conversation. The draft invents a convenient listening position to retain the dialogue. That needs a supported reporting frame or a different staging decision before publication.

The repeated “on the wall” replies are attributed to Vukradin and Soma. “Payday! I'm going to the casino!” is correctly Soma's joke, not invented speech for Denvar. Less successfully, literal present-tense enforcement creates “When I first come to Neverwinter” and “I once cannot afford”; those memories should use ordinary past tense. Watching the mannequins' hands is a plausible bodily reaction, but its repeated prominence is a new characterization choice worth judging rather than mistaking for a played event.

## What the measurements do—and do not—show

| Scene / narrator | Original words | Test words | Original quoted % | Test quoted % |
|---|---:|---:|---:|---:|
| 1 / Vukradin | 1,655 | 2,315 | 45.8 | 30.5 |
| 2 / Valphine | 1,106 | 1,792 | 47.1 | 28.1 |
| 3 / Vukradin | 1,092 | 1,669 | 51.2 | 35.2 |
| 4 / Soma, earlier test | 1,336 | 1,805 | 63.5 | 41.4 |
| 5 / Brewbarry | 1,377 | 1,734 | 61.7 | 33.3 |

These are descriptive counts, not a dialogue quota. Scene 3 actually contains more quoted words than its baseline, yet reads more like a scene. The experiment's benefit is not simply deleting dialogue.

The lexical diagnostics matched 74/79 quotation spans in Scene 1, 59/59 in Scene 2, 68/72 in Scene 3, and 67/68 in Scene 5. All ten flagged spans are supported joins of existing lines by the same speaker, in source order: five Vukradin joins in Scene 1, four in Scene 3, and Soma's “Let's do both! Porque no los dos” in Scene 5. Some Scene 1 joins cross incidental interjections; they are not all adjacent source lines. No invented quoted wording was found against the supplied smoothed extractions. This is not certification of the raw VTT, every attribution, or the newly written interior prose.

Modern references still await the usual register pass: Patreon, Japan, Albuquerque, walkie-talkies, the doctor's-office analogy, and the American Way remain among them. Preserved economic vocabulary and player jokes should be adjudicated by the campaign's scrub policy, not automatically deleted. Soma's earlier seven-o'clock timing problem and absent-player-contribution caveat remain documented in the [Scene 4 review](trial_02/review.md).

The standard style linter flags one Scene 1 expression: “with the prospect of a program that will have both music and the names of people who.” On manual inspection this is a regex false positive, not a class-of-person portrait. Other new scenes have no standard findings. The installed linter ignores `extra_tics` and expects `##` rather than the outputs' `###` headings, so the four extra expressions and first-person filing were checked separately against unquoted prose; all were absent. An in-memory heading adaptation also allowed the normal section checks to run. These narrow checks do not establish voice quality.

## Scope and conclusion

All four new run records report unchanged input hashes, also verified after rendering. The shared writing brief is unchanged from the accepted Soma test. The generalized runner reproduces Soma's captured system and user prompts byte-for-byte. The old Soma metadata understandably records an earlier runner hash; that runner was generalized for this follow-up, not used to regenerate Soma. Production narration, source documents, character files, campaign configuration, and CampaignGenerator implementation were left untouched.

The baseline was a five-scene bundle; these are individual renders through the current checkout. This supports a qualitative judgment of the writing contract, not a controlled claim about one instruction or all future sessions. Valphine has only one narration scene here, so this tests her investigative voice, not her full theological or emotional range.

I would keep this prompt direction. The remaining weaknesses call for focused staging, source-fidelity, tense, and register review—not reinstating blanket dialogue-retention or expansion requirements. Most importantly, the players' words now have situations and perspectives around them, and those perspectives are recognizably different.
