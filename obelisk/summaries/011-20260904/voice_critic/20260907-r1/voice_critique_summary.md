# Chapter 11 voice critique

Latest status: approved scene 07 tag promoted to narration on 2026-09-07 at the GM's request. Three referrals remain pending; no assembly. See application.md and manifest.json for promotion verification. Earlier baseline/application status below is historical.

Update: all four decisions approved. The speaker tag is applied in a separate derived revision; three referrals are recorded for follow-up, not repaired. [Application results and corrected counts](application.md). The original review below is retained as the pre-application baseline. Narration has not been promoted.

Review ID: `voice-critic:011-20260904:all-scenes-r1`. Input shape: seven promoted per-scene narration files. Open: one supported attribution edit, three separate source/continuity referrals. No files of narration changed.

## Inputs and coverage

All seven effective scenes read; scene 01 uses the scrubbed copy. Six promoted revisions match their approved application hashes; scene 02 matches its frozen original. Narration/source mapping comes from dialogue_edit.sources.yaml and the successful bundle record, not filename guesses. Input and reference SHA-256 digests, line/character sizes, exact spans and analysis line mapping are in manifest.json and analysis_line_map.json.

Declared voices: Zenvon Forepot, Veyra of the Blue Candle, Sister Maela Dawnforge, Pip Thistlewick. Only Zenvon narrates. Declared Zenvon examples and shared house_style.md used; no orphan voice/example files found. Roster, player identities, party prose and register policy reviewed. Stage directions—not the GM player label—identify speakers. Older example incidents and party prose are not current event evidence.

Genre is **unset**, not a missing expected file: all seven knobs and current paths.genre_file are null; no voice/_genre.md exists. No historical prompt pair or reference digests retained in the identified run records: historical delivery/version comparison is unavailable. Current generator voice/examples resolvers, base.md and writing_brief.md guide the present critique, not proof of historical instructions. Current base.md contains no HARD BANS. No genre quotas were invented. Reference sizes/digests are in the manifest; no genre digest exists.

Mechanical lint ran on one analysis-only concatenation of the seven exact scene bodies with mapped synthetic headings; no assembly or publication was performed. It scans dialogue too, unlike the prose-share count. Its hardcoded portable defaults are diagnostics, not established current campaign bans. Bookkeeping is explicitly skipped without a genre file. See lint.stdout.txt and lint.stderr.txt for separate errors/warnings/notes and manifest.json for the exact invocation.

Reading covered generic prose, clichés, voice/register, within-narrator repetition, attribution, em-dash context and adjacent scene joins. Pricing language is licensed by the Zenvon spec and examples (notably “I priced him correctly”); no blanket accounting-language fix is proposed. Brief unornamented emotion and short action sentences are not defects. No broader voice drift confirmed. Full event coverage, canon consistency and tape fidelity are not certified.

## Locked dialogue and reclassified speech

All eleven approved dialogue edits are protected. Comprehensible ESL diction, doubled acknowledgements, formal reach, and licensed modern table idioms are retained. No new anachronism scope decision is needed. Clear alternating two-speaker exchanges, including the scene 06 loot negotiation, do not need tag inflation. The scene 07 answer is the supported exception. Zero reclassified table-speech HTML hatches found in the seven selected source narration files; this is observed absence, not an assembly inference. No dialogue ending in an em-dash occurs; connective dashes do not establish interrupted speech.

## Measurement and budget ledger

Unicode word tokens with internal apostrophes; curly double speech excluded from prose using balanced state parser, including multiline speech; attribution and italic text included. Headings/frontmatter excluded. No comments or apparatus present. Italic quoted remembered phrase remains in non-double-quoted prose; share is typographic, not a semantic dialogue ratio.

| Scene | Narrator | Prose words | Total words | Prose share | Prose / speech em-dashes |
|---|---|---:|---:|---:|---:|
| 01 | Zenvon Forepot | 436 | 750 | 58.1% | 2 / 1 |
| 02 | Zenvon Forepot | 345 | 556 | 62.1% | 0 / 2 |
| 03 | Zenvon Forepot | 181 | 483 | 37.5% | 1 / 3 |
| 04 | Zenvon Forepot | 431 | 529 | 81.5% | 0 / 0 |
| 05 | Zenvon Forepot | 393 | 664 | 59.2% | 0 / 0 |
| 06 | Zenvon Forepot | 425 | 862 | 49.3% | 0 / 1 |
| 07 | Zenvon Forepot | 511 | 1084 | 47.1% | 0 / 1 |

