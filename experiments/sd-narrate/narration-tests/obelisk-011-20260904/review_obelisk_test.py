"""Non-mutating source/quote diagnostics; optionally build an isolated reader."""

import argparse
import hashlib
import html
import json
from pathlib import Path
import re

ROOT = Path('/home/kostadis/obelisk/obelisk/summaries/011-20260904/narration_prompt_test')
QUOTE = re.compile(r'"([^"\n]+)"|“([^”\n]+)”')


def quotes(text):
    return [m.group(1) or m.group(2) for m in QUOTE.finditer(text)]


def normalized(text):
    return re.sub(r'[^\w]+', ' ', text.casefold().replace('’', "'")).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reader', action='store_true')
    args = parser.parse_args()
    sections = []
    results = []
    for scene in [1, 3]:
        trial = ROOT / f'v1_voices_scene_{scene:02d}_trial_01'
        metadata = json.loads((trial/'run.json').read_text())
        paths = list(trial.glob('session_doc_scene_*.md'))
        if metadata['status'] != 'rendered' or len(paths) != 1:
            raise ValueError(f'Scene {scene} has not finished successfully')
        source = Path(metadata['source_path']).read_text()
        draft = paths[0].read_text()
        draft = re.sub(r'\A---\n.*?\n---\n', '', draft, count=1, flags=re.S).strip()
        source_quotes = [normalized(q) for q in quotes(source)]
        draft_quotes = quotes(draft)
        joined_source = ' '.join(source_quotes)
        flags = []
        for quote in draft_quotes:
            value = normalized(quote)
            if any(value in source_quote for source_quote in source_quotes):
                continue
            flags.append({'quote':quote, 'match':'joined source spans' if value in joined_source else 'manual review'})
        duplicates = [b for a,b in zip(draft_quotes,draft_quotes[1:]) if normalized(a)==normalized(b)]
        changed = [path for path,digest in metadata['input_sha256'].items()
                   if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=digest]
        result = {'scene':scene,'output':str(paths[0]),'words':len(draft.split()),
                  'quoted_words':sum(len(q.split()) for q in draft_quotes),
                  'quote_spans':len(draft_quotes),'quote_flags':flags,
                  'consecutive_duplicate_quotes':duplicates,'changed_inputs':changed}
        print(json.dumps(result,ensure_ascii=False,indent=2))
        results.append(result)
        title = html.escape(metadata['scene_name'])
        link = html.escape(str(paths[0].relative_to(ROOT)))
        sections.append(f'<section id="scene{scene}"><h2>Scene {scene}: {title}</h2>'
                        f'<p><a href="{link}">Raw narration</a> · {result["words"]} words</p>'
                        f'<div class="columns"><article><h3>Narration — Zenvon Forepot</h3><div class="prose">{html.escape(draft)}</div></article>'
                        f'<article><h3>Source extraction</h3><div class="source">{html.escape(source)}</div></article></div></section>')
    if args.reader:
        document = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Obelisk scenes 1 and 3 — v1 narration test</title>
<style>body{max-width:1450px;margin:2rem auto;padding:0 1.5rem;background:#faf8f3;color:#292825;font:17px/1.55 system-ui,sans-serif}a{color:#285666}.columns{display:grid;grid-template-columns:1fr 1fr;gap:2rem}article{min-width:0;background:#fff;padding:1.5rem;border:1px solid #ddd8cc}.prose,.source{white-space:pre-wrap;overflow-wrap:anywhere}.prose{font:19px/1.65 Georgia,serif}.source{font:14px/1.6 system-ui,sans-serif}section{margin-top:3rem}h1{line-height:1.2}h3{margin-top:0}@media(max-width:850px){.columns{grid-template-columns:1fr}}</style>
<h1>Obelisk: v1 narration test</h1><p>gpt-6-astra · medium reasoning · Zenvon POV · all four party voice notes supplied, including the confirmed Veyra and Pip notes. The accepted v1 writing brief is unchanged. These are unedited test drafts, not promoted campaign narration.</p>
<nav><a href="#scene1">Scene 1</a> · <a href="#scene3">Scene 3</a> · <a href="review.md">Review</a> · <a href="prompt_v1.md">Writing brief</a></nav>
'''+('<details><summary>Read the review</summary><div class="source">'+html.escape((ROOT/'review.md').read_text())+'</div></details>' if (ROOT/'review.md').exists() else '')+''.join(sections)+'</html>\n'
        target = ROOT/'obelisk_test_reader.html'
        diagnostics = ROOT/'quote_review.json'
        if target.exists() or diagnostics.exists():
            raise ValueError('Reader already exists; refusing to overwrite')
        target.write_text(document)
        diagnostics.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
        print(f'Reader: {target}')


if __name__ == '__main__':
    main()
