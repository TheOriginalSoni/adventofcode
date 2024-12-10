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
    b = [int(x) for x in list(line)]
    a.append(b)

n = len(a)
m = len(a[0])

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
a1 = [[set() for x in range(m)] for y in range(n)] 
a2 = [[list() for x in range(m)] for y in range(n)] 

for x in range(9,-1,-1):
    for i in range(n):
        for j in range(m):
            if(a[i][j]==x):
                if(x==9):
                    a1[i][j].add((i,j))
                    a2[i][j].append((i,j))
                else:
                    #temp=0
                    for d in dirs:
                        i2=i+d[0]
                        j2=j+d[1]
                        if(i2>=0 and i2<n and j2>=0 and j2<m):
                            if(a[i2][j2]==x+1):
                                #temp=temp+a2[i2][j2]
                                for xx in a1[i2][j2]:
                                    a1[i][j].add(xx)
                                for xx in a2[i2][j2]:
                                    a2[i][j].append(xx)
                    #a2[i][j]=temp

ans1=0
ans2=0
for i in range(n):
    for j in range(m):
        if(a[i][j]==0):
            #ans2=ans2+a2[i][j]
            ans2=ans2+len(a2[i][j])
            ans1=ans1+len(a1[i][j])

print(ans1)
print(ans2)

