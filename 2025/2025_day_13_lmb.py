from collections import Counter
from collections import defaultdict
from functools import reduce
from functools import cmp_to_key
from functools import cache
import re
from utils import *

#[1,2,3,4,5,6] becomes [(1,2),(3,4),(5,6)]
def group(l, n):
    return [tuple(l[x:x+n]) for x in range(0,len(l),n)]

def neighbours(xy):
    x,y=xy
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

def dist(a1,a2):
    return abs(a1[0]-a2[0])**2 +abs(a1[1]-a2[1])**2 + abs(a1[2]-a2[2])**2

#===============================================

# Solving AoL from LMB!
# https://lovemathboy.github.io/day13.html

with open('2025/testcases.txt') as f:
    lines = f.readlines()
lines = [x.replace('\n'," ").strip() for x in lines]
lines = [x.split(" ") for x in lines]

#print(lines)

### PART 1

oddsum = 0
oddcount = 0
evensum = 0
evencount = 0
for line in lines:
    if(line[0]=="plant"):
        x = int(line[1])
        if(x%2==1):
            oddsum=oddsum+x
            oddcount = oddcount+1
        else:
            evensum=evensum+x
            evencount=evencount+1
    else:
        if(line[1]=="odd"):
            oddsum=oddsum+oddcount
            evensum=evensum+oddsum
            evencount=evencount+oddcount
            oddsum=0
            oddcount=0      
        elif(line[1]=="even"):
            evensum=evensum+evencount
            oddsum=evensum+oddsum
            oddcount=evencount+oddcount
            evensum=0
            evencount=0      
        else:
            s1 = oddsum+oddcount
            s2 = evensum+evencount
            oddcount,evencount = evencount,oddcount
            oddsum,evensum = s2,s1
ans1 =oddsum+evensum 
print(ans1)

### PART 2, NAIVE
#a = defaultdict(int)
odda = defaultdict(int)
evena = defaultdict(int)
i=0
for line in lines:
    if(i%100==0):
        print(i,len(odda),len(evena))
    i+=1
    #print(a)
    if(line[0]=="plant"):
        x = int(line[1])
        if(x%2==1):
            odda[x]+=1
        else:
            evena[x]+=1
        #a[x]+=1
    else:
        odd=0
        even=0
        if():
            odd=1
        elif(line[1]=="even"):
            even=1
        else:
            odd=1
            even=1

        a2 = defaultdict(int)
        a3 = defaultdict(int)
        if(line[1]=="odd"):
            for keys in odda:
                p = keys//2
                if(p%2==1):
                    a2[p]+=odda[keys]
                else:
                    evena[p]+=odda[keys]
            odda = a2.copy()
        elif(line[1]=="even"):
            for keys in evena:
                p = keys//2
                if(p%2==1):
                    a2[p]+=evena[keys]
                else:
                    odda[p]+=evena[keys]
            evena = a2.copy()
        else:
            for keys in odda:
                p = keys//2
                if(p%2==1):
                    a2[p]+=odda[keys]
                else:
                    a3[p]+=odda[keys]
            for keys in evena:
                p = keys//2
                if(p%2==1):
                    a2[p]+=evena[keys]
                else:
                    a3[p]+=evena[keys]
            odda = a2.copy()
            evena = a3.copy()
            
#print(a)
ans2 = 0
for key in odda:
    ans2 += key*odda[key]
for key in evena:
    ans2 += key*evena[key]

print(ans2)
#print(odda)
#print(evena)

#'''

'''
# PART 2, TRIE
class TreeNode:
    def __init__(self,number,count,leftchild,rightchild):
        self.n = number
        self.count=count
        self.leftchild=leftchild
        self.rightchild=rightchild

def newTrie(list_numbers):
    if(len(list_numbers)==0):
        return None
    if(len(list_numbers)==1):
        return TreeNode(list_numbers[0],1,None,None)
    n = list_numbers[0]
    tl = newTrie(list_numbers[1:])
    if(n==0):
        return TreeNode(n,0,tl,None)
    else:
        return TreeNode(n,0,None,tl)

def mergeTrie(t1:TreeNode,t2:TreeNode) -> TreeNode:
    if(t1==None):
        return t2
    if(t2==None):
        return t1
    if(t1.n!=t2.n):
        print("error")
        print(t1,t1.n,t1.count,t1.leftchild,t1.rightchild)
        print(t2,t2.n,t2.count,t2.leftchild,t2.rightchild)

    if(t1.leftchild==None):
        t1.leftchild=t2.leftchild
    elif(t2.leftchild==None):
        pass
    else:
        t1.leftchild=mergeTrie(t1.leftchild,t2.leftchild)

    if(t1.rightchild==None):
        t1.rightchild=t2.rightchild
    elif(t2.rightchild==None):
        pass
    else:
        t1.rightchild=mergeTrie(t1.rightchild,t2.rightchild)

    t1.count = t1.count + t2.count
    return t1

def printTrie(n:TreeNode):
    print(n)
    if(n is not None):
        print(n.n,n.count)
        printTrie(n.leftchild)
        printTrie(n.rightchild)
    else:
        print(n)

lefta = None
righta = None
i=0
for line in lines:
    if(i%100==0):
        print(i)
    i+=1
    #print(a)
    if(line[0]=="plant"):
        x = int(line[1])
        binary_string = [int(x) for x in list(bin(x)[2:])]
        binary_string = binary_string[::-1]
        #print(binary_string)
        tn = newTrie(binary_string)
        if(x%2==0):
            lefta = mergeTrie(lefta,tn)
        else:
            righta = mergeTrie(righta,tn)
    else:
        pass
        odd=0
        even=0
        if(line[1]=="odd"):
            x = righta
            if(x==None):
                continue
            lefta = mergeTrie(lefta,x.leftchild)
            righta = x.rightchild
        elif(line[1]=="even"):
            x = lefta
            if(x==None):
                continue
            righta = mergeTrie(righta,x.rightchild)
            lefta = x.leftchild
        else:
            x= lefta
            y=righta
            if(x==None):
                righta = y.rightchild
                lefta = y.leftchild
            elif(y==None):
                lefta = x.leftchild
                righta = x.rightchild
            else:
                lefta = mergeTrie(x.leftchild,y.leftchild)
                righta = mergeTrie(x.rightchild,x.rightchild)
        

ans2 = []
def ansTrie(x:TreeNode,prefix):
    if(x==None):
        return
    newprefix = prefix + [x.n]
    if(x.count>0):
        ans2.append((newprefix,x.count))
    ansTrie(x.leftchild,newprefix)
    ansTrie(x.rightchild,newprefix)

ansTrie(lefta,[])
ansTrie(righta,[])

print(ans2)
#printTrie(a)
#'''