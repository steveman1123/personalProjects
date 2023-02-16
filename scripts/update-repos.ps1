#pull the repos located in the specified directories

#location of the git dirs
$dir=".\"

#loop through each dir in the specified directory
Get-ChildItem $dir -Directory | 
Foreach-Object {
  #enter the dir
  echo $_.Name
  cd $_.Name
  #determine if the directory has the git dir
  #-Force=show hidden and not hidden, -filter isolates the .\.git
  $hasgitdir = gci $pwd -Force -filter ".\.git"
  #update or skip
  if($hasgitdir) { git pull }
  else { echo "not a git dir" }
  #exit the dir
  cd ..
}