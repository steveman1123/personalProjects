import numpy as np
import math
from time import sleep

In = "000100001100000000100000000000010000110000100100100000000000100000001000000000000"

leng = int(math.sqrt(len(In)))
comps = np.zeros(shape=(leng,leng))

for i in range(0,leng):
    for j in range(0,leng):
        comps[i][j] = In[leng*i+j]

start = comps

for a in range(0,500):
    for i in range(0,leng-0):
        for j in range(0,leng-0):
            n=0
            if i>0:
                if comps[i-1][j]==1:
                    n += 1
            if i<leng-1:
                if comps[i+1][j]==1:
                    n += 1
            if j<leng-1:
                if comps[i][j+1]==1:
                    n += 1
            if j>0:
                if comps[i][j-1]==1:
                    n += 1
            if n>=2:
                comps[i][j] = 1
            
print(np.matrix(start))
print("\n")
print(np.matrix(comps))