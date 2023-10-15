#convert a file name to id3v2 tags
#especially of format "{track} - {title}.mp3"
#also set containing folfer as album and next folder up as artist

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

#artist=grandparent dir
artist=${dirarr[-2]}
#album=parent dir
album=${dirarr[-1]}

echo artist: $artist;
echo album: $album;



#TODO: add a confirm that these are OK to set
#TODO: add a prompt to ask to delete all previous data (id3v2 -D)
#TODO: prompt for year and genre, then write if it's not null

echo -n "delete all existing tags? (y/N) "
read deleteall;

echo $deleteall;
if [[ "${deleteall,,}" == "y" ]] then
  #echo "deleting existing tags"
  deleteall="y";
else
  #echo "not deleting existing tags"
  deleteall="n";
fi

#TODO: check if yesr and genre are nuneric
#https://stackoverflow.com/questions/806906/how-do-i-test-if-a-variable-is-a-number-in-bash#3951175

echo -n "release year: "
read year;

#if [[ ${#year} -eq 4 ]] then
#  echo "year is $year"
#else
#  echo "year not valid"
#fi


id3v2 -L
echo -n "album genre number: "
read genreNum;

#if [[ $genreNum -gt -1 ]] then
#  echo "genre is $(id3v2 -L | grep $genreNum)"
#else
#  echo "bad genre"
#fi

echo -e
echo -e
echo "deleting existing tags? $deleteall"
echo "writing the following:"
echo "artist: $artist"
echo "album: $album"
echo "year: $year"
echo "genre: $(id3v2 -L | grep $genreNum)"

echo -n "continue? (Y/n)"
read okgo

if [[ ${okgo,,} == "n" ]] then
  okgo="n";
else
  okgo="y";
fi

if [[ $okgo == "y" ]] then

  if [[ $deleteall == "y" ]] then
    echo "deleting existing tags";
    id3v2 -D
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

    #write the tags
    id3v2 -T "$track" "$f";
    id3v2 -t "$title" "$f";
    id3v2 -a "$artist" "$f";
    id3v2 -A "$album" "$f";
    id3v2 -g "$genreNum" "$f";
    id3v2 -y "$year" "$f";
  done

else
  echo "cancelling";
fi
