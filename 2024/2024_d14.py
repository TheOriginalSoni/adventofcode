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

a=[]
for line in lines:
    line = line.replace('\n',"")
    line = line.replace("=",",")
    line = line.replace(" ",",")
    line=line.split(",")
    #print(line)
    a.append([(int(line[1]),int(line[2])),(int(line[4]),int(line[5]))])
    #a.append([int(x[2:]) for x in line])
print(a)

N,M=101,103
q1,q2,q3,q4=0,0,0,0
for t in range(N*M+20):
    a2=[]
    for b in a:
        b2x,b2y = b[0][0]+t*b[1][0],b[0][1]+t*b[1][1]
        b2x = b2x%N
        b2y=b2y%M
        while(b2x<0):
            b2x=b2x+N
        while(b2x>=N):
            b2x=b2x-N
        while(b2y<0):
            b2y=b2y+M
        while(b2y>=M):
            b2y=b2y-M
        if(b2x<N//2):
            if(b2y<M//2):
                q1=q1+1
            elif(b2y>M//2):
                q2=q2+1
            else:
                pass
        elif(b2x>N//2):
            if(b2y<M//2):
                q3=q3+1
            elif(b2y>M//2):
                q4=q4+1
            else:
                pass
        a2.append((b2x,b2y))
    
    if(len(set(a2))==len(a2)):
        #pretend all are unique
        print(t)
        for i in range(N):
            for j in range(M):
                if((i,j) in a2):
                    print("#",end="")
                    pass
                else:
                    print(" ",end="")
                    pass
            print()
    if(t%100==0):
        print(t)
    #time.sleep(2)

ans = q1*q2*q3*q4
print(ans)
