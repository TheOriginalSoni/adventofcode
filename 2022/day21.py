from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache

lines = get_data(year=2022, day=21)
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

a = []
allc = []
for b in lines:
	b = b.replace(":","=")
	b = b.replace(" ","")

	b2 = b.replace("+","=")
	b2 = b2.replace("/","=")
	b2 = b2.replace("*","=")
	b2 = b2.replace("-","=")
	b2 = b2.split("=")
	a.append([b2[0],b,b2])

	allc.append(b2[0])

a2 = []
donec = []
while(len(donec)<len(allc)):
	for x in a:
		if(x[0] not in donec):
			b = x[1]
			b2 = x[2]
			if(len(b2)==2):
				a2.append(x)
				donec.append(x[0])
				continue
			else:
				if(b2[1] in donec and b2[2] in donec):
					a2.append(x)
					donec.append(x[0])

'''
for i in range(0,100000000000):
	for x in a2:
		if(x[0]=="humn"):
			exec(f"humn={i}")
		elif(x[0]=="root"):
			exec(f"root={x[2][1]}-{x[2][2]}")
		else:
			exec(x[1])
	if(root==0):
		print(f"ans={i}")
		break
	if(i%10000==0):
		print(i)
	#if(i==301):
	#	print(f"{root},{humn}")

print(root)
#'''

def redo_over(b,b2,x):
	idx = b2.index(x)
	if(b.find("+")!=-1): #0 = 1+2
		if(idx==1):
			return f"{b2[1]}={b2[0]}-{b2[2]}"
		if(idx==2):
			return f"{b2[2]}={b2[0]}-{b2[1]}"
		return "ERROR"
	if(b.find("-")!=-1): #0 = 1-2
		if(idx==1):
			return f"{b2[1]}={b2[0]}+{b2[2]}"
		if(idx==2):
			return f"{b2[2]}={b2[1]}-{b2[0]}"
		return "ERROR"
	if(b.find("/")!=-1): #0 = 1/2
		if(idx==1):
			return f"{b2[1]}={b2[0]}*{b2[2]}"
		if(idx==2):
			return f"{b2[2]}={b2[1]}/{b2[0]}"
		return "ERROR"
	if(b.find("*")!=-1): #0 = 1*2
		if(idx==1):
			return f"{b2[1]}={b2[0]}/{b2[2]}"
		if(idx==2):
			return f"{b2[2]}={b2[0]}/{b2[1]}"
		return "ERROR"
	return "ERROR"

a3 = []
donec = []
humnc = []
while(True):
	xxx = len(donec) + len(humnc)
	for x in a2:
		b = x[1]
		b2 = x[2]

		if(x[0] not in humnc):
			
			if(x[0]=="humn"):
				continue

			if(x[0]=="root"):
				if(b2[2] in donec):
					a3.append([b2[1],f"{b2[1]}={b2[2]}",[b2[1],b2[2]]])
					donec.append(b2[1])
					humnc.append("root")					
					continue
				if(b2[1] in donec):
					a3.append([b2[2],f"{b2[2]}={b2[1]}",[b2[2],b2[1]]])
					donec.append(b2[2])
					humnc.append("root")					
					continue

			if(len(b2)==2):
				a3.append(x)
				donec.append(x[0])
				humnc.append(x[0])
				continue

			if(b2[1] in donec and b2[2] in donec):
				a3.append(x)
				donec.append(b2[0])
				humnc.append(x[0])					
				continue

			if(b2[0] in donec and b2[2] in donec):
				redo = redo_over(b,b2,b2[1])
				#s = redo[:redo.find("=")]
				a3.append([b2[1],redo,[b2[1],b2[0],b2[2]]])
				donec.append(b2[1])
				humnc.append(x[0])					
				continue

			if(b2[0] in donec and b2[1] in donec):
				redo = redo_over(b,b2,b2[2])
				s = redo[:redo.find("=")]
				a3.append([b2[2],redo,[b2[2],b2[0],b2[1]]])
				donec.append(b2[2])
				humnc.append(x[0])					
				continue

	if(len(donec) + len(humnc) ==xxx):
		break

a4 = []
donec = []
while(len(donec)<len(a3)):
	xxx = len(donec)
	for x in a3:
		if(x[0] not in donec):
			b = x[1]
			b2 = x[2]
			if(len(b2)==2):
				if(b2[1] in donec):
					a4.append(x)
					donec.append(x[0])
					continue
				elif(b2[1].isdigit()):
					a4.append(x)
					donec.append(x[0])
					continue
			else:
				if(b2[1] in donec and b2[2] in donec):
					a4.append(x)
					donec.append(x[0])
					continue

	if(len(donec)==xxx):
		break

for x in a4:
	exec(x[1])

print(humn)

#'''
