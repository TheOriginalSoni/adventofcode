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
#dirs_8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1)]

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
M = len(a[0])

node=[]
start=(-1,-1)
end=(-1,-1)
for i in range(N):
    for j in range(M):
        if(a[i][j]=='S'):
            start=(i,j)
        if(a[i][j]=='E'):
            end = (i,j)
        if(a[i][j]!='#'):
            node.append((i,j))

print("start=",start)
print("end=",end)
print("len=",len(node))
#print(node)

st = []
startd={}
startd[start]=0
st.append(start)

while(len(st)>0):
    currpos=st.pop()
    for d in dirs:
        newpos = (currpos[0]+d[0],currpos[1]+d[1])
        if(newpos[0]>=0 and newpos[0]<N and newpos[1]>=0 and newpos[1]<M):
            if(a[newpos[0]][newpos[1]]!='#'):
                if(newpos in startd and startd[newpos]<=startd[currpos]+1):
                    pass
                else:
                    startd[newpos]=startd[currpos]+1
                    st.append(newpos)

#print(startd)
#print(startd[end])

st = []
endd={}
endd[end]=0
st.append(end)

while(len(st)>0):
    currpos=st.pop()
    for d in dirs:
        newpos = (currpos[0]+d[0],currpos[1]+d[1])
        if(newpos[0]>=0 and newpos[0]<N and newpos[1]>=0 and newpos[1]<M):
            if(a[newpos[0]][newpos[1]]!='#'):
                if(newpos in endd and endd[newpos]<=endd[currpos]+1):
                    pass
                else:
                    endd[newpos]=endd[currpos]+1
                    st.append(newpos)

print("Path=",endd[start])

ans1=0
ansx = {}
for x in node:
    for d1 in dirs:
        for d2 in dirs:
            y=(x[0]+d1[0]+d2[0],x[1]+d1[1]+d2[1])
            if(y[0]>=0 and y[0]<N and y[1]>=0 and y[1]<M):
                if(y in node):
                    if(startd[x]<startd[y]):
                        if(startd[x]+endd[y]+2< startd[end]):
                            currans=-1*(startd[x]+endd[y]+2-startd[end])
                            if(currans in ansx):
                                ansx[currans]=ansx[currans]+1
                            else:
                                ansx[currans]=1
                            #print(x,y,currans)
                            if(currans>=100):
                                ans1=ans1+1
#print(ansx)

ak = sorted(list(ansx.keys()))
for x in ak:
    #print(x,"=",ansx[x])
    pass

print(ans1)


