#run on python 2.7

import re

with open('./day02in.txt','r') as f:
  t = f.read()

r = [re.split('-| |:\n',e) for e in t]


pt1 = [e[4] for e in r if e[4].count(e[2])>=int(e[0]) and e[4].count(e[2])<=int(e[1])]

pt2 = [e[4] for e in r if ((e[4][int(e[0])-1]==e[2]) != (e[4][int(e[1])-1]==e[2]))]

print len(pt1)
print len(pt2)

