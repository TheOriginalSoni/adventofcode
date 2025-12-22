from collections import Counter
from collections import defaultdict
from functools import reduce
from functools import cmp_to_key
from functools import cache
from utils import *
from math import gcd,lcm
import re
import math
import heapq
import itertools

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

def orthoneighbours(xy):
    x,y=xy
    return [(x-1,y),(x,y-1),(x,y+1),(x+1,y)]

def dist(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2 + abs(a1[2]-a2[2])**2

def dist2D(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2


#===============================================

# Solving AoL from LMB!
# https://lovemathboy.github.io/day15.html

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]

a=[]
b=[]
for line in lines:
    #line=list(line) #.split(" ")
    if(line == ""):
        a.append(b)
        b=[]
    else:
        line=line.split(":")
        line=line[-1]
        if(line!=""):
            b.append(int(line))

a.append(b)

#print(a)

def permute(arr, mindig, n, div):
    ans = -1
    if(len(arr)<n):
        for i in range(mindig,10):
            currans = permute(arr+[i], i, n, div)
            if(currans != -1):
                if(ans==-1 or currans<ans):
                    ans = currans
        return ans
    allperms = list(itertools.permutations(arr))
    for currperm in allperms:
        if(currperm[0]!=0):
            currnum = int("".join([str(x) for x in currperm]))
            if(currnum % div ==0):
                if(ans ==-1 or currnum<ans):
                    ans=currnum
    return ans

'''
ans1 = 0
for x in a:
    dig = x[0]
    div = x[1]
    ansnotfound = 1
    n = 1
    while(ansnotfound):
        minx = (n+1)//2
        arr  = [dig]*minx
        currans = permute(arr, 0, n, div)
        if(currans!=-1):
            print(x,currans)
            ans1 = ans1+currans
            ansnotfound=0
        n+=1
        #print("-",x,n)
        #for i in range(minx,n):
        #    arr = [dig]*i
        #    #for j in range(

print(ans1)
'''

ans2 = 0
for x in a:
    favdig = x[0]
    favdiv = x[1]
    dp = []
    dp.append(defaultdict(int))
    dp.append(defaultdict(int))
    
    for i in range(1,10):
        currremain = i%favdiv
        if(i == favdig):
            dp[1][(1,currremain)] += 1
        else:
            dp[1][(0,currremain)] +=1

    for n in range(2,16+1):
        dp.append(defaultdict(int))    
        for keys in dp[n-1]:
            currfav,currremain = keys
            for i in range(0,10):
                newremain = (currremain*10 + i)%favdiv
                if(i == favdig):
                    dp[n][(currfav+1,newremain)] += dp[n-1][(currfav,currremain)]
                else:
                    dp[n][(currfav,newremain)] += dp[n-1][(currfav,currremain)]

    currans = 0
    for n in range(8,16+1):
        for keys in dp[n]:
            favdigs,curr_remain = keys
            if(curr_remain == 0 and favdigs >= (n+1)//2):
                currans += dp[n][(favdigs,curr_remain)]
    ans2 += currans

print(ans2)