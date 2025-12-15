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

#===============================================

with open('2025/testcases.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]

a1 =[]
a2 =[]
b = []
for line in lines:
    if(line==""):
        continue
    if(line.find(":")>0):
        if(b!=[]):
            a1.append(b)
            b=[]
    else:
        b.append(line)
    if(line.find("x")>0):
        line=line.replace("x"," ")
        line=line.replace(": "," ")
        line=line.split(" ")
        line=[int(x) for x in line]
        a2.append([(line[0],line[1]),line[2:]])
        continue
    #print(line)

#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       print(a1)
#print(a2)

a11 = []
for curr in a1:
    s = "".join(curr)
    s2 = s.replace("#","")
    a11.append(len(s)-len(s2))

#print(a11)

ans1=0
ans12=0
for curr in a2:
    x,y = curr[0]
    currl = curr[1]
    #print(x,y,currl)
    s=0
    f1=0
    f2=0
    for i in range(len(a11)):
        s=s+currl[i]*a11[i]
    if ((x//3*y//3)>=sum(currl)):
        ans12=ans12+1
        f1=1
    if(x*y>s):
        ans1=ans1+1
        f2=1
    if(f1!=f2):
        print(x,y,currl)
    #sum(currl)

print(ans1)
print(ans12)