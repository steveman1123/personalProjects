#get the comments of a python file
#TODO should also output the line number the comment is found on
#TODO: should also be able to read multiline comments in ''' blocks
#TODO: should ignore such comment delims if they're in quotes or already in a comment
import sys,os

#pass the filename as an argument
if(len(sys.argv)<2):
  print("please specify a file to read the comments from")
  exit()
elif(os.path.isfile(sys.argv[1])):
  fileName = sys.argv[1]
else:
  print("couldn't find that file. Try something else")
  exit()

#read the file as bytes
fileObj = open(fileName,'rb')

#get the comments
content = str(fileObj.read()).split("#")
comments = []
for i in content:
  comments.append(str(i.split("\\r\\n")[0]))

#output
print(*comments, sep="\n")