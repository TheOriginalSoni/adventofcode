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

with open('2025/testcases.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]

#print(a)
lines = [x.replace("Pattern:","").replace("String:","") for x in lines]
lines = lines[1:]

flag = 0
a = []
b=[]
for x in lines:
    if(x==""):
        flag=1
        continue
    if(flag==0):
        a.append(list(x))
    else:
        b = list(x)

print(a)
print(b)

ans1 = 0
for x in a:
    flag=1
    #print(x)
    #print(b)
    for i in range(len(x)):
        if(x[i]=="?" or x[i]==b[i]):
            pass
        else:
            flag=0
    ans1 += flag

print(ans1)

a2 = [y for y in x for x in a]

dp = []
for i in range(len(a2)):
    b = []
    for j in range(len(a)):
        b.append(0)
    dp.append(b.copy())
print(dp)

dp = [0]*len(a2)
ans2 = 0
#print(a2)

for i in range(len(a2)):
    flag=1    
    for j in range(len(b)):
        if(i+j>= len(a2)):
            flag=0
            break
        if(a2[i+j]=="?" or a2[i+j]==b[j]):
            pass
        else:
            flag=0
    ans2 += flag

    if(False):
        for j in range(len(b)):
            if(a2[i+j]=="?"):
                a2[i+j]=b[j]

print(ans2)