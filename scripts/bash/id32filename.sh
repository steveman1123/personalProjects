#convert the filename to format "{track with leading 0} - {title}.mp3"
#so long as id3 tags are complete

dir=".";
delim="): ";

for f in "$dir"/*.mp3; do
  echo $f;
  #isolate the line with the track number
  track=$(eval id3v2 --list \"$f\" | grep 'TRCK');
  title=$(eval id3v2 --list \"$f\" | grep 'TIT2');
  
  tmptrk=$track$delim;
  tmptit=$title$delim;
  track=();
  title=();
  while [[ $tmptrk ]]; do
    track+=( "${tmptrk%%"$delim"*}" );
    title+=( "${tmptit%%"$delim"*}" );

    tmptrk=${tmptrk#*"$delim"};
    tmptit=${tmptit#*"$delim"};
  done

  
  track=$((10#${track[1]}));
  title=${title[1]};

  #append leading 0 to tracks less than 10
  #TODO: instead of just 10, append min(1,log_10(number of tracks))
  #That is: if <10: append 1 0, if <100: append 1 0, if <1000: append 2 0 to <10, append 1 0 to <100, etc, etc
  if (( $track < 10 )); then
    track=0$track;
  fi

  echo moving \"$f\" to \"$dir/$track - $title.mp3\";
  mv --verbose "$f" "$dir/$track - $title.mp3";

done
