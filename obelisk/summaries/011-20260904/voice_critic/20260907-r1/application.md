# Approved voice-critic application

Continuity follow-up (2026-09-07): GM approved the exact suggested scene 04 fix. Live narration now reads `The remaining bugbears understand. They get out of her way.` This replaces the premature departure into the ravine; departures remain in scene 05. vc-s04-ref01 resolved in narration. SHA-256: 9d9002c4322f6c0977a7ae35edc850c3ceab3bb080e582bd1bd669303ad57e99. Scene 04 prose 431 → 424 words; total 529 → 522; share 81.5% → 81.2%. Dialogue and dash counts unchanged. Scene lint: exit 0, zero errors/warnings, bookkeeping skipped without genre. The adjacent scene transition was reread; no other text changed. Scene 07 GM reminder is the sole remaining referral. No assembly performed.

Referral follow-up (2026-09-07): GM explicitly directed deletion of scene 05's `“That was Pip,” she tells me.` Removed only that paragraph from live narration; retained Zenvon's self-correction. vc-s05-ref01 is resolved. Result SHA-256: f385877ab3dd823ee22b431f5329cd0113422d5fa508af027f875296671a1daf. Scene 05 lint: exit 0; zero errors/warnings; bookkeeping still skipped without genre. Three speech words and three prose words removed (scene 05: 390 prose / 658 total, 59.3%); no new text or boundary changes. GM confirmed scene 07 reminder's source, without explicitly directing its deletion. Scene 07 and scenes 04–05 continuity referrals remain pending. Earlier statuses below are historical.

Promotion update (2026-09-07): explicitly authorized by “promote.” The approved revision is now in narration/session_doc_scene_07_dinner_with_the_red_wizard.md. Verified byte-identical to the approved revision (SHA-256 2e39214c187fa37d49155b885411515f3f476bd0cd3b2c82c52659d9971bc9f3); the other six scenes are unchanged. Three referrals remain pending. No assembly or publication. The application-stage account below is retained as history; its not-promoted statements are superseded by this update.

Review: `voice-critic:011-20260904:all-scenes-r1`. Returned decisions saved in decisions.json; 4 approved, 0 rejected/discussed/unmarked.

Applied **vc-s07-01** exactly to [derived scene 07](applied/approved-r1/session_doc_scene_07_dinner_with_the_red_wizard.md:73): `“Yes.”` → `“Yes,” I say.` Source and reference hashes validated before writing; full diff retained in applied/approved-r1/approved.diff. Original narration and all frozen dialogue-edit records remain unchanged. No promotion, production assembly or publication.

## Validation

All seven original narration hashes remain unchanged. The derived file differs by only the approved attribution and dependent punctuation. Changed paragraph and adjacent exchange read: Zenvon answers for Veyra, then Hamun resumes; no invented action or orphaned reply. Scene boundaries are unchanged. The tag `“Yes,” I say.` occurs 1 time before and 2 times after across the selection; the existing instance introduces the sword answer, so the short attribution's reuse is functional, not a new stylistic defect.

Scene 07 prose 511 → 513 words; total 1084 → 1086; prose share 47.1% → 47.2%. All other scene counts unchanged. Speech stays 573 words; dashes remain 11 document-wide (3 outside speech); trailing dialogue dashes remain 0. Cross-narrator convergence remains inapplicable (one narrator). Re-run lint: exit 1, one ERROR for the same two portrait constructions, zero warnings, one bookkeeping-skipped note. No new checker finding. This is diagnostic under the checker default, not an established current campaign ban. Genre budgets remain not checked: no rulebook configured.

## Approved referrals — recorded, not repaired

- **vc-s05-ref01**: GM correction presented as Maela dialogue; source/scrub follow-up pending.
- **vc-s07-ref01**: GM apprentice reminder presented as Hamun dialogue; source/scrub follow-up pending.
- **vc-s04-ref01**: remaining bugbears leave twice across scenes 04–05; continuity follow-up pending.

Referral approval authorized recording follow-up only, not a guessed replacement. Their original evidence remains in the review manifest and reports. The style edit is resolved in the derived revision; the three underlying issues are not resolved. The original critique reports describe the pre-application baseline; this application record supersedes their open-status/count statements for vc-s07-01 only.
