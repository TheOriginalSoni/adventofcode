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
lines=[x.replace(":","") for x in lines]
lines = [x.split(" ") for x in lines]

a = []
for line in lines:
    #print(line)
    line[1] = line[1][1:]
    a.append((int(line[6]),int(line[12])))

#print(a)

#PART 1
a.sort()
intervals = set()
for x in a:
    intervals.add(x[0])
    intervals.add(x[1])

intervals = list(intervals)
intervals.sort()

#print(intervals)
ans1 = [0]*(len(intervals))
j=0
for x in a:
    i1 = intervals.index(x[0])
    i2 = intervals.index(x[1])
    maxleft = 0
    for i in range(i1+1):
        maxleft = max(maxleft,(ans1[i]))
    #print(i1,i2,maxleft)
    ans1[i2]=maxleft+1
    #if(j%100==0):
    #    print(j)
    j=j+1

print(max(ans1))

#PART 1, BETTER WAY 
b = [(x,y) for (y,x) in a]
b.sort()
ans12 = 0
currt = b[0][1]
for x in b:
    if(currt <= x[1]):
        currt = x[0]
        ans12 += 1
    else:
        pass

print(ans12)

generator = [0]*len(intervals)
for x in a:
    i1 = intervals.index(x[0])
    i2 = intervals.index(x[1])
    generator[i1]+= 1
    generator[i2]+= -1

ans2 = 0
curr = 0
for i in range(len(intervals)):
    curr = curr + generator[i]
    ans2 = max(ans2,curr)

print(ans2)
