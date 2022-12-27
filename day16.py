from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key

lines = get_data(year=2022, day=16)
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

i=0
a=[]
a2=[]
for line in lines:
    line = line.replace("Valve ","")
    line = line.replace(" has flow rate=",";")
    line = line.replace("; tunnels lead to","")
    line = line.replace("; tunnel leads to","")
    line = line.replace("valves",";")
    line = line.replace("valve",";")
    #print(line)
    b = line.split(";")
    b[1] = int(b[1])
    b[2] = [x.strip() for x in b[2].split(",")]
    a.append(b)

print(a)

#a - [['AA', 0, ['DD', 'II', 'BB']], ['BB', 13, ['CC', 'AA']], ['CC', 2, ['DD', 'BB']], ['DD', 20, ['CC', 'AA', 'EE']], ['EE', 3, ['FF', 'DD']], ['FF', 0, ['EE', 'GG']], ['GG', 0, ['FF', 'HH']], ['HH', 22, ['GG']], ['II', 0, ['AA', 'JJ']], ['JJ', 21, ['II']]]

a2 = list(map(lambda x: x[0],list(filter(lambda x:x[1]>0,a))))
a2.append("AA")
a2a = list(map(lambda x: x[0],list(a)))
a2a.sort()
a2.sort()

#a2 = All nodes where value>0
#['AA', 'BB', 'CC', 'DD', 'EE', 'HH', 'JJ']

print(a2)
print(len(a2))
print(a2a)
print(len(a2a))

#a2a = All nodes (just names)
#['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ']

a3 = []
flowrates = {}

#print("=== a====")
#print(a)

for b in a:
    if(b[0] in a2):
        flowrates[b[0]] = b[1] 
    for x in b[2]:
        a3.append((b[0],x,1))

#flowrates - {'AA': 0, 'BB': 13, 'CC': 2, 'DD': 20, 'EE': 3, 'HH': 22, 'JJ': 21}
#a3 - All edges
#print(a3)

for b in a2a:
    #print(b,len(a3))
    if(b not in a2):
        src = list(filter(lambda x:x[1]==b,a3))
        dest = list(filter(lambda x:x[0]==b,a3))

        for x in src:
          if(x in a3):
            a3.remove(x)
        for y in dest:
          if(y in a3):
            a3.remove(y)

        for xx in src: #xx,b,num1
            for yy in dest: #b,yy,num2
                if(xx[0]!=yy[1]):
                    sd = list(filter(lambda x1:x1[0]==xx[0] and x1[1]==yy[1],a3))
                    for sx in sd:
                        a3.remove(sx)
                    
                    minl = xx[2]+yy[2]

                    if(len(sd)>0):
                        minl = min(list(map(lambda x1:x1[2],sd)))
                        minl = min(minl,xx[2]+yy[2])

                    a3.append((xx[0],yy[1],minl))

a3.sort()
print("Len a3")
print(len(a3))

#Edge simplification above

#a3 now - All edges (but only nodes that are in a2) 
#[where a2 = 'AA' + all nodes with value>0]

print("====flowrates")
print(flowrates)

tot_time = 26

allx = [set() for x in range(tot_time+1)]
allx[0] = set([('AA',frozenset(),0,0,frozenset())])
#allx[n] = ('location',set(visited),current_time,flow till now,paths since last valve open)
ally = set()
#ally - All (location, already visited) tuples - We visit ranges in time order so should be good

ans = 0
for round in range(tot_time+1):
    allo = list(allx[round])
    allo.sort()
    for currl,currv,currt,currf,currp in allo:

        ally.add((currl,frozenset(currv)))
        if(currt<tot_time):
          if(currl not in currv and currl not in currp):
              newcurrv = set(currv.copy())
              newcurrv.add(currl)
              newcurrf = currf + (tot_time-currt-1)*flowrates[currl]
              ans = max(ans,newcurrf)
              newcurrp = frozenset()

              allx[currt+1].add((currl,frozenset(newcurrv),currt+1,newcurrf,newcurrp))

        neigh = list(filter(lambda x:x[0]==currl,a3))
        for xx in neigh:
            nextl = xx[1]
            dist = xx[2]
            if(currt+dist<=tot_time and nextl not in currp):
                newcurrl = nextl
                newcurrt = currt + dist
                newcurrp = set(currp.copy())
                newcurrp.add(currl)

                allx[newcurrt].add((newcurrl,currv,newcurrt,currf,frozenset(newcurrp)))
    
    #allo = list(alln)
    print(f"{round},{len(allx[round])}\t{ans}")

print(ans)

ans2 = {}

#ans2[(location,visited)] = max you can get for

for round in range(tot_time+1):
    for b in allx[round]:
        currl = b[0]
        currv = b[1]
        currt = b[2]
        currf = b[3]
        currp = b[4]
        if(currv in ans2):
            ans2[currv] = max(ans2[currv],currf)
        else:
            ans2[currv] = currf

print(f"ans2 len={len(ans2)}")
print()

#for x in ans2:
#  print(f"{x}\t{ans2[x]}")

ansf = 0
for i in range(2**len(a2)):

    if(i%10000==0):
        print(f"i={i}")
    curra = set()
    f = "{0:0"+str(len(a2))+"b}"
    si = f.format(i)

    #print(si)

    for j in range(len(a2)):
        if(si[j]=='1'):
            curra.add(a2[j])

    curraf = frozenset(curra)

    if(curraf in ans2):
        mx1 = ans2[curraf]

        not_curra = list(ans2.items())
        for bx in curraf:
            not_curra = list(filter(lambda x:bx not in x[0],not_curra))

        not_curra = list(not_curra)

        ncl = list(map(lambda x:x[1],not_curra))
        if(len(ncl)>0):
          mx2 = max(ncl)
        else:
          mx2 = 0

        ansf = max(ansf,mx2+mx1)

print(ansf)
