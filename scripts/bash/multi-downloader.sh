#download/save multiple OSMAnd maps from their links in a given file
#TODO: specify an array of filenames and loop through to read all of them

#specify the file to read the urls from
file="./files2download.txt"
#specify the directory to save the downloaded files to
saveDir="./"

#convert the file from dos to unix format
echo ensuring file is in unix format
dos2unix $file


#load the file into an array
mapfile -t urls < $file

#display the array
#declare -p urls



#for every object in the array
for ((i=0;i<${#urls[@]};i++))
do
  #set the url var to the current index
  url=${urls[$i]}
  
  #make sure that it's not a blank line
  if [ ${#urls[$i]} -gt 1 ];

  then
    #set the filename
    
    #replace "%20" with " "
    filename="${url//[%20]/ }/"
    #split location into proper file name (trim off beginning of link)
    filenameparts=();
    while [[ $filename ]]; do
      filenameparts+=( "${filename%%"/"*}" );
      filename=${filename#*"/"};
      #echo $filename
    done
    filename=${filenameparts[-1]}

    #specify the save dir
    filename=$saveDir$filename
    
    #display the current url line and the file it's saving to
    echo $i \| ${#urls[@]} - $filename;
    curl -L -o "$filename" "$url"
    echo -e
  fi
  
done


echo "done"

