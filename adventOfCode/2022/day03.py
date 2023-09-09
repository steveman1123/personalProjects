#get input
with open("day03in.txt",'r') as f:
  din = f.read().split("\n")
  f.close()


#split each line in half
halves = [[e[:int(len(e)/2)],e[int(len(e)/2):]] for e in din if len(e)>1]
print(halves[:10])

#see which char is the same in each
for i,e in enumerate(halves):
  same[i] = [x for x in e[0] if x in e[1]][0]
  #print(i,din[i])
  
#convert chars to priorities
for i,e in enumerate(same):
  same[i] = ord(e)-96 if e.islower() else ord(e)-38
  #print(i,e,din[i])


#sum priorities
out = sum(same)
print(out)




#pt 2
groups = [

