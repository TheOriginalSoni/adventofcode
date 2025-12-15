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

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]

a1=[]
a2=[]
a3=[]
for line in lines:
    line=line.replace("[","")
    line=line.replace("] ","\t")
    line=line.replace(" {","\t")
    line=line.replace("}","")
    line=line.split("\t")
    line[0]=list(line[0])
    line[0]=[0 if x=="." else 1 for x in line[0]]
    line[1]=line[1].replace("(","")
    line[1]=line[1].replace(")","")
    line[1]=line[1].split(" ")
    line[1]=[[int(z) for z in y.split(",")] for y in line[1]]
    line[2]=[int(y) for y in line[2].split(",")]
    a1.append(line[0])
    a2.append(line[1])
    a3.append(line[2])
#a = [[y for y in x.split("")] for x in lines]

#print(a1)
#print(a2)
#print(a3)

ans1=0
for i in range(len(a1)):
    currans=-1
    ax1 = a1[i]
    ax2 = a2[i]
    nx = len(ax2)
    #curr = [0]*len(ax1)
    for jx in range(2**nx):
        curr = [0]*len(ax1)
        binary_string = [int(x) for x in list(format(jx, f'0{nx}b'))]
        #print(jx,binary_string,curr)
        for b in range(nx):
            if(binary_string[b]==1):
                elem = ax2[b]
                for kx in elem:
                    curr[kx]=1-curr[kx]
            else:
                pass
        if(curr==ax1):
            #print(jx,binary_string,i,ax1,ax2,curr)
            if(currans==-1):
                currans = sum(binary_string)
            else:
                currans=min(sum(binary_string),currans)
            '''
            for b in range(nx):
                if(binary_string[b]==1):
                    pass
                    #print(ax2[b],end="\t")
            #print()
            '''
    #print(currans)
    ans1 = ans1+currans
print(ans1)    


ans2 = 0
for i in range(len(a1)):
    currans=-1
    ax3 = a3[i]
    ax2 = a2[i]
    nx2 = len(ax2)
    nx3 = len(ax3)
    st = [[tuple([0]*nx3),0]]
    print(ax2,ax3,st)
    bestvals = {}
    while(len(st)>0):
        currt,currval = st.pop(0)
        if(currt in bestvals and currval > bestvals[currt]):
            continue
        
        print(len(st),currval,currt)
        
        for j in range(nx2):
            nextt = list(currt).copy()
            for k in ax2[j]:
                nextt[k]=nextt[k]+1
            nextval=currval+1
            nextt = tuple(nextt)
            if(nextt not in bestvals or nextval < bestvals[nextt]):
                #print(nextt,nextval,ax2)
                flag=1
                for k in range(nx3):
                    if(ax3[k]<nextt[k]):
                        flag=0
                if(flag):
                    bestvals[nextt]=nextval
                    st.append([nextt,nextval])
            #if(bestvals[nextt]>nextval):
    print(ax3,bestvals[tuple(ax3)])
    ans2 = ans2 + bestvals[tuple(ax3)]

print(ans2)
            #nextt[]
#for val in bestvals:
#    print(val,bestvals[val])

