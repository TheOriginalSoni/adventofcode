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

with open('2024/testcases.txt') as f:
    lines = f.readlines()

a1=[]
a2=[]
t = 0
for line in lines:
    line = line.replace('\n',"")
    line = line.replace(':',"")
    line = line.replace('-> ',"")
    line2=line.split(" ")
    if(len(line)==0 and t==0):
        t=1
    elif(t==0):
        a1.append(line2)
    else:
        a2.append(line2)

#print(a1)
#print(a2)

a_all = [x[0] for x in a1] + [x[0] for x in a2] + [x[2] for x in a2] + [x[3] for x in a2]
a_all = sorted(list(set(a_all)))

#print(a_all)

def values(a1,a2):
    #print(a1,a2)
    a_vals = [-1]*len(a_all)
    t = 0
    for x in a1:
        a_vals[a_all.index(x[0])] = int(x[1])
        t=t+1

    a_val_prev = a_vals.copy()
    while(t<len(a_all)):
        #print(a_vals)
        for x in a2:
            x1 = a_all.index(x[0])
            x2 = a_all.index(x[2])
            x3 = a_all.index(x[3])
            if(a_vals[x1] != -1 and a_vals[x2] != -1 and a_vals[x3]==-1):
                s=x[1]
                if(s=="OR"):
                    a_vals[x3]=max(a_vals[x1],a_vals[x2])
                elif(s=="AND"):
                    a_vals[x3]=min(a_vals[x1],a_vals[x2])
                elif(s=="XOR"):
                    a_vals[x3]=(a_vals[x1]+a_vals[x2])
                    if(a_vals[x3]==2):
                        a_vals[x3]=0
                else:
                    print("Error")
                t=t+1
        if(a_val_prev == a_vals):
            return -1
        a_val_prev = a_vals.copy()
    return a_vals

def extract_ans(avals1):
    #print(a_vals)
    #print(a_all)
    ans1 = 0
    pow = 0
    for x in range(len(a_all)):
        if(a_all[x][0]=="z"):
            #print(a_all[x],a_vals[x],ans1)
            ans1=ans1 + avals1[x] * (2**pow)
            pow=pow+1
            #ans1=ans1+str(a_vals[x])
    return ans1

avals1= values(a1,a2)
ans1 = extract_ans(avals1)
#ans1.reverse()
print(ans1)

def doesitblend(a1,a_all,a2):
    for a in range(len(a1)):
        a1[a][1]=0
    avals = values(a1,a2)
    if(avals == -1):
        return False
    ans2 = extract_ans(avals)
    if(ans2==0):
        return True
    return False

for x1 in range(len(a2)):
    for x2 in range(x1):
        for x3 in range(len(a2)):
            for x4 in range(x3):
                if(x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4):
                    a22 = a2.copy()
                    #print(a1)
                    #print(a22)
                    temp = a22[x1][3]
                    a22[x1][3] = a22[x2][3]
                    a22[x2][3] = temp
                    temp = a22[x3][3]
                    a22[x3][3] = a22[x4][3]
                    a22[x4][3] = temp
                    #print(x1,x2,x3,x4,a22[x1][3],a22[x2][3],a22[x3][3],a22[x4][3])
                    if(doesitblend(a1,a_all,a22)):
                        print("Y",x1,x2,x3,x4,a22[x1][3],a22[x2][3],a22[x3][3],a22[x4][3])



