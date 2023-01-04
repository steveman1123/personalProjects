#convert a file name to id3v2 tags
#especially of format "{track} - {title}.mp3"
#also set containing folfer as album and next folder up as artist

#location of mp3 files
#TODO: take in as a program argument
dir=$PWD;
echo $dir;

#seperator between track and title
delim=" - ";

#obtain original Internal Field Seperator
ogifs=$IFS
#split dir by /
IFS="/" dirarr=($dir)
#reset seperator
IFS=$ogifs

#artist=dir.split[-2]
artist=${dirarr[-2]}
#album=dir.split[-1]
album=${dirarr[-1]}

echo artist: $artist;
echo album: $album;

#for every mp3
for f in "$dir"/*.mp3; do
  #split by / and get the filename
  IFS="/" filename=($f)
  filename=${filename[-1]}
  IFS=$ogifs;
  
  #split filename by delim and get the track and title
  tmp=$filename$delim trackandtitle=();
  while [[ $tmp ]]; do
    trackandtitle+=( "${tmp%%"$delim"*}" );
    tmp=${tmp#*"$delim"};
  done
  
  track=${trackandtitle[0]}
  title=${trackandtitle[1]}
  echo $track, $title;

  #write the tags
  id3v2 -T "$track" "$f";
  id3v2 -t "$title" "$f";
  id3v2 -a "$artist" "$f";
  id3v2 -A "$album" "$f";
done
