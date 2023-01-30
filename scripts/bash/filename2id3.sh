#convert a file name to id3v2 tags
#especially of format "{track} - {title}.mp3"
#also set containing folfer as album and next folder up as artist

#9et the location of mp3 files as an arg
if (( $# != 1 )); then
  echo wrong number of args. Please pass the directory to work from
  exit;
else
  #set the directory var
  dir=$1;

echo $dir;


#seperator between track and title
delim=" - ";

#obtain original Internal Field Seperator
ogifs=$IFS
#split dir by /
IFS="/" dirarr=($dir)
#reset seperator (this kind of split only works for single char delims)
IFS=$ogifs

#artist=grandparent dir
artist=${dirarr[-2]}
#album=parent dir
album=${dirarr[-1]}

echo artist: $artist;
echo album: $album;
#TODO: add a confirm that these are OK to set

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

  #isolate the track
  track=${trackandtitle[0]}
  #trim the ".mp3" from the filename to get the title
  title=${trackandtitle[1]:0:${#trackandtitle[1]}-4}
  echo $track, $title;

  #write the tags
  id3v2 -T "$track" "$f";
  id3v2 -t "$title" "$f";
  id3v2 -a "$artist" "$f";
  id3v2 -A "$album" "$f";
done
