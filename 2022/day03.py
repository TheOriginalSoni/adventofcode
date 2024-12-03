lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

s=0
for line in lines:
    a1 = list(line[0:len(line)//2])
    a2 = list(line[len(line)//2:])
    ans = list(set(a1)& set(a2))[0]
    if(ans<='Z' and ans>='A'):
        s = s + ord(ans) - ord ('A') + 27
    elif(ans<='z' and ans>='a'):
        s = s + ord(ans) - ord ('a') + 1

print(s)

s=0
for i in range(len(lines)-2):
    if(i%3==0):
        ans = list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))[0]
        #print(ans)
        if(ans<='Z' and ans>='A'):
            s = s + ord(ans) - ord ('A') + 27
        elif(ans<='z' and ans>='a'):
            s = s + ord(ans) - ord ('a') + 1

print(s)
        
