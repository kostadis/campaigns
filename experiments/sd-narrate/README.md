# sd_narrate voice and dialogue experiments

Shared, cross-campaign evidence for [CampaignGenerator #387](https://github.com/kostadis/CampaignGenerator/issues/387). These are experiments and frozen fixtures, **not campaign canon or active production prompts**. No production behavior is installed by this directory.

## Start here

- [Dialogue-edit review and recommendation](dialogue-edit-tests/review.md): start with B as a separate, reviewed contextual-dialogue pass; retain C as an optional scene-level edit. Cadence safeguards proposed in #387 still need testing. Do not stack A → B → C automatically.
- [Selected passages](dialogue-edit-tests/passages.md) and [portable A/B/C reader](readers/dialogue-edit-tests/index.html).
- [All-scene Phandalin review](narration-tests/phandalin-20260902/all_scenes_review.md), [v2 review](narration-tests/phandalin-20260902/v2_review.md), and [medium/high review](narration-tests/phandalin-20260902/astra_high_review.md). The first revised narration brief, v1, was accepted; v2 was not.
- [Portable Phandalin comparison](readers/narration-tests/phandalin-20260902/index.html) and [medium/high comparison](readers/narration-tests/phandalin-20260902/astra_effort_comparison.html).
- [Obelisk review](narration-tests/obelisk-011-20260904/review.md) and [portable Obelisk reader](readers/narration-tests/obelisk-011-20260904/obelisk_test_reader.html), covering scenes 1 and 3 with the confirmed Veyra and Pip references.
- [Prompt files](prompts/) and [verification notes](VERIFICATION.md).

GitHub displays the Markdown documents directly. Download/clone and open the HTML readers locally for interactive comparisons.

## Layout and authority

| Directory/file | Purpose |
|---|---|
| `prompts/` | Accepted v1, rejected v2 with rationale, original short editing proposal, and the exact tested common/A/B/C instructions. Maintained prompt surface for future trials. |
| `tooling/` | Portable experiment runners, comparison builders, archive resolver, and helper tests. These call installed CampaignGenerator; they are not application implementation. |
| `tooling/archive/` | Original CampaignGenerator experiment scripts/docs/tests, unchanged, for provenance—not runnable installation instructions. |
| `fixtures/` | Frozen campaign inputs, source/draft/reference snapshots, and relative-path case manifests. Not replacements for authoritative campaign files. |
| `narration-tests/phandalin-20260902/` | Entire original v1/v2 and medium/high experiment directory, including failed/prepared attempts, all reviews, and raw outputs. |
| `narration-tests/obelisk-011-20260904/` | Entire original Obelisk experiment directory, including preliminary prepared attempts and the completed supporting-voice trials. |
| `dialogue-edit-tests/` | All nine independent A/B/C runs: submitted prompts, baseline, response, diff, metrics, review, and selected passages. |
| `readers/` | Derived HTML copies with relocated links. Original HTML remains unchanged in the archived test directories. |
| `relocation_manifest.json` | Original → archive paths, byte hashes, and recorded-input verification results. Absolute paths here and in old logs are historical evidence, not runtime dependencies. |

The old campaign-local scripts and their READMEs intentionally retain their original paths and commands. **Do not execute those archived scripts.** Use the portable tooling below. The active helpers resolve everything inside this directory, relative to their manifests; no original `/home/kostadis/...` or old `/tmp/...` experiment location is required. The editable CampaignGenerator installation remains an external dependency.

For the editor, the tested system message is `prompts/editor_common.md` plus a blank line and `prompts/approach_{a,b,c}.md`. It is not the narration prompt plus the editor instructions. The narration v1 tests used different reference assembly for Phandalin and Obelisk; the full submitted messages retain those differences.

## Verify without model calls

Requires Python 3.10+, pytest, and an installed CampaignGenerator exposing the public `campaignlib` API. The original runs used its Codex CLI backend. Use an interpreter with that package available; no package installation or API call is required for these checks in the existing development environment.

From this directory:

```bash
python -B tooling/archive_paths.py
python -B -m pytest -q -p no:cacheprovider tooling/tests
```

The helper tests verify archive integrity, source immutability, default preparation without calls, portable path resolution, exact reconstruction of all nine original A/B/C submitted message snapshots, refusal to overwrite completed responses, and backend-identity failure handling. They do not establish semantic voice fidelity.

## Run another A/B/C editing comparison

Each arm starts from the same original draft. Default preparation makes **zero** model calls:

```bash
dialogue_trial_dir=$(mktemp -d /tmp/sd-narrate-dialogue.XXXXXX)
python -B tooling/run_dialogue_test.py \
  --cases fixtures/dialogue_cases.json --output-root "$dialogue_trial_dir"
```

Inspect the prepared prompts. To explicitly authorize **nine** new gpt-6-astra/medium calls:

```bash
python -B tooling/run_dialogue_test.py \
  --cases fixtures/dialogue_cases.json --output-root "$dialogue_trial_dir" \
  --render --workers 3
python -B tooling/build_reader.py "$dialogue_trial_dir"
```

Use a fresh directory for a new trial; completed responses and differing snapshots cannot be overwritten. The runner rejects output inside this preserved experiment tree. Changing the prompts produces a new experiment, not a replacement for the archived outputs.

## Replay a narration prompt pair

The complete submitted narration messages can be replayed without rebuilding the original campaign-dependent loader:

```bash
python -B tooling/run_narration_replay.py --list
narration_trial_dir=$(mktemp -d /tmp/sd-narrate-replay.XXXXXX)
python -B tooling/run_narration_replay.py \
  --case phandalin-20260902/scene_01_trial_01 \
  --output-root "$narration_trial_dir"
```

This prepares only. Adding `--render` authorizes **one** call using that case's recorded model/effort. All 17 historical narration attempts with saved message pairs are listed, including failed/prepared attempts; replaying one does not relabel its historical status. The replay removes exactly the one newline each historical snapshot writer added to the submitted message. It does not reconstruct the original loader or guarantee deterministic output. Review results as new proposals.

## Rebuild readers without modifying historical artifacts

Choose a new, nonexistent output directory:

```bash
python -B tooling/build_archive_readers.py /tmp/sd-narrate-new-readers
python -B tooling/build_reader.py dialogue-edit-tests \
  --output-root /tmp/sd-narrate-new-dialogue-reader
```

The first command relocates links in copies of all 16 historical HTML readers. The second rebuilds the A/B/C viewer from verified raw responses and frozen inputs. Neither changes original readers, responses, or metadata. `tooling/extract_passages.py` preserves the original case-specific excerpt selection logic; use it only on a new output set, and expect anchors to fail if a new generation no longer contains those passages.

## Provenance and limits

Consolidated 2026-09-06 from the Phandalin and Obelisk campaign-local `narration_prompt_test/` directories and CampaignGenerator's experiment branch/results. The original CampaignGenerator branch `narration-v1-dialogue-edit` remains historical, with commits `b13bfe2`, `046801c`, and `c72e9e4`; this shared campaigns directory is now the maintained home. The application backend revision used by the original trials was `a9081774725f2fd0faec56d925df679c79055d0a`.

317 preserved file copies total about 5.7 MB before derived readers. All copied artifact bytes match their originals. Of 337 historical input checks, 327 match frozen files. The other ten refer only to three earlier revisions of the Phandalin `run_experiment.py` that were overwritten during the original experiment. Their historical hashes remain recorded; the currently available script is explicitly marked **historical-version-unavailable** for those runs. No missing script version was fabricated. Submitted prompt snapshots and generated outputs are preserved, and all nine A/B/C input ledgers match.

This is qualitative evidence, not a blinded or repeated model evaluation. Source coverage remains the separate concern tracked in [#386](https://github.com/kostadis/CampaignGenerator/issues/386). Campaign register protections and human review must survive implementation; see [#368](https://github.com/kostadis/CampaignGenerator/issues/368) and [#369](https://github.com/kostadis/CampaignGenerator/issues/369).
