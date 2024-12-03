from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key

lines = get_data(year=2022, day=17)
lines = lines.split("\n")

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

#===============================================

xx = 2722 + (2747 * 569800568) + 4905 - 2722
print(xx)

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

a=[]
for line in lines:
    b = line
    a = a + list(b)

symbs = [["####"],[".#.","###",".#."],["###","..#","..#"],["#","#","#","#"],["##","##"]]

#print(a)

alls = []

rocks = 1000000000000

def disp():
    for i2 in range(len(alls)-1,-1,-1):
        print("".join(alls[i2]))
    print()

emptyline = [".",".",".",".",".",".","."]

def findpoints(miny,maxy):
    points = []
    for i in range(miny,maxy):
        for j in range(len(alls[i])):
            if(alls[i][j]=="#"):
                points.append((i,j))
    points.sort()
    return points

miny = 0
maxy = 0
jxx = 0
ans = []
for ixx in range(rocks):
    i2 = ixx%5
    ans.append((ixx,jxx,len(alls)))

    #if(ixx%10000 == 0):
    #	print(ixx)
    if(jxx ==0 or ixx==3160):
    	print(f"{ixx}, {i2}, {jxx}, {len(alls)}")
    if(i2 == 0 and ixx != 0 and jxx == 0):
    	print(f"{ixx}, {len(alls)}")
    	break

    #print(ixx)
    alls.append(emptyline.copy())
    alls.append(emptyline.copy())
    alls.append(emptyline.copy())

    curr = symbs[i2]
    miny = len(alls)
    maxy = miny + len(curr)

    for y in range(len(curr)):
        currl = list(curr[y]).copy()
        s = [".","."]
        s = s + currl
        while(len(s)<7):
            s = s + ["."]
        alls.append(s)

    flag = 1
    while flag:

        points = findpoints(miny,maxy)

        lr = a[jxx]
        jxx = (jxx+1)%len(a)
        if(lr=="<"):
            lr = -1
        else:
            lr = 1

        flaglr = 1
        for (i,j) in points:
            if(j+lr>=0 and j+lr<len(alls[i])):
                if(alls[i][j+lr]=="%"):
                    flaglr = 0
            else:
                flaglr = 0

        #disp()
        if(flaglr):
            if(lr==1):
                points.reverse()

            for (i,j) in points:
                alls[i][j+lr] = alls[i][j]
                alls[i][j] = "."
            points.sort()
        #print(f"{lr},{jxx}")
        #disp()
        points = findpoints(miny,maxy)

        if(miny<=0):
            flag = 0
        else:
            for (i,j) in points:
                if(alls[i-1][j]=="%"):
                    flag = 0
        
        if(flag):
            for (i,j) in points:
                #disp()
                #print(f"{i} {j} {points}")
                alls[i-1][j] = "#"
                alls[i][j] = "."
                #disp()
            miny = miny-1
            maxy = maxy-1

    for (i,j) in points:
        alls[i][j] = "%"

    while(alls[len(alls)-1]==emptyline):
        alls.pop(len(alls)-1)
    #disp()

print(len(alls))

