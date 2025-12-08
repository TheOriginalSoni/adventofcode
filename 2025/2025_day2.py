#Day 1
from collections import Counter
#from aocd import get_data
#from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re

'''
lines = get_data(year=2024, day=1)
lines = lines.split("\n")
#'''

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

with open('2025/testcases2.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ") for x in lines]
lines = lines[0].split(",")
#'''

a=[]
for line in lines:
    b = line.split("-")
    b = [int(x) for x in b]
    a.append(b)

#PART 1 was done initially on Google Sheets and manual

#PART 2, original logic took 15s
ans2 = 0
for curra in a:
    b1 = curra[0]
    b2 = curra[1]
    #l = max(len(b1,b2))
    for x in range(b1,b2+1):
        newflag=0
        l = len(str(x))
        for y in range(2,l+1):
            flag=1
            if(l%y!=0):
                continue
            newl = l//y
            sx = str(x)
            xs0 = sx[0:newl]
            for i in range(y):
                if(sx[newl*i:newl*(i+1)]!=xs0):
                    flag=0
            #print(f"{x} {y} = {l} = {newl} # {sx} \t {xs0} \t {sx[newl*i:newl*i+1]}")
            if(flag):
                newflag=1
        if(newflag):
            ans2=ans2+x
            #print(x)
    #print(curra)

print(ans2)