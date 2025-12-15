from collections import Counter
from collections import defaultdict
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
from utils import *
import math
from math import gcd,lcm
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
lines=[x.replace(":","") for x in lines]
lines = [x.split(" ") for x in lines]

minx = 999999999999999999999999
for line in lines:
    if(line[0]=="receive"):
        line[1]=int(line[1])
        minx = min(minx,line[1])
    #print(line)

i=1
ans1=0
lowerh = []
upperh = []
for line in lines:
    if(line[0]=="receive"):
        if(len(upperh)==0 or line[1]>upperh[0]):
            heapq.heappush(upperh,line[1])
        else:
            heapq.heappush(lowerh,-1*line[1])

        if(len(upperh)>len(lowerh)+1):
            x = heapq.heappop(upperh)
            heapq.heappush(lowerh,-1*x)
        elif(len(lowerh)>len(upperh)):
            x = heapq.heappop(lowerh)
            heapq.heappush(upperh,-1*x)
        #print(line[1],lowerh,upperh)
    else:
        elem = heapq.heappop(upperh)
        if(len(upperh)>len(lowerh)+1):
            x = heapq.heappop(upperh)
            heapq.heappush(lowerh,-1*x)
        elif(len(lowerh)>len(upperh)):
            x = heapq.heappop(lowerh)
            heapq.heappush(upperh,-1*x)

        ans1=ans1+(i*elem)
        i=i+1
#'''
print(ans1)

i=1
ans2=0
lowerh = []
lowerhn = 0
upperh = []
upperhn = 0

def heap_balance():
    global lowerh
    global lowerhn
    global upperh
    global upperhn
        
    if(upperhn>lowerhn+1):
        rem = ((upperhn+lowerhn)//2)-lowerhn
        while(rem >= upperh[0][1]):
            x = heapq.heappop(upperh)
            if(lowerhn>0 and lowerh[0][0]==-1*x[0]):
                lowerh[0] = (lowerh[0][0],lowerh[0][1]+x[1])
            else:
                heapq.heappush(lowerh,(-1*x[0],x[1]))
            rem=rem-x[1]
            upperhn -= x[1]
            lowerhn += x[1]
        
        x = upperh[0]
        if(lowerhn >0 and lowerh[0][0]==-1*x[0]):
            lowerh[0] = (lowerh[0][0],lowerh[0][1]+rem)
            upperh[0] = (upperh[0][0],upperh[0][1]-rem)
            lowerhn += rem
            upperhn -= rem
        else:
            upperh[0] = (upperh[0][0],upperh[0][1]-rem)
            heapq.heappush(lowerh,(-1*x[0],rem))
            lowerhn += rem
            upperhn -= rem
    elif(upperhn<lowerhn):
        rem = lowerhn - ((upperhn+lowerhn)//2)
        while(lowerhn>0 and rem >= lowerh[0][1]):
            x = heapq.heappop(lowerh)
            if(upperh[0][0]==-1*x[0]):
                upperh[0] = (upperh[0][0],upperh[0][1]+x[1])
            else:
                heapq.heappush(upperh,(-1*x[0],x[1]))
            rem=rem-x[1]
            upperhn += x[1]
            lowerhn -= x[1]
        
        x = lowerh[0]
        if(upperhn > 0 and upperh[0][0]==-1*x[0]):
            lowerh[0] = (lowerh[0][0],lowerh[0][1]-rem)
            upperh[0] = (upperh[0][0],upperh[0][1]+rem)
            lowerhn -= rem
            upperhn += rem
        else:
            lowerh[0] = (lowerh[0][0],lowerh[0][1]-rem)
            heapq.heappush(upperh,(-1*x[0],rem))
            lowerhn -= rem
            upperhn += rem

for line in lines:
    if(line[0]=="receive"):
        curr = line[1]
        if(len(upperh)==0 or curr>upperh[0][0]):
            heapq.heappush(upperh,(curr,curr))
            upperhn += curr
        else:
            heapq.heappush(lowerh,(-1*curr,curr))
            lowerhn += curr
        heap_balance()
    else:
        x = upperh[0]
        elem = x[0]
        if(x[1]==1):
            heapq.heappop(upperh)
        else:
            upperh[0] = (upperh[0][0],upperh[0][1]-1)
            upperhn -= 1
        
        ans2=ans2+(i*elem)
        i=i+1
        heap_balance()
        print(i,lowerhn,upperhn)

print(ans2)