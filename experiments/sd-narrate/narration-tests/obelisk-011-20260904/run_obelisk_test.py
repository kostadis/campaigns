"""Isolated Obelisk scenes 1/3 test of the accepted narration v1 brief."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import contextlib
from datetime import datetime, timezone
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys

CAMPAIGN = Path('/home/kostadis/obelisk/obelisk')
SESSION = CAMPAIGN / 'summaries/011-20260904'
OUTPUT = SESSION / 'narration_prompt_test'
ACCEPTED = Path('/home/kostadis/phandalin/Phandalin/summaries/20260902/narration_prompt_test/prompt.md')
ACCEPTED_SHA = '67feb055f9efa13a384c3ae80d7c1b3eac20436c88d418aed2b79482806f2aa6'


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
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--scene', type=int, choices=[1, 3])
    args = parser.parse_args()
    if args.scene is None:
        assert hashlib.sha256(ACCEPTED.read_bytes()).hexdigest() == ACCEPTED_SHA
        OUTPUT.mkdir(exist_ok=True)
        brief = OUTPUT / 'prompt_v1.md'
        if brief.exists() and brief.read_bytes() != ACCEPTED.read_bytes():
            raise ValueError('Existing local brief differs; refusing to overwrite')
        brief.write_bytes(ACCEPTED.read_bytes())
        runner = OUTPUT / 'run_obelisk_test.py'
        if Path(__file__).resolve() != runner:
            if runner.exists() and runner.read_bytes() != Path(__file__).read_bytes():
                raise ValueError('Existing runner differs; refusing to overwrite')
            runner.write_bytes(Path(__file__).read_bytes())
        # Test-only scaffolding preserves ordinal scene indices. Scene 2 is
        # never rendered and this is not a campaign narration-plan decision.
        titles = ['Arrival at Wyvern Tor', 'Ambush at the Ravine', 'Scouting the Cave']
        plan = '\n\n'.join(f'## Scene {n}\nnarrator: Zenvon Forepot\nchunks: {n}\nscene: {title}\nfocus: Render the source scene within its recorded boundaries.' for n,title in enumerate(titles,1)) + '\n'
        plan_path = OUTPUT / 'test_plan.md'
        if plan_path.exists() and plan_path.read_text() != plan:
            raise ValueError('Existing test plan differs; refusing to overwrite')
        plan_path.write_text(plan)
        def run(n):
            cmd = [sys.executable, '-B', str(runner), '--scene', str(n)]
            if args.render:
                cmd.append('--render')
            print(f'Scene {n}: {"rendering" if args.render else "preparing"}', flush=True)
            result = subprocess.run(cmd, capture_output=True, text=True)
            print(f'Scene {n}: {"complete" if result.returncode == 0 else "FAILED"}', flush=True)
            if result.returncode:
                print((result.stderr + result.stdout)[-4000:], flush=True)
            return result.returncode
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = [f.result() for f in as_completed([pool.submit(run,n) for n in [1,3]])]
        return int(any(results))

    os.chdir(CAMPAIGN)
    os.environ.setdefault('CG_CODEX_TIMEOUT', '1800')
    sd = importlib.import_module('session_doc.sd_narrate')
    trial = OUTPUT / f'v1_scene_{args.scene:02d}_trial_01'
    trial.mkdir(exist_ok=True)
    if list(trial.glob('session_doc_scene_*.md')):
        parser.error('Completed trial already exists; refusing to overwrite')
    source = next((SESSION/'scene_extractions_smoothed').glob(f'{args.scene:02d}_*.md'))
    party = sd.load_party_config_arg(str(CAMPAIGN/'config/party.yaml'))
    declared = {c.name:c for c in party.characters}['Zenvon Forepot']
    inputs = [source, SESSION/'session_summary.md', OUTPUT/'test_plan.md', OUTPUT/'prompt_v1.md',
              CAMPAIGN/'config/party.yaml', CAMPAIGN/'config/players.yaml', CAMPAIGN/'docs/party.md',
              CAMPAIGN/'docs/entity_registry.yaml', CAMPAIGN/'notes/scrub_register_policy.md', Path(__file__).resolve()]
    inputs += [p for c in party.characters for p in [c.voice,c.sheet,c.examples] if p]
    inputs += list(party.shared_examples)
    inputs = list(dict.fromkeys(inputs))
    hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    assert hashes[str(OUTPUT/'prompt_v1.md')] == ACCEPTED_SHA
    repo = Path(sd.__file__).resolve().parents[1]
    metadata = {'status':'running' if args.render else 'preparing', 'scene':args.scene,
        'narrator':declared.name,'model':'gpt-6-astra','reasoning_effort':'medium','backend':'codex-cli',
        'source_path':str(source),'prompt_version':'v1','input_sha256':hashes,
        'started_utc':datetime.now(timezone.utc).isoformat(),
        'revision':subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        'adaptation':'Unchanged accepted writing brief. Obelisk full declared voice notes and examples; local register policy as style reference. No Phandalin voice/genre content. Test-only Zenvon assignment for scenes 1/3; no existing session narration plan or baseline.'}
    original_system, original_user = sd.build_narrate_system, sd.build_narrate_prompt
    def system(*pos,**kw):
        (trial/'original_system_prompt.md').write_text(original_system(*pos,**kw)+'\n')
        voice = kw['voice_note']
        assert voice.strip() == declared.voice.read_text().strip()
        blocks = [(OUTPUT/'prompt_v1.md').read_text().strip(),
                  f"Scene: {kw['scene']}\nNarrator: {kw['narrator']}",
                  '## Character perspective\n\n'+voice.strip()]
        if kw.get('genre'):
            blocks.append('## Campaign style reference\n\n'+kw['genre'].strip())
        if kw.get('char_examples'):
            blocks.append("## Narrator's established prose examples\n\n"+kw['char_examples'].strip())
        if pos and pos[0]:
            blocks.append('## Shared prose examples\n\n'+pos[0].strip())
        candidate='\n\n'.join(blocks)
        (trial/'system_prompt.md').write_text(candidate+'\n')
        (trial/'character_reference.md').write_text(voice+'\n')
        metadata['scene_name']=kw['scene']
        metadata['system_prompt_words']=len(candidate.split())
        return candidate
    def user(*pos,**kw):
        result=original_user(*pos,**kw)
        (trial/'user_prompt.md').write_text(result+'\n')
        metadata['user_prompt_words']=len(result.split())
        return result
    sd.build_narrate_system, sd.build_narrate_prompt=system,user
    cli=['sd_narrate',str(SESSION/'session_summary.md'),'--plan',str(OUTPUT/'test_plan.md'),
         '--scene-extractions',str(source.parent),'--scene-extraction-file',str(source),
         '--scene',str(args.scene),'--per-scene-output',str(trial),
         '--party',str(CAMPAIGN/'docs/party.md'),'--party-config',str(CAMPAIGN/'config/party.yaml'),
         '--players-config',str(CAMPAIGN/'config/players.yaml'),'--voice-dir',str(CAMPAIGN/'voice'),
         '--examples',str(CAMPAIGN/'examples'),'--alias-registry',str(CAMPAIGN/'docs/entity_registry.yaml'),
         '--no-alias-normalize','--narration-genre-file',str(CAMPAIGN/'notes/scrub_register_policy.md'),
         '--backend','codex-cli','--model','gpt-6-astra','--codex-reasoning-effort','medium',
         '--narrate-tokens','32000','--prose-mode','--reflections']
    if not args.render:
        cli.append('--dry-run')
    metadata['argv']=cli
    def save():
        (trial/'run.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
    save()
    sys.argv=cli
    try:
        with (trial/('render.log' if args.render else 'prepare.log')).open('w') as log:
            with contextlib.redirect_stdout(Tee(sys.stdout,log)),contextlib.redirect_stderr(Tee(sys.stderr,log)):
                sd.main()
        metadata['status']='rendered' if args.render else 'prepared'
    except BaseException as exc:
        metadata['status']='failed';metadata['error']=str(exc)
        raise
    finally:
        metadata['finished_utc']=datetime.now(timezone.utc).isoformat()
        metadata['changed_inputs']=[str(p) for p in inputs if hashlib.sha256(p.read_bytes()).hexdigest()!=hashes[str(p)]]
        save()
    return 0


if __name__=='__main__':
    sys.exit(main())
