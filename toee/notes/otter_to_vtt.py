#!/usr/bin/env python3
"""Convert an Otter-style closed-caption .txt to Zoom-style WebVTT.

Otter format:
    [Speaker Name] HH:MM:SS
    dialogue line 1
    dialogue line 2

    [Other Speaker] HH:MM:SS
    ...

Zoom VTT format (what vtt-spell-pass expects):
    WEBVTT

    1
    00:00:01.000 --> 00:00:05.000
    Speaker Name: dialogue line 1 dialogue line 2

Usage:
    python otter_to_vtt.py <input.txt> <output.vtt>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HEADER_RE = re.compile(r"^\[(?P<speaker>[^\]]+)\]\s+(?P<ts>\d{1,2}:\d{2}(?::\d{2})?)\s*$")


def parse(text: str) -> list[tuple[str, str, str]]:
    """Returns list of (speaker, timestamp_hhmmss, joined_dialogue)."""
    blocks = []
    cur_speaker = None
    cur_ts = None
    cur_lines: list[str] = []
    for raw in text.splitlines():
        m = HEADER_RE.match(raw)
        if m:
            if cur_speaker is not None and cur_lines:
                blocks.append((cur_speaker, cur_ts, " ".join(cur_lines).strip()))
            cur_speaker = m.group("speaker").strip()
            cur_ts = m.group("ts")
            if cur_ts.count(":") == 1:
                cur_ts = "00:" + cur_ts
            cur_lines = []
            continue
        if raw.strip():
            cur_lines.append(raw.strip())
    if cur_speaker is not None and cur_lines:
        blocks.append((cur_speaker, cur_ts, " ".join(cur_lines).strip()))
    return blocks


def hms_to_seconds(hms: str) -> int:
    h, m, s = (int(x) for x in hms.split(":"))
    return h * 3600 + m * 60 + s


def fmt_ts(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}.000"


def render_vtt(blocks: list[tuple[str, str, str]]) -> str:
    out = ["WEBVTT", ""]
    for i, (speaker, ts, dialogue) in enumerate(blocks, 1):
        start_s = hms_to_seconds(ts)
        end_s = start_s + 3  # arbitrary, doesn't matter for spell-pass
        out.append(str(i))
        out.append(f"{fmt_ts(start_s)} --> {fmt_ts(end_s)}")
        out.append(f"{speaker}: {dialogue}")
        out.append("")
    return "\n".join(out)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    src = Path(argv[1])
    dst = Path(argv[2])
    blocks = parse(src.read_text(encoding="utf-8"))
    dst.write_text(render_vtt(blocks), encoding="utf-8")
    print(f"Wrote {dst}  ({len(blocks)} blocks)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
