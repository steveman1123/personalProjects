with open('day06in.txt','r') as f:
  t=f.read().split('\n\n') #split into groups right away

#responses for the whole group
g=[e.replace('\n','') for e in t]

pt1 = sum([len(set(e)) for e in g])

#get responses of every individual
p = [e.split('\n') for e in t]

pt2 = 0 #initialize the output
for g in p: #for every group in the responde
  i = set(g[0]) #init the intersect set
  for e in g: #for every person in the group
    i = i & set(e) #compare their answers to the common answers of the previous group members
  pt2 += len(i) #add the number of responses that are the same

print(pt1)
print(pt2)
