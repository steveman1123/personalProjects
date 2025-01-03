#!/bin/bash

#move files from /path/to/file.xyz to /path/to-file.xyz

# Loop through each child directory
for dir in */; do
  # Remove the trailing slash from the directory name
  base="${dir%/}"

  # Loop through each file in the directory
  for file in "$dir"*; do
    # Check if it is a file (not a directory)
    if [ -f "$file" ]; then
      # Move the file to the current directory with the directory name prepended
      mv -i "$file" "./${base}-$(basename "$file")"
    fi
  done
done

