from collections import Counter
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
import sys
#from aocd import get_data
#from aocd import submit

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

#===============================================

with open('2024/testcases2.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]

a = []
for line in lines:
    b = [int(x) for x in line.split()]
    a = b

#print(a)

all_a = []
all_a.append({})
for x in a:
    all_a[0][x]=1

m = {}

N=75
for i in range(1,N+1):
    #print(i)
    preva = all_a[i-1]
    curra = {}
    for x in preva:
        sx = str(x)
        if(x==0):
            if(1 not in curra):
                curra[1]=0
            curra[1]=curra[1]+preva[x]
        elif(len(sx)%2==0):
            x1 = int(sx[0:len(sx)//2])
            x2 = int(sx[len(sx)//2:])
            if(x1 not in curra):
                curra[x1]=0
            if(x2 not in curra):
                curra[x2]=0
            curra[x1]=curra[x1]+preva[x]
            curra[x2]=curra[x2]+preva[x]
        else:
            x1 = x*2024
            if(x1 not in curra):
                curra[x1]=0
            curra[x1]=curra[x1]+preva[x]
    all_a.append(curra)


ans1 = sum(all_a[25][x] for x in all_a[25])
print(ans1)

ans2 = sum(all_a[75][x] for x in all_a[75])
print(ans2)