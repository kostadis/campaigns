#!/bin/bash

# Script to rename files from <name>-8.md to <name>.md
# Usage: ./rename-files.sh

for file in *-8.md; do
    if [[ -f "$file" ]]; then
        # Extract the name part before "-8.md"
        name="${file%-8.md}"
        new_name="${name}.md"
        
        echo "Renaming: $file -> $new_name"
        mv "$file" "$new_name"
    fi
done

echo "Done!"
