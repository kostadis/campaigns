"""Isolated per-scene prompt experiment using the installed sd_narrate pipeline.

Only prompt builders are replaced, in this process. Source loading, aliases,
roster, backend, model selection, and narration-file writing remain sd_narrate's.
No CampaignGenerator checkout or shared campaign configuration is edited.
"""

from __future__ import annotations

import argparse
import contextlib
from datetime import datetime, timezone
import hashlib
import importlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
CAMPAIGN = ROOT.parents[2]
SESSION = ROOT.parent


class Tee:
    def __init__(self, terminal, log):
        self.terminal, self.log = terminal, log

    def write(self, text):
        self.terminal.write(text)
        self.log.write(text)
        self.log.flush()
        return len(text)

    def flush(self):
        self.terminal.flush()
        self.log.flush()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render", action="store_true", help="Call gpt-6-astra; otherwise prepare prompts only")
    parser.add_argument("--scene", type=int, default=4)
    parser.add_argument("--trial", default=None)
    parser.add_argument("--prompt-version", choices=["v1", "v2"], default="v1")
    parser.add_argument("--reasoning-effort", choices=["medium", "high"], default="medium")
    args = parser.parse_args()
    prefix = "" if args.prompt_version == "v1" else "v2_"
    if args.reasoning_effort != "medium":
        prefix += args.reasoning_effort + "_"
    args.trial = args.trial or f"{prefix}scene_{args.scene:02d}_trial_01"
    if not args.trial.replace("_", "").isalnum():
        parser.error("trial must contain only letters, digits, and underscores")
    out = ROOT / args.trial
    out.mkdir(exist_ok=True)
    if list(out.glob("session_doc_scene_*.md")):
        parser.error("trial already contains a narration; choose a new trial name")

    os.chdir(CAMPAIGN)
    # The existing CLI adapter needs time for a complete narration response.
    os.environ.setdefault("CG_CODEX_TIMEOUT", "1800")
    sd = importlib.import_module("session_doc.sd_narrate")
    original_system = sd.build_narrate_system
    original_user = sd.build_narrate_prompt
    plan_path = SESSION / "narration2/plan.md"
    extraction_dir = SESSION / "scene_extractions_smoothed"
    sections = sd.parse_plan(plan_path.read_text(), len(sd.load_scene_extractions(extraction_dir)))
    if not 1 <= args.scene <= len(sections):
        parser.error(f"scene must be between 1 and {len(sections)}")
    section = sections[args.scene - 1]
    narrator = section["narrator"]
    source_path = sd.resolve_scene_extraction_file(extraction_dir, args.scene, section["scene"])
    if source_path is None:
        parser.error("scene has no unambiguous extraction")
    baselines = list((SESSION / "narration2").glob(f"session_doc_scene_{args.scene:02d}_*.md"))
    if len(baselines) != 1:
        parser.error("scene must have exactly one original narration for comparison")
    party_config = sd.load_party_config_arg(str(CAMPAIGN / "config/party.yaml"))
    declarations = {character.name: character for character in party_config.characters}
    declared = declarations[narrator]
    brief_path = ROOT / ("prompt.md" if args.prompt_version == "v1" else "prompt_v2.md")
    identity_inputs = [
        SESSION / "session-summary.md",
        source_path,
        plan_path,
        baselines[0],
        CAMPAIGN / "docs/party.md",
        CAMPAIGN / "docs/entity_registry.yaml",
        CAMPAIGN / "config/party.yaml",
        CAMPAIGN / "config/players.yaml",
        declared.voice,
        CAMPAIGN / "voice/_genre.md",
        declared.examples,
        brief_path,
        Path(__file__).resolve(),
    ]
    if args.scene > 1:
        previous = declarations[sections[args.scene - 2]["narrator"]]
        if previous.examples:
            identity_inputs.append(previous.examples)
    identity_inputs = list(dict.fromkeys(p for p in identity_inputs if p is not None))
    hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in identity_inputs}
    repo = Path(sd.__file__).resolve().parents[1]
    revision = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    metadata = {
        "status": "running" if args.render else "preparing",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "backend": "codex-cli", "model": "gpt-6-astra", "reasoning_effort": args.reasoning_effort,
        "prompt_version": args.prompt_version, "brief_path": str(brief_path),
        "scene": args.scene, "narrator": narrator, "scene_name": section["scene"],
        "source_path": str(source_path), "baseline_path": str(baselines[0]),
        "repository": str(repo), "revision": revision,
        "input_sha256": hashes,
        "comparison_limit": "Existing narration2 was a five-scene bundle; this trial is a single-scene render using the current checkout. This is a qualitative prompt experiment, not a controlled model benchmark.",
    }

    def save_meta():
        (out / "run.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")

    def build_system(*pos, **kw):
        baseline = original_system(*pos, **kw)
        (out / "original_system_prompt.md").write_text(baseline + "\n")
        voice = kw["voice_note"]
        # Read the unique section in the explicitly declared voice file. The
        # heading may use "Valphine" while her roster name is "Valphine Sotorra".
        # This does not infer identity from filenames or first-name matching.
        headings = list(re.finditer(r"(?m)^[^\n]+ voice specification:\n", voice))
        if len(headings) != 1 or "\nFailure-prevention rules:" not in voice:
            raise ValueError("Voice file structure changed; inspect before extracting the character specification")
        character = voice[headings[0].end():].split("\nFailure-prevention rules:", 1)[0].strip()
        genre = kw["genre"]
        changes = {
            "Description is sparse but specific; favor the material noun over the poetic image.":
                "Description is specific and sufficient to establish the setting, action, and material clues; favor the material noun over the poetic image.",
            "- **Dialogue is broken in.** Tag lines are minimal — often just a thought between the speech beats — and characters interrupt each other, talk past each other, finish other characters' sentences.":
                "- **Dialogue belongs to an enacted scene.** Use enough attribution and physical context to make the speakers and their interaction clear. Preserve meaningful interruptions, cross-talk, and completed sentences without reproducing every transcript boundary.",
            '- Use the character\'s stock phrases verbatim — they are signatures: "fair-trade, conflict-free gold," "deliciously painful," "shell sprout," "the Overbright," "my bale."':
                "- Let characteristic vocabulary appear where it fits the moment; it is not a checklist of signatures to insert.",
        }
        if args.prompt_version == "v2":
            # Resolve the tense conflict in the supplied reference itself. The
            # shared genre file stays untouched, and v1 remains reproducible.
            old_tense = next((line for line in genre.splitlines() if line.startswith("- **First-person present tense, always**")), None)
            if old_tense is None:
                raise ValueError("Expected the existing genre tense instruction")
            changes[old_tense] = "- **Close first-person perspective; present-tense scene.** Narrate the unfolding action from inside the POV character. Use ordinary past tense for earlier events and memories, and natural future or conditional tense for plans. Other people may be described in the third person without switching POV; their private thoughts remain unavailable."
        for before, after in changes.items():
            if genre.count(before) != 1:
                raise ValueError(f"Expected one genre instruction: {before}")
            genre = genre.replace(before, after)
        blocks = [
            brief_path.read_text().strip(),
            f"Scene: {kw['scene']}\nNarrator: {kw['narrator']}",
            "## Character perspective\n\n" + character,
            "## Campaign style reference\n\n" + genre.strip(),
        ]
        if kw.get("char_examples"):
            blocks.append("## Narrator's established prose examples\n\n" + kw["char_examples"].strip())
        if pos and pos[0]:
            blocks.append("## Shared prose examples\n\n" + pos[0].strip())
        candidate = "\n\n".join(blocks)
        (out / "system_prompt.md").write_text(candidate + "\n")
        (out / "character_reference.md").write_text(character + "\n")
        metadata["system_prompt_words"] = len(candidate.split())
        metadata["original_system_prompt_words"] = len(baseline.split())
        return candidate

    def build_user(*pos, **kw):
        # Identical source payload and user instructions to the normal pipeline.
        user = original_user(*pos, **kw)
        (out / "user_prompt.md").write_text(user + "\n")
        metadata["user_prompt_words"] = len(user.split())
        return user

    sd.build_narrate_system = build_system
    sd.build_narrate_prompt = build_user
    cli = [
        "sd_narrate", str(SESSION / "session-summary.md"),
        "--plan", str(plan_path),
        "--scene-extractions", str(extraction_dir),
        "--scene-extraction-file", str(source_path),
        "--per-scene-output", str(out), "--scene", str(args.scene),
        "--backend", "codex-cli", "--model", "gpt-6-astra", "--codex-reasoning-effort", args.reasoning_effort,
        "--party", str(CAMPAIGN / "docs/party.md"),
        "--party-config", str(CAMPAIGN / "config/party.yaml"),
        "--players-config", str(CAMPAIGN / "config/players.yaml"),
        "--voice-dir", str(CAMPAIGN / "voice"), "--examples", str(CAMPAIGN / "examples"),
        "--alias-registry", str(CAMPAIGN / "docs/entity_registry.yaml"),
        "--narrate-tokens", "70000", "--prose-mode", "--reflections",
        "--narration-genre-file", str(CAMPAIGN / "voice/_genre.md"),
    ]
    if not args.render:
        cli.append("--dry-run")
    metadata["argv"] = cli
    save_meta()
    sys.argv = cli
    try:
        with (out / ("render.log" if args.render else "prepare.log")).open("w") as log:
            with contextlib.redirect_stdout(Tee(sys.stdout, log)), contextlib.redirect_stderr(Tee(sys.stderr, log)):
                sd.main()
        metadata["status"] = "rendered" if args.render else "prepared"
    except BaseException as exc:
        metadata["status"] = "failed"
        metadata["error"] = str(exc)
        raise
    finally:
        metadata["finished_utc"] = datetime.now(timezone.utc).isoformat()
        metadata["changed_inputs"] = [str(p) for p in identity_inputs if hashlib.sha256(p.read_bytes()).hexdigest() != hashes[str(p)]]
        save_meta()


if __name__ == "__main__":
    main()
