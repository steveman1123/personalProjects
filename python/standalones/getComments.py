#get the comments of a python file

import tokenize

fileName = ""

fileObj = open(fileName,'rb')

content = str(fileObj.read()).split("#")
comments = []

for i in content:
  comments.append(i.split("\\r\\n")[0])

print(*comments, sep="\n")