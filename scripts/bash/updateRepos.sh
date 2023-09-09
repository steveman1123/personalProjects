#update all repos in a specified directory (relative or absolute)
#TODO: create a git-setup file that does the following:
#set: git config --global credential.helper "/path/to/git.tokens"
#ensure colors can be displayed: git -c color.status=always status


#specify directory
gitdir=".";

#loop through all objects in dir
for i in $gitdir/* ; do
  #if directory
  if [ -d "$i" ]; then
    #tell us
    echo "$i";
    #move into it
    cd "$i";
    #echo "$(pwd -P)";
    #get all hidden directories
    dirs=$(ls -ad ./.*/);
    #if .git/ is contained in the hidden directories
    if  [[ "$dirs" == *".git/"* ]]; then
      #echo "pulling"
      #attempt to pull the new version
      pulldata=$(git pull 2>&1);
      
      echo "$pulldata"
      
      #add the directory if necessary (first run)
      #TODO: this part isn't tested
      if [[ $pulldata == *"--add safe.directory"* ]]; then
        echo "adding new safe directory";
        git config --global --add safe.directory "$(pwd -P)"
        echo "attempting to pull again";
        git pull
      fi

      
    else
      echo "Not a git dir"
    fi
    #go back to the parent dir
    cd ..
  fi
done
