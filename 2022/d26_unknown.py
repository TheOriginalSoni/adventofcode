#Day 1
from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re

'''
lines = get_data(year=2022, day=24)
lines = lines.split("\n")
#'''

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]
#'''

a = []
for line in lines:
    b=line.strip().replace(":","").split(" ")
    a.append(b)

#print(a)

vert = {}       #letter to num
n = 0           #total # of vertices

for b in a:
    for x in b:
        if(x not in vert):
            vert[x] = n
            n = n+1

#print(vert)
#print(rev_vert)

edgelist = []
edges = [[]]*n
for b in a:
    par = b[0]
    for i in range(len(b)):
        if(i != 0):
            v1 = vert[par]
            v2 = vert[b[i]]
            edgelist = edgelist + [f"{v1} {v2}"]
            edges[v1] = edges[v1] + [v2]
            edges[v2] = edges[v2] + [v1]

#for i in range(len(edges)):
#    print(f"{i} - {edges[i]}")
#print(edges)

all_v = [i for i in range(n)]
all_cc = []
count_e = []
count_odd = []

while(len(all_v) >0):
    edge_ct = 0
    par = all_v[0]
    curr_cc = []

    st = [par]
    while (len(st)>0):
        curr_v = st.pop()
        if(curr_v not in curr_cc):
            curr_cc = curr_cc + [curr_v]
            for x in edges[curr_v]:
                edge_ct = edge_ct + 1
                if(x not in curr_cc):
                    st = st + [x]

    odd_ct=0
    for x in curr_cc:
        all_v.remove(x)
        if(len(edges[x]) %2 !=0):
            odd_ct = odd_ct+1

    all_cc = all_cc + [curr_cc]
    count_e = count_e + [edge_ct//2]
    count_odd = count_odd + [odd_ct]

#print(all_cc)
print(count_e)
print(count_odd)

ans = 0
for i in range(len(count_e)):
    curr_n = len(all_cc[i])
    curr_e = count_e[i]
    curr_odd = count_odd[i]

    if(curr_e == (curr_n*(curr_n+1))//2):
        pass
    else:
        ans = ans + curr_e - (curr_odd//2)

print(ans)
#print(edgelist)
#for e in edgelist:
#    print(e)