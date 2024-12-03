from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key

lines = get_data(year=2022, day=20)
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

a = [int(b) for b in lines]
n = len(a)

#print(len(list(set(a))))
#print(a)
#print(len(a))

#aorg = a.copy()

a = [ba*811589153 for ba in a]

ax = a.copy()
a = []
for i in range(n):
  a.append((ax[i],i))

#print(a)

for bigi in range(10):
  print()
  print("Iter = ",bigi)
  #print(a)
  for i in range(n):
    j = 0
    while(a[j][1] != i):
      j=j+1

    #print(a[j][0])

    curr = a[j][0]
    currid = a[j][1]

    curr2= curr % (n-1)

    jnew = (j + curr2)
    if(jnew<0):
      jnew = jnew+n-1
    if(jnew>=n):
      jnew=jnew-n+1

    a.pop(j)
    a.insert(jnew,(curr,currid))

    #print(f"{i} j={j} {curr} shift={curr%(n-1)} {currid} {jnew}")
    #print(list(map(lambda x:x[0],a)))


#print(a)

ax=list(map(lambda x: x[0],a))
z = ax.index(0)
z1 = (z+1000)%(n)
z2 = (z+2000)%(n)
z3 = (z+3000)%(n)
print(ax[z1]+ax[z2]+ax[z3])
print(f"{z}\t{z1}\t{z2}\t{z3}\t")
print(f"{ax[z]}\t{ax[z1]}\t{ax[z2]}\t{ax[z3]}\t")
