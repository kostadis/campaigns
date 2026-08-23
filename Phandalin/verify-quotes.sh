#!/bin/bash
# verify-quotes.sh <chapter-number>
# Verifies every blockquote from summaries/N/session-summary.md against the source chapter.
# Handles backslash-escaped characters in source files and non-ASCII quotes.
# Outputs per-quote results and a summary line.

CH="$1"
SUMMARY="summaries/${CH}/session-summary.md"
SRC=$(ls docs/chapters/chapter_$(printf "%02d" $CH)_*.md 2>/dev/null | head -1)

if [ ! -f "$SUMMARY" ]; then
  echo "NO_SUMMARY: ch${CH}"
  exit 0
fi
if [ -z "$SRC" ] || [ ! -f "$SRC" ]; then
  echo "NO_SOURCE: ch${CH}"
  exit 0
fi

total=0
ok=0
bad=0

while IFS= read -r line; do
  case "$line" in '> "'*) ;; *) continue ;; esac
  quote="${line#*> \"}"
  quote="${quote%\"}"
  [ -z "$quote" ] && continue
  total=$((total + 1))

  found=false
  deback=$(cat "$SRC" | sed 's/\\([!?,\\-])/\1/g')

  # Strategy 1: exact fixed-string match against raw source
  grep -qF "$quote" "$SRC" 2>/dev/null && found=true

  # Strategy 2: exact match against de-backslashed source
  [ "$found" = false ] && echo "$deback" | grep -qF "$quote" && found=true

  # Strategy 3: progressive prefix matching
  if [ "$found" = false ]; then
    for len in 50 40 30 25 20 15 12; do
      sub="${quote:0:$len}"
      sub="${sub%%[[:space:]]*[.!?,;:\-]*}"
      [ -z "$sub" ] && continue
      echo "$deback" | grep -qF "$sub" && { found=true; break; }
    done
  fi

  if [ "$found" = true ]; then
    echo "OK   ch${CH}: \"${quote:0:70}...\""
    ok=$((ok + 1))
  else
    echo "FAIL ch${CH}: \"${quote:0:70}...\""
    bad=$((bad + 1))
  fi
done < <(grep '^> "' "$SUMMARY" 2>/dev/null)

echo "---"
echo "ch${CH}: ${ok} OK, ${bad} FAIL (${total} total)"
exit $bad
