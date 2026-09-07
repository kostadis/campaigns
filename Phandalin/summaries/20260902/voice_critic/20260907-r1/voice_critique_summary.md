# Voice critique — session 20260902

Review ID: `voice-critic:20260902:20260907-r1`

Status: **resolved — 7/7 approved and applied** to the mapped raw and scrubbed
narration files. Decisions were returned at `2026-09-07 00:13 UTC`.

## 1. Identity

The selected corpus is the five effective, promoted `narration3/*.scrubbed.md`
scenes named by `narration3/plan.md`; the alternate scene 01 and 05 renders are
excluded. Scenes 01–03 are narrated by Vukradin and scenes 04–05 by Soma, as
declared in YAML frontmatter.

| Scene | Narrator | Selected SHA-256 | Dialogue-edit state |
|---|---|---|---|
| 01 — Patrons of the Chord | Vukradin | `8fe36fa116564bbd6a0fe38ac01608284cdba2b2a654563f8d00dad7627e5e53` | promoted; matches approved application |
| 02 — Nine Crates at Low Tide | Vukradin | `7aaf129d54f484ad68a1b72bdad457f3c116ed9ec61b6baa2bf62e09cdabcfde` | reviewed; no dialogue changes proposed |
| 03 — Lost in Rsolk’s Tunnels | Vukradin | `c20e0bd316e0e1f80c4bc65bda11a672430751e261de8d6bf89f7d2d5f9ceb99` | promoted dialogue base; voice fixes applied |
| 04 — Denvar’s Unsettled Account | Soma | `121da991d24f13d0af366098d65434287d9567e78db70f93b5994a2068a754db` | promoted dialogue base; voice fixes applied |
| 05 — Harpers Behind the Wall | Soma | `1d0c7385d9d8cd58efd9bde6903d37469e414095f59293430dbc8b5e6dba3aa0` | promoted dialogue base; voice fixes applied |

Input shape: five per-scene Markdown files with frontmatter, analyzed once as a
single session corpus. This review does not include report prose, dialogue-edit
snapshots, raw/scrubbed duplicates, or alternate renders.

## 2. Inputs resolved

- Render records: `.cg/activity.jsonl` entries 15–20 and the five selected
  `.knobs.json` files. Observable backend: `codex-cli`. The records do not attest
  a model or reasoning effort, so both remain unknown; the current backend config
  is not substituted as historical evidence.
- Rendered genre: `/home/kostadis/phandalin/Phandalin/voice/_genre.md`, recorded
  digest `0a3d011c5f27` and 105 lines. The installed resolver hashes stripped content;
  the current stripped-content SHA-256 is
  `0a3d011c5f27e0eb954bc53efa92d2280add90520e94eab9c6aa4e2e28ffe0cb`,
  105 lines, 11,618 characters. It therefore matches the render record. The raw
  file-byte digest is `7a848f23…` because the file has a trailing newline.
- Current config: `config/session_doc.yaml` also resolves `voice/_genre.md`.
- Declared voices: `voice/vukradin_new_pipeline.md` (`2f175089…`, 76 lines,
  7,229 chars) and `voice/soma_new_pipeline.md` (`a1e45a11…`, 78 lines,
  6,662 chars). The current resolver uses exact roster declarations. Historical
  delivery is not independently hash-attested in the run sidecars.
- Declared examples: `examples/vukradin.md` (`1d10b874…`, 162 lines,
  15,910 chars) and `examples/soma.md` (`adc71f8c…`, 128 lines, 7,060 chars).
  `shared_examples` is unset. Every non-underscore voice/example file in these
  directories is declared by the party roster; no orphan file was promoted into
  prompt evidence.
- Identity: `config/party.yaml` and `config/players.yaml`; the prose party file
  was supporting campaign context, not a voice roster.
- Exact reviewed sources: the five files in `scene_extractions_smoothed/` bound
  by the frozen dialogue-edit `review.json` records. All were read in full.
