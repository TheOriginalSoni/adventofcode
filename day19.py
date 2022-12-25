from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache

lines = get_data(year=2022, day=19)
lines = lines.split("\n")

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

#===============================================


with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

a=[]
for line in lines:
        b = line.replace("Blueprint ","")
        b = b.replace(": Each ore robot costs ",",")
        b = b.replace(" ore. Each clay robot costs ",",")
        b = b.replace(" ore. Each obsidian robot costs ",",")
        b = b.replace(" ore and ",";")
        b = b.replace(" clay. Each geode robot costs ",",")
        b = b.replace(" obsidian.","")
        b = b.split(",")
        #b[0]=int(b[0])
        b[1]=int(b[1])
        b[2]=int(b[2])
        b[3]=(int((b[3].split(";"))[0]),int((b[3].split(";"))[1]))
        b[4]=(int((b[4].split(";"))[0]),int((b[4].split(";"))[1]))
        a.append(b[1:])

print(a)

maxg = 0

ans = {}

def better(xtotal,total):
  if(xtotal==total):
    return 0
  if(xtotal[0]>=total[0] and xtotal[1]>=total[1] and xtotal[2]>=total[2] and xtotal[3]>=total[3]):
    return 1
  return -1

#PART 1
'''
i=1
ans2 = 0
for b in a:
    ans = {}
    finalg = tryit(b)
    print(f"{b}\t {i},{finalg},{len(ans)}")
    ans2 = ans2+(i*finalg)
    i=i+1
'''

def recurse_bfs(b,total,counts):
    alln = []
    allp = [(total,counts)]

    for round in range(1,32+1):
        #allp = alls[round]
        alln = set()

        for ax in allp:
            total = ax[0]
            counts = ax[1]

            ore = total[0]
            clay = total[1]
            obsidian = total[2]
            geode = total[3]

            orec = b[0]
            clayc = b[1]
            obsc = b[2]
            geoc = b[3]

            if(round == 32 and counts[3]==0):
                continue

            if(round == 31 and total[3]==0 and total[2]<geoc[1]):
                continue

            if(geoc[1]<counts[2] or obsc[1]<counts[1]):
                #pass
                continue

            if(counts[0]>max(orec,clayc,geoc[0],obsc[0])):
                #pass
                continue

            if(total[0] >= geoc[0] and total[2] >= geoc[1]): #Each geode robot costs 4 ore and 19 obsidian
                newtotal = (total[0]+counts[0]-geoc[0],total[1]+counts[1],total[2]+counts[2]-geoc[1],total[3]+counts[3])
                newcounts = (counts[0],counts[1],counts[2],counts[3]+1)
                alln.add((newtotal,newcounts))

            if(total[0] >= obsc[0] and total[1] >= obsc[1]): #Each obsidian robot costs 4 ore and 12 clay
                newtotal = (total[0]+counts[0]-obsc[0],total[1]+counts[1]-obsc[1],total[2]+counts[2],total[3]+counts[3])
                newcounts = (counts[0],counts[1],counts[2]+1,counts[3])
                alln.add((newtotal,newcounts))

            if(total[0] >= clayc): #Each clay robot costs 4 ore
                newtotal = (total[0]+counts[0]-clayc,total[1]+counts[1],total[2]+counts[2],total[3]+counts[3])
                newcounts = (counts[0],counts[1]+1,counts[2],counts[3])
                alln.add((newtotal,newcounts))

            if(total[0] >= orec): #Each ore robot costs 4 ore
                newtotal = (total[0]-orec+counts[0],total[1]+counts[1],total[2]+counts[2],total[3]+counts[3])
                newcounts = (counts[0]+1,counts[1],counts[2],counts[3])
                alln.add((newtotal,newcounts))

            if(total[0]>max(geoc[0],obsc[0],clayc,orec) and total[2] >= geoc[1] and total[1] >= obsc[1]):
                continue
                #pass
            else:
                #if True:
                newtotal = (total[0]+counts[0],total[1]+counts[1],total[2]+counts[2],total[3]+counts[3])
                newcounts = (counts[0],counts[1],counts[2],counts[3])
                alln.add((newtotal,newcounts))

        alln = list(alln).copy()

        allnd = {}
        for bx in alln:
            if(bx[0] in allnd):
                allnd[bx[0]].append(bx[1])
            else:
                allnd[bx[0]] = [bx[1]]
        #print(allnd)

        allnn = []
        for k in allnd.keys():
            ax = allnd[k]
            for xx in ax:
                flag=1
                for yy in ax:
                    #print(yy,xx)
                    if(better(yy,xx)==1):
                        flag=0
                        break
                if(flag):
                    allnn.append((k,xx))

        alln = allnn.copy()

        ans = max(list(map(lambda x:x[0][3],alln)))

        print(f"{round}:{len(alln)}\t {ans}")
        #print(alln)

        allp = alln.copy()
        alln = []

        #alls.append(alln)
        #for dxx in alln:
        #    print(dxx)

    ans = max(list(map(lambda x:x[0][3],allp)))
    return ans

def bfs_tryit(b):
    total = (0,0,0,0)
    counts = (1,0,0,0)

    finalg = recurse_bfs(tuple(b),total,counts)
    return finalg

ans2 = 1
for i in range(1,3+1):
    b=a[i]
    ans = {}
    finalg = bfs_tryit(b)
    print(f"{b}\t {i},{finalg}")
    ans2 = ans2*(finalg)

print(ans2)
#submit(ans2)
