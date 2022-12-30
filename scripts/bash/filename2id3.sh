#convert a file name to id3v2 tags
#especially of format "{track} - {title}.mp3"
#also set contsining folfer as album and next folfer up as artist

dir="/storage/6132-3739/Music/SunSquabi/Instinct";
delim=" - ";

ogifs=$IFS
IFS="/" dirarr=($dir)
IFS=$ogifs

#artist=dir.split[-2]
artist=${dirarr[-2]}
#album=dir.split[-1]
album=${dirarr[-1]}

echo $artist;
echo $album;


for f in $dir/*.mp3; do
  IFS="/" filename=($f)
  filename=${filename[-1]}
  IFS=$delim trackandtitle=($filename)
  track=${trackandtitle[0]}
  title=${trackandtitle[1]}
  echo $track, $title;

  #uncomment for tag writing
  id3v2 -T $track $f;
  id3v2 -t $title $f;
  id3v2 -a $artist $f;
  id3v2 -A $album $f;
done
