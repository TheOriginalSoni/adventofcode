#Day 1
from collections import Counter
#from aocd import get_data
#from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re

'''
lines = get_data(year=2024, day=1)
lines = lines.split("\n")
#'''

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

with open('2025/testcases.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ") for x in lines]

a=[]
for line in lines:
    line=line.strip()
    b = list(line)
    a.append(b)

#print(a)

N = len(a)
M = len(a[0])

print(N,M)

ans=0

for x in range(0,N):
    for y in range(0,M):
        if(a[x][y]=="@"):
            n=0
            d = neighbours((x,y))
            for curr in d:
                if(curr[0]>=0 and curr[0]<M and curr[1]>=0 and curr[1]<N):
                    if(a[curr[0]][curr[1]]=="@"):
                        n=n+1
            if(n<4):
                ans=ans+1
print(ans)

ans2=0
while(True):
    currans=0
    for x in range(0,N):
        for y in range(0,M):
            if(a[x][y]=="@"):
                n=0
                d = neighbours((x,y))
                for curr in d:
                    if(curr[0]>=0 and curr[0]<M and curr[1]>=0 and curr[1]<N):
                        if(a[curr[0]][curr[1]]=="@"):
                            n=n+1
                if(n<4):
                    ans2=ans2+1
                    currans=currans+1
                    a[x][y]="."
    if(currans==0):
        break
print(ans2)