| Check | Observed | Permitted | Verdict |
|---|---|---|---|
| Genre/bookkeeping limits | Not measured against a rule | Undeclared | not checked: genre unset in all seven renders and current config |
| Portable relative-clause portraits | 2; checker exit 1, one ERROR, zero warnings | Checker default cap 1; not established as a current campaign cap | Diagnostic only: current base.md does not contain the HARD BANS claimed by checker comments |
| Shape-of / taxonomy expressions | 0 / 0 | Checker default cap 1 each | ok against checker defaults only, not historical-rule certification |
| Em-dashes | 11 total; 3 outside speech | Undeclared | not checked as a numerical budget; connective usage reviewed |
| Trailing dialogue em-dashes | 0 | No universal cap | No interruption candidate; VTT tracing not needed |
| Cross-narrator convergence | One narrator | Not applicable | not checked: no second narrator in selection |

Rule-source digests: see manifest.json references (current base.md / writing_brief.md / voice_lint.py); no delivered genre source exists.

The two portrait matches are scene 01:35, “with the expression of someone who has been assigned a job he does not want,” and scene 06:105, “with the satisfaction of someone who has recovered a lost proof.” Both are outside dialogue. The former assesses guard alertness; the latter is tailored to Veyra's academic behavior. Their shared frame is noticeable, but neither establishes voice loss on its own. Keep both in this review: no numerical campaign ban was resolved and no rewrite is needed merely to silence a stale default. The lint note separately reports bookkeeping skipped; stderr is empty. The 11 em-dashes comprise 3 connective/parenthetical narration dashes and 8 internal speech dashes, with no terminal interrupted utterance.

## Findings

### vc-s07-01 — Identify Zenvon as the speaker answering for Veyra

Status: open. Severity: medium. Category: edit.

Target: `summaries/011-20260904/narration/session_doc_scene_07_dinner_with_the_red_wizard.md:71`

Before:

```text
“Fascinating,” he says. “Very interesting. And you said, Veyra, you've seen this before.”

“Yes.”
```

Proposed replacement:

```text
“Fascinating,” he says. “Very interesting. And you said, Veyra, you've seen this before.”

“Yes,” I say.
```

The addressed character is Veyra, so the untagged reply naturally reads as hers. The reviewed extraction explicitly assigns it to Zenvon. Only the attribution and dependent comma change; the spoken word is preserved.

Evidence (relative to session unless stated): scene_extractions_smoothed/07_dinner_with_the_red_wizard.md:245–246; current writing_brief.md: keep clear attribution and distinguish player from character.

### vc-s05-ref01 — Refer the Maela correction to source/scrub review

Status: open. Severity: medium. Category: referral.

Target: `summaries/011-20260904/narration/session_doc_scene_05_battle_against_gog.md:79`

Before:

```text
“That was Pip,” she tells me.
```

Proposed replacement: none. Approve records a follow-up referral only; no narration/source edit is authorized.

The source labels this as a GM attribution correction, not Maela speaking. No known in-world speaker is established. Do not fix by guessing another speaker. This is pre-existing narration, not one of the eleven approved dialogue edits.

Evidence (relative to session unless stated): scene_extractions_smoothed/05_the_battle_against_gog.md:247–252; current writing_brief.md: table procedure is not spoken dialogue.

### vc-s07-ref01 — Refer the apprentice reminder to source/scrub review

Status: open. Severity: medium. Category: referral.

Target: `summaries/011-20260904/narration/session_doc_scene_07_dinner_with_the_red_wizard.md:45`

Before:

```text
“My apprentice,” Hamun reminds me.
```

Proposed replacement: none. Approve records a follow-up referral only; no narration/source edit is authorized.

Hamun previously identifies his apprentice in actual speech, but this extra reply comes from a GM reminder. The source does not establish Hamun saying the proposed quotation here. No automatic speech rewrite.

Evidence (relative to session unless stated): scene_extractions_smoothed/07_dinner_with_the_red_wizard.md:169–175; current writing_brief.md: do not invent dialogue from GM clarifications.

### vc-s04-ref01 — Refer the repeated bugbear departure to continuity review

Status: open. Severity: medium. Category: referral.

Target: `summaries/011-20260904/narration/session_doc_scene_04_ambush_inside_the_cave.md:63`

Before:

```text
The remaining bugbears understand. They move around her rather than through her and flee into the ravine.
```

Proposed replacement: none. Approve records a follow-up referral only; no narration/source edit is authorized.

Scene 4 completes the remaining departures; scene 5:13 and :23 then narrates further departures. The source orders the first escape, Maela’s warning/yielding, then staggered exits during combat. Review the whole join before deciding where to limit or remove completion language.

Evidence (relative to session unless stated): scene_extractions_smoothed/04_the_ambush_inside_the_cave.md:119–149; scene_extractions_smoothed/05_the_battle_against_gog.md:60–106; narration/session_doc_scene_05_battle_against_gog.md:13,23.

## Verdict and next action

Voice broadly holds. The strongest executable finding is the scene 07 speaker tag. Scenes 01–03 and 06 have no proposed voice changes; scenes 04–05 have referrals, not style rewrites. Approve/reject/discuss each item on review.html, then return its decision JSON. An approved edit will create a separate derived revision; promotion is not included. Referrals remain distinct from executable edits. No regeneration, publication or production assembly performed.
