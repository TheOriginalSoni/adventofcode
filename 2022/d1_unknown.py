#Day 1
from collections import Counter
from aocd import get_data
from aocd import submit
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re

'''
lines = get_data(year=2022, day=24)
lines = lines.split("\n")
#'''

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

#===============================================

with open('testcases.txt') as f:
    lines = f.readlines()

lines = [x.replace('\n'," ") for x in lines]
#'''

print(lines)
a = []
for line in lines:
    b=list(line)
    a.append(b)

ans = sum(list(map(lambda x: int(x[0]+x[-1]), list(map(lambda x: re.findall("[0123456789]",x), a)))))
print(ans)

#a = " ".join(a)
#print(a)

#start = (0,1)
#n,m = len(a),len(a[0])
#end = (n-1,m-1-1)

#=============================================

#a = a.join(" ")
#
#print(ans)

'''
from num2words import num2words
x2 = dict([[num2words(i),str(i)] for i in range (10)])

lambda x: x.replace(num2words(i),str(y)) for y in range(10),

[[,str(i)] for i in range (10)]

re.sub(r'nine', '9', x)


res = [reduce(lambda i, j: i.replace(*j), sub.items(), ele) for ele in test_list1]


[reduce(lambda i, j: i.replace(*j), dict([[num2words(i),str(i)] for i in range (10)]), ele) for ele in a]

ans = [reduce(lambda i, j: i.replace(*j), dict([[num2words(i),str(i)] for i in range (10)]).items(), ele) for ele in a]



# python code to demonstrate working of reduce() 
  
# importing functools for reduce() 
import functools 
  
# initializing list 
lis = [1, 3, 5, 6, 2] 
  
# using reduce to compute sum of list 
print("The sum of the list elements is : ", end="") 
print(functools.reduce(lambda a, b: a+b, lis)) 


[ reduce(lambda i,j: a[0].replace([[num2words(i),str(i)]) for i in range (10)] ]


[reduce(lambda i,j: x.replace(i,j) for ele in [[num2words(i),str(i)],i) for i in range (10)]] for x in a]

[reduce(lambda x: x.replace(ele),ele) for ele in dict([[num2words(i),str(i)] for i in range (10)]) ]

re.sub(r'one','1',x)
'''