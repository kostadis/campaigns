"""Make portable HTML copies without modifying any historical reader or prose."""
import argparse
import html
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from archive_paths import Archive


def build(output):
    archive = Archive()
    output = Path(output).resolve()
    if output.exists():
        raise ValueError('Choose a new reader output directory')
    documents = [r for r in archive.manifest['files'] if r['path'].endswith('.html')]
    destinations = {r['original']:output/r['path'] for r in documents}
    rendered = []
    missing = []
    for record in documents:
        destination = destinations[record['original']]
        def replace(match):
            value = html.unescape(match.group(2))
            url = urlsplit(value)
            if not url.path or (url.scheme and url.scheme != 'file'):
                return match.group(0)
            old = str((Path(record['original']).parent/unquote(url.path)).resolve())
            if old not in archive.paths:
                missing.append({'reader':record['path'],'target':value})
                return match.group(0)
            new = destinations.get(old) or archive.resolve(old)
            relative = os.path.relpath(new,destination.parent)
            if url.query:
                relative += '?'+url.query
            if url.fragment:
                relative += '#'+url.fragment
            return match.group(1)+'="'+html.escape(relative,quote=True)+'"'
        original = (archive.root/record['path']).read_text()
        document = re.sub(r'(href|src)=["\']([^"\']+)["\']',replace,original)
        rendered.append((destination,document))
    if missing:
        raise ValueError('Unresolved reader links: '+json.dumps(missing,indent=2))
    for destination,document in rendered:
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_text(document)
    return {'portable_readers':len(rendered),'unresolved_links':0}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output',type=Path)
    print(json.dumps(build(parser.parse_args().output),indent=2))
