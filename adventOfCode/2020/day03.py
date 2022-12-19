#run with python 2.7 (only difference should be the prints)

with open('./day03in.txt','r') as f:
  t = f.read()

t = t.split('\n')
t = [e for e in t if len(e)>0]

startCol = 0 #column to start at
hm = 3 #horizontal mvmt

#part 1: move 3 to the right, down 1
pt1 = [i for i,e in enumerate(t) if e[(startCol+hm*i)%len(e)]=="#"]

#part 2: move x to the right, down 1
pt2 = []
for h in [1,3,5,7]:
  tmp = [i for i,e in enumerate(t) if e[(startCol+h*i)%len(e)]=="#"]
  pt2.append(len(tmp))
  
#also move 1 to the right, down 2
#remove odd rows from the trees
t = [e for i,e in enumerate(t) if not i%2]

#append the 1 over, 2 down trees
pt2.append(len([i for i,e in enumerate(t) if e[(startCol+1*i)%len(e)]=="#"]))

#multiply everything together
pt2 = reduce(lambda a,b:a*b,pt2,1)


print len(pt1)

print pt2