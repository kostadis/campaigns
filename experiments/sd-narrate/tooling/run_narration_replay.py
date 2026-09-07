"""Replay a saved narration prompt pair, not the old campaign-dependent loader.

Default is preparation only; --render explicitly authorizes one model call.
This reproduces submitted text, not deterministic output or pipeline behavior.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

from archive_paths import ROOT
from run_dialogue_test import save_identical_or_new


def load_case(identifier):
    manifest = ROOT/'fixtures/narration_replays.json'
    cases = json.loads(manifest.read_text())
    matches = [c for c in cases if c['id'] == identifier]
    if len(matches) != 1:
        raise ValueError('Choose an exact case ID from --list')
    case = matches[0].copy()
    for field in ['system', 'user', 'run']:
        case[field] = (manifest.parent/case[field]).resolve()
    return case


def replay(case, output, render=False):
    output = Path(output).resolve()
    if output.is_relative_to(ROOT):
        raise ValueError('Choose an output directory outside the archive')
    if (output/'response.md').exists():
        raise ValueError('Completed response exists; choose a new output directory')
    output.mkdir(parents=True,exist_ok=True)
    snapshots = {name:case[name].read_bytes() for name in ['system','user','run']}
    texts = {}
    for name in ['system','user']:
        saved = snapshots[name].decode('utf-8')
        if not saved.endswith('\n'):
            raise ValueError('Expected the historical snapshot writer newline')
        # Each original writer saved the submitted text plus one newline.
        texts[name] = saved[:-1]
        save_identical_or_new(output/f'{name}_prompt.md',saved)
    identity = {k:case[k] for k in ['id','model','reasoning_effort','max_tokens']}
    save_identical_or_new(output/'case.json',json.dumps(identity,indent=2)+'\n')
    metadata = {**identity, 'status':'running' if render else 'prepared',
                'backend':'codex-cli', 'historical_status':case['historical_status'],
                'started_utc':datetime.now(timezone.utc).isoformat(),
                'input_sha256':{str(case[k]):hashlib.sha256(v).hexdigest() for k,v in snapshots.items()},
                'system_sha256':hashlib.sha256(texts['system'].encode()).hexdigest(),
                'user_sha256':hashlib.sha256(texts['user'].encode()).hexdigest(),
                'scope':'Saved-message replay, not original sd_narrate pipeline reconstruction'}
    def save():
        (output/'run.json').write_text(json.dumps(metadata,indent=2)+'\n')
    save()
    if not render:
        return metadata
    try:
        from campaignlib import make_client, call_api
        os.environ.setdefault('CG_CODEX_TIMEOUT','1800')
        client = make_client(backend='codex-cli',model_override=case['model'],
                             reasoning_effort=case['reasoning_effort'],reasoning_effort_source='cli')
        response = call_api(client,texts['system'],texts['user'],case['model'],max_tokens=case['max_tokens'])
        (output/'response.md').write_text(response)
        actual = client.last_run_identity.as_dict()
        metadata['actual_identity'] = actual
        if actual['model'] != case['model'] or actual['codex_reasoning_effort'] != case['reasoning_effort']:
            raise ValueError('Backend identity does not match requested replay')
        if any(case[k].read_bytes() != v for k,v in snapshots.items()):
            raise ValueError('Replay input changed during generation')
        metadata['response_sha256'] = hashlib.sha256(response.encode()).hexdigest()
        metadata['status'] = 'rendered'
    except BaseException as exc:
        metadata['status'] = 'failed'
        metadata['error'] = str(exc)
        raise
    finally:
        metadata['finished_utc'] = datetime.now(timezone.utc).isoformat()
        save()
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list',action='store_true')
    parser.add_argument('--case')
    parser.add_argument('--output-root',type=Path)
    parser.add_argument('--render',action='store_true')
    args = parser.parse_args()
    if args.list:
        for case in json.loads((ROOT/'fixtures/narration_replays.json').read_text()):
            print(f'{case["id"]}: {case["historical_status"]} ({case["reasoning_effort"]})')
        return
    if not args.case or not args.output_root:
        parser.error('--case and --output-root are required unless using --list')
    print(json.dumps(replay(load_case(args.case),args.output_root,args.render),indent=2))


if __name__ == '__main__':
    main()
