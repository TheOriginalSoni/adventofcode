from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key

lines = get_data(year=2022, day=14)
lines = lines.split("\n")

'''
with open('testcases.txt') as f:
	lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

start = (500,0)

i=0
a=[]
a2=[]
for line in lines:
	line = line.replace("->",",")
	b = [int(x) for x in line.split(",")]
	a.append(b)

a2 =[]
for b in a:
	b2 = []
	for i in range(len(b)):
		if(i%2==1):
			b2.append((b[i-1],b[i]))
	a2.append(b2)

print(a2)

maxx,maxy = 500,0
minx,miny = 500,0

for b in a2:
	for (x,y) in b:
		maxx = max(maxx,x)
		maxy = max(maxy,y)
		minx = min(minx,x)
		miny = min(miny,y)

print([maxx,maxy,minx,miny])

sl = set()
for b in a2:
	if(len(b)==1):
		sl.add(b[0])
	for i in range(len(b)-1):
		x1,y1 = b[i][0],b[i][1]
		x2,y2 = b[i+1][0],b[i+1][1]

		if(x1==x2):
			for j in range(min(y1,y2),max(y1,y2)+1):
				sl.add((x1,j))
		elif(y2==y1):
			for j in range(min(x1,x2),max(x1,x2)+1):
				sl.add((j,y1))
		else:
			print("wtf")

#print(list(sl))
print(len(sl))


start = (500,0)

ans = 0
flag = 1
while flag:
	curr = (500,0)

	while flag:
		#print(curr)
		x,y = curr[0],curr[1]
		if(y==maxy+1):
			#print(curr)
			sl.add(curr)
			ans = ans + 1
			break			
		if((x,y+1) not in sl):
			curr = (x,y+1)
		elif((x-1,y+1) not in sl):
			curr = (x-1,y+1)
		elif((x+1,y+1) not in sl):
			curr = (x+1,y+1)
		else:
			#print(curr)
			sl.add(curr)
			ans = ans + 1
			break

	if(curr==start):
		break
print(ans)
