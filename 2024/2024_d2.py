#Day 2
from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re


lines = get_data(year=2024, day=2)
lines = lines.split("\n")
#'''

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]
#'''


a = []
for line in lines:
    b=line.split()
    b = [int(x) for x in b]
    #strip().replace(":","").split(" ")
    a.append(b)

#for b in a:
#    print(b)

#print(len(b))

#print (line)

x1=[]
x2=[]

ans1 = 0
for x in range(len(a)):
    b=a[x]
    b2 = b
    safe = 1
    if(sorted(b2) == b2 or sorted(b2) == b2[::-1]):
        safe=1
    else:
        safe=0
    for y in range(len(b2)-1):
        if(abs(b2[y]-b2[y+1])>3 or abs(b2[y]-b2[y+1])<1):
            safe=0
    ans1=ans1+safe

print(ans1)

ans2 = 0
for x in range(len(a)):
    b=a[x]
    safe_full = 0
    for y in range(len(b)):
        b2 = b[0:y] + b[y+1:]
        safe = 1
        if(sorted(b2) == b2 or sorted(b2) == b2[::-1]):
            safe=1
        else:
            safe=0
        for y in range(len(b2)-1):
            if(abs(b2[y]-b2[y+1])>3 or abs(b2[y]-b2[y+1])<1):
                safe=0
        safe_full=max(safe,safe_full)
    ans2=ans2+safe_full

print(ans2)
