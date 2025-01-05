from collections import Counter
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
import sys
#from aocd import get_data
#from aocd import submit
import numpy as np
import time

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

with open('2024/testcases.txt') as f:
    lines = f.readlines()

a1=[]
a2=[]
t = 0
for line in lines:
    line = line.replace('\n',"")
    #line = line.replace("=",",")
    line = line.replace(" ",",")
    line=list(line)
    if(len(line)==0):
        t=1
    elif(t==0):
        a1.append(line)
    else:
        a2.append(line)
    #print(line)
    #a.append([(int(line[1]),int(line[2])),(int(line[4]),int(line[5]))])
    #a.append([int(x[2:]) for x in line])
a2 = sum(a2, [])

print(a1)
print(a2)

N=len(a1)
M=len(a1[0])

a12 = []
for i in range(N):
    atemp = ""
    for j in range(M):
        if(a1[i][j]=="@"):
            #a1[i][j]="."
            start=(i,j)
        if(a1[i][j]=="@"):
            atemp = atemp + ("@.")
        elif(a1[i][j]=="#"):
            atemp = atemp + ("##")
        elif(a1[i][j]=="."):
            atemp = atemp + ("..")
        elif(a1[i][j]=="O"):
            atemp = atemp + ("[]")
        else:
            print("error")
    a12.append(list(atemp))

def display():
    for i in range(N):
        for j in range(M):
            print(a1[i][j],end="")
        print()

a11 = a1.copy()
a1 = a12.copy()

M=M*2
start=(i,j*2)

display()
curr=start
for x in a2:
    if(x=="^"):
        dir=(-1,0)
    elif(x=="v"):
        dir=(1,0)
    elif(x==">"):
        dir=(0,1)
    elif(x=="<"):
        dir=(0,-1)
    else:
        print("Error")
    
    newpos = (curr[0]+dir[0],curr[1]+dir[1])
    xpos=curr
    #print(x,dir)
    #print(dir)
    while(a1[xpos[0]][xpos[1]]=="[" or a1[xpos[0]][xpos[1]]=="]" or a1[xpos[0]][xpos[1]]=="@"):
        xpos=(xpos[0]+dir[0],xpos[1]+dir[1])
    if(a1[xpos[0]][xpos[1]])=="#":
        pass
    elif(a1[xpos[0]][xpos[1]]=="."):
        a1[curr[0]][curr[1]]="."
        x2pos = (curr[0]+dir[0],curr[1]+dir[1])
        if(a1[x2pos[0]][x2pos[1]]=="O"):
           a1[xpos[0]][xpos[1]]="O"
        a1[curr[0]+dir[0]][curr[1]+dir[1]]="@"
        curr = (curr[0]+dir[0],curr[1]+dir[1])
        #print(curr,dir)
        #print(xpos)
        #print(x2pos)
        #display()
    else:
        print("Error")
    
display()

ans1=0
for i in range(N):
    for j in range(M):
        if(a1[i][j]=="O"):
            ans1 = ans1+(100*i+j)

print(ans1)