"""Build a read-only comparison of completed A/B/C experiment artifacts."""

import argparse
import hashlib
import html
import json
from pathlib import Path
from archive_paths import Archive, ROOT


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results',type=Path)
    parser.add_argument('--output-root',type=Path, help='New viewer directory; leaves raw results untouched')
    args=parser.parse_args()
    root=args.results.resolve()
    output = args.output_root.resolve() if args.output_root else root
    archive = Archive()
    def input_path(path, expected=None):
        if str(path) in archive.paths:
            return archive.resolve(path, expected)
        return Path(path)
    cases=json.loads((root/'cases.json').read_text())
    data={}
    summaries=[]
    sections=[]
    for case in cases:
        case_id=case['id']
        data[case_id]={'baseline':(root/case_id/'a/baseline.md').read_text()}
        cards=[]
        for arm in ['a','b','c']:
            trial=root/case_id/arm
            metadata=json.loads((trial/'run.json').read_text())
            if metadata['status']!='rendered':
                raise ValueError(f'Not complete: {case_id}/{arm}')
            response=(trial/'response.md').read_text()
            if hashlib.sha256((trial/'response.md').read_bytes()).hexdigest()!=metadata['response_sha256']:
                raise ValueError(f'Raw response has been edited: {case_id}/{arm}')
            changed=[p for p,h in metadata['input_sha256'].items()
                     if hashlib.sha256(input_path(p,h).read_bytes()).hexdigest()!=h]
            if changed:
                raise ValueError(f'Inputs changed after the test: {changed}')
            data[case_id][arm]=response
            summaries.append({'case':case_id,'approach':arm,**metadata['diagnostics'],
                              'actual_identity':metadata['actual_identity'],'changed_inputs':changed})
            d=metadata['diagnostics']
            cards.append(f'<a href="{case_id}/{arm}/response.md">{arm.upper()}: {d["edited_words"]} words</a> '
                         f'(<a href="{case_id}/{arm}/changes.diff">diff</a>, <a href="{case_id}/{arm}/system_prompt.md">prompt</a>)')
        title=html.escape(case['narrator']+' — '+case['scene'])
        source=html.escape(input_path(case['source']).read_text())
        options='<option value="baseline">Original v1 draft</option><option value="a">A — Light dialogue copyedit</option><option value="b">B — Contextual dialogue edit</option><option value="c">C — Integrated scene line edit</option>'
        sections.append(f'<section id="{case_id}"><h2>{title}</h2><p>{" · ".join(cards)}</p>'
                        f'<div class="columns"><article><select id="{case_id}-left-select" onchange="show(\'{case_id}\',\'left\')">{options}</select><div class="prose" id="{case_id}-left"></div></article>'
                        f'<article><select id="{case_id}-right-select" onchange="show(\'{case_id}\',\'right\')">{options}</select><div class="prose" id="{case_id}-right"></div></article></div>'
                        f'<details><summary>Source extraction</summary><div class="source">{source}</div></details></section>')
    payload=json.dumps(data,ensure_ascii=False).replace('<','\\u003c')
    document='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Three dialogue-editing approaches</title>
<style>body{max-width:1450px;margin:2rem auto;padding:0 1.5rem;background:#faf8f3;color:#292825;font:17px/1.55 system-ui,sans-serif}a{color:#285666}.columns{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}article{min-width:0;background:#fff;padding:1.5rem;border:1px solid #ddd8cc}.prose,.source{white-space:pre-wrap;overflow-wrap:anywhere}.prose{font:19px/1.65 Georgia,serif}.source{font:14px/1.6 system-ui,sans-serif}section{margin-top:3rem}h1{line-height:1.2}select{font:inherit;max-width:100%;margin-bottom:1.5rem;padding:.4rem}details{margin:1.5rem 0}summary{cursor:pointer}@media(max-width:850px){.columns{grid-template-columns:1fr}}</style>
<h1>Three approaches to editing the same narration</h1><p>gpt-6-astra · medium reasoning · nine independent edits of three unchanged v1 drafts. Compare any two versions using the selectors. Word counts are descriptive, not quality scores. Raw model responses are unedited.</p>
<nav><a href="#zenvon">Zenvon</a> · <a href="#vukradin">Vukradin</a> · <a href="#valphine">Valphine</a> · <a href="review.md">Review and recommendation</a> · <a href="passages.md">Selected passages</a></nav>
<p>A: only light changes inside quoted dialogue. B: contextual dialogue editing, with minimal attribution changes. C: line-edit dialogue and inner prose together.</p>
'''+''.join(sections)+f'<script>const data={payload};'+'''
function show(id,side){const choice=document.getElementById(id+'-'+side+'-select').value;document.getElementById(id+'-'+side).textContent=data[id][choice];}
for(const id of Object.keys(data)){document.getElementById(id+'-right-select').value='c';show(id,'left');show(id,'right');}
</script></html>
'''
    if output != root:
        import os
        import re
        def relocate(match):
            value = match.group(1)
            if value.startswith('#'):
                return match.group(0)
            return 'href="'+html.escape(os.path.relpath(root/value,output),quote=True)+'"'
        document = re.sub(r'href="([^"]+)"',relocate,document)
    targets={output/'index.html':document,output/'metrics.json':json.dumps(summaries,ensure_ascii=False,indent=2)+'\n'}
    if any(p.exists() for p in targets):
        raise ValueError('Comparison artifacts already exist; refusing to overwrite')
    if output == root and root.is_relative_to(ROOT):
        raise ValueError('Do not write into preserved results; choose --output-root')
    output.mkdir(parents=True,exist_ok=True)
    for path,text in targets.items():
        path.write_text(text)
    print(json.dumps(summaries,ensure_ascii=False,indent=2))
    print(f'Reader: {output/"index.html"}')


if __name__=='__main__':
    main()
