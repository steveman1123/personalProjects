#compare contents of two directories

import os

path1 = input("path 1: ") #first path
path2 = input("path 2: ") #second path

p1contents = os.listdir(path1) #contents of the first path
p2contents = os.listdir(path2) #contents of the second path

shared = [e for e in p1contents if e in p2contents] #items in both
inp1 = [e for e in p1contents if e not in p2contents] #items only in path 1
inp2 = [e for e in p2contents if e not in p1contents] #items only in path 2

maxLines = 10 #max lines to display without a prompt (anything more will display a prompt to display anything)


print("\n\n")


#display the shared items
if(len(shared)>maxLines):
  dispAll = input(f"There are {len(shared)} shared items. Do you want to display all results? (y/n) ")
  if(dispAll=="y"):
    print("Shared:\n\t",end="")
    print(*shared, sep="\n\t")
else:
  print("Shared:\n\t",end="")
  print(*shared, sep="\n\t")

print("\n\n")

#display the items in path 1
if(len(inp1)>maxLines):
  dispAll = input(f"There are {len(inp1)} items in path 1 not in path 2. Do you want to display all results? (y/n) ")
  if(dispAll=="y"):
    print(f"Only in {path1}:\n\t",end="")
    print(*inp1, sep="\n\t")
else:
  print(f"Only in {path1}:\n\t",end="")
  print(*inp1, sep="\n\t")

print("\n\n")

#display the items in path 2
if(len(inp2)>maxLines):
  dispAll = input(f"There are {len(inp2)} items in path 2 not in path 1. Do you want to display all results? (y/n) ")
  if(dispAll=="y"):
    print(f"Only in {path2}\n\t",end="")
    print(*inp2, sep="\n\t")
else:
  print(f"Only in {path2}:\n\t",end="")
  print(*inp2, sep="\n\t")

print("\n\n")
