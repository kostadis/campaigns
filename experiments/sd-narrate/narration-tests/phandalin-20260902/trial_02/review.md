# Scene 4 experimental narration review

The experiment is a promising improvement in scene construction. Soma's practical, dry voice remains recognizable, and the setting, observed behavior, and payment reasoning receive substantially more connected narration. This is an assessment of one unedited draft, not approval to replace the production prompt.

Read the [experimental scene](session_doc_scene_04_denvar_s_room_and_unpaid_rent.md) or the [side-by-side comparison](comparison.html). The [writing brief](../prompt.md), [complete system prompt](system_prompt.md), and [source payload](user_prompt.md) make the test reproducible.

## What changed on the page

| Measure | Existing narration2 | Experiment |
|---|---:|---:|
| Total words | 1,336 | 1,805 |
| Words inside quotations | 849 | 747 |
| Words outside quotations | 487 | 1,058 |
| Percentage inside quotations | 63.5% | 41.4% |
| Quotation spans | 96 | 79 |

Counts exclude headings, frontmatter, and provenance comments and use the same word-token normalization for both files. They are descriptive, not a target or quality score. The useful change is that observations and actions now develop between the exchanges while much of the original dialogue remains.

The early meal, Denvar's belongings, and the up-front rent requirement now form a connected inference about his income. The landlord's persistent attention to Soma's shell gives her "That's not what I asked" a situation to react to. Later, his scrutiny of the party's equipment explains his nervousness. The unstamped chit and rent deadline give the decision to keep following Denvar a clear reason.

The sunlight repetition is retained and attributed with "she repeats." Several consecutive fragments from the same speaker share a paragraph. The scene still has a substantial landlord conversation; it has not been reduced to a few catchphrases and a summary.

## Voice and quotation fidelity

The shell correction, "It's so progressive," the refusal to educate the landlord, the shell-sprouts pretext, the privacy challenge, the serial-killer exchange, and Soma's sincere housing advice remain. "Oh shit, I want that gig" and the suspicious single-contract reaction also survive. The prose uses her practical concerns and dry responses rather than adding a new speech to demonstrate personality.

The [lexical quote review](quote_review.md) matches 78 of 79 output quotation spans to a complete line or contiguous excerpt in the voice-smoothed extraction, allowing punctuation and capitalization differences. The remaining span is:

> Yes, yes, we mean Denvar. He dropped something last night.

That is the exact wording of two consecutive Soma source lines, joined in their existing order (source lines 357 and 360). Manual review resolves it as supported. No invented quoted wording was found relative to the supplied smoothed source. This does not certify the raw VTT, every attribution, or every new prose claim. The delivery instruction is a quotation of a document, not an invented spoken line.

Vukradin's table interjections do not appear, including his drugs warning and comments about the landlord's racism. They were absent from the existing narration2 Scene 4 as well. The experiment avoids placing him physically with the followers while he is in the sewers, but it therefore does not solve how to retain all of that player's table contributions. The source line labels alone do not establish that those remarks were heard through the Sending Stones. If those jokes must survive in fiction, their delivery still needs a supported framing decision.

## Remaining review findings

1. **A suggested time becomes an event.** At output line 45, "We wait until morning. By seven..." treats the source's "You can wait till the morning, like 7am" (source line 140) as a confirmed decision. The extraction's summary does not establish that time. Remove the definite seven-o'clock timing in a reviewed revision unless the GM confirms it. The raw test is left unchanged.
2. **Some transcript-shaped material remains.** The cabin line retains "oh god, where did we start?" and the chit passage retains "Third up" followed by the correction. The new freedom removed several acknowledgments and search questions, but did not fully resolve every procedural fragment. Whether these carry useful player rhythm is a reading decision.
3. **Modern-reference cleanup is still downstream.** "Denvar, Colorado" and "Just asking questions guy has entered the chat" remain. The KYC joke also remains for a register decision; imported economics is already campaign canon, so it should not be deleted merely for being modern vocabulary. No replacement joke was invented. The source's Jesse Jackson joke was omitted, as it was in narration2.
4. **Some reasoning repeats.** The draft explains the meaning of the unpaid chit, then restates the observed delivery and the need to collect payment. This is much easier to follow than the original fragments, but could be tightened after judging the voice. There is also room to compress the repeated observation that the landlord has not yet answered the rent question.

## Event coverage and checks

The scene retains the early solitary breakfast, Bluelake lodging, rat search, lack of obvious insignia, apparent overpayment, landlord's ancestry questions and alarm, discounted-room offer, Denvar's name, lost-pouch pretext, seven-to-ten-day run of records, client reference and house mark without a personal name, nine/third-hour/eight-up/one-down instruction, weekly settlement, unpaid newest chit, rent due that day, quiet-tenant account, decision to wait and follow, and sincere Tortle housing advice. The definite count of seven chits is supported by the later spoken source; it is not an invented number. The draft stops before the next scene's dead drop.

The existing `voice_lint` ran without its standard findings. It reported that this installed version ignores the campaign's `extra_tics` key, so those four additional configured expressions were checked separately against the unquoted prose: all had zero matches. These are narrow style checks, not a substitute for the voice reading above or a full consistency pass.

The run used `gpt-6-astra`, medium reasoning, through the existing text-only Codex backend. The runtime log confirms the explicit model selection. Recorded source hashes were unchanged when the run finished. The original narrations, source documents, shared voice files, campaign configuration, and CampaignGenerator checkout were not modified by this experiment.

Comparison limit: narration2 was a five-scene bundle. This was a single-scene render against the currently installed checkout. The trial supports assessing the revised writing contract, but does not isolate one instruction or establish a general model-quality conclusion.
