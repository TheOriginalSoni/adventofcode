from collections import Counter
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
import sys
#from aocd import get_data
#from aocd import submit
import numpy as np

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

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
dirs_8 = []

#===============================================
M = 10000000000000

with open('2024/testcases.txt') as f:
    lines = f.readlines()

a=[]
for line in lines:
    line = line.replace('\n',"")
    line = line.replace("Button A: ","")
    line = line.replace("Button B: ","")
    line=line.replace(",","")
    line=line.replace("Prize: ","")
    line=line.split()
    a.append([int(x[2:]) for x in line])
print(a)

a21=[]
a22=[]
ix = 0
while(ix<len(a)):
    p1 = a[ix]
    p2 = a[ix+1]
    p3 = a[ix+2]
    a21.append((p1,p2,[p3[0],p3[1]]))
    a22.append((p1,p2,[p3[0]+M,p3[1]+M]))
    ix=ix+4

print(a22)

ans1=0
for b in a21:
    b1 = b[0]
    b2 = b[1]
    bans = b[2]
    valid=0
    cans=0
    for x in range(105):
        for y in range(105):
            if(b1[0]*x + b2[0]*y == bans[0] and b1[1]*x + b2[1]*y == bans[1]):
                if(valid==0):
                    cans = 3*x+y
                else:
                    cans = min(cans,3*x+y)
    ans1=cans+ans1
    #print(cans)
print(ans1)

ans2=0
for b in a21:
    b1 = b[0]
    b2 = b[1]
    bans = b[2]
    det=b1[0]*b2[1]-b2[0]*b1[1]
    cans=0
    if(det==0):
        if(b1[0]<b2[0]):
            bm=b1
            bM=b2
        else:
            bm=b2
            bM=b1
        if(bans[0] % bm[0] == 0):
            n = bans[0] // bm
            if(n*bm[1]==bans[1]):
                cans = n
            else:
                cans=0
        else:
            cans=0
    else:
        b12 = np.array([b1,b2])
        bans = np.transpose(np.array(bans))
        print(b12,bans)
        x = np.linalg.solve(b12,bans)
        print(x)
        cans = x[0]*3+x[1]
        #Non determinant
        if(np.allclose(np.dot(b12, x), bans) and abs(np.rint(x[0])-x[0])<0.01 and abs(np.rint(x[1])-x[1])<0.01):
            ans2=ans2+int(round(cans))
            print(cans)
        print()
print(ans2)
