from collections import Counter
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
import sys
#from aocd import get_data
#from aocd import submit
import numpy as np

def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph
        )
        X.add(v)

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

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
#dirs_8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1)]

#===============================================
M = 10000000000000

with open('2024/testcases2.txt') as f:
    lines = f.readlines()

a=[]
for line in lines:
    line = line.replace('\n',"")
    line=line.split("-")
    a.append(line)
#print(a)
#print(a)

a_all = list(set(sum(a, [])))
#print(a_all)

maps={}
for x in a_all:
    maps[x]=[]

for x in a:
    maps[x[0]].append(x[1])
    maps[x[1]].append(x[0])

#print(maps)

ans1=0

for x in a_all:
    for z1 in maps[x]:
        for z2 in maps[x]:
            if(z1 != z2 and z1 in maps[z2]):
                if(x<z1 and z1<z2):
                    if(z1[0]=="t" or z2[0]=="t" or x[0]=="t"):
                        ans1=ans1+1

print(ans1)

edges = []


V = len(a_all)
for x in a_all:
    for y in maps[x]:
        edges.append([a_all.index(x),a_all.index(y)])
#print(edges)

n=V

# Create an adjacency list from the edges
graph = {i: set() for i in range(1, n + 1)}
for u, v in edges:
    graph[u+1].add(v+1)
    graph[v+1].add(u+1)

# Convert set keys into sorted lists for consistent ordering
graph = {key: set(graph[key]) for key in graph}

all_cliques = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))
if all_cliques:
    max_clique_size = max(len(clique) for clique in all_cliques)
else:
    max_clique_size = -1

print(max_clique_size)

for clique in all_cliques:
    if(len(clique)==max_clique_size):
        ans2 = sorted([a_all[x-1] for x in clique])
        print(",".join(ans2))

