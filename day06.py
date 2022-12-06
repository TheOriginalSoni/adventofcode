from aocd import get_data
from aocd import submit

lines = get_data(year=2022, day=6)
lines = lines.split("\n")


'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

a = []
for line in lines:
	b = list(line)
	a.append(b)

#print(a)

c = sum([(min([x+4 if len(set([b[x],b[x+1],b[x+2],b[x+3]]))==4 else len(b)+4 for x in range(len(b)-4)])) for b in a])

print(c)

#print(submit(c))

d = sum([(min([x+14 if len(set([b[y+x] for y in range(14)]))==14 else len(b)+14 for x in range(len(b)-14)])) for b in a])

print(d)
#print(submit(d))
