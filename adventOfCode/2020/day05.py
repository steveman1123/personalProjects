with open('day05in.txt','r') as f:
  t=f.read().split('\n')

#calculate seat id's from the given row, col id
ids = [int(e.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2) for e in t if(len(e)>0)]

#pt1 asks for the max id
pt1 = max(ids)
print(pt1)

#pt2 asks for the missing seat
pt2 = [e for e in list(range(min(ids),max(ids))) if e not in ids][0]
print(pt2)
