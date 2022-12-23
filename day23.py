from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache

lines = get_data(year=2022, day=23)
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
for line in lines:
    b=list(line)
    a.append(b)

a2 = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if(a[i][j]=="#"):
            a2.append((i,j))

dirs = [[(-1,0),[(-1,-1),(-1,0),(-1,1)]],
        [(1,0),[(1,-1),(1,0),(1,1)]],
        [(0,-1),[(-1,-1),(0,-1),(1,-1)]],
        [(0,1),[(-1,1),(0,1),(1,1)]],
        [(-1,0),[(-1,-1),(-1,0),(-1,1)]],
        [(1,0),[(1,-1),(1,0),(1,1)]],
        [(0,-1),[(-1,-1),(0,-1),(1,-1)]],
        [(0,1),[(-1,1),(0,1),(1,1)]]]

#for x in dirs:
#    print(x)

def addpos(pos1,pos2):
    return (pos1[0]+pos2[0],pos1[1]+pos2[1])

def disp():
    minx = min(list(map(lambda x:x[0],a2)))
    maxx = max(list(map(lambda x:x[0],a2)))
    miny = min(list(map(lambda x:x[1],a2)))
    maxy = max(list(map(lambda x:x[1],a2)))
    for x in range(minx,maxx+1):
        for y in range(miny,maxy+1):
            if((x,y) in a2):
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()

#disp()
#print()

def neighin(xy):
    x,y=xy[0],xy[1]
    if((x-1,y-1) in a2): return 0
    if((x-1,y) in a2): return 0
    if((x-1,y+1) in a2): return 0
    if((x,y-1) in a2): return 0
    #if((x,y) in a2): return 0
    if((x,y+1) in a2): return 0
    if((x+1,y-1) in a2): return 0
    if((x+1,y) in a2): return 0
    if((x+1,y+1) in a2): return 0
    return 1
    
a2 = set(a2)
for round in range(10**10):
    a22 = set()
    rr = round%4
    dirc = dirs[rr:rr+4] #All 4 directions
    #print(dirc)
    prop = {}
    for currp in a2:
        #print(currp)
        #l = len(list(filter(lambda xy:xy[0]>=currp[0]-1 and xy[0]<=currp[0]+1 and xy[1]>=currp[1]-1 and xy[1]<=currp[1]+1,a2)))
        #if(l==1):
        #    prop[currp] = currp
        if(neighin(currp)==1):
            prop[currp]=currp
        else:
            for dircc in dirc:
                #print(f"{dircc[1][0]},{dircc[1][1]},{dircc[1][2]}")
                if((addpos(currp,dircc[1][0]) not in a2) and (addpos(currp,dircc[1][1]) not in a2) and (addpos(currp,dircc[1][2]) not in a2)):
                    prop[currp] = addpos(currp,dircc[0])
                    break

    #print(prop)
    proplist1 = list(prop.values())

    for p in a2:
        if(p in prop):
            if(proplist1.count(prop[p])==1):
                a22.add(prop[p])
            else:
                a22.add(p)
        else:
            a22.add(p)

    if(a2==a22):
        print(round+1)
        submit(round+1)
        break

    a2 = a22.copy()

    #print(f"R{round+1}")
    #print(a2)
    #print(f"==={round}===")
    #disp()
    #print()


#print(a2)

minx = min(list(map(lambda x:x[0],a2)))
maxx = max(list(map(lambda x:x[0],a2)))
miny = min(list(map(lambda x:x[1],a2)))
maxy = max(list(map(lambda x:x[1],a2)))

#print(len(a2))

ans = (((maxy - miny+1)*(maxx - minx+1)) - len(a2))
#print(f"{minx},{miny},{maxx},{maxy}")
print(ans)

