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

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
dirs_8 = []

#===============================================
M = 10000000000000

with open('2024/testcases2.txt') as f:
    lines = f.readlines()

a=[]
for line in lines:
    line = line.replace('\n',"")
    line=list(line)
    a.append(line)
#print(a)

N = len(a)
M=len(a[0])

start=(-1,-1)
end=(-1,-1)
for i in range(N):
    for j in range(M):
        if(a[i][j]=="S"):
            start=(i,j)
        if(a[i][j]=="E"):
            end=(i,j)

st = set()
st.add((start,2,0))

bestscore = [[[-1 for d in dirs] for i in b] for b in a]
#bestscore[start[0]][start[1]][3] = 0

while(len(st)>0):
    print(len(st))
    (curr,currd,currscore) = st.pop()
    #print(curr,currd,currscore)
    if(bestscore[curr[0]][curr[1]][currd]==-1 or bestscore[curr[0]][curr[1]][currd]>currscore):
        bestscore[curr[0]][curr[1]][currd] = currscore
        for d in range(len(dirs)):
            if abs(currd-d)==0:
                pass
            elif(abs(currd-d)==2):
                st.add((curr,d,currscore+2000))
            else:
                st.add((curr,d,currscore+1000))
        dx=dirs[currd]
        newpos = (curr[0]+dx[0],curr[1]+dx[1])
        if(newpos[0]>=0 and newpos[0]<N and newpos[1]>=0 and newpos[1]<M):
            if(a[newpos[0]][newpos[1]]!="#"):
                st.add((newpos,currd,currscore+1))
    else:
        pass

ans1 = -1
for d in range(len(dirs)):
    if(ans1==-1):
        ans1=bestscore[end[0]][end[1]][d]
    ans1=min(ans1,bestscore[end[0]][end[1]][d])

print(ans1)


for i in range(N):
    for j in range(M):
        ax = 10**10
        for d in range(len(dirs)):
            ax = min(ax,bestscore[i][j][d])
        #print(ax,end="")
        #print("\t",end="")
    #print()

#print(ans1)

ans2_key=set()
for d in range(len(dirs)):
    if(bestscore[end[0]][end[1]][d]==ans1):
        ans2_key.add((end,d))

while(len(ans2_key)>0):
    curr,currd = ans2_key.pop()
