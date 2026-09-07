"""Build a reading copy and a navigable comparison of all five experiments."""

import html
import json
from pathlib import Path
import re

from review_quotes import prose


ROOT = Path(__file__).resolve().parent
TRIALS = {1: "scene_01_trial_01", 2: "scene_02_trial_01", 3: "scene_03_trial_01", 4: "trial_02", 5: "scene_05_trial_01"}


def main():
    sections, options, summaries = [], [], []
    reading = ["# Narration prompt experiment — complete session", "", "Unedited experimental narrations using gpt-6-astra at medium reasoning. Scene 4 is the accepted earlier test; the other four use the same writing brief. Review findings are in all_scenes_review.md. This is a reading copy, not a replacement for the campaign's production narration.", ""]
    for scene, trial_name in TRIALS.items():
        trial = ROOT / trial_name
        run = json.loads((trial / "run.json").read_text())
        if run["status"] != "rendered":
            raise ValueError(f"Scene {scene} has not rendered")
        outputs = list(trial.glob("session_doc_scene_*.md"))
        if len(outputs) != 1:
            raise ValueError(f"Scene {scene} requires exactly one narration")
        output = outputs[0]
        original = Path(run.get("baseline_path", ROOT.parent / "narration2/session_doc_scene_04_denvar_s_room_and_unpaid_rent.md"))
        title = run.get("scene_name", "Denvar’s Room and Unpaid Rent")
        narrator = run["narrator"]
        metrics = json.loads((trial / "metrics.json").read_text())
        reading += [f"## Scene {scene}: {title}", "", re.sub(r"\A---\n.*?\n---\n", "", output.read_text(), flags=re.S).strip(), ""]
        options.append(f'<option value="{scene}">{scene}. {html.escape(narrator)} — {html.escape(title)}</option>')
        panels = []
        for key, label, path in [("original", "Original narration2", original), ("experiment", "Experimental narration", output)]:
            paragraphs = "\n".join(f"<p>{html.escape(p)}</p>" for p in prose(path).split("\n\n"))
            m = metrics[label]
            panels.append(f'<article class="{key}"><h3>{label}</h3><p class="stats">{m["words"]:,} words · {m["quoted_word_percent"]}% in quotation marks</p>{paragraphs}</article>')
        sections.append(f'<section data-scene="{scene}" {"" if scene == 1 else "hidden"}><h2>{html.escape(title)} <span>— {html.escape(narrator)}</span></h2><p class="links"><a href="{trial_name}/{output.name}">Read scene file</a> · <a href="{trial_name}/system_prompt.md">Exact prompt</a> · <a href="{trial_name}/quote_review.md">Quote comparison</a></p><div class="panels">' + "\n".join(panels) + "</div></section>")
        summaries.append({"scene": scene, "title": title, "narrator": narrator, "trial": trial_name, "output": str(output), "metrics": metrics})
    (ROOT / "all_scenes.md").write_text("\n".join(reading) + "\n")
    (ROOT / "collection.json").write_text(json.dumps(summaries, ensure_ascii=False, indent=2) + "\n")
    page = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Narration experiment — five scenes</title>
<style>
:root{color-scheme:light}body{margin:0;background:#f3f0e8;color:#282c26;font:18px/1.65 Georgia,serif}
main{max-width:1450px;padding:28px;margin:auto}h1,h2,h3,.intro,.controls,.links,.stats{font-family:system-ui,sans-serif}
h1{font-size:28px;margin:0}h2{font-size:23px}h2 span{font-weight:400}h3{font-size:18px;margin-top:0}
.intro,.links,.stats{font-size:14px}.intro{max-width:1050px}.stats{color:#5d665a;border-bottom:1px solid #dedbd0;padding-bottom:14px}
.controls{display:flex;gap:20px;flex-wrap:wrap;background:#f3f0e8;padding:14px 0;position:sticky;top:0;border-bottom:1px solid #d0cebf}
label{font-size:13px;display:grid;gap:4px}select{font:15px system-ui;padding:10px;background:#fffef9;border:1px solid #b7beae;border-radius:5px;max-width:95vw}
.panels{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}article{background:#fffef9;border:1px solid #dedbd0;border-radius:8px;padding:28px 32px}
article p{white-space:pre-wrap;margin:0 0 19px}a{color:#275540}[hidden]{display:none!important}
body[data-view="experiment"] .original,body[data-view="original"] .experiment{display:none}
body[data-view="experiment"] .panels,body[data-view="original"] .panels{grid-template-columns:minmax(0,850px);justify-content:center}
@media(max-width:850px){.panels{grid-template-columns:1fr}main{padding:14px}article{padding:22px}.controls{position:static}}
</style><body data-view="both"><main>
<h1>The voices, with room for the scene</h1>
<p class="intro">Five scenes from the September 2 session. All use the same experimental writing brief and gpt-6-astra at medium reasoning, with each narrator’s own character reference and examples. Soma is the earlier accepted test. New narrations are unedited.</p>
<p class="links"><a href="all_scenes.md">Read the whole session</a> · <a href="all_scenes_review.md">Review findings</a> · <a href="prompt.md">Writing brief</a></p>
<div class="controls"><label>Scene<select id="scene">__OPTIONS__</select></label><label>View<select id="view"><option value="both">Side by side</option><option value="experiment">Experimental narration</option><option value="original">Original narration2</option></select></label></div>
__SECTIONS__
<p class="intro">Comparison limitation: narration2 was a five-scene bundle; these tests render scenes individually. Quotation percentage describes the text and is not a quality target.</p>
</main><script>
document.querySelector('#scene').addEventListener('change',e=>{document.querySelectorAll('[data-scene]').forEach(s=>s.hidden=s.dataset.scene!==e.target.value);window.scrollTo(0,0)});
document.querySelector('#view').addEventListener('change',e=>document.body.dataset.view=e.target.value);
</script></body></html>'''
    (ROOT / "index.html").write_text(page.replace("__OPTIONS__", "\n".join(options)).replace("__SECTIONS__", "\n".join(sections)) + "\n")
    print(f"Wrote reading copy and comparison gallery for {len(summaries)} scenes")


if __name__ == "__main__":
    main()