- Dialogue provenance: the four `application.json` records are complete. Before
  this review’s fixes, the promoted narration hashes matched their approved
  dialogue outputs; those original and resulting hashes are retained in
  `review-map.json` and `voice_fixes_20260902.md`. A dedicated
  `dialogue_edit.sources.yaml` and a separate promotion manifest are absent;
  direct hash equality supplies promotion verification, but that missing
  convenience record is reported rather than invented.
- Campaign policy: `notes/scrub_register_policy.md`, the scrub manifest, the
  no-mech manifest, and `voice_smooth.sources.yaml` were applied. Approved scrub
  divergences and dialogue rewrites remain locked speech.
- Generator checkout: `/home/kostadis/src/CampaignGenerator` at
  `26ec5b0b4b3ec48d0de51ae173e395c05dc30e78`. The current declared-path
  resolvers, `narrate/base.md`, and `writing_brief.md` were read. No retained
  narration3 prompt transcript attests that checkout’s exact historical prompt.
  Current `base.md` contains template composition rather than a literal HARD BANS
  block; the effective campaign genre contains the relevant bans.
- Lint command:
  `PYTHONPATH=/home/kostadis/src/CampaignGenerator python3 -m session_doc.voice_lint /tmp/voice_critic_20260902_assembled.md --genre-file voice/_genre.md`
  The temporary document added only `## Narrator — Scene` headings and otherwise
  copied the five selected bodies exactly. Result: exit 0, zero errors, zero
  warnings, one config note: current `voice_lint` ignores the genre file’s
  `extra_tics` key. Those extra regex families are therefore **not checked
  mechanically**, not passed.

## 3. Budget ledger

Measurement scope is the five selected scenes together. Dialogue, frontmatter,
headings, and HTML comments are excluded from prose-word counts. Attribution and
other narration outside quotes count as prose. A stateful straight/curly quote
scan was used; Markdown edge cases remain a parsing limitation.

| Rule | Source | Scope | Observed | Permitted | Verdict |
|---|---|---|---:|---:|---|
| `the shape of` | genre + installed lint | corpus | 0 | 0 | ok |
| `with-the-X-of-a-man-who` | genre + installed lint | corpus | 0 | 0 | ok |
| `the-way-X-do-when` | genre + installed lint | corpus | 0 | 0 | ok |
| first-person `I file/filed` | genre + installed lint | corpus/narrator | 0 | 0 for all narrators | ok |
| genre `extra_tics` families | genre | corpus | — | 0 | **not checked mechanically** — installed checker ignored the block; full reading found no candidate |
| epigrammatic abstract balanced closers | genre line 23 | Vukradin across session | 1 after (4 before) | 1 | ok — VC-001 resolved |
| epigrammatic abstract balanced closers | genre line 23 | Soma across session | 1 after (2 before) | 1 | ok — VC-002 resolved |
| em-dashes in narration | genre line 40 | corpus | 0 | interruption only | ok |
| em-dashes in locked dialogue | genre line 40 + locked-dialogue policy | corpus | 5 total: 3 interruption/self-repair, 2 connective | n/a to narration edits | scope recorded; no rewrite proposed |

The Vukradin closer retained as the one earned instance is scene 01 line 353:
Petra’s commercial success is not the same as preserving the Common Chord. The
three scene 03 instances are proposed for concrete reframing. Soma’s retained
instance is scene 04 line 129: “Not kindness. Accounting.” The earlier balanced
age aphorism is proposed as physical reaction.

## 4. Findings

All seven findings below are **resolved by approved exact replacements**. The
original proposals and decisions remain in `review-map.json` and `decisions.json`.

### VC-001 — medium — confirmed budget breach

Scene 03 contains three surplus abstract balanced closers at lines 55, 127, and
159. Together with the retained scene 01 closer, Vukradin totals four against a
cap of one. The review card presents three linked exact replacements as one
cap-remediation consent unit; each keeps his moral reasoning but lands in
responsibility, action, or ledger language.

### VC-002 — medium — confirmed budget breach

