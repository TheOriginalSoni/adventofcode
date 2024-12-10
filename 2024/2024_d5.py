from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1)]

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

#'''
lines = get_data(year=2024, day=5)
lines = lines.split("\n")
#'''

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]
#'''

#=================================================

a1=[]
a2=[]
tag=0
for line in lines:
    line=line.replace("|",",")
    line=line.replace(' ',",")
    if(line==""):
        tag=1
    else:
        b=[int(x) for x in line.split(",")]
        if(tag==0):
            a1.append(tuple(b))
        else:
            a2.append(b)

ans1=0
ans2=0
for b in a2:
    cans=1
    for i1 in range(len(b)):
        for i2 in range(i1):
            if((b[i1],b[i2]) in a1):
                cans=0
                temp=b[i2]
                b[i2]=b[i1]
                b[i1]=temp
                #print(b,b[i2],b[i1])
    if(cans==1):
        ans1=ans1+b[len(b)//2]
    else:
        ans2=ans2+b[len(b)//2]

print(ans1)
print(ans2)