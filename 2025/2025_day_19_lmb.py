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

#print(a)

a = []
b=[]
for x in lines:
    if(x==""):
        a.append(b)
        b = []
        continue
    b.append([int(y) for y in list(x)])
a.append(b)

#print(a)

# ORIGINAL ANS1
def ans1fn(a):
    n = len(a)
    dp = [[0]*n for i in a] 
    st = [(0,0)]
    dp[0][0] = a[0][0]
 
    while(len(st)>0):
        curr = st.pop(0)
        x,y = curr
    
        nx = x+1
        ny = y
        if(nx >=0 and nx<n and ny>=0 and ny<n):
            if(dp[nx][ny]<dp[x][y]+a[nx][ny]):
                dp[nx][ny]= max(dp[nx][ny], a[nx][ny]+dp[x][y])
                st.append((nx,ny))

        nx = x
        ny = y+1
        if(nx >=0 and nx<n and ny>=0 and ny<n):
            if(dp[nx][ny]<dp[x][y]+a[nx][ny]):
                dp[nx][ny]= max(dp[nx][ny], a[nx][ny]+dp[x][y])
                st.append((nx,ny))

    #print(dp)
    return(dp[n-1][n-1])

ans1 = 1
for grid in a:
    xx = ans1fn(grid)
    ans1 = ans1 * xx

print(ans1)

# ANS1 AND AND2 COMBINED
def ans2fn(a,start,neighs):
    n = len(a)
    dp = [[0]*n for i in a] 
    startx,starty = start
    st = [start]
    dp[startx][starty] = a[startx][starty]
 
    while(len(st)>0):
        curr = st.pop(0)
        x,y = curr
        
        for (dx,dy) in neighs:
            nx=dx+x
            ny=dy+y
            if(nx >=0 and nx<n and ny>=0 and ny<n):
                if(dp[nx][ny]<dp[x][y]+a[nx][ny]):
                    dp[nx][ny]= max(dp[nx][ny], a[nx][ny]+dp[x][y])
                    st.append((nx,ny))
    return(dp)

ans11 = 1
ans2 = 1
for grid in a:
    n = len(grid)
    dp1 = ans2fn(grid,(0,0),[(0,1),(1,0)])
    dp2 = ans2fn(grid,(n-1,n-1),[(0,-1),(-1,0)])
    dp3 = ans2fn(grid,(n-1,0),[(0,1),(-1,0)])
    dp4 = ans2fn(grid,(0,n-1),[(1,0),(0,-1)])

    currans = 0
    for i in range(n):
        for j in range(n):
            if(i-1>=0 and i+1<n and j-1>=0 and j+1<n):
                t1 = dp1[i-1][j] + 2*grid[i][j] + dp2[i+1][j] + dp3[i][j-1] + dp4[i][j+1]
                currans = max(currans,t1)
                t2 = dp1[i][j-1] + 2*grid[i][j] + dp2[i][j+1] + dp3[i+1][j] + dp4[i-1][j]
                currans = max(currans,t2)
    ans11 = ans11 * dp1[n-1][n-1]
    ans2 = ans2*currans         
    #print(currans)

print(ans11)
print(ans2)

