from collections import Counter
from collections import defaultdict
from functools import reduce
from functools import cmp_to_key
from functools import cache
from utils import *
from math import gcd,lcm
import re
import math
import heapq

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

def dist(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2 + abs(a1[2]-a2[2])**2

#===============================================

# Solving AoL from LMB!
# https://lovemathboy.github.io/day15.html

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]
lines=[x.replace("-> ","") for x in lines]
lines = [x.split(" ") for x in lines]

a = [[int(x) for x in line] for line in lines]
#print(a)
from collections import Counter
from collections import defaultdict
from functools import reduce
from functools import cmp_to_key
from functools import cache
from utils import *
from math import gcd,lcm
import re
import math
import heapq

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

def dist(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2 + abs(a1[2]-a2[2])**2

#===============================================

# Solving AoL from LMB!
# https://lovemathboy.github.io/day15.html

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]
lines=[x.replace("-> ","") for x in lines]
lines = [x.split(" ") for x in lines]

a = [[int(x) for x in line] for line in lines]
#print(a)

allnodes = set()
outedges = defaultdict(list)
inedges = defaultdict(list)

a.sort()

for x in a:
    allnodes.add(x[0])
    allnodes.add(x[1])
    outedges [ x[0] ] += [ x[1] ]
    inedges [ x[1] ] += [ x[0] ]

allnodes = list(allnodes)
allnodes.sort()

ans1 = defaultdict(int)
for x in a:
    t1 = x[0]
    t2 = x[1]
    ans1[t2] = max(ans1[t2], ans1[t1]+1)

maxans1 = 0
for t in ans1:
    maxans1 = max(maxans1,ans1[t])

print(f"ans1 = {maxans1+1}")

roots = 0
nodes = 0
for x in allnodes:
    if(outedges[x]==[]):
        nodes += 1
    if(inedges[x]==[]):
        roots += 1

ans2 = max(roots,nodes)
print(f"ans2 = {ans2}")