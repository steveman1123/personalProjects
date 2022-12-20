#update all repos in a specified directory (relative or absolute)

#specify directory
gitdir="."

#loop through all objects in dir
for i in $gitdir/* ; do
  #if directory
  if [ -d "$i" ]; then
    #tell us
    echo "$i"
    #move into it
    cd "$i"
    #echo "$(pwd -P)"
    #get all hidden directories
    dirs=$(ls -ad ./.*/)
    #if .git/ is contained in the hidden directories
    if  [[ "$dirs" == *".git/"* ]]; then
      #echo "pulling"
      #add the directory if necessary (firs run)
      #git config --global --add safe.directory "$(pwd -P)"
      #pull the new version
      git pull
    else
      echo "Not a git dir"
    fi
    #go back to the parent dir
    cd ..
  fi
done
