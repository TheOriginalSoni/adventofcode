from collections import Counter
#from aocd import get_data
#from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re

'''
lines = get_data(year=2024, day=1)
lines = lines.split("\n")
#'''

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

with open('2025/testcases.txt') as f:
    lines = f.readlines()
lines = [x.replace("\n"," ") for x in lines]

a=[]
for x in lines:
    x=x.split(" ")
    b=[]
    for y in x:
        if(y==""):
            pass
        else:
            b=b+[y]
    a=a+[b]

#print(lines)
#print(a)

a1 = [[int(y) for y in x] for x in a[:-1]]
a2 = a[-1:][0]

#print(a1)
#print(a2)

ans1=0
for i in range(len(a2)):
    c = a2[i]
    curr = a1[0][i]
    for j in range(1,len(a1)):
        #print(c,curr,i,j)
        #print(a1[j][i])
        #print(i,j)
        if(c=="*"):
            curr=curr*a1[j][i]
        elif(c=="+"):
            curr=curr+a1[j][i]
        else:
            print("error")
    #print(ans1,curr)
    ans1=ans1+curr
print(ans1)


#print(lines)

ans2=0
currans=0
c=""
for j in range(len(lines[0])-1):
    flag=0
    s=""
    for i in range(len(lines)):
        s = s+lines[i][j]
    #print(s,currans,ans2)
    if(s[-1]=="+" or s[-1]=="*"):
        ans2=ans2+currans
        currans=0
        c=s[-1]
        s=s[:-1]
        flag=1
    s=s.strip()
    if(len(s)==0):
        continue
    else:
        s=int(s)
    if(flag==1):
        currans=s
    else:
        if(c=="*"):
            currans=currans*s
        elif(c=="+"):
            currans=currans+s
        else:
            print("error")    
    #pass
ans2=ans2+currans
print(ans2)

