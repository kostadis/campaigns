# Prompt v2 — targeted follow-up

The proposed [writing brief](prompt_v2.md) preserves the first experiment's main change: the players' actual speech belongs inside a developed scene, with no dialogue quota or per-beat expansion requirement. It responds to [all_scenes_review.md](all_scenes_review.md) without feeding the earlier generated prose or review into the rendering model.

## Changes proposed before rendering

- **Procedural dialogue and repetition:** distinguish declarations of character action from spoken lines; narrate the former without inventing a rewritten quote. Compress intermediate clarification while retaining the characteristic exchange, practical conclusion, and meaningful humor.
- **Evidence and timing:** distinguish observation, inference, suggestion, completed action, and the scope of remembered information. Unmentioned behavior is not observed absence. This targets the added construct behavior and the overstatement of Vukradin's navigation knowledge.
- **Access to dialogue:** forbid manufactured proximity, messages, or debriefs to make an inaccessible exchange audible. Preserve supported remote communication. This addresses the underlying Brewbarry staging issue, although that scene is not rerun in this requested test.
- **Narrator-specific interior prose:** keep convictions sincere within their owner's perspective, allow another character to misread them, and avoid spreading one generic sardonic commentator across voices. Do not turn new gestures into a personality checklist.
- **Tense:** keep present-tense scene action and natural past-tense memory. Replace the contradictory “present tense, always” paragraph in the process-local genre reference for v2 only. Shared genre and character files are unchanged.
- **Register:** leave meaningful source jokes for downstream review; do not manufacture replacement jokes or turn a real-world reference into new world facts.

The OpenAI Docs skill informed the instruction-conflict check and explicit prose contract. Official Astra guidance recommends auditing contextual instructions and specifying the intended writing style; the particular narrative changes above come from the local review, not from a model-quality claim. [Official GPT-6 Astra prompting guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#prompting-best-practices).

## Test design

One new generation each for Scene 1 (Vukradin at the Common Chord), Scene 2 (Valphine's stakeout), and Scene 3 (Vukradin meeting Rsolk). Use gpt-6-astra, medium reasoning, the same text-only backend, sources, scene boundaries, character specifications, examples, and user-prompt assembly as v1. Maximum two simultaneous generation requests. No rerolls or hand-edits to select a better result.

Compare against the immediately preceding experimental drafts, not only the older narration2. Verify unchanged source payloads and read for both gains and losses: preserving signature exchanges, Vukradin's sincerity, Valphine's distinctive analysis, scene continuity, attribution, and evidence boundaries. The removed third-person procedural quotes and invented negative observations are targeted checks, not sufficient proof of overall quality.

This is one sample per scene, not a statistical evaluation. Valphine's investigative voice is tested; her theological and emotional range, Brewbarry's hearing problem, and Soma's time-of-day problem are not directly retested.

```bash
/home/kostadis/.venv/bin/python -B summaries/20260902/narration_prompt_test/run_scene_set.py --scenes 1 2 3 --prompt-version v2
/home/kostadis/.venv/bin/python -B summaries/20260902/narration_prompt_test/run_scene_set.py --scenes 1 2 3 --prompt-version v2 --render
```

The first command prepares without model calls. The second renders into new `v2_scene_NN_trial_01` directories; completed narrations cannot be overwritten. Later experiments must choose new trial names with `run_experiment.py --trial ...`.
