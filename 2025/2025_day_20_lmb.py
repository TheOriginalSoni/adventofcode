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

def dist2D(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2


#===============================================

# Solving AoL from LMB!
# https://lovemathboy.github.io/day15.html

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]

a=[]
for line in lines:
    line=line.replace(",","")
    line=line.replace(")","")
    line=line.replace("(","")
    line=line.replace("r=","")
    line=line.split(" ")
    line = [int(x) for x in line]
    line = [(line[0],line[1]),line[2]]
    a.append(line)

#print(lines)
#print(a)

ans1 = defaultdict(int)

for i in range(len(a)):
    for j in range(i):
        #print(a[i][0])
        #print(a[j][0])
        if(dist2D(a[i][0],a[j][0])< (a[i][1]+a[j][1])**2):
            ans1[i] += 1
            ans1[j] += 1

bestkey = 0
maxans1 = ans1[0]
for key in ans1:
    if(ans1[key]>maxans1):
        maxans1=ans1[key]
        bestkey=key

print(maxans1)
bestans1 = a[bestkey][0][0]*a[bestkey][0][1] + maxans1
print(a[bestkey])
print(bestans1)