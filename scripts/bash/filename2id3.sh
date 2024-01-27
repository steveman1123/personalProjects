#convert a file name to id3v2 tags
#especially of format "{track} - {title}.mp3"
#sets containing folder as album and next folder up as artist, also checks for multi discs
#prompts for other tags
#checks for "folder.jpg" and if exists, asks to set as cover art

echo -e
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
#split dir by /
IFS="/" dirarr=($dir)
#reset seperator (this kind of split only works for single char delims)
IFS=$ogifs;


#if folders found starting with "disc", "disk", or "part", then set album name to "Album Name (Disc #)"
isseries="n";
if [[ $(echo "${dirarr[-1]}" | grep -E "^(Part|Disc|Disk|Vol|Volume) [0-9]+$") ]]; then
  echo -n "is this album part of a series? (Y/n) "
  read isseries;
fi


if [[ "${isseries,,}" == "n" ]]; then
  #is organized as /artist/album/
  #artist=grandparent dir
  artist=${dirarr[-2]}
  #album=parent dir
  album=${dirarr[-1]}
else
  #is organized as /artist/album/Disc X
  artist=${dirarr[-3]}
  album="${dirarr[-2]} (${dirarr[-1]})"
fi

#echo artist: $artist;
#echo album: $album;




echo -n "delete all existing tags? (Y/n) "
read deleteall;

echo $deleteall;
if [[ "${deleteall,,}" == "n" ]]; then
  #echo "deleting existing tags"
  deleteall="n";
else
  #echo "not deleting existing tags"
  deleteall="y";
fi


if test -f "$dir/folder.jpg"; then
  echo -n "\"folder.jpg\" is found. Resize to 600x600 and use it as the cover art? (Y/n)"
  read writeimg;
  if [[ ${writeimg,,} == "n" ]]; then
    writeimg="n";
  else
    writeimg="y"
  fi
fi



#TODO: check if year and genre are nuneric
#https://stackoverflow.com/questions/806906/how-do-i-test-if-a-variable-is-a-number-in-bash#3951175

echo -n "release year: "
read year;

#if [[ ${#year} -eq 4 ]]; then
#  echo "year is $year"
#else
#  echo "year not valid"
#fi


id3v2 -L | less
echo -n "album genre number: "
read genreNum;

#if [[ $genreNum -gt -1 ]]; then
#  echo "genre is $(id3v2 -L | grep $genreNum)"
#else
#  echo "bad genre"
#fi

echo -e
echo -e
echo "writing the following:"
echo -e
echo "deleting existing tags? $deleteall"
echo "set folder.jpg as album cover? $writeimg"
echo "artist: $artist"
echo "album: $album"
echo "year: $year"
echo "genre: $(id3v2 -L | grep $genreNum | head -1)"

echo -n "continue? (Y/n)"
read okgo

if [[ ${okgo,,} == "n" ]]; then
  okgo="n";
else
  okgo="y";
fi

if [[ $okgo == "y" ]]; then

  #resize the folder.jpg image
  if [[ $writeimg == "y" ]]; then
    echo "resizing folder.jpg"
    convert -resize "600x600>" "$dir/folder.jpg" "$dir/tmp.jpg"
    mv "$dir/tmp.jpg" "$dir/folder.jpg"
  fi


  #for every mp3
  for f in "$dir"/*"$fileext"; do
    #split by / and get the filename
    IFS="/" filename=($f);
    filename=${filename[-1]};
    IFS=$ogifs;
    
    #split filename by delim and get the track and title
    tmp=$filename$delim;
    trackandtitle=();
    while [[ $tmp ]]; do
      trackandtitle+=( "${tmp%%"$delim"*}" );
      tmp=${tmp#*"$delim"};
    done

    #isolate the track
    track=${trackandtitle[0]};
    #trim the file extension from the filename to get the title
    title=${trackandtitle[1]:0:${#trackandtitle[1]}-${#fileext}};
    echo $track, $title;

    #delete all previous tags if requested
    if [[ $deleteall == "y" ]]; then
      id3v2 -D "$f"
    fi

    echo -e
    echo "writing new tags"
    #write the tags
    id3v2 -T "$track" "$f";
    id3v2 -t "$title" "$f";
    id3v2 -a "$artist" "$f";
    id3v2 -A "$album" "$f";
    id3v2 -g "$genreNum" "$f";
    id3v2 -y "$year" "$f";

    if [[ $writeimg == "y" ]]; then
      eyeD3 --add-image "$dir/folder.jpg":FRONT_COVER "$f";
    fi
    echo -e
    echo -e
  done

else
  echo "cancelling";
fi
