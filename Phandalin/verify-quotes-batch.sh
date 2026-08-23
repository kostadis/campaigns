#!/bin/bash
# verify-quotes-batch.sh <start_ch> <end_ch>
# For each chapter, check every blockquote against the source.
# Uses single-digit dir names (summaries/2/, summaries/10/)

BASEDIR=~/src/campaigns/Phandalin
cd "$BASEDIR"

problems=""
total_ok=0
total_problems=0

for ch in $(seq "$1" "$2"); do
  summary="summaries/${ch}/session-summary.md"
  src=$(ls docs/chapters/chapter_$(printf "%02d" $ch)_*.md 2>/dev/null | head -1)

  if [ ! -f "$summary" ]; then
    echo "SKIP: ch${ch} (no summary)"
    continue
  fi
  if [ -z "$src" ] || [ ! -f "$src" ]; then
    echo "SKIP: ch${ch} (no source)"
    continue
  fi

  ch_ok=0
  ch_problems=0
  
  while IFS= read -r quote; do
    [ -z "$quote" ] && continue
    
    found=false
    for keylen in 50 40 30 20 15; do
      key=$(echo "$quote" | grep -oP ".{$keylen,}" | head -1)
      [ -z "$key" ] && continue
      if grep -qF "$key" "$src" 2>/dev/null; then
        found=true
        break
      fi
    done
    
    if [ "$found" = false ]; then
      # Try without backslash-escaped chars
      cleaned=$(echo "$quote" | sed 's/\\//g')
      for keylen in 50 40 30 20 15; do
        key=$(echo "$cleaned" | grep -oP ".{$keylen,}" | head -1)
        [ -z "$key" ] && continue
        if grep -qF "$key" "$src" 2>/dev/null; then
          found=true
          break
        fi
      done
    fi
    
    if [ "$found" = true ]; then
      ch_ok=$((ch_ok + 1))
    else
      echo "PROBLEM: ch${ch} — \"${quote:0:80}...\""
      ch_problems=$((ch_problems + 1))
    fi
  done < <(grep -oP '(?<=^> ").*(?=")' "$summary" 2>/dev/null)

  echo "ch${ch}: ${ch_ok} OK, ${ch_problems} PROBLEMS"
  total_ok=$((total_ok + ch_ok))
  total_problems=$((total_problems + ch_problems))
done

echo ""
echo "=== FINAL: ${total_ok} quotes OK, ${total_problems} problems across ch$1-ch$2 ==="
exit $total_problems
