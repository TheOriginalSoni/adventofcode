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
lines = [x.replace('\n'," ").strip() for x in lines]

#print(lines)

a1=[]
a2=[]
flag=0
for x in lines:
    if(x==""):
        flag=1
        continue
    if(flag):
        a2=a2+[int(x)]
    else:
        a1=a1+[[int(y) for y in x.split("-")]]

'''
#PART 1
ans=0
for x in a2:
    curr = 0
    for y in a1:
        if(y[0]<=x and y[1]>=x):
            curr=1
        if(curr==1):
            break 
    ans=ans+curr
print(ans)

#PART 2
a1.sort()

b1 = a1.copy()
c1 = []
while(len(b1)>0):
    ax=b1[0]
    b1.remove(ax)
    flag=1
    while(flag==1):
        flag=0
        for y in b1:
            ay = y
            if (ax[0]<=ay[0] and ax[1]>=ay[1]):
                b1.remove(ay)
                flag=1
            elif (ax[0]<=ay[0] and ax[1]>=ay[0]):
                ax[1]=ay[1]
                b1.remove(ay)
                flag=1    
    c1.append(ax)

ans2 = 0
for x in c1:
    ans2=ans2+x[1]-x[0]+1

print(ans2)

#PART 2, BETTER METHOD with interval tracking
d1 = []
for x in a1:
    d1.append([x[0],1])
    d1.append([x[1]+1,-1])

d1.sort()

flag = 0
curr = d1[0][0] 
prev = d1[0][0]

ans3=0
for x in d1:
    curr = x[0]
    if(flag>0):
        ans3=ans3+curr-prev
    flag=flag+x[1]
    prev = curr

print(ans3)
'''

a1.sort()
print(a1)
ax = None
c1 = []

for y in a1:
    print(f"{y} - {ax} \t={c1}")
    if ax is None:
        ax = y
    else:
        ay = y
        if (ax[0]<=ay[0] and ax[1]>=ay[1]):
            pass
        elif (ax[0]<=ay[0] and ax[1]>=ay[0]):
            ax[1]=ay[1]
        else:
            c1.append(ax)
            ax = y

if ax is not None:
    c1.append(ax)

ans2 = 0
for x in c1:
    ans2=ans2+x[1]-x[0]+1

print(ans2)