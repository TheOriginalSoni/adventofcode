from aocd import get_data
from aocd import submit

lines = get_data(year=2022, day=9)
lines = lines.split("\n")

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

a=[]

for line in lines:
    b = line.split()
    a.append([b[0],int(b[1])])


a2 = []
for b in a:
    for c in range(b[1]):
        a2.append(b[0])

hx,hy = 0,0
tx,ty = 0,0

a3 = []
for b in a2:
    #print(f"{hx} {hy} {tx} {ty} {b}")

    if(b=='U'):
        nhx,nhy = hx,hy+1
    elif(b=='D'):
        nhx,nhy = hx,hy-1
    elif(b=='L'):
        nhx,nhy = hx-1,hy
    elif(b=='R'):
        nhx,nhy = hx+1,hy

    if(nhx==tx+2):
        ntx,nty = tx+1,nhy
    elif(nhx==tx-2):
        ntx,nty = tx-1,nhy
    elif(nhy==ty+2):
        ntx,nty = nhx,ty+1
    elif(nhy==ty-2):
        ntx,nty = nhx,ty-1
    else:
        ntx,nty = tx,ty
    a3.append([nhx,nhy,ntx,nty])

    hx,hy = nhx,nhy
    tx,ty = ntx,nty

ans1 = len(set([(b[2],b[3]) for b in a3]))

print(ans1)
#submit(ans1)

'''PART 2'''

p = [[0,0] for x in range(10)]

a3 = []
ans = set()
ans.add((0,0))
for b in a2:
    np = []

    hx,hy = p[0][0],p[0][1]
    if(b=='U'):
        np.append([hx,hy+1])
    elif(b=='D'):
        np.append([hx,hy-1])
    elif(b=='L'):
        np.append([hx-1,hy])
    elif(b=='R'):
        np.append([hx+1,hy])

    for i in range(9):
        tx,ty = p[i+1][0],p[i+1][1]
        nhx,nhy = np[i][0],np[i][1]
        if(nhx==tx+2):
            if(nhy==ty):
                ntx,nty = tx+1,ty
            elif(nhy<ty):
                ntx,nty = tx+1,ty-1
            elif(nhy>ty):
                ntx,nty = tx+1,ty+1
        elif(nhx==tx-2):
            if(nhy==ty):
                ntx,nty = tx-1,ty
            elif(nhy<ty):
                ntx,nty = tx-1,ty-1
            elif(nhy>ty):
                ntx,nty = tx-1,ty+1
        elif(nhy==ty+2):
            if(nhx==tx):
                ntx,nty = tx,ty+1
            elif(nhx<tx):
                ntx,nty = tx-1,ty+1
            elif(nhx>tx):
                ntx,nty = tx+1,ty+1
        elif(nhy==ty-2):
            if(nhx==tx):
                ntx,nty = tx,ty-1
            elif(nhx<tx):
                ntx,nty = tx-1,ty-1
            elif(nhx>tx):
                ntx,nty = tx+1,ty-1
        else:
            ntx,nty = tx,ty

        np.append([ntx,nty])
    p = np.copy()
    ans.add((np[9][0],np[9][1]))

print(len(ans))
submit(len(ans))
