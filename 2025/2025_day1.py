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

with open('2025/testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]
#'''

a = []
x1=[]
x2=[]
for line in lines:
    a=a+[line]
    #print(line)

ans = 0
curr = 50
for x in a:
    if(x[0]=="L"):
        i=-1
    else:
        i=1
    num = int(x[1:])*i
    #print(num)
    prevcurr = curr
    curr = curr + num
    
    ans = ans + abs((prevcurr // 100) - (curr // 100))
    if(curr % 100 == 0): ans=ans+1 
    #if (prevcurr % 100 == 0): ans=ans-1

    '''
    if(curr==0):
        ans=ans+1
    elif(curr>=100 and prevcurr < 100):
        while(curr>=100): 
            curr = curr - 100
            ans=ans+1
    elif(curr<0 and prevcurr != 0):
        while(curr<0): 
            curr = curr + 100
            ans=ans+1
    '''
    #print(f"{num} - {curr} - {ans}")
    #print(curr)
    #if(curr==0): ans=ans+1

ans=0
currnum = 50
for x in a:
    i=0
    if(x[0]=="L"):
        i=-1
    else:
        i=1
    intx = int(x[1:])
    num = intx*i
    #print(num)
    for x in range(intx):
        currnum=currnum+i
        if(currnum==0 or currnum == 100):
            ans=ans+1
        if(currnum==100):
            currnum=0
        if(currnum==-1):
            currnum=99
    #print(f"{x} {num} = {ans} /\t {currnum}")
    #print(num)

print(a)
print(ans)