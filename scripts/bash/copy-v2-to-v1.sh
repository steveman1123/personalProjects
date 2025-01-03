#!/bin/bash

# Check if required commands are available
if ! command -v id3v2 &> /dev/null; then
  echo "id3v2 could not be found. Please install it."
  exit 1
fi

# Function to copy ID3v2 to ID3v1
copy_id3v2_to_id3v1() {
  for file in "$1"; do
    if [[ -f "$file" ]]; then
      echo "Processing '$file'..."

      # Extract ID3v2 tags
      artist=$(id3v2 -l "$file" | grep "TPE1" | cut -d ':' -f 2- | xargs -0)
      title=$(id3v2 -l "$file" | grep "TIT2" | cut -d ':' -f 2- | xargs -0)
      album=$(id3v2 -l "$file" | grep "TALB" | cut -d ':' -f 2- | xargs -0)
      year=$(id3v2 -l "$file" | grep "TYER" | cut -d ':' -f 2- | xargs)
      track=$(id3v2 -l "$file" | grep "TRCK" | cut -d ':' -f 2- | xargs -0)
      genre=$(id3v2 -l "$file" | grep "TCON" | cut -d ':' -f 2- | xargs -0)
      #isolate just the genre number
      genrenum=$(echo "$genre" | grep -oP '\(\K[^)]*')
      genrenum=$(echo "$genrenum" | grep -oP '\d+')

      # Update ID3v1 tags
      echo artist: $artist
      echo track: $track
      echo title: $title
      echo album: $album
      echo year: $year
      echo genre: $genre
      echo genre \#: $genrenum

      if [ ${#artist} -gt 0 -a ${#track} -gt 0 -a ${#title} -gt 0 -a ${#album} -gt 0 -a ${#year} -gt 0 -a ${#genre} -gt 0 -a $genrenum -ne "255" ]; then
        id3v2 -a "$artist" -t "$title" -A "$album" -y "$year" -g "$genrenum" -T "$track" "$file"
        echo "copied v2 to v1"
        exit 1;
        #sleep 0.75
      else
        echo "missing some id3v2 tags";
        exit 0;
      fi

    else
      echo "file does not exist: '$file'"
      exit 0;
    fi
    echo -e
  done
}

# Call the function with the provided arguments
export -f copy_id3v2_to_id3v1

find "$1"* -iname "*.mp3" -exec bash -c 'copy_id3v2_to_id3v1 "$0"' {} \; -quit
