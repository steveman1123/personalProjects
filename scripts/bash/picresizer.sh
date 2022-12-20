#resize all pictures in a folder to a specified max width

#specify directory
picdir="./media";
#specify width in px
imgwidth=900;

#loop through and resize
#https://www.howtogeek.com/109369/how-to-quickly-resize-convert-modify-images-from-the-linux-terminal/
for i in "$picdir"/*;
do
  echo $i;
  convert $i -resize $imgwidth $i;
done

echo "done";
