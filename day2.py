lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

def score(m,n):
    if(n==m+1 or n==m-2):
        return n+6
    elif n==m:
        return n+3
    else:
        return n+0

#1 for Rock, 2 for Paper, and 3 for Scissors
#X for Rock, Y for Paper, and Z for Scissors
#A for Rock, B for Paper, and C for Scissors

def ABCtoRPS(m):
    return ord(m)-ord('A')+1

def XYZtoRPS(m):
    return ord(m)-ord('X')+1

#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
def XYZtoRPS2(n,m):
    m2 = ABCtoRPS(m)
    if(n=='Y'):
        return m2
    if(n=='Z'):
        x = m2+1
        if(x==4):
            x=x-3
        return x
    if (n=='X'):
        x = m2 - 1
        if(x==0):
            x=x+3
        return x
    return 0

a= []
a2 = []
for line in lines:
    b = line.split()
    c1 = ABCtoRPS(b[0])
    c2 = XYZtoRPS(b[1])
    c2_2 = XYZtoRPS2(b[1],b[0])
    a.append((c1,c2))
    a2.append((c1,c2_2))

s=0
for line in a:
    x = score(line[0],line[1])
    s=s+x

print(s)

s=0
for line in a2:
    x = score(line[0],line[1])
    s=s+x

print(s)
