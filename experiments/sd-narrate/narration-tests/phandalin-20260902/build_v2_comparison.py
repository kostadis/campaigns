"""Assemble the three unedited v2 drafts beside their immediate v1 baselines."""

import argparse
import html
import json
from pathlib import Path
import re

from review_quotes import prose

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compare-effort", action="store_true", help="Compare identical v2 prompts at medium and high")
    args = parser.parse_args()
    effort = args.compare_effort
    page_name = "astra_effort_comparison" if effort else "v2_comparison"
    reading_name = "astra_high_scenes.md" if effort else "v2_scenes.md"
    review_name = "astra_high_review.md" if effort else "v2_review.md"
    labels = ["v2 / medium reasoning", "v2 / high reasoning"] if effort else ["Previous experiment (v1)", "Revised prompt (v2)"]
    title = "Vukradin and Valphine: Astra medium / high" if effort else "Vukradin and Valphine: prompt v1 / v2"
    intro = ("Byte-identical v2 system and user prompts, including source payloads, character references, and examples. Same text-only backend and model (gpt-6-astra). Only requested reasoning effort changes from medium to high. One generation per scene per condition; all drafts are unedited. Percentages describe the text, not a quality target." if effort else "Same source payloads, character references, examples, text-only backend, model (gpt-6-astra), and reasoning (medium). The revision changes the writing brief and resolves the genre reference's tense conflict. One generation per scene; all drafts are unedited. Percentages describe the text, not a quality target.")
    sections, options, collection = [], [], []
    reading = [
        "# " + title,
        "",
        f"One unedited gpt-6-astra {'high' if effort else 'medium'} generation per scene. [Side-by-side comparison]({page_name}.html), [review findings]({review_name}), and [tested prompt](prompt_v2.md). These are test drafts, not replacements for production narration.",
        "",
    ]
    for n in [1, 2, 3]:
        paths = ([ROOT / f"v2_scene_{n:02d}_trial_01", ROOT / f"v2_high_scene_{n:02d}_trial_01"] if effort else [ROOT / f"scene_{n:02d}_trial_01", ROOT / f"v2_scene_{n:02d}_trial_01"])
        panels, scene_stats = [], {}
        run = json.loads((paths[1] / "run.json").read_text())
        assert run["status"] == "rendered", f"Scene {n} not rendered"
        scene_title = f"Scene {n}: {run['scene_name']} — {run['narrator']}"
        for key, label, trial in zip(["v1", "v2"], labels, paths):
            outputs = list(trial.glob("session_doc_scene_*.md"))
            assert len(outputs) == 1
            output = outputs[0]
            stats = json.loads((trial / "metrics.json").read_text())["Experimental narration"]
            scene_stats[key] = stats
            body = "\n".join(f"<p>{html.escape(p)}</p>" for p in prose(output).split("\n\n"))
            links = f'<a href="{trial.name}/{output.name}">Scene file</a> · <a href="{trial.name}/system_prompt.md">Exact prompt</a> · <a href="{trial.name}/quote_review.md">Source quote check</a>'
            panels.append(f'<article class="{key}"><h3>{label}</h3><p class="stats">{stats["words"]:,} words · {stats["quoted_word_percent"]}% quoted</p><p class="links">{links}</p>{body}</article>')
            if key == "v2":
                reading += [f"## Scene {n}: {run['scene_name']}", "", re.sub(r"\A---\n.*?\n---\n", "", output.read_text(), flags=re.S).strip(), ""]
        options.append(f'<option value="{n}">{html.escape(scene_title)}</option>')
        sections.append(f'<section data-scene="{n}" {"" if n == 1 else "hidden"}><h2>{html.escape(scene_title)}</h2><div class="panels">' + "\n".join(panels) + "</div></section>")
        if effort:
            scene_stats = {"medium": scene_stats["v1"], "high": scene_stats["v2"]}
        collection.append({"scene": n, "narrator": run["narrator"], "title": run["scene_name"], "metrics": scene_stats})
    page = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
body{margin:0;background:#f3f0e8;color:#282c26;font:18px/1.65 Georgia,serif}main{max-width:1450px;margin:auto;padding:28px}
h1,h2,h3,.intro,.controls,.links,.stats{font-family:system-ui,sans-serif}h1{font-size:28px}h2{font-size:22px}h3{font-size:19px}
.intro,.stats,.links{font-size:14px}.stats{color:#5d665a}.controls{display:flex;gap:20px;flex-wrap:wrap;padding:14px 0;position:sticky;top:0;background:#f3f0e8;border-bottom:1px solid #ccc}
label{display:grid;font-size:13px;gap:4px}select{font:15px system-ui;padding:10px;max-width:92vw;background:#fffef9;border:1px solid #bbb;border-radius:5px}
.panels{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}article{padding:28px 32px;background:#fffef9;border:1px solid #dedbd0;border-radius:8px}
article>p{white-space:pre-wrap;margin:0 0 19px}a{color:#275540}[hidden]{display:none!important}
body[data-view="v2"] .v1,body[data-view="v1"] .v2{display:none}body[data-view="v1"] .panels,body[data-view="v2"] .panels{grid-template-columns:minmax(0,850px);justify-content:center}
@media(max-width:850px){.panels{grid-template-columns:1fr}main{padding:14px}article{padding:22px}.controls{position:static}}
</style><body data-view="both"><main><h1>__TITLE__</h1>
<p class="intro">__INTRO__</p>
<p class="links"><a href="__READING__">Read the new scenes</a> · <a href="__REVIEW__">Review findings</a> · <a href="prompt_v2.md">Tested brief</a> · <a href="v2_proposal.md">Prompt rationale</a> · <a href="index.html">Earlier narration2 / v1 comparison</a></p>
<div class="controls"><label>Scene<select id="scene">__OPTIONS__</select></label><label>View<select id="view"><option value="both">Side by side</option><option value="v2">__NEW_LABEL__</option><option value="v1">__OLD_LABEL__</option></select></label></div>
__SECTIONS__
<p class="intro">This is a three-scene qualitative test, not a statistical comparison. It does not retest Brewbarry or Soma.</p>
</main><script>
document.querySelector('#scene').addEventListener('change',e=>{document.querySelectorAll('[data-scene]').forEach(s=>s.hidden=s.dataset.scene!==e.target.value);window.scrollTo(0,0)});
document.querySelector('#view').addEventListener('change',e=>document.body.dataset.view=e.target.value);
</script></body></html>'''
    replacements = {"__TITLE__": html.escape(title), "__INTRO__": html.escape(intro), "__READING__": reading_name, "__REVIEW__": review_name, "__OLD_LABEL__": html.escape(labels[0]), "__NEW_LABEL__": html.escape(labels[1]), "__OPTIONS__": "\n".join(options), "__SECTIONS__": "\n".join(sections)}
    for placeholder, value in replacements.items():
        page = page.replace(placeholder, value)
    (ROOT / reading_name).write_text("\n".join(reading) + "\n")
    (ROOT / f"{page_name}.json").write_text(json.dumps(collection, ensure_ascii=False, indent=2) + "\n")
    (ROOT / f"{page_name}.html").write_text(page + "\n")
    print(f"Wrote {page_name} for scenes 1, 2, and 3")


if __name__ == "__main__":
    main()
