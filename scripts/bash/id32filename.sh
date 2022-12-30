#convert the filename to format "{track with leading 0} - {title}.mp3"
#so long as id3 tags are complete


dir="/storage/6132-3739/Music/SunSquabi/Instinct"
ogifs=$IFS

for f in $dir/*.mp3; do
  echo $f;
  #isolate the line with the track number
  track=$(eval id3v2 --list \"$f\" | grep 'TRCK');
  title=$(eval id3v2 --list \"$f\" | grep 'TIT2');
  IFS="\)\: "
  track=($track);
  title=($title);
  IFS=$ogifs;
  track=${track[-1]}
  title=${title[-1]}
  echo $track - $title


done
