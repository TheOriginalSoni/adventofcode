from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce

#This code is bad. I'm sorry

lines = get_data(year=2022, day=11)
lines = lines.split("\n")

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

N = 8

def func(i,a):
    if(i==0):
        return a*17
    elif(i==1):
        return a+7
    elif(i==2):
        return a*a
    elif(i==3):
        return a+1
    elif(i==4):
        return a*3
    elif(i==5):
        return a+4
    elif(i==6):
        return a+8
    elif(i==7):
        return a+6

def func2(i,a):
    if(i==0):
        return a*19
    elif(i==1):
        return a+6
    elif(i==2):
        return a*a 
    elif(i==3):
        return a+3

a=[[] for x in range(N)]
i=0
for line in lines:
    b=line.split()
    mi = i//7

    if(i%7==1):
        s=line
        nums = [int(x) for x in s[s.find(":")+1:].replace(" ","").split(",")]
        a[mi].append(nums)
    if(i%7==3):
        s=line
        nums = int(s[s.find("by ")+len("by "):])
        a[mi].append(nums)
    if(i%7==4):
        s=line
        nums = int(s[s.find("monkey ")+len("monkey "):])
        a[mi].append(nums)
    if(i%7==5):
        s=line
        nums = int(s[s.find("monkey ")+len("monkey "):])
        a[mi].append(nums)
    #a.append(b)
    i=i+1

print(a)

ans = [0 for i in range(N)]

aaa = [x[1] for x in a]

aaa = reduce((lambda x, y: x * y), aaa)
print(aaa)

##Part 1 code = commented out #s

for i in range(10000): #20
    for j in range(N):
        print(f"{i+1} - {j} : {a[j][0]}")
        while(len(a[j][0])>0):
            curr = a[j][0].pop(0)
            ans[j] = ans[j]+1
            curr1 = func(j,curr)
            curr2 = curr1%aaa #//3
            if(curr2%a[j][1] == 0):
                a[a[j][2]][0].append(curr2)
            else:
                a[a[j][3]][0].append(curr2)
            #print(f"{curr}, {curr1} , {curr2}")
ans.sort(reverse=True)
print(ans)

print(ans[0]*ans[1])
#submit(ans)

submit(ans[0]*ans[1])
