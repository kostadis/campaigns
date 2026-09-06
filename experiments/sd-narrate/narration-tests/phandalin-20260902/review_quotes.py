"""Produce source-aligned quote diagnostics for an experimental narration.

This is a reading aid, not a semantic verdict. Punctuation and capitalization
are ignored for lexical matching. A match proves supplied words, not the right
speaker, timing, or fictional meaning. Missing quotes can be intentional edits.
"""

import argparse
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
QUOTE = re.compile(r'"([^"\n]+)"|“([^”\n]+)”')


def spans(text):
    return [m.group(1) or m.group(2) for m in QUOTE.finditer(text)]


def normalized(text):
    return " ".join(re.findall(r"[\w]+(?:['’][\w]+)*", text.casefold().replace("’", "'")))


def prose(path):
    text = path.read_text()
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"^#+ .*\n", "", text, flags=re.M).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trial", type=Path)
    args = parser.parse_args()
    trial = args.trial.resolve()
    paths = list(trial.glob("session_doc_scene_*.md"))
    if len(paths) != 1:
        parser.error("trial must contain exactly one scene narration")
    metadata = json.loads((trial / "run.json").read_text())
    source_path = Path(metadata.get("source_path", ROOT.parent / "scene_extractions_smoothed/04_the_stakeout_of_denvar.md"))
    baseline_path = Path(metadata.get("baseline_path", ROOT.parent / "narration2/session_doc_scene_04_denvar_s_room_and_unpaid_rent.md"))
    title = f'Scene {metadata["scene"]}: {metadata.get("scene_name", "Denvar’s Room and Unpaid Rent")}'
    source = []
    speaker, context = "", ""
    for line in source_path.read_text().split("## Voiced moments", 1)[1].splitlines():
        match = re.match(r"\*\*(.*?)\*\*\s*—\s*\*(.*?)\*", line)
        if match:
            speaker, context = match.groups()
        if line.startswith(">"):
            for quote in spans(line):
                source.append({"speaker": speaker, "context": context, "quote": quote, "norm": normalized(quote)})

    metrics, reports = {}, ["# Quote comparison\n", "Lexical matches allow punctuation and capitalization changes. They do not verify speaker, timing, or meaning. Missing lines may be deliberate editorial choices.\n"]
    for label, path in [("Original narration2", baseline_path), ("Experimental narration", paths[0])]:
        text = prose(path)
        quotes = spans(text)
        words = len(normalized(text).split())
        quote_words = sum(len(normalized(q).split()) for q in quotes)
        matches = []
        for quote in quotes:
            norm = normalized(quote)
            candidates = [q for q in source if norm == q["norm"] or f" {norm} " in f" {q['norm']} "]
            matches.append(candidates)
        repeated = [quotes[i] for i in range(1, len(quotes)) if normalized(quotes[i]) == normalized(quotes[i - 1])]
        metrics[label] = {
            "path": str(path), "words": words, "quoted_words": quote_words,
            "unquoted_words": words - quote_words, "quoted_word_percent": round(quote_words / words * 100, 1),
            "quote_spans": len(quotes), "lexically_matched_quote_spans": sum(bool(m) for m in matches),
            "consecutive_identical_quotes": repeated,
            "unmatched_quotes": [q for q, m in zip(quotes, matches) if not m],
        }
        reports += [f"## {label}\n", "| Output quotation | Source speaker(s) | Match |", "|---|---|---|"]
        for quote, candidates in zip(quotes, matches):
            names = ", ".join(dict.fromkeys(q["speaker"] for q in candidates)) or "—"
            exact = any(normalized(quote) == q["norm"] for q in candidates)
            kind = "full line" if exact else ("contiguous excerpt" if candidates else "REVIEW")
            reports.append(f"| {quote.replace('|', '&#124;')} | {names} | {kind} |")
        reports.append("")

    experimental = [normalized(q) for q in spans(prose(paths[0]))]
    reports += ["## Source lines not reproduced in full in the experiment\n", "These may be partly quoted, have become narration, been omitted as incidental, or lost meaningful voice. Read them in context. Repeated identical source lines cannot be distinguished by this lexical check.\n", "| Speaker | Context | Source quotation |", "|---|---|---|"]
    for q in source:
        if not any(n == q["norm"] or f" {q['norm']} " in f" {n} " for n in experimental):
            reports.append(f"| {q['speaker']} | {q['context']} | {q['quote'].replace('|', '&#124;')} |")
    (trial / "quote_review.md").write_text("\n".join(reports) + "\n")
    (trial / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n")
    panels = []
    for label, path in [("Original narration2", baseline_path), ("Experimental narration", paths[0])]:
        paragraphs = "\n".join("<p>" + html.escape(p) + "</p>" for p in prose(path).split("\n\n"))
        m = metrics[label]
        panels.append(f'<article><header><h2>{label}</h2><p>{m["words"]:,} words · {m["quoted_word_percent"]}% in quotation marks</p></header>{paragraphs}</article>')
    comparison = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>__SCENE_TITLE__ — narration prompt comparison</title>
<style>
body{margin:0;background:#f4f1e9;color:#272924;font:18px/1.65 Georgia,serif}
main{max-width:1450px;margin:auto;padding:30px}h1,h2,header,p.note{font-family:system-ui,sans-serif}
h1{font-size:27px;margin-bottom:8px}p.note{font-size:14px;max-width:1000px}
.panels{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:start}
article{background:#fffef9;padding:28px 32px;border:1px solid #d8d5cb;border-radius:8px}
article header{border-bottom:1px solid #d8d5cb;margin-bottom:24px}header p{font-size:13px;color:#596256}
h2{font-size:19px}article>p{white-space:pre-wrap;margin:0 0 20px}a{color:#285244}
@media(max-width:850px){.panels{grid-template-columns:1fr}main{padding:15px}article{padding:20px}}
</style><main><h1>__SCENE_TITLE__</h1>
<p class="note">__NARRATOR__ · __MODEL__ · __EFFORT__ reasoning. Compare the players’ voices, setting, action, and speaker clarity. Quotation percentage is descriptive, not a quality score.</p>
<p class="note">The original was part of a five-scene bundle; the experiment renders this scene alone. The output below has not been hand-edited. <a href="system_prompt.md">Test prompt</a> · <a href="quote_review.md">Quote review</a></p>
<div class="panels">''' + "\n".join(panels) + "</div></main></html>\n"
    comparison = comparison.replace("__SCENE_TITLE__", html.escape(title)).replace("__NARRATOR__", html.escape(metadata["narrator"]))
    comparison = comparison.replace("__MODEL__", html.escape(metadata["model"])).replace("__EFFORT__", html.escape(metadata["reasoning_effort"]))
    (trial / "comparison.html").write_text(comparison)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
