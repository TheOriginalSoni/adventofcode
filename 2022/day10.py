from collections import Counter
from aocd import get_data
from aocd import submit

lines = get_data(year=2022, day=10)
lines = lines.split("\n")

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''


a=[]
for line in lines:
    b=line.split()
    if(b[0]=="noop"):
        a.append((0,0))
    else:
        a.append((1,int(b[1])))

#print(a)

ansl = [20, 60, 100, 140, 180, 220]

x=1
addp = 0
addc = 0
i=1
a2 = []
for b in a:
    #print(f"{i} - {b[1]} - {x}")
    if(b[0]==0):
        a2.append((i,x))
        i = i+1
    else:
        a2.append((i,x))
        i=i+1
        addc = b[1]
        a2.append((i,x))
        x = x + addc
        i=i+1

#print(a2)

a3 = list(filter(lambda x: x[0] in ansl,a2))
a4 = sum(list(map(lambda x: x[1]*x[0],a3)))


#print(a3)
print(a4)

#submit(a4)

print(a2)

a3 = []
for i in range(0,240):
    flag = 0
    i2 = i%40
    #print(f"{i} {i2}")
    if ((i+1,i2-1) in a2):
        flag=1
    if ((i+1,i2) in a2):
        flag=1
    if ((i+1,i2+1) in a2):
        flag=1
    print(f"{i} {i2} {flag}")
    a3.append(flag)

for i in range(6):
    for j in range(40):
        c = a3[i*40+j]
        if(c==0):
            print(".",end="")
        else:
            print("#",end="")
    print()
print()

#submit("RZHFGJCB")
