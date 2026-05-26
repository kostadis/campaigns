#!/usr/bin/env bash
# Delete files older than a given age. Dry-run by default.
#
# Usage:
#   delete-older-than.sh <dir> <age> [--delete] [--time mtime|atime|ctime]
#                                    [--include-dirs] [--glob PATTERN]
#
# <age> accepts: Nm (minutes), Nh (hours), Nd (days), Nw (weeks)
#
# Examples:
#   delete-older-than.sh ~/tmp 30d                   # preview .* (mtime > 30 days)
#   delete-older-than.sh ~/tmp 30d --delete          # actually delete
#   delete-older-than.sh ~/logs 2h --glob '*.log'    # preview matching files
#   delete-older-than.sh ~/cache 1w --time atime --delete

set -euo pipefail

usage() {
  sed -n '2,15p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-1}"
}

[[ ${1:-} == -h || ${1:-} == --help ]] && usage 0
[[ $# -lt 2 ]] && usage

dir=$1
age=$2
shift 2

delete=0
time_field=mtime
include_dirs=0
glob=

while [[ $# -gt 0 ]]; do
  case $1 in
    --delete) delete=1 ;;
    --time)
      time_field=$2
      shift
      [[ $time_field =~ ^(mtime|atime|ctime)$ ]] || { echo "bad --time: $time_field" >&2; exit 2; }
      ;;
    --include-dirs) include_dirs=1 ;;
    --glob) glob=$2; shift ;;
    -h|--help) usage 0 ;;
    *) echo "unknown arg: $1" >&2; usage ;;
  esac
  shift
done

[[ -d $dir ]] || { echo "not a directory: $dir" >&2; exit 2; }

# Convert age into a find predicate.
unit=${age: -1}
num=${age%?}
[[ $num =~ ^[0-9]+$ ]] || { echo "bad age: $age" >&2; exit 2; }

case $unit in
  m) find_age=( "-${time_field%time}min"  "+$num" ) ;;
  h) find_age=( "-${time_field%time}min"  "+$((num * 60))" ) ;;
  d) find_age=( "-${time_field}"          "+$num" ) ;;
  w) find_age=( "-${time_field}"          "+$((num * 7))" ) ;;
  *) echo "bad age unit: $unit (use m/h/d/w)" >&2; exit 2 ;;
esac

find_args=( "$dir" )
[[ $include_dirs -eq 0 ]] && find_args+=( -type f )
[[ -n $glob ]] && find_args+=( -name "$glob" )
find_args+=( "${find_age[@]}" )

count=$(find "${find_args[@]}" | wc -l)

if [[ $delete -eq 0 ]]; then
  echo "DRY RUN — would delete $count item(s) in $dir older than $age ($time_field):"
  find "${find_args[@]}" -print
  echo
  echo "Re-run with --delete to remove them."
else
  echo "Deleting $count item(s) in $dir older than $age ($time_field)..."
  find "${find_args[@]}" -print -delete
fi
