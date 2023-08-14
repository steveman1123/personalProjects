#download/save multiple video files specified from a file containing 1 url per line
#convert all mkvs to mp4s
#TODO: specify an array of filenames and loop through to read all of them

#specify the file to read the urls from
file="./files2download.txt"
#specify the directory to save the downloaded files to
saveDir="/run/media/steve/Site/Site/stevenw/Medio/Unconverted Videos/"

#convert the file from dos to unix format
echo ensuring file is in unix format
dos2unix $file


#load the file into an array
mapfile -t urls < $file

#display the array
#declare -p urls

#echo ${urls[3]}
#exit

#for every object in the array
for ((i=0;i<${#urls[@]};i++))
do
  #set the url var to the current index
  url=${urls[$i]}
  #make sure that it's not a blank line or commented out
  if [ ${#url} -gt 1 ] && [ ${url:0:1} != "#" ]; then
  
    #set the filename
    
    #replace "%20" with " "
    #echo "replacing spaces"
    #filename="${url//[%20]/ }/"
    filename="${url//%20/ }/"
    #join repeat spaces
    #echo "joining spaces"
    #filename=$(echo "$filename" | tr -s ' ')
    
    #split location into proper file name (trim off beginning of link)
    filenameparts=();
    #echo "isolating filename"
    while [[ $filename ]]; do
      filenameparts+=( "${filename%%"/"*}" );
      filename=${filename#*"/"};
      #echo $filename
    done
    filename=${filenameparts[*]: -1}

    #specify the save dir
    filename=$saveDir$filename
    
    #display the current url line and the file it's saving to
    echo $i \| ${#urls[@]} - $filename;

    #continually attempt to download if a failure is encountered (curl should return 0 if done, 1 if failed)
    #TODO: why doesn't it start over if the file already exists (ie program is exited during a download, then restarted)
    while ! curl -L -o "$filename" "$url" -C -; do
      echo "errored, trying again"
      rm *.mkv
      sleep 120
    done
    echo -e
  fi
  


  #convert from mkv to mp4 if applicable
  #TODO: ensure it's lowercase using ,,
  if [ "${filename: -4}" == ".mkv" ]; #ensure that it's a .mkv first
  then
    newfilename="${filename::-4}.mp4"
    echo "converting $filename --> $newfilename and scaling to 1080p"
    ffmpeg -hwaccel auto -i "$filename" -ac 2 -vf scale="1080:trunc(ow/a/2)*2" -y "$newfilename"

    #remove original mkv file
    rm "$filename"
    #TODO: write the current url as commented once it's all done
  fi
  
done


echo "done"

