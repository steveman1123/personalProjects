#!/bin/bash

#rename files for featured artists etc

# Check if directory path is provided
if [ -z "$1" ]; then
  echo "Usage: $0 directory_path"
   exit 1
fi

# Loop through each file in the specified directory
for filename in "$1"/*; do
  # Only process files with the correct naming pattern
  if [[ "$filename" =~ ^(.+)\ -\ (.+)\ -\ (.+)\.(.+)$ ]]; then
    # Extract components using regex groups
    a="${BASH_REMATCH[1]}"
    b="${BASH_REMATCH[2]}"
    c="${BASH_REMATCH[3]}"
    ext="${BASH_REMATCH[4]}"

    # Construct new filename
    new_filename="${a} - ${c} (ft. ${b}).${ext}"
    
    # Rename the file
    mv "$filename" "$1/$new_filename"
    echo "Renamed: $filename -> $new_filename"
  else
    echo "Skipping: $filename (doesn't match pattern)"
  fi
done
