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

a={}
all = set()
for line in lines:
    b=line.split(": ")
    curr0 = b[0]
    curr1 = b[1].split(" ")
    a[curr0]=curr1
    all.add(curr0)
    for curr in curr1:
        all.add(curr)

all = list(all)
all.sort()

#print(a)
#print(all)

def ans1solver(start,end):
    ans1 = defaultdict(int)
    ans1[start]=1
    st = [start]
    while(len(st)>0):
        curr = st.pop(0)
        if(curr in a):
            neighs = a[curr]
            for n in neighs:
                ans1[n]=ans1[n]+1
                st.append(n)
    print(start,end,ans1[end])
    return ans1[end]

print(ans1solver("you","out"))
#print(ans1)

ans22 = ans1solver("dac","fft")
ans21 = ans1solver("fft","dac")

if(ans21 == 0):
    ans2 = ans1solver("svr","dac")*ans22*ans1solver("fft","out")
else:
    ans2 = ans1solver("svr","fft")*ans21*ans1solver("dac","out") 

print(ans2)
