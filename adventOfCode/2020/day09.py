#determine if x is the sum of 2 numbers in arr
def isSum(arr, x):
  for i,e in enumerate(arr):
    for f in arr[i+1:]:
      if(e+f==x):
        return True
  return False

#open the file
with open('day09in.txt','r') as f:
  t = f.read().split('\n')
t = [int(e) for e in t] #convert strings to ints

#define the cypher/filter
fltrStart = 0
fltrLen = 25
fltr = t[fltrStart:fltrLen]

#loop through the numbers to determine which one is incorrect
while isSum(fltr,t[fltrLen+fltrStart]):
  fltrStart += 1
  fltr = t[fltrStart:fltrLen+fltrStart]

pt1 = t[fltrLen+fltrStart]
print pt1

#once we have that number, loop thru to find the consecutive numbers that add to it
for i in range(fltrLen+fltrStart):
  for j in range(i+2,fltrLen+fltrStart):
    if(sum(t[i:j])==pt1):
      arr = t[i:j]
      break

#then find the sum of the min and max of that list
pt2 = min(arr)+max(arr)

print pt2