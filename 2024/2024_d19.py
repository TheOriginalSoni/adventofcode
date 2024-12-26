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

a1=lines[0].replace('\n',"").replace(' ',"").split(",")
a2=[]
for line in lines[2:]:
    line = line.replace('\n',"")
    #line=list(line)
    a2.append(line)
#print(a)

print(a1)
N = max([len(x) for x in a1])
print(N)

print(a2)
#N = len(a)
#M=len(a[0])

ans1=0
for x in a2:
    poss=0
    curr = [0]*(len(x)+1)
    curr[0]=1
    for i1 in range(len(x)):
        for i2 in range(i1+1,len(x)+1):
            if(i2-i1<=N):
                t = x[i1:i2]
                #print(i1,i2,t)
                if(curr[i1] and t in a1):
                    curr[i2]=curr[i2]+curr[i1]
    if(curr[len(x)]):
        ans1=ans1+curr[len(x)]

print(ans1)