Scene 04 line 85 supplies Soma’s second abstract balanced closer. Replace the
age aphorism with a jaw-tightening physical reaction; retain the stronger
“Not kindness. Accounting.” closer.

### VC-003 — high — confirmed POV-frame conflict

Scene 04 line 15 says Valphine “finds” the truth about Denvar from inside Soma’s
POV. The extraction establishes Valphine’s judgment, so the proposed wording
reports that judgment rather than entering her interior.

### VC-004 — medium — attribution and register

Scene 04 lines 183–187 contain consecutive Soma lines inside a longer
three-speaker quote run. The extraction identifies Soma as both the repeater and
the place-name joker. “A good name deserves a place” is also an abstract portable
bridge. The replacement makes the first-person attribution explicit and reduces
the bridge to Soma’s practical “A name is useful.” Raw and scrubbed targets retain
their existing Colorado/Daggerford divergence.

### VC-005 — medium — plausible POV framing concern

Scene 05 line 201 states Vukradin’s unspoken feeling (“fame has been bothering
him”). The source establishes that he raises the mystery, not that Soma knows his
private emotion. The proposed observation is “Vukradin has started asking why we
are famous.”

### VC-006 — medium — confirmed Soma register drift

Scene 05 line 211 turns the fame mystery into an ornate city-mouth/swallow
metaphor. Soma’s declared voice requires practical, physical-first prose and
specifically says to blunt pretty metaphors. The replacement states the operation
and unknown objective directly.

### VC-007 — low — plausible generic-prose concern

Scene 05 line 101 uses the portable transition “until the answer presents
itself,” immediately followed by the answer. The replacement names the open
tavern door, making the discovery physical and specific.

## 5. Per-scene grid

| Scene | Narrator | Prose words | Dialogue words | Total measured words | Prose share | Open findings |
|---|---|---:|---:|---:|---:|---|
| 01 | Vukradin | 1,711 | 906 | 2,617 | 65.4% | none; one closer deliberately retained |
| 02 | Vukradin | 1,204 | 527 | 1,731 | 69.6% | none |
| 03 | Vukradin | 957 | 514 | 1,471 | 65.1% | VC-001 resolved |
| 04 | Soma | 952 | 903 | 1,855 | 51.3% | VC-002, VC-003, VC-004 resolved |
| 05 | Soma | 1,026 | 855 | 1,881 | 54.5% | VC-005, VC-006, VC-007 resolved |
| **Session** | — | **5,850** | **3,705** | **9,555** | **61.2%** | **7 resolved** |

No minimum prose share is declared. The lower Soma shares are diagnostic only,
not failures.

## 6. Locked-dialogue scope calls

All dialogue is treated as protected, including the 18 approved dialogue-edit
rewrites and the scrub manifest’s authorial divergences. The five em-dashes occur
only inside locked dialogue. Two are connective rather than interruption, but one
is an approved scrub divergence and neither is proposed as a narration-style fix.
No unresolved anachronism scope call was found after applying the campaign’s
standing register rulings.

## 7. Reclassified table speech

No `<!-- table-speech reclassified: … -->` hatch appears in any of the five
selected source scenes. This is an actual absence, not an unavailable check.

The scan found 36 runs of three or more quote-led paragraphs. Full reading and
source-stage review found most to be clear two-speaker alternation or deliberate
chorus. The scene 04 Denvar-name handoff is the one run requiring an attribution
proposal (VC-004).

## 8. Verdict and carry-forward

Scenes 01 and 02 required no voice edit. All seven approved findings in scenes
03–05 were applied to both raw and scrubbed narration. Vukradin’s closer budget
is now 1/1 and Soma’s is 1/1. Post-apply lint remains at zero errors and zero
warnings, with the same config note that `extra_tics` is ignored by the installed
checker. A full join reread found no stranded grammar or lost attribution.

This is a voice review, not a certification of complete consistency, coverage,
or transcript fidelity. The ignored `extra_tics` checker block, absent dedicated
dialogue promotion manifest, and unavailable historical prompt transcript remain
explicit limitations.
