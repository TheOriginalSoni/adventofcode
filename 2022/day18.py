from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key

lines = get_data(year=2022, day=18)
lines = lines.split("\n")

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
  return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

#===============================================

'''
with open('testcases.txt') as f:
  lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

a=[]
for line in lines:
    b = tuple([int (x) for x in line.split(",")])
    a.append(b)

#print(a)

s = 6 * len(a)

sa = {}
for b in a:
  sa[b]=6

for b in a:
  if ((b[0]+1,b[1],b[2]) in a):
    sa[b] = sa[b] - 1
  if ((b[0]-1,b[1],b[2]) in a):
    sa[b] = sa[b] - 1
  if ((b[0],b[1]+1,b[2]) in a):
    sa[b] = sa[b] - 1
  if ((b[0],b[1]-1,b[2]) in a):
    sa[b] = sa[b] - 1
  if ((b[0],b[1],b[2]+1) in a):
    sa[b] = sa[b] - 1
  if ((b[0],b[1],b[2]-1) in a):
    sa[b] = sa[b] - 1

s = sum(sa[b] for b in sa)
print(s)

#submit(s)

maxx = max(list(map(lambda x: x[0],a)))
minx = min(list(map(lambda x: x[0],a)))
maxy = max(list(map(lambda x: x[1],a)))
miny = min(list(map(lambda x: x[1],a)))
maxz = max(list(map(lambda x: x[2],a)))
minz = min(list(map(lambda x: x[2],a)))

a.sort()
ans = 0

print(a)

#print(st)

st = a[0]

ee = set()
for b in a:
  if ((b[0]+1,b[1],b[2]) not in a):
    ee.add((b[0]+1,b[1],b[2]))
  if ((b[0]-1,b[1],b[2]) not in a):
    ee.add((b[0]-1,b[1],b[2]))
  if ((b[0],b[1]+1,b[2]) not in a):
    ee.add((b[0],b[1]+1,b[2]))
  if ((b[0],b[1]-1,b[2]) not in a):
    ee.add((b[0],b[1]-1,b[2]))
  if ((b[0],b[1],b[2]+1) not in a):
    ee.add((b[0],b[1],b[2]+1))
  if ((b[0],b[1],b[2]-1) not in a):
    ee.add((b[0],b[1],b[2]-1))

print(len(ee))

ee = list(ee)

aaa = []
outside = []
i=0
stt = []

def visit(n):
  if(n[0]<minx or n[0]>maxx or n[1]<miny or n[1]>maxy or n[2]<minz or n[2]>maxz):
    outside[i]=1
  else:
    if(n in a or n in aaa[i]):
      pass
    else:
      if(n in ee):
        ee.pop(ee.index(n))
      stt.append(n)
      aaa[i].append(n)

print(ee)

while(len(ee)>0):
  curr = ee.pop()
  print(f"{i} : {curr}")
  aaa.append([curr])
  outside.append(0)
  stt = [curr]
  while(len(stt)>0):
    cc = stt.pop()

    #print(f"{len(stt),len(ee)}")

    n = (cc[0]+1,cc[1],cc[2])
    visit(n)

    n = (cc[0]-1,cc[1],cc[2])
    visit(n)

    n = (cc[0],cc[1]+1,cc[2])
    visit(n)

    n = (cc[0],cc[1]-1,cc[2])
    visit(n)

    n = (cc[0],cc[1],cc[2]+1)
    visit(n)

    n = (cc[0],cc[1],cc[2]-1)
    visit(n)
  i=i+1

for i in range(len(aaa)):
    print(f"{len(aaa[i])} - {outside[i]}")
    print(aaa[i])

finala = []
ans = 0
for i in range(len(aaa)):
  if(outside[i]==0):
    finala = finala + aaa[i]

s2 = 6 * len(finala)

sa2 = {}
for b in finala:
  sa2[b]=6
  if ((b[0]+1,b[1],b[2]) in finala):
    sa2[b] = sa2[b] - 1
  if ((b[0]-1,b[1],b[2]) in finala):
    sa2[b] = sa2[b] - 1
  if ((b[0],b[1]+1,b[2]) in finala):
    sa2[b] = sa2[b] - 1
  if ((b[0],b[1]-1,b[2]) in finala):
    sa2[b] = sa2[b] - 1
  if ((b[0],b[1],b[2]+1) in finala):
    sa2[b] = sa2[b] - 1
  if ((b[0],b[1],b[2]-1) in finala):
    sa2[b] = sa2[b] - 1

s2 = sum(sa2[b] for b in sa2)

print(s-s2)
