#!/usr/bin/env python3

import sys
import os

def replace_in_file(filepath, old_string, new_string):
    """
    Replace all occurrences of old_string with new_string in the given file.
    The file is modified in-place.
    """
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    # Perform replacement
    new_content = content.replace(old_string, new_string)

    # Write back to the same file
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
    except Exception as e:
        print(f"Error writing to file: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Replaced '{old_string}' with '{new_string}' in '{filepath}'")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 replace_in_file.py <filepath> <old_string> <new_string>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    old_string = sys.argv[2]
    new_string = sys.argv[3]

    replace_in_file(filepath, old_string, new_string)
