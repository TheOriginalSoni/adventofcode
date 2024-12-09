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

with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]

a = []
for line in lines:
    #print(line)
    b=line.split()[0]
    a.append(b)

startpos=-1,-1
n=len(a)
m=len(b)
for i in range(len(a)):
    b=a[i]
    for j in range(len(b)):
        if(a[i][j]=='^'):
            startpos=(i,j)
            #a[i][j]='.'
startdir=(-1,0)
currdir = startdir
print("Start=",startpos)
currpos=startpos

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1)]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

def next_dir(currdir):
    x = dirs.index(currdir)
    if(x==len(dirs)-1):
        x=0
    else:
        x=x+1
    return dirs[x]

visited=[]
stopped_visited=[]
while(True):
    visited.append((currpos,currdir))
    newpos = (currpos[0]+currdir[0],currpos[1]+currdir[1])    
    if(newpos[0]>=0 and newpos[1]>=0 and newpos[0]<n and newpos[0]<m):
        if(a[newpos[0]][newpos[1]]!='#'):
            #visited.append(newpos)
            currpos=newpos
        else:
            stopped_visited.append((currpos,currdir))
            currdir=next_dir(currdir)
    else:
        break

visited_pos = list(set([x[0] for x in visited]))
print("Part1 = ",len(visited_pos))

ans = []
for xpos,xdir in visited:
    blocked_pos = (xpos[0]+xdir[0],xpos[1]+xdir[1])
    currpos=startpos
    currdir=startdir
    #currdir = next_dir(currdir)
    curr_loops = False
    new_visited=set()
    while(not curr_loops):
        if((currpos,currdir) in new_visited):
            curr_loops=True
            break
        new_visited.add((currpos,currdir))           
        newpos = (currpos[0]+currdir[0],currpos[1]+currdir[1])    
        if(newpos[0]>=0 and newpos[1]>=0 and newpos[0]<n and newpos[1]<m):
            if(a[newpos[0]][newpos[1]]!='#' and newpos != blocked_pos):
                #visited.append(newpos)
                currpos=newpos
            else:
                currdir=next_dir(currdir)
        else:
            break

    if(curr_loops):
        #print(curr_loops)
        #print("start",startpos,startdir,next_dir(startdir))
        #print("Curr",currpos,currdir)
        #print("Block=",blocked_pos)
        #print(new_visited)
        if(blocked_pos[0]>=0 and blocked_pos[1]>=0 and blocked_pos[0]<n and blocked_pos[0]<m):
            if(blocked_pos!=startpos and a[blocked_pos[0]][blocked_pos[1]]!='#'):
                ans.append(blocked_pos)

#print(visited)

ans = list(set(ans))
#print(ans)
print(len(ans))