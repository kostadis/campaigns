"""Check portable reader links and inline JavaScript without a browser or model."""
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess
from urllib.parse import unquote, urlsplit

from archive_paths import ROOT


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.scripts = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for name in ['href','src']:
            if name in attributes:
                self.links.append(attributes[name])
        if tag == 'script' and 'src' not in attributes:
            self.current = []

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == 'script' and self.current is not None:
            self.scripts.append(''.join(self.current))
            self.current = None


def verify(root=ROOT/'readers'):
    node = shutil.which('node')
    links = scripts = pages = 0
    for path in sorted(Path(root).rglob('*.html')):
        page = Page()
        page.feed(path.read_text())
        pages += 1
        for target in page.links:
            url = urlsplit(target)
            if url.scheme or not url.path:
                continue
            if not (path.parent/unquote(url.path)).exists():
                raise ValueError(f'Broken local link: {path}: {target}')
            links += 1
        for script in page.scripts:
            if node:
                subprocess.run([node,'--check'],input=script,text=True,check=True,capture_output=True)
                scripts += 1
    return {'readers':pages,'local_file_links':links,
            'javascript_checked':scripts if node else 'not checked: node unavailable'}


if __name__ == '__main__':
    print(json.dumps(verify(),indent=2))
