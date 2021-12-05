with open('day10in.txt','r') as f:
  t = f.read().split('\n')
  t = [int(e) for e in t if len(e)>0] #convert numbers from str to int

t.sort() #sort in ascending order
#get the differences between each element
diff = [1]+[j-i for i, j in zip(t[:-1], t[1:])]+[3]

#get all the differences that are 1's and 3's
ones = len([e for e in diff if e==1])
threes = len([e for e in diff if e==3])

pt1 = ones*threes #pt1 wants the multiple


#pt2 wants the number of unique combinations that will be equivilant to part 1

#the idea for the following is that we looks for groups of 1's that can be converted to higher orders, so any group of 2 or more 1's

oneGroups = [] #list of lengths of groups of 1's (more than one individual 1)
i=0 #index of the diff
while i < len(diff)-1:
  grplen=1 #length of the group of 1's
  while(diff[i]==diff[i+1]==1): #if there's a group
    grplen+=1 #figure out how big the group is
    i+=1
  if(grplen>1): #only record the groups that have more than one 1
    oneGroups.append(grplen)
  i+=1

#alternative combinations per group depends on how many 1's in the group (if it's more than 2, then it's a linear relationship, if it's 2, then there's only 2 combinations that can be made,
# so we just look for whichever is greater
alts = [max(3*e-5,2) for e in oneGroups]
pt2 = reduce(lambda a,b:a*b,alts) #multiply together to get the total combinations


print pt1
print pt2

'''
For example:
0,1,2,3,6
has a diff of
1,1,1,3
which makes it a group of 3
That means there are combinations of:
0,1,2,3,6
0,2,3,6
0,1,3,6
0,3,6
That's 4 unique groups and represented in 3*e-5
But since a group of 2 doesn't follow the same rule, it just has 2 combinations, so that can be represented as max(3*e-5,2)
'''
