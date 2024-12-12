from collections import Counter
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
import sys
#from aocd import get_data
#from aocd import submit

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

with open('2024/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n',"") for x in lines]

a = []
for line in lines:
    b = [x for x in list(line)]
    a.append(b)

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
chars = list(set(sum(a, [])))

n=len(a)
m=len(a[0])
area={}
peri={}

visited=[[0 for x in range(m)] for y in range(n)]

ix = 0
ans1=0
for i in range(n):
    for j in range(m):
        if(visited[i][j]==0):
            peri[ix]=[]
            area[ix]=0
            st = []
            st.append((i,j))
            ca,cp=0,0
            while(len(st)>0):
                curr = st.pop()
                ci,cj=curr[0],curr[1]
                if(visited[ci][cj]==0):
                    visited[ci][cj]=1
                    x=a[ci][cj]
                    ca = ca+1
                    for d in dirs:
                        i1,j1=ci+d[0],cj+d[1]
                        if(i1>=0 and i1<n and j1>=0 and j1<m):
                            if(a[i1][j1]!=x):
                                cp=cp+1
                                peri[ix].append(((ci,cj),d))
                            elif(visited[i1][j1]==0):
                                st.append((i1,j1))
                        else:
                            cp=cp+1
                            peri[ix].append(((ci,cj),d))   
            ans1=ans1+(ca*cp)
            area[ix]=ca
            ix=ix+1

#Solution that got me AC
'''
ans2=0
for x in range(ix):
    currsides=list(set(peri[x]))
    ca=area[x]
    cp=0
    for d in dirs:
        pos = [y[0] for y in currsides if y[1]==d]
        temp=pos[0]
        if(d[0]==0):
            p1=(1,0)
            p2=(-1,0)
        else:
            p1=(0,1)
            p2=(0,-1)
        while(len(pos)>0):
            curr = pos.pop()
            xx=curr
            pos.append(curr)
            while(xx in pos):
                pos.remove(xx)
                xx=xx[0]+p1[0],xx[1]+p1[1]
            xx=curr
            pos.append(curr)
            while(xx in pos):
                pos.remove(xx)
                xx=xx[0]+p2[0],xx[1]+p2[1]
            cp = cp+1
    print(x,"Area=",ca,"Peri=",cp,"Ans=",ca*cp,"Pos=",temp,a[temp[0]][temp[1]])
    ans2=ans2+(ca*cp)
'''

#Figured it out later with help from friends
ans2=0
for x in range(ix):
    currsides=list(set(peri[x]))
    ca=area[x]
    cp=0
    for d in dirs:
        if(d[0]==0):
            perp=(1,0)
        else:
            perp=(0,1)
        pos = [y[0] for y in currsides if y[1]==d]
        for p in pos:
            if((p[0]+perp[0],p[1]+perp[1]) not in pos):
               cp=cp+1
    ans2=ans2+(cp*ca)

print(ans1)
print(ans2)
