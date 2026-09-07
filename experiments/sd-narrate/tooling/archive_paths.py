"""Resolve historical input names inside the relocated, immutable archive."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Archive:
    def __init__(self, root=ROOT):
        self.root = Path(root).resolve()
        self.manifest = json.loads((self.root/'relocation_manifest.json').read_text())
        self.paths = {}
        for record in self.manifest['files']:
            self.paths.setdefault(record['original'], []).append(record)

    def resolve(self, historical_path, expected=None):
        records = self.paths.get(str(historical_path), [])
        if expected is not None:
            records = [r for r in records if r['sha256'] == expected]
        if not records:
            raise ValueError(f'No matching archived input: {historical_path}')
        path = (self.root/records[0]['path']).resolve()
        if not path.is_relative_to(self.root):
            raise ValueError(f'Archive path escapes root: {path}')
        if digest(path) != records[0]['sha256']:
            raise ValueError(f'Archived input has changed: {path}')
        return path

    def verify(self):
        for record in self.manifest['files']:
            path = (self.root/record['path']).resolve()
            if not path.is_relative_to(self.root) or digest(path) != record['sha256']:
                raise ValueError(f'Archive integrity failure: {record["path"]}')
        counts = {}
        for check in self.manifest['input_checks']:
            actual = digest(self.root/check['path']) if check['path'] else None
            if actual != check['snapshot_sha256']:
                raise ValueError(f'Snapshot changed: {check["path"]}')
            state = ('matched' if actual == check['recorded_sha256'] else
                     'missing' if actual is None else 'historical-version-unavailable')
            if state != check['status']:
                raise ValueError(f'Input ledger disagrees: {check["run"]}')
            counts[state] = counts.get(state, 0) + 1
        return {'preserved_files':len(self.manifest['files']), 'input_checks':counts}


if __name__ == '__main__':
    print(json.dumps(Archive().verify(), indent=2))
