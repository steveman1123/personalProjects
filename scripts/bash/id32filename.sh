#convert the filename to format "{track with leading 0} - {title}.mp3"
#so long as id3 tags are complete

#TODO: ensure unicode characters are allowed
#TODO: expand to recursive directories (only rename if all tracks in a folder have unique data for track and title)
#TODO: improve handling of filenames with ' in them

#ensure directory is supplied as an arg
if (( $# != 1 )); then
  echo "wrong number of args. Please supply the directory";
  exit
else
  #set the directory to the supplied argument
  dir=$1;
fi

delim="): ";

for f in "$dir"/*.mp3; do
  echo $f;
  
  #isolate the line with the track number
  #replace instances of "$" with "\$" in the filename
  track=$(eval id3v2 --list \"${f//$/\\$}\" | grep 'TRCK');
  title=$(eval id3v2 --list \"${f//$/\\$}\" | grep 'TIT2');
  
  tmptrk=$track$delim;
  tmptit=$title$delim;
  track=();
  title=();
  #split the track and title into the data
  #while there's still data in the tmp data
  while [[ $tmptrk ]]; do
    #append the data as an element
    track+=( "${tmptrk%%"$delim"*}" );
    title+=( "${tmptit%%"$delim"*}" );

    #remove the text before the delim
    tmptrk=${tmptrk#*"$delim"};
    tmptit=${tmptit#*"$delim"};
  done
  #sometimes the tracks are <track>/<totalTracks>, this scrubs the second totalTracks
  track=${track[1]};
  track=( "${track%%/*}" );

  #interpret the track as an arithmetic in base 10
  track=$((10#${track}));

  #replace all illegal file name characters with "-"
  title="${title[1]//[\>\<\:\"\/\\\|\?\*\#\%\&\@]/-}";

  #TODO: ensure the data is present
  #if(len(track)>0 and len(title)>0); then
    #do all this stuff
  #else
    #echo "incomplete track or title data"
  #fi

  #append leading 0 to tracks less than 10
  #TODO: instead of just 10, append min(1,log_10(number of tracks))
  #That is, make it look like 001,002,003...099,100,101...999
  if (( $track < 10 )); then
    track=0$track;
  fi

  #echo moving \"$f\" to \"$dir/$track - $title.mp3\";
  mv --verbose "$f" "$dir/$track - $title.mp3";

done
