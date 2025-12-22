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

def orthoneighbours(xy):
    x,y=xy
    return [(x-1,y),(x,y-1),(x,y+1),(x+1,y)]

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
b=[]
for line in lines:
    line=list(line) #.split(" ")
    if(line == []):
        a.append(b)
        b=[]
    else:
        b.append(line)

a.append(b)

print(a)

def traverse(grid):
    ends = []
    visited=[]
    N = len(grid)
    M = len(grid[0])
    for i in range(N):
        currv = []
        for j in range(M):
            if(grid[i][j]=="O"):
                ends.append((i,j))
            if(grid[i][j]!="#"):
                currv.append(0)
            else:
                currv.append(1)
        visited.append(currv)

    st = [ends[0]]
    dist = defaultdict(int)
    dist[ends[0]]=0
    visited[ends[0][0]][ends[0][1]]=1
    while(len(st)>0):
        curr = st.pop(0)
        for n in orthoneighbours(curr):
            if(n[0]>=0 and n[0]< N and n[1]>=0 and n[1]<M):
                if(visited[n[0]][n[1]]==0):
                    visited[n[0]][n[1]]=1
                    dist[n] = dist[curr] + 1
                    st.append(n)
    print(visited)
    print(dist)
    #print(ends)
    return dist[ends[1]]
    #return 1

ans1 = 1
for b in a:
    currans = traverse(b)
    print(currans-1)
    ans1 = ans1 * (currans-1)

print(ans1)