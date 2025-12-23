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
import itertools

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
lines= [list(x) for x in lines]

a=[]
b=[]
for line in lines:
    #line=list(line) #.split(" ")
    if(line == []):
        a.append(b)
        b=[]
    else:
        if(line!=[]):
            b.append(line)
a.append(b)

#print(a)

def ans1fn(a,n,m):
    dp = [[0]*n for i in a] 
    st = [(0,0)]
    dp[0][0] = a[0][0]
 
    while(len(st)>0):
        curr = st.pop(0)
        x,y = curr
    
        for nxy in orthoneighbours((x,y)):
            nx,ny = nxy
            if(nx >=0 and nx<n and ny>=0 and ny<n):
                if(dp[nx][ny]==0 or dp[nx][ny]>dp[x][y]+a[nx][ny]):
                    dp[nx][ny]= a[nx][ny]+dp[x][y]
                    st.append((nx,ny))

    #print(dp)
    return(dp[n-1][n-1])

a2 = []
for grid in a:
    n=len(grid)
    m=len(grid[0])
    grid[0][0]="0"
    grid[n-1][m-1]="0"
    newgrid = [[int(x) for x in y] for y in grid]
    a2.append(newgrid)
#print(a2)

ans1 = 1
for grid in a2:
    #print(ans1fn(grid,n,m))
    ans1 = ans1 * ans1fn(grid,n,m)

print("ans1=",ans1)

ans2 = 1
for grid in a2:
    n=len(grid)
    m=len(grid[0])

    V = n*m*2
    source = 0 #0,1 are two sources
    sink = 2*((n*m)-1)+1

    uvwc = [(0,1,2,0,True),(sink-1,sink,2,0,True)]
    for i in range(n):
        for j in range(m):
            #print(i,j)
            ij = (i*m + j)*2
            if((i==0 and j==0) or (i==n-1 and j==m-1)):
                pass
            else:
                uvwc.append([ij,ij+1,1,grid[i][j],True])

            for nxy in orthoneighbours((i,j)):
                nx,ny = nxy
                if(nx>=0 and nx<n and ny>=0 and ny<m):
                    nxyij = (nx*m + ny)*2
                    uvwc.append([ij+1,nxyij,1,0,True])
                    #uvwc.append([nxyij+1,ij,1,0,True])
    E = len(uvwc)

    s,t = source,sink
    print(E,s,t,V)
    mf = Min_Cost_Max_Flow(V)
    #uvwc = [[0,1,2,1],[1,2,2,1],[0,2,1,1]]
    for i in range(E):
        u, v, w, c,flag = uvwc[i] #starting vertex, ending vertex, width, cost
        mf.add_edge(u, v, w, c,flag)
    res = mf.mcmf(s, t) #max flow, min cost
    print(res)
    #print(res[1])
    ans2=ans2*res[1]

print(ans2)