import re
from collections import Counter
from itertools import permutations


'''
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)
'''

with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]

a=[]
for line in lines:
    line=line.replace("-",",")
    b = line.split(",")
    a.append([int(x) for x in b])

#print(a)

s=0
for b in a:
    if(b[0]<=b[2] and b[1]>=b[3]):
        s=s+1
    elif(b[0]>=b[2] and b[1]<=b[3]):
        s=s+1

print(s)

s=0
for b in a:
    if(b[0]>= b[2] and b[0]<= b[3]):
        s=s+1
    elif(b[1]>= b[2] and b[1]<= b[3]):
        s=s+1
    elif(b[2]>= b[0] and b[2]<= b[1]):
        s=s+1
    elif(b[3]>= b[0] and b[3]<= b[1]):
        s=s+1

print(s)
