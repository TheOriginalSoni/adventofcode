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

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ") for x in lines]

a=[]
for line in lines:
    line=line.strip()
    b = [int(x) for x in list(line)]
    a.append(b)

#PART 1, OLD
ans=0
for b in a:
    best = 0
    for x1 in range(len(b)):
        for x2 in range(x1+1,len(b)):
            best = max(best,b[x1]*10+b[x2])
    ans=ans+best
print(ans)

#PART 2 and 1 kinda
def solve(N):
    ans2 = 0
    for b in a:
        l=0
        r=len(b)
        bestbest=0
        for m in range(N):
            best=b[l]
            newl=l
            for x in range(l,r):
                if(x<len(b)-N+1+m):
                    if(best<b[x]):
                        best=b[x]
                        newl=x
            bestbest=bestbest*10+best
            l=newl+1
        #print(bestbest)
        ans2=ans2+bestbest
    return ans2

ans = solve(2)
print(ans)

ans2 = solve(12)
print(ans2)