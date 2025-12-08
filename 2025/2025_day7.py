from collections import Counter
#from aocd import get_data
#from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
from collections import defaultdict

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
lines = [x.replace('\n'," ").strip() for x in lines]
a = [list(x) for x in lines]

print(a)
#print(lines)

si=-1
sj=-1
for i in range(len(a)):
    for j in range(len(a[0])):
        if(a[i][j]=="S"):
            si=i
            sj=j

curr = [sj]
curri = si
ans1=0
for i in range(si+1,len(a)):
    #print(i,ans,curr)
    newr = []
    for j in curr:
        if(j>=0 and j<len(a[0])):
            if(a[i][j]=="^"):
                newr = newr + [j-1,j+1]
                ans1=ans1+1
            elif(a[i][j]=="."):
                newr = newr + [j]
            else:
                pass
    curr = list(set(newr.copy()))

print(ans1)

curr = defaultdict(int)
curr[sj]=1
#curr = [(sj,1)]
curri = si
ans2=0
for i in range(si+1,len(a)):
    #print(i,ans2,curr)
    newr = defaultdict(int)
    for j in curr:
        jn = curr[j]
        if(j>=0 and j<len(a[0])):
            if(a[i][j]=="^"):
                newr[j-1]+= jn
                newr[j+1]+= jn
                ans2=ans2+jn
            elif(a[i][j]=="."):
                newr[j]+= jn
                #newr = newr + [j]
            else:
                pass
    curr = newr.copy()

print(ans2+1)

ans3 = 0
for j in curr:
    ans3=ans3+curr[j]
print(ans3)