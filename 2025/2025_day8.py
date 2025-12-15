from collections import Counter
from collections import defaultdict
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
from utils import *

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]
a = [[int(y) for y in x.split(",")] for x in lines]

def dist(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2 + abs(a1[2]-a2[2])**2

dists = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        dists.append((dist(a[i],a[j]),i,j))
dists.sort()

#print(dists)

# PART 1
b=list(range(len(a)))

N=1000
for i in range(N):
    curr = dists[i]
    #print(curr)
    val1 = b[curr[1]]
    val2 = b[curr[2]]
    if(val1 != val2):
        for i2 in range(len(a)):
            if(b[i2]==val2):
                b[i2]=val1

#print(b)
c = Counter(b)
#print(c)
c2 = c.most_common(3)
ans1 = c2[0][1]*c2[1][1]*c2[2][1]

print(ans1)

b=list(range(len(a)))

N=len(a)
for i in range(len(dists)):
    curr=dists[i]
    val1 = b[curr[1]]
    val2 = b[curr[2]]
    if(val1 != val2):
        N-=1
        for i2 in range(len(a)):
            if(b[i2]==val2):
                b[i2]=val1
    if(N==1):
        print(a[curr[1]][0]*a[curr[2]][0])
        break

## PART 1 using DSU

b=DSU(len(a))

N=1000
for i in range(N):
    curr = dists[i]
    val1 = b.find(curr[1])
    val2 = b.find(curr[2])
    if(val1 != val2):
        b.union(curr[1],curr[2])
    val1 = b.find(curr[1])

print(b.parents)
print(b.ranks)
print(b.sizes)
print(b.numdisjoint)
bp = [b.find(i) for i in range(len(a))]
c = Counter(bp)
c2 = c.most_common(3)
ans1 = c2[0][1]*c2[1][1]*c2[2][1]
print(ans1)


## PART 2 using DSU

b=DSU(len(a))

i=0
while(b.numdisjoint>1):
    curr = dists[i]
    val1 = b.find(curr[1])
    val2 = b.find(curr[2])
    if(val1 != val2):
        b.union(curr[1],curr[2])
    val1 = b.find(curr[1])
    i=i+1

print(a[curr[1]][0]*a[curr[2]][0])
