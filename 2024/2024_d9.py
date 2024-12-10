from collections import Counter
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
import sys

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

lines = [x.replace('\n'," ") for x in lines]

a = []
for line in lines:
    #print(line)
    b=[int(x) for x in list(line.split()[0])]
    a = b

L = sum(a)+1
print("arr length=",L)

arr = [-1]*(L+1)
#print(arr)

idx = 0 #0-1-2-...
loc = 0 #location
place = []
unplace=[]
par = 1
for b in a:
    if(par == 1):
        for x in range(b):
            #print(loc,x)
            arr[loc+x] = idx
        par=0
        idx = idx+1
        unplace.append((loc,b))
        loc = loc+b
    else:
        place.append((loc,b))
        loc = loc+b
        par = 1

#print(arr)

arr1=arr.copy()
point=0
for x in range(len(arr1)-1,0,-1):
    if(arr1[x]!=-1):
        while(arr1[point]!=-1):
            point = point+1
        if(x>point):
            arr1[point]=arr1[x]
            arr1[x]=-1
        else:
            break
ans1 = 0

for x in range(len(arr1)):
    if(arr1[x]==-1):
        break
    ans1=ans1+(x*arr1[x])

#print(a)
print(ans1)

y=0
while(y<len(place)-1):
    if(place[y][0]+place[y][1]==place[y+1][0]):
        print(place[y],place[y+1])
        place[y] = (place[y][0],place[y+1][1]+place[y][1])
        place.pop(y+1)
    else:
        y=y+1

arr2=arr.copy()
#print(arr2)
for ix in range(len(unplace)-1,0,-1):
    for iy in range(len(place)):
        y = place[iy]
        x = unplace[ix]
        if(y[1]>=x[1] and y[0]<x[0]):
            #print(y,x,arr[y[0]],arr[x[0]])
            for z in range(x[1]):
                arr2[y[0]+z]=arr2[x[0]+z]
                arr2[x[0]+z]=-1
            y=(y[0]+x[1],y[1]-x[1])
            place[iy]=y
            break

#print(arr2)
ans2= 0
for x in range(len(arr2)):
    if(arr2[x]==-1):
        pass
    else:
        ans2=ans2+(x*arr2[x])
print(ans2)