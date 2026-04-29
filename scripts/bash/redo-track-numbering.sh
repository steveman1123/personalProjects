#!/bin/bash

# Directory to search (1st arg)
dir="${1}"


find "$dir" -type f -name "[0-9]* - *.mp3" -exec $(dirname "$(realpath "$0")")/track-title-to-tags.sh {} \;
