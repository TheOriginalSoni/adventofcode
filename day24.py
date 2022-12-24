from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache

lines = get_data(year=2022, day=24)
lines = lines.split("\n")

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

a = []
for line in lines:
    b=list(line)
    a.append(b)

#print(a)
start = (0,1)
n,m = len(a),len(a[0])
end = (n-1,m-1-1)

a2 = []
for i in range(len(a)):
    for j in range(len(a[0])):
        c = a[i][j]
        if(c==">"):
            a2.append(((i,j),(0,1)))
        elif(c=="<"):
            a2.append(((i,j),(0,-1)))
        if(c=="v"):
            a2.append(((i,j),(1,0)))
        if(c=="^"):
            a2.append(((i,j),(-1,0)))
#print()
#for b in a2:
#    print(b)

def allplaces(rounds, a2):
    a3 = set()
    for b in a2:
        fpx = b[0][0]+(b[1][0]*rounds)
        fpy = b[0][1]+(b[1][1]*rounds)
        while(fpx<=0): fpx = fpx + (n-2)
        while(fpx>=n-1): fpx = fpx - (n-2)
        while(fpy<=0): fpy = fpy + (m-2)
        while(fpy>=m-1): fpy = fpy - (m-2)
        a3.add((fpx,fpy))
    return a3

def disp(a3):
    for i in range(n):
        for j in range(m):
            if((i,j) in a3):
                print("%",end="")
            else:
                print(".",end="")
        print()
    print()

#for i in range(20):
#    a3 = allplaces(i,a2)
#    print(i)
#    disp(a3)

ans = 0
ff = 0 #0-start to end, 1-end to start, 2=start to end

a4 = []
a4.append([start])
flag=1
for ix in range(10**10):
    a4c = a4[ix]
    a3r = allplaces(ix+1,a2)
    a4n = set()

    neigh = [(0,1),(1,0),(0,-1),(-1,0),(0,0)]
    for b in a4c:
        for nx in neigh:
            nb = (b[0]+nx[0],b[1]+nx[1])
            x,y = nb[0],nb[1]
            #print(nb,x,y,type(x),type(y))
            if(nb not in a3r):
                if(nb==end):
                    ans = (ix+1)
                    print(ans)
                    flag=0
                elif(nb==start):
                    a4n.add(nb)
                elif(x<=0 or x>=n-1 or y<=0 or y>=m-1):
                    pass
                else:
                    a4n.add(nb)

    a4.append(list(a4n))
    if(flag==0):
        break

    if(ix%100==0):
        print(f"i={ix}")

ixx = ans
a4[ixx] = [end]
flag = 1
#a4.append()
flag=1
for ix in range(ixx,10**10):
    a4c = a4[ix]
    a3r = allplaces(ix+1,a2)
    a4n = set()

    neigh = [(0,1),(1,0),(0,-1),(-1,0),(0,0)]
    for b in a4c:
        for nx in neigh:
            nb = (b[0]+nx[0],b[1]+nx[1])
            x,y = nb[0],nb[1]
            #print(nb,x,y,type(x),type(y))
            if(nb not in a3r):
                if(nb==start):
                    ans = (ix+1)
                    print(ans)
                    flag=0
                elif(nb==end):
                    a4n.add(nb)
                elif(x<=0 or x>=n-1 or y<=0 or y>=m-1):
                    pass
                else:
                    a4n.add(nb)

    a4.append(list(a4n))
    if(flag==0):
        break

    if(ix%100==0):
        print(f"i={ix}")

ixx = ans
a4[ixx] = [start]
flag = 1
#a4.append()
flag=1
for ix in range(ixx,10**10):
    a4c = a4[ix]
    a3r = allplaces(ix+1,a2)
    a4n = set()

    neigh = [(0,1),(1,0),(0,-1),(-1,0),(0,0)]
    for b in a4c:
        for nx in neigh:
            nb = (b[0]+nx[0],b[1]+nx[1])
            x,y = nb[0],nb[1]
            #print(nb,x,y,type(x),type(y))
            if(nb not in a3r):
                if(nb==end):
                    ans = (ix+1)
                    print(ans)
                    flag=0
                elif(nb==start):
                    a4n.add(nb)
                elif(x<=0 or x>=n-1 or y<=0 or y>=m-1):
                    pass
                else:
                    a4n.add(nb)

    a4.append(list(a4n))
    if(flag==0):
        break

    if(ix%100==0):
        print(f"i={ix}")
