#resize all pictures in a folder to a specified max width

#ensure directory is supplied as an arg
if (( $# != 1 )); then
 echo "wrong number of args. Please supply the directory";
  exit
else
  #set the directory to the supplied argument
  picdir=$1;
fi

#specify directory
#picdir="./media";


#specify width in px
newimgwidth=1008;

#loop through and resize
#https://www.howtogeek.com/109369/how-to-quickly-resize-convert-modify-images-from-the-linux-terminal/
for i in "$picdir"/*;
do
  echo $i;
  #get the current image width
  oldimgwidth=$(identify -ping -format '%W' "$i");
  #if the widths do not match, then resize to match
  if(($oldimgwidth != $newimgwidth)); then
    echo "$oldimgwidth --> $newimgwidth";
    convert $i -resize $imgwidth $i;
  else
    #else, don't resize (save some time)
    echo "same size";
  fi
done

echo "done";
