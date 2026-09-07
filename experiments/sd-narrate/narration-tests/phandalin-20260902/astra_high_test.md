# Astra high retry — fixed prompt, changed reasoning effort

The user asked whether the v2 medium regression might be a model-execution issue and requested a retry at high reasoning. This test holds the v2 writing brief fixed, including its existing information-access wording. The narrower post-test proposal in v2_review.md is **not** used.

Before rendering, the system prompt, user prompt, and character reference for each high run were verified byte-identical to that scene's v2 medium run. Source data, examples, model (`gpt-6-astra`), text-only backend, and single-scene rendering are held fixed. The requested reasoning effort alone changes from medium to high; output paths and run bookkeeping necessarily differ.

One high generation each for Scenes 1 and 3 (Vukradin) and Scene 2 (Valphine), with at most two simultaneous requests. No rerolls or hand-edits.

## Questions fixed before seeing the high results

1. Does Valphine retain the magical-disinterest ending, and the promise correction exchange, through the established Sending Stones without adding unsupported access?
2. Does she retain her distinctive motive-reading and supported description while avoiding the previous invented negative observations and procedural self-reference?
3. Does Vukradin remain sincere and recognizable, with his important jokes and commitments intact?
4. Does the sewer opening respect that Vukradin entered alone? Are memory, disinterest, and navigation distinguished?
5. Does greater coverage bring new invented dialogue, unsupported facts, redundancy, or weaker prose?

A high result that restores the missing material would show the v2 prompt can produce a more complete result at high in this sample. It would not prove that medium caused the omission or that the prompt has no ambiguity. Failure at high would likewise not establish that the model is incapable. With one sample per condition, ordinary variation remains a confounder; conclusions should be local and comparative.

```bash
/home/kostadis/.venv/bin/python -B summaries/20260902/narration_prompt_test/run_scene_set.py --scenes 1 2 3 --prompt-version v2 --reasoning-effort high --render
```

Results go into `v2_high_scene_NN_trial_01` without replacing the medium outputs. Completed trial names cannot be reused.
