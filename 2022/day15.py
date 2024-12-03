from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key

lines = get_data(year=2022, day=15)
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

def manhat(t1, t2):
  x1,y1 = t1[0],t1[1]
  x2,y2 = t2[0],t2[1]

  return abs(x1-x2) + abs(y1-y2)

i=0
a=[]
a2=[]
for line in lines:
  line = line.replace("Sensor at x=","")
  line = line.replace(": closest beacon is at x=",",")
  line = line.replace(" y=","")
  #print(line)
  b = [int(x) for x in line.split(",")]
  a.append(b)

a2 = [group(b,2) for b in a]

#print(a2)

maxx = max(list(map(lambda x: x[0],sum(a2,[]))))
minx = min(list(map(lambda x: x[0],sum(a2,[]))))
maxy = max(list(map(lambda x: x[1],sum(a2,[]))))
miny = min(list(map(lambda x: x[1],sum(a2,[]))))

#print([minx,miny,maxx,maxy])

#PART 1
''' 
ans = []
for b in a2:
  y = 10
  d = manhat(b[0],b[1])
  sx,sy = b[0]
  if(abs(sy-y)>d):
    pass
  else:
    dx = d - abs(sy-y)
    x1 = sx-dx
    x2 = sx+dx
    ans.append([(x1,y),(x2,y)])

print(ans)

ans2 = set()
for b in ans:
  x1,y1 = b[0]
  x2,y2 = b[1]
  for x in range(x1,x2+1):
    ans2.add((x,y1))

ans2 = list(ans2)
ans2 = list(filter(lambda x: x not in list(map(lambda x: x[1],a2)),ans2))
ans2.sort()
print(len(ans2))
'''

bot = 0
top = 4000000

def reduce_ranges(ranges):
    ranges.sort()
    ranges = list(filter(lambda x:x[0]<=top and x[1]>=bot,ranges))
    ranges = list(map(lambda x:(max(bot,x[0]),min(top,x[1])),ranges))

    new_ranges = []
    left, right = ranges[0]
    for range in ranges[1:]:
        next_left, next_right = range
        if right + 1 < next_left:             # Is the next range to the right?
            new_ranges.append((left, right))  # Close the current range.
            left, right = range               # Start a new range.
        else:
            right = max(right, next_right)  # Extend the current range.
    new_ranges.append((left, right))  # Close the last range.
    return new_ranges

#a2 = list(map(lambda x: (x[0][0],x[1][0]),ans))
#print(reduce_ranges(a2))




for y in range(bot,top+1):
  ans = []
  for b in a2:
    d = manhat(b[0],b[1])
    sx,sy = b[0]
    if(abs(sy-y)>d):
      pass
    else:
      dx = d - abs(sy-y)
      x1 = sx-dx
      x2 = sx+dx
      ans.append((x1,x2))

  ans.sort()
  ans = reduce_ranges(ans)

  if(len(ans)>1):
    print(f"{ans},{y}")
# Manual manipulation from this point to hack at the ans

  if(y%10000==0):
    print(y)

