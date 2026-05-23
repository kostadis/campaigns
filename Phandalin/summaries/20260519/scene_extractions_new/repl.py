#!/usr/bin/env python3

import sys
import os
import glob

def replace_in_files(pattern, old_string, new_string):
    """
    Replace all occurrences of old_string with new_string in all files matching the glob pattern.
    Files are modified in-place.
    """
    files = glob.glob(pattern)
    if not files:
        print(f"No files match pattern: {pattern}", file=sys.stderr)
        sys.exit(1)

    for filepath in files:
        if not os.path.isfile(filepath):
            print(f"Skipping non-file: {filepath}", file=sys.stderr)
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception as e:
            print(f"Error reading {filepath}: {e}", file=sys.stderr)
            continue

        # Perform replacement
        new_content = content.replace(old_string, new_string)

        # Only write if content changed
        if content != new_content:
            try:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Replaced '{old_string}' with '{new_string}' in '{filepath}'")
            except Exception as e:
                print(f"Error writing to {filepath}: {e}", file=sys.stderr)
        else:
            print(f"No changes needed in '{filepath}'")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 replace_in_files.py <pattern> <old_string> <new_string>", file=sys.stderr)
        print("Example: python3 replace_in_files.py '*.py' 'old_text' 'new_text'", file=sys.stderr)
        sys.exit(1)

    pattern = sys.argv[1]
    old_string = sys.argv[2]
    new_string = sys.argv[3]

    replace_in_files(pattern, old_string, new_string)
