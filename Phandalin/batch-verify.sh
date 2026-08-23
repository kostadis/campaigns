#!/bin/bash
# batch-verify.sh <start> <end>
# Verifies all blockquotes in summary files against source chapter docs.
# Also detects "invented dialogue" patterns where summaries have blockquotes
# but the source is entirely third-person narrative with no direct speech.
#
# Usage: bash batch-verify.sh <start> <end>

BASEDIR=~/src/campaigns/Phandalin
cd "$BASEDIR" || exit 1

total_ok=0
total_fail=0
total_chapters=0
invented_alerts=0

for ch in $(seq "$1" "$2"); do
  summary="summaries/${ch}/session-summary.md"
  src=$(ls docs/chapters/chapter_$(printf "%02d" $ch)_*.md 2>/dev/null | head -1)

  [ ! -f "$summary" ] && continue
  [ -z "$src" ] || [ ! -f "$src" ] && continue

  total_chapters=$((total_chapters + 1))
  ch_ok=0
  ch_fail=0

  # --- Count source quotes for invented-dialogue detection ---
  curly=$(grep -oP '“[^”]{4,}”' "$src" 2>/dev/null | wc -l)
  straight=$(grep -oP '"[^"]{4,}"' "$src" 2>/dev/null | wc -l)
  src_qcount=$((curly + straight))

  # Count summary blockquotes
  sum_qcount=0
  while IFS= read -r line; do
    case "$line" in '> "'*) sum_qcount=$((sum_qcount + 1)) ;; esac
  done < "$summary"

  # Alert if summary has blockquotes but source has very few quoted phrases
  if [ "$sum_qcount" -gt 2 ] && [ "$src_qcount" -lt 3 ]; then
    echo "INVENTED_WARNING ch${ch}: ${sum_qcount} blockquotes in summary, only ${src_qcount} quoted phrases in source!"
    invented_alerts=$((invented_alerts + 1))
  fi

  # --- Verify each blockquote ---
  while IFS= read -r line; do
    case "$line" in '> "'*) ;; *) continue ;; esac
    quote="${line#*> \"}"
    quote="${quote%\"}"
    [ -z "$quote" ] && continue

    found=false
    # Build de-backslashed source content
    deback=$(cat "$src" | sed 's/\\\([!?,\\-]\|!\)/\1/g' 2>/dev/null)

    # Strategy 1: exact match against raw source
    grep -qF "$quote" "$src" 2>/dev/null && found=true

    # Strategy 2: exact match against de-backslashed source
    if [ "$found" = false ]; then
      echo "$deback" | grep -qF "$quote" && found=true
    fi

    # Strategy 3: strip curly quotes from source and try matching straight quotes
    if [ "$found" = false ]; then
      decurly=$(python3 -c "import sys; print(sys.stdin.read().replace('\u201c', '\"').replace('\u201d', '\"'))" < "$src" 2>/dev/null)
      echo "$decurly" | grep -qF "$quote" && found=true
    fi

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
      ch_ok=$((ch_ok + 1))
    else
      echo "FAIL ch${ch}: \"${quote:0:80}...\""
      ch_fail=$((ch_fail + 1))
    fi
  done < <(grep '^> "' "$summary" 2>/dev/null)

  echo "ch${ch}: ${ch_ok} OK, ${ch_fail} FAIL (source: ${src_qcount} quotes, summary: ${sum_qcount} blockquotes)"
  total_ok=$((total_ok + ch_ok))
  total_fail=$((total_fail + ch_fail))
done

echo ""
echo "=== FINAL ==="
echo "Chapters scanned: ${total_chapters}"
echo "Quotes OK: ${total_ok}"
echo "Quotes FAIL: ${total_fail}"
echo "Invented-dialogue alerts: ${invented_alerts}"
echo ""
echo "RULES:"
echo "  INVENTED_WARNING = summary has >2 blockquotes but source <3 quoted phrases"
echo "  Likely third-person narrative source; blockquotes may be invented."
echo "  Replace with descriptive text."
exit $total_fail
