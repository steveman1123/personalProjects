#convert a file name to id3v2 tags
#especially of format "{track} - {title}.mp3"
#DOES NOTE set containing folder as album and next folder up as artist, also checks for multi discs
echo -e

#set the location of mp3 files as an arg
if (( $# != 1 )); then
  echo "wrong number of args. Please pass the directory to work from"
  exit;
else
  #set the directory var
  dir=$1;
fi
echo $dir;


#seperator between track and title
delim=" - ";

#extension of the files to parse
fileext=".mp3"

#obtain original Internal Field Seperator
ogifs=$IFS;

#for every mp3
for f in "$dir"/*"$fileext"; do
  #split by / and get the filename
  IFS="/" filename=($f);
  filename=${filename[-1]};
  IFS=$ogifs;

  basename="${filename%.*}"
  #echo $basename;

  #isolate the track
  track="${basename%%"$delim"*}";
  #trim the file extension from the filename to get the title
  title="${basename#*"$delim"}";

  #echo $track, $title;

  if [ ${#track} -gt 0 -a ${#title} -gt 0 ]; then
    echo -e
    echo "writing track and title"
    echo $f
    echo $track, $title;
    #write the tags
    id3v2 -T "$track" -t "$title" "$f";
  else
    echo "missing track or title?"
  fi

  echo -e
  echo -e
done
