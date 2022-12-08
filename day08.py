from aocd import get_data
from aocd import submit

lines = get_data(year=2022, day=8)
lines = lines.split("\n")

'''
with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n',"") for x in lines]
#'''

a=[]
for line in lines:
    b = [int(x) for x in list(line)]
    a.append(b)

print(a)

s=set()
for i in range(len(a)):
   maxh=-1
   for j in range(len(a[i])):
        i2,j2=i,j
        #print(f"{i2} {j2}")
        if(a[i2][j2]>maxh):
            s.add((i2,j2))
        maxh = max(maxh,a[i2][j2])

   maxh=-1
   for j in range(len(a[i])):
        i2,j2=i,len(a[i])-1-j
        #print(f"{i2} {j2}")
        if(a[i2][j2]>maxh):
            s.add((i2,j2))
        maxh = max(maxh,a[i2][j2])

   maxh=-1
   for j in range(len(a[i])):
        i2,j2=j,i
        #print(f"{i2} {j2}")
        if(a[i2][j2]>maxh):
            s.add((i2,j2))
        maxh = max(maxh,a[i2][j2])

   maxh=-1
   for j in range(len(a[i])):
        i2,j2=len(a)-1-j,i
        #print(f"{i2} {j2}")
        if(a[i2][j2]>maxh):
            s.add((i2,j2))
        maxh = max(maxh,a[i2][j2])


print(s)
s2=len(s)

print(s2)

#submit(s2)

maxans=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if(i==0 or j==0 or i==len(a)-1 or j==len(a[i])-1):
            continue

        ans = 1

        curr=0
        i2,j2=i+1,j
        while(i2<len(a) and a[i][j]>a[i2][j2]):
            i2=i2+1
            curr=curr+1
        if(i2<len(a)):
            curr=curr+1
        ans = ans*curr
        #print(curr)

        curr=0
        i2,j2=i-1,j
        while(i2>=0 and a[i][j]>a[i2][j2]):
            i2=i2-1
            curr=curr+1
        if(i2>=0):
            curr=curr+1
        ans = ans*curr
        #print(curr)

        curr=0
        i2,j2=i,j+1
        while(j2<len(a[i]) and a[i][j]>a[i2][j2]):
            j2=j2+1
            curr=curr+1
        if(j2<len(a[i])):
            curr=curr+1
        ans = ans*curr
        #print(curr)

        curr=0
        i2,j2=i,j-1
        while(j2>=0 and a[i][j]>a[i2][j2]):
            j2=j2-1
            curr=curr+1
        if(j2>=0):
            curr=curr+1
        ans = ans*curr
        #print(curr)

        maxans = max(ans,maxans)

        #print(f"{i} {j} - {ans}")


print(maxans)


#submit(maxans)

'''
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end = " ")
    print()
#'''
