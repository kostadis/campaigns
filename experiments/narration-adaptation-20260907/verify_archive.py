"""Read-only, offline verification of the archived narration experiments."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
FIRST = ROOT / 'experiments/20260907-phandalin-adaptation'
SECOND = ROOT / 'experiments/20260907-phandalin-scene-composition'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text())


def check_case(folder):
    case = read_json(folder / 'case.json')
    for relative, expected in case['input_sha256'].items():
        target = (folder / relative).resolve()
        require(target.is_relative_to(folder.resolve()), f'Unsafe manifest path: {relative}')
        require(sha(target.read_bytes()) == expected, f'Frozen input changed: {target}')
    return case


def check_run(folder, case_folder, case):
    run = read_json(folder / 'run.json')
    require(run['status'] == 'rendered', f'Incomplete run: {folder}')
    require(run['case_sha256'] == sha((case_folder / 'case.json').read_bytes()), 'Case hash changed')
    require(run['response_sha256'] == sha((folder / 'response.md').read_bytes()), 'Response changed')
    identity = run['actual_identity']
    require(identity['model'] == case['model'] == 'gpt-6-astra', 'Model selection differs')
    require(identity['codex_reasoning_effort'] == case['reasoning_effort'] == 'medium', 'Effort differs')
    require(identity['backend'] == 'codex-cli', 'Backend differs')
    return run


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.articles = 0

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if 'id' in attributes:
            self.ids.add(attributes['id'])
        if tag == 'a' and 'href' in attributes:
            self.links.append(attributes['href'])
        if tag == 'article':
            self.articles += 1


def check_reader(folder, expected_articles):
    parser = Links()
    parser.feed((folder / 'comparison.html').read_text())
    require(parser.articles == expected_articles, 'Wrong number of comparison panels')
    for link in parser.links:
        parts = urlsplit(link)
        require(not parts.scheme and not parts.netloc, f'Unexpected external reader link: {link}')
        if parts.path:
            target = (folder / unquote(parts.path)).resolve()
            require(target.is_relative_to(ROOT) and target.is_file(), f'Broken local reader link: {link}')
        elif parts.fragment:
            require(unquote(parts.fragment) in parser.ids, f'Broken reader anchor: {link}')
    return len(parser.links)


def verify():
    first_case = check_case(FIRST)
    second_case = check_case(SECOND)
    check_run(FIRST, FIRST, first_case)
    runs = {arm: check_run(SECOND / arm, SECOND, second_case)
            for arm in ('control', 'composition')}
    user_hash = sha((SECOND / 'user_prompt.md').read_bytes())
    for arm, run in runs.items():
        require(run['user_sha256'] == user_hash, 'A/B user inputs differ')
        require(run['system_sha256'] == sha((SECOND / arm / 'system_prompt.md').read_bytes()), 'System changed')
    control = (SECOND / 'control/system_prompt.md').read_text()
    composition = (SECOND / 'composition/system_prompt.md').read_text()
    old_blocks = [p for p in control.split('\n\n') if p.startswith('Compose complete scenes with')]
    require(len(old_blocks) == 1, 'Cannot identify control composition block')
    new_block = (SECOND / 'composition_block.md').read_text().strip()
    require(composition.count(new_block) == 1, 'Cannot identify treatment block')
    require(composition.replace(new_block, old_blocks[0], 1) == control, 'More than one prompt block changed')
    key_file = SECOND / 'assignment.json'
    require(sha(key_file.read_bytes()) == second_case['assignment_sha256'], 'Assignment changed')
    assignment = read_json(key_file)
    require(set(assignment) == {'A', 'B'} and set(assignment.values()) == {'control', 'composition'}, 'Invalid assignment')
    for label, arm in assignment.items():
        require((SECOND / f'version-{label}.md').read_bytes() == (SECOND / arm / 'response.md').read_bytes(), 'Anonymous copy differs')
    require((SECOND / 'inputs/parent_case.json').read_bytes() == (FIRST / 'case.json').read_bytes(), 'Parent provenance differs')
    require((SECOND / 'inputs/source.md').read_bytes() == (FIRST / 'inputs/Phandalin/summaries/20260902/scene_extractions_smoothed/05_the_dead_drop_at_the_house_of_a_thousand_faces.md').read_bytes(), 'A/B scene source differs from parent')
    require(sha((SECOND / 'blind_review.md').read_bytes()) == '78b5f89762e0b7b8d40ee91548bc21455465553361eb947bfa8fb740667a555d', 'Pre-reveal notes changed')
    links = check_reader(FIRST, 10) + check_reader(SECOND, 2)
    return {
        'status': 'verified', 'frozen_input_entries_checked': len(first_case['input_sha256']) + len(second_case['input_sha256']),
        'completed_generation_runs': 3, 'raw_responses_unchanged': True,
        'actual_model_and_effort': 'gpt-6-astra / medium',
        'single_composition_block_difference': True, 'shared_ab_user_message': True,
        'anonymous_copies_match_raw': True, 'pre_reveal_notes_unchanged': True,
        'local_html_links_checked': links, 'network_calls': 0, 'model_calls': 0,
        'scope': 'File integrity and experiment isolation only; not semantic certification.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, help='Write a new report file; refuses overwrite')
    args = parser.parse_args()
    result = json.dumps(verify(), indent=2) + '\n'
    if args.report:
        with args.report.open('x') as report:
            report.write(result)
    print(result, end='')
