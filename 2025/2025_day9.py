from collections import Counter
from collections import defaultdict
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
from utils import *

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

def dist(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2 + abs(a1[2]-a2[2])**2

def isLeft(a, b, c):
  return (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])

#===============================================

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]
a = [[int(y) for y in x.split(",")] for x in lines]

ans1=0
answers = []
for i in range(len(a)):
    for j in range(len(a)):
        area = (abs(a[i][0]-a[j][0])+1)*(1+abs(a[i][1]-a[j][1]))
        answers.append([area,i,j])
        if(area>ans1):
            ans1=max(ans1,area)
            #print(area,a[i],a[j])

#print(a)
print(ans1)

a2 = a + [a[0]]

answers.sort()
#print(answers)
#for i in range(len(a)):
#

inside = [60000,60000]
#inside = [10,4]
i=len(answers)-1
while(i>0):
    area,i1,i2=answers[i]
    corners = [[a[i1][0],a[i1][1]],[a[i1][0],a[i2][1]],[a[i2][0],a[i1][1]],[a[i2][0],a[i2][1]]]
    #print(area,i1,i2,a[i1],a[i2])
    for ix in range(len(a)):
        flag=1
        for cx in corners:
            dir1 = isLeft(a2[ix],a2[ix+1],inside)
            dir2 = isLeft(a2[ix],a2[ix+1],cx)
            between=0
            if(a2[ix][0]==a2[ix+1][0]):
                if max(a2[ix][1],a2[ix+1][1]) >= cx[1] and cx[1] >= min(a2[ix][1],a2[ix+1][1]):
                    between=1
            else:
                if max(a2[ix][0],a2[ix+1][0]) >= cx[0] and cx[0] >= min(a2[ix][0],a2[ix+1][0]):
                    between=1

            if(dir1<0 and dir2 >0 and between):
                flag=0
                break
            elif(dir1>0 and dir2 <0 and between):
                flag=0
                break
        if(not flag):
            #print("-",ix,ix+1,a[ix],a[ix+1],cx)
            break
    if(flag):
        print(area,i1,i2,a[i1],a[i2])
        break            
    i=i-1