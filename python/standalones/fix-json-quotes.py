#in a malformed json file of format {"x":"abc "def" xyz","y":"123"}, escape the quotes so it's valid as {"x":"abc \"def\" xyz","y":"123"}

import sys

inputfile = sys.argv[1]


intxt = open(inputfile,'r').read()

#replace any current instances of \" with just "

#split by "

# if there are extra " than none in the text

#rejoin the first 3 and last 2 " as "

#rejoin the rest as \"

intxt = intxt.replace(":5",':"5"')

intxt = intxt.replace('\\"','"')

splittext = intxt.split('"')
if(len(splittext)>9):
  finaltxt = '"'.join(splittext[:4])+'\\"'.join(splittext[3:-5])+'"'+'"'.join(splittext[-5:])


else:
  finaltxt=intxt

  print(inputfile)


print("writing to "+inputfile)
with open(inputfile,'w') as f:
  f.write(finaltxt)
  f.close()
