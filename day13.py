from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce

lines = get_data(year=2022, day=13)
lines = lines.split("\n")

'''
with open('testcases.txt') as f:
	lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

i=0
a=[]
a2=[]
for line in lines:
	if(len(line)>0):
		b= eval(line)
		if(i%2==0):
			a.append(b)
		else:
			a2.append(b)
		i=i+1

print(a)
print(a2)

#print(len(a))
#print(len(a2))

def comp(s1,s2):
	if(len(s1)==0 and len(s2)==0):
		return 0
	if(len(s1)==0):
		return 1
	if(len(s2)==0):
		return -1
	ax = s1[0]
	bx = s2[0]

	if(type(ax)==type(0) and type(bx)==type(0)):
		if(ax<bx):
			return 1
		if(ax>bx):
			return -1
		return(comp(s1[1:],s2[1:]))
	if(type(ax)==type(bx)):
		cc = comp(ax,bx)
		if(cc == 0):
			return(comp(s1[1:],s2[1:]))
		else:
			return cc
	if(type(ax)==type(0)):
		ax = [ax]
	else:
		bx = [bx]

	cc = comp(ax,bx)
	if(cc == 0):
		return(comp(s1[1:],s2[1:]))
	else:
		return cc

a3=[]
for i in range(len(a)):
	if(comp(a[i],a2[i])==1):
		a3.append(i+1)

#print(a3)

print(sum(a3))

#submit(sum(a3))

aa = a+a2

aa.append([[2]])
aa.append([[6]])

from functools import cmp_to_key
#aa = sorted(aa, cmp_to_key=lambda x, y: comp(x,y)) # Sort with cmp
aa = sorted(aa, key=cmp_to_key(comp),reverse=True)

for x in aa:
	#print(x)
	pass

i1 = aa.index([[2]])
i2 = aa.index([[6]])

#print(i1)
#print(i2)
print((i1+1) * (i2+1))

#submit((i1+1) * (i2+1))
