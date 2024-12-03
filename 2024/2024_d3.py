#Day 1
from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re

lines = get_data(year=2024, day=3)
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

a = lines

a2 = []
for b in a:
    b1=re.findall(r'do\(\)|don\'t\(\)|mul\([0-9]+,[0-9]+\)',b)
    a2.append(b1)
    
for b in a2:
    print(b1)

ans1 = 0
for b in a2:
    for x in b:
        if(x=="do()"):
            pass
        elif(x=="don't()"):
            pass
        else:
            x2 = [int(z) for z in x[4:-1].split(',')]
            ans1 = ans1+(x2[0]*x2[1])

print(ans1)

ans2 = 0
valid=1
for b in a2:
    for x in b:
        if(x=="do()"):
            valid=1
        elif(x=="don't()"):
            valid=0
        else:
            x2 = [int(z) for z in x[4:-1].split(',')]
            if(valid):
                ans2 = ans2+(x2[0]*x2[1])

print(ans2)
