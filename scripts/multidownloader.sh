#download/save multiple urls listed in a file using curl

#specify the file to read the urls from
file=".urlfile.txt"
#specify the directory to save the downloaded files to
saveDir="./"

#load the file into an array
mapfile -t urls < $file

#display the array
#declare -p urls

#for every url in the array
for ((i=0;i<${#urls[@]};i++))
do
  #set the url
  url=${urls[$i]}
  #split location into proper file name (trim off beginning of link (change this per url file - TODO to make it more general)
  filename="$saveDir${url:0}"

  #display the current url line and the file it's saving to
  echo -e
  echo $i \| ${#urls[@]} - $filename

  #request the file and save it
  curl -L -o $filename "$url"
done

