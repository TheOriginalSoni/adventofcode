from collections import Counter
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
import sys

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

'''
lines=[] 
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    else:
        lines.append(line)
'''

'''
lines = get_data(year=2024, day=4)
lines = lines.split("\n")
#'''

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

with open('testcases2.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]

a = []
for line in lines:
    #print(line)
    line = line.replace(":"," ")
    b=[int(x) for x in line.split()]
    a.append(b)

ans=0
for b in a:
    tot = b[0]
    c = b[1:]
    currans = 0
    for i in range(2**(len(c)-1)):
        currtot = b[1]
        x = str(bin(i))[2:]
        while(len(x)<len(c)-1):
            x="0"+x
        for z in range(len(x)):
            if(x[z]=="0"):
                currtot = currtot + b[z+2]
            else:
                currtot = currtot * b[z+2]
        if(currtot == tot):
            currans = 1
    ans = ans + tot * currans

#print(a)
print(ans)

ix=1
ans2=0
for b in a:
    tot = b[0]
    c = b[1:]
    currans = 0
    currtots = []
    currtots.append([b[1]])
    for z in range(0,len(c)-1):
        currtot = []
        for x in currtots[z]:
            if(x<=tot):
                currtot.append(x + b[z+2])
                currtot.append(x * b[z+2])
                currtot.append(int(str(x) + str(b[z+2])))
        currtots.append(currtot)
    if tot in currtots[len(currtots)-1]:
        ans2 = ans2 + tot
    ix=ix+1
print(ans2)

''' 
#Naive slower way - Got AC before faster way was done
ix=1
ans2=0
for b in a:
    tot = b[0]
    c = b[1:]
    currans = 0
    for i in range(3**(len(c)-1)):
        currtot = b[1]
        x = baseN(i,3)
        while(len(x)<len(c)-1):
            x="0"+x
        for z in range(len(x)):
            #print("=",x,z,currtot,tot)
            if(len(str(currtot))>len(str(tot))):
                break       
            if(x[z]=="0"):
                currtot = currtot + b[z+2]
            elif(x[z]=="1"):
                currtot = currtot * b[z+2]
            else:
                currtot = int(str(currtot) + str(b[z+2]))
            if(currtot > tot):
                break
        #print("=",x,currtot,tot)
        if(currtot == tot):
            currans = 1
            #print(tot)
    if(ix%50==0):
        print(ix)
    ans2 = ans2 + tot * currans
    ix=ix+1
print(ans2)
'''