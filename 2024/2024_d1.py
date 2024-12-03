#Day 1
from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re


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

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]
#'''

a = []
x1=[]
x2=[]
for line in lines:
    b=line.split()
    b = [int(x) for x in b]
    a.append(b)
    x1.append(b[0])
    x2.append(b[1])

x1.sort()
x2.sort()

#print(x1)
#print(x2)

ans1 = sum([abs(x1[x]-x2[x]) for x in range(len(x1))])
print(ans1)

ans2 = sum([x* x2.count(x) for x in x1])
print(ans2)