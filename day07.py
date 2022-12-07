from aocd import get_data
from aocd import submit

lines = get_data(year=2022, day=7)
lines = lines.split("\n")


'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

a = []
a.append(['/',0])

parentstack = []
curr = ""
flag = 0
for line in lines:
	if(flag):
		if(line[0]=='$'):
			flag=0
		else:
			b = line.split()
			#print(b)
			if(b[0]=="dir"):
				fs = ",".join(parentstack + [b[1]])
				a.append([fs,0])
			else:
				fs = ",".join(parentstack + [b[1]])
				sz = int(b[0])
				a.append([fs,sz])
	if(line[2:4]=="ls"):
		flag=1
		continue
	if(line[2:4]=="cd"):
		dir = line[5:]
		if(dir==".."):
			last = parentstack.pop()
			curr = parentstack[len(parentstack)-1]
		else:
			curr = dir
			parentstack.append(curr)

#print(a)

dirs = list(filter(lambda x: x[1]==0,a))

#print(dirs)

ans = 0
for d in dirs:
	dd = d[0]+","
	subtree = list(filter(lambda x: x[0].startswith(dd),a))
	s = sum(list(map(lambda x:x[1],subtree)))
	if(s<=100000): 
		ans=ans+s

print(ans)
#submit(ans)

totsize = sum(list(map(lambda x:x[1],a)))

toreduce = totsize - 40000000

ans = []
for d in dirs:
	dd = d[0]+","
	subtree = list(filter(lambda x: x[0].startswith(dd),a))
	s = sum(list(map(lambda x:x[1],subtree)))
	if(s>=toreduce): 
		ans.append(s)

print(min(ans))
submit(min(ans))
