#Day 1
from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re

lines = get_data(year=2024, day=4)
lines = lines.split("\n")
#'''

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

#'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]
#'''

a = []
for line in lines:
    b=line.split()[0]
    a.append(b)

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1)]

n=len(a)
m=len(b)
print(n)
print(m)

ans1=0
for dir in dirs:
    for x in range(n):
        for y in range(m):
            if(x+3*dir[0]>=0 and x+3*dir[0]<n and y+3*dir[1]>=0 and y+3*dir[1]<m):
                if(a[x][y]=='X' and a[x+1*dir[0]][y+1*dir[1]]=='M' and a[x+2*dir[0]][y+2*dir[1]]=='A' and a[x+3*dir[0]][y+3*dir[1]]=='S'):
                    ans1=ans1+1
print(ans1)

a2=[]
count=0
for dir in dirs:
    for x in range(n):
        for y in range(m):
            if(x+1*dir[0]>=0 and x+1*dir[0]<n and y+1*dir[1]>=0 and y+1*dir[1]<m):
                if(x-1*dir[0]>=0 and x-1*dir[0]<n and y-1*dir[1]>=0 and y-1*dir[1]<m):
                    if(a[x][y]=='A' and a[x+1*dir[0]][y+1*dir[1]]=='S' and a[x-1*dir[0]][y-1*dir[1]]=='M'):
                        a2.append([(x,y),(dir)])

ans2=0
#print(a2)
for x in a2:
    for y in a2:
        if(x[0]==y[0]):
            if(x[1]!=y[1]):
                if(x[1][1]==0 or x[1][0]==0):
                    if(y[1][1]==0 or y[1][0]==0):   
                        pass
                    else:
                        pass
                else:
                    if(y[1][1]==0 or y[1][0]==0):
                        pass
                    else:
                        ans2=ans2+1

print(ans2//2)
