from collections import Counter
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
import sys

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

'''
lines=[] 
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    else:
        lines.append(line)
'''

'''
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

with open('testcases2.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]

a = []
for line in lines:
    line = list(line)
    #print(line)
    a.append(line)

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
m = {}
for c in chars:
    m[c]=[]

for i in range(len(a)):
    b=a[i]
    for j in range(len(b)):
        if(b[j] in chars):
            m[b[j]].append((i,j))

#print(m)
N = len(a)
M = len(a[0])
print(N,M)

ans = set()
for x in m:
    l = m[x]
    if(len(l)<=1):
        continue
    for i in range(len(m[x])):
        for j in range(i):
            val1 = m[x][i]
            val2 = m[x][j]
            x1 = (val1[0]+val1[0]-val2[0],val1[1]+val1[1]-val2[1])
            if(x1[0]>=0 and x1[0]<N and x1[1]>=0 and x1[1]<M):
                #if(a[x1[0]][x1[1]]=="."):
                ans.add(x1)
            x2 = (val2[0]+val2[0]-val1[0],val2[1]+val2[1]-val1[1])
            if(x2[0]>=0 and x2[0]<N and x2[1]>=0 and x2[1]<M):
                #if(a[x2[0]][x2[1]]=="."):
                ans.add(x2)
#print(a)
#print(ans)
print(len(ans))

#print(a)

ans2 = set()
for x in m:
    l = m[x]
    if(len(l)<=1):
        continue
    for i in range(len(m[x])):
        for j in range(i):
            val1 = m[x][i]
            val2 = m[x][j]
            x1 = (val1[0],val1[1])
            while(x1[0]>=0 and x1[0]<N and x1[1]>=0 and x1[1]<M):
                ans2.add(x1)
                x1 = (x1[0]+val1[0]-val2[0],x1[1]+val1[1]-val2[1])
            x1 = (val2[0],val2[1])
            while(x1[0]>=0 and x1[0]<N and x1[1]>=0 and x1[1]<M):
                ans2.add(x1)
                x1 = (x1[0]+val2[0]-val1[0],x1[1]+val2[1]-val1[1])

print(len(ans2))
