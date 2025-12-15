from collections import Counter
from collections import defaultdict
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
from utils import *
import math
from math import gcd,lcm

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

def dist(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2 + abs(a1[2]-a2[2])**2

#===============================================

# Solving AoL from LMB!
# https://lovemathboy.github.io/day14.html

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]
lines=[x.replace(":","") for x in lines]
lines = [x.split(" ") for x in lines]

a = {}
for line in lines:
    a[line[0]]= line[1:]

def returnans1(number):
    nums = defaultdict(int)
    st = ["INP"]
    nums["INP"] = number

    while(len(st)>0):
        curr = st.pop(0)
        currnum = nums[curr]
        if(currnum==0 or curr=="OUT"):
            continue
        neighs = a[curr]
        n = len(neighs)
        for i in range(n):
            div = (i+currnum) // n
            if (neighs[i]=="BIN"):
                pass
            else:
                nums[neighs[i]] += div
                st.append(neighs[i])
        nums[curr]=0
    return(nums["OUT"])

#print(returnans1(123456))
#print(returnans1(12**3456))

def returnans2():
    nums = {}
    st = ["INP"]
    nums["INP"] = (1,1)
    while(len(st)>0):
        curr = st.pop(0)
        currnum_n,currnum_d = nums[curr]
        if(currnum_n==0 or curr=="OUT"):
            continue
        neighs = a[curr]
        n = len(neighs)
        for i in range(n):
            ni = neighs[i]
            #div = (i+currnum) // n
            if (ni=="BIN"):
                pass
            else:
                if(ni not in nums or nums[ni][0]==0):
                    nums[ni] = (currnum_n,currnum_d*n)
                else:
                    prev_n, prev_d = nums[ni]
                    new_d = lcm(prev_d,currnum_d*n)
                    new_n = (currnum_n * new_d)//(currnum_d*n) + (prev_n* new_d)//(prev_d)
                    nums[ni] = (new_n,new_d)
                st.append(neighs[i])
        nums[curr]=(0,1)
        ax = []
        for num in nums:
            if(nums[num][0]!=0):
                ax.append((num,nums[num]))
    return(nums["OUT"])

num,den = returnans2()
ans1 = num * 12**56 // den
for i in range(3400):
    ans1 = ans1 * 12
    ans1 = int(str(ans1)[-15:])

print(ans1)
