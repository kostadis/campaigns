# Narration prompt experiment — all five scenes

Purpose: let the players' voices emerge in a readable, described scene while preserving their actual speech and the events of the session.

Follow-up: [proposed v2 prompt](prompt_v2.md), [rationale](v2_proposal.md), [three new Vukradin/Valphine scenes](v2_scenes.md), [v1/v2 comparison](v2_comparison.html), and [v2 findings](v2_review.md). The second test is mixed: Vukradin retains his voice, but Valphine loses an important closing exchange. No version has been promoted to production.

Completed results: [all-scene comparison](index.html), [whole-session reading copy](all_scenes.md), and [voice and fidelity review](all_scenes_review.md). Scenes 1 and 3 are Vukradin, Scene 2 is Valphine Sotorra, Scene 4 is Soma, and Scene 5 is Brewbarry. All narrations are unedited model outputs.

The [accepted Scene 4](trial_02/session_doc_scene_04_denvar_s_room_and_unpaid_rent.md) and its [original review](trial_02/review.md) are unchanged. The remaining four scenes use that same writing brief, with their own declared character references and examples. `trial_01` records the initial failed sandbox initialization; no narration was generated in that attempt. `scene_04_prepare_check` verifies that the generalized runner assembles byte-identical system and user prompts to the accepted Soma run; it is not another render.

This is an isolated test of `gpt-6-astra` at medium reasoning effort. The existing `narration2` files, scene extractions, voice files, campaign configuration, and CampaignGenerator checkout are not edited. The runner replaces `sd_narrate`'s system-prompt builder only for its own process. The source loading, user-prompt builder, canonical-name handling, roster, backend, and output writer remain the installed pipeline's.

## Changed instructions

- The experimental [writing brief](prompt.md) replaces the generic narration, every-quote, per-beat expansion, and long mechanical-conversion instructions.
- Each narrator's character specification is retained verbatim. Its surrounding rewrite instructions and repeated quote-preservation and failure-prevention lists are omitted. Voice and example files are selected through the explicit party configuration.
- The genre reference appears once. Three instructions change: description must be sufficient to establish the scene; dialogue needs clear attribution and physical context; characteristic vocabulary is used when natural rather than as a signature checklist.
- The declared prose examples and the normal assembled user prompt are retained.
- Quote selection and paragraphing have editorial freedom. Invented dialogue, altered events, invented evidence, and invented motives remain prohibited.

The runner records the exact assembled prompts, source digests, repository revision, explicit model selection, and render log in the trial directory. `original_system_prompt.md` records what the current normal builder would have supplied for the same inputs; it is not a recovered historical bundle prompt.

## Reproduce

From the campaign workspace:

```bash
/home/kostadis/.venv/bin/python -B summaries/20260902/narration_prompt_test/run_experiment.py --scene 2 --trial scene_02_trial_02
/home/kostadis/.venv/bin/python -B summaries/20260902/narration_prompt_test/run_experiment.py --scene 2 --trial scene_02_trial_02 --render
```

The first command prepares the prompts without a model call. The second renders the scene. Choose a new trial name after a narration exists; the runner refuses to overwrite one.

`run_scene_set.py --render` was used for scenes 1, 2, 3, and 5, with at most two concurrent text-generation calls. Its default trial names now contain results and cannot be reused. `review_quotes.py TRIAL_DIRECTORY` builds a lexical comparison; `build_gallery.py` assembles the five selected results without rewriting them.

## Review criteria

Read the result for these together, without a target dialogue percentage:

- Soma's practical, dry perspective and the players' distinctive exchanges remain recognizable.
- Setting, physical action, the landlord's reactions, and the investigation form a continuous scene.
- The retained dialogue has sufficient speaker attribution; repetition has an understandable function.
- The room and meal suggest unusually good pay; no obvious insignia are found; the chits specify nine crates, third hour, eight up and one down, a client reference and house mark without a personal name, and a weekly settlement. Prior work is paid and the latest delivery is unpaid.
- Denvar is named, rent is due that day, and following him after he wakes follows from those facts. Soma's sincere housing advice remains. The narration ends before the next scene's payment collection.
- No new clues, material events, motives, or unsupported character presence have appeared.

The criteria above originated with the Soma test. The all-scene review additionally checks Vukradin's sincerity, Valphine's motive-reading and limits of knowledge, Brewbarry's bodily perspective, and whether separated characters can actually hear the retained dialogue.

Comparison limitation: the existing `narration2` was rendered as a five-scene bundle. These experiments render scenes individually through the currently installed checkout. This is a qualitative prompt trial, not a controlled model benchmark or evidence that a single changed instruction caused an improvement.
