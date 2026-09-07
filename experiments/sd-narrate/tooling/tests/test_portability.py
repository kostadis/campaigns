import hashlib
import json
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from archive_paths import Archive, ROOT
from run_dialogue_test import load_cases, run_case
from run_narration_replay import load_case, replay


def test_archive_bytes_and_historical_gap_are_explicit():
    archive = Archive()
    report = archive.verify()
    assert report['preserved_files'] == 317
    assert report['input_checks'] == {'matched':327,'historical-version-unavailable':10}
    gaps = [i for i in archive.manifest['input_checks'] if i['status'] != 'matched']
    assert all(i['original'].endswith('/narration_prompt_test/run_experiment.py') for i in gaps)


def test_every_portable_dialogue_case_resolves_within_archive(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    cases = load_cases(ROOT/'fixtures/dialogue_cases.json')
    assert {c['id'] for c in cases} == {'zenvon','vukradin','valphine'}
    for case in cases:
        for path in [case['draft'],case['source'],*case['references']]:
            assert Path(path).is_relative_to(ROOT)
            assert Path(path).is_file()


@pytest.mark.parametrize('arm',['a','b','c'])
def test_relocated_assembly_matches_original_submitted_prompts(tmp_path, arm):
    for case in load_cases(ROOT/'fixtures/dialogue_cases.json'):
        with patch('campaignlib.make_client') as client, patch('campaignlib.call_api') as api:
            run_case(case,arm,tmp_path,False)
        client.assert_not_called()
        api.assert_not_called()
        for name in ['system_prompt.md','user_prompt.md','baseline.md']:
            assert (tmp_path/case['id']/arm/name).read_bytes() == (
                ROOT/'dialogue-edit-tests'/case['id']/arm/name).read_bytes()


def test_narration_replay_is_dry_by_default_and_preserves_messages(tmp_path):
    case = load_case('phandalin-20260902/scene_01_trial_01')
    with patch('campaignlib.make_client') as client, patch('campaignlib.call_api') as api:
        metadata = replay(case,tmp_path)
    assert metadata['status'] == 'prepared'
    client.assert_not_called()
    api.assert_not_called()
    for kind in ['system','user']:
        snapshot = case[kind].read_bytes()
        assert (tmp_path/f'{kind}_prompt.md').read_bytes() == snapshot
        assert metadata[f'{kind}_sha256'] == hashlib.sha256(snapshot[:-1]).hexdigest()


def test_replay_refuses_existing_response(tmp_path):
    (tmp_path/'response.md').write_text('Keep me')
    with pytest.raises(ValueError,match='Completed response'):
        replay(load_case('phandalin-20260902/scene_01_trial_01'),tmp_path)
    assert (tmp_path/'response.md').read_text() == 'Keep me'


def test_replay_refuses_archive_output():
    with pytest.raises(ValueError,match='outside the archive'):
        replay(load_case('phandalin-20260902/scene_01_trial_01'),ROOT/'unwanted')
    assert not (ROOT/'unwanted').exists()


def test_replay_records_backend_mismatch_as_failure(tmp_path):
    client = Mock()
    client.last_run_identity.as_dict.return_value = {
        'model':'wrong','codex_reasoning_effort':'medium'}
    with patch('campaignlib.make_client',return_value=client), patch('campaignlib.call_api',return_value='Raw response'):
        with pytest.raises(ValueError,match='identity'):
            replay(load_case('phandalin-20260902/scene_01_trial_01'),tmp_path,True)
    assert (tmp_path/'response.md').read_text() == 'Raw response'
    assert json.loads((tmp_path/'run.json').read_text())['status'] == 'failed'


def test_case_manifest_reports_missing_input(tmp_path):
    path = tmp_path/'cases.json'
    path.write_text(json.dumps([{'id':'missing','draft':'missing.md','source':'source.md','references':[]}]))
    with pytest.raises(ValueError,match='Missing case input'):
        load_cases(path)


def test_all_narration_replay_paths_are_portable():
    rows = json.loads((ROOT/'fixtures/narration_replays.json').read_text())
    assert len(rows) == 17
    for row in rows:
        case = load_case(row['id'])
        for name in ['system','user','run']:
            assert case[name].is_relative_to(ROOT)
            assert case[name].is_file()


def test_historical_input_resolver_does_not_read_original_paths():
    archive = Archive()
    original = '/home/kostadis/obelisk/obelisk/voice/pip_voice.md'
    assert archive.resolve(original).is_relative_to(ROOT)
    with pytest.raises(ValueError,match='No matching'):
        archive.resolve(original, 'not-the-recorded-hash')
