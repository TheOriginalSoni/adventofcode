lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

a = []
b=0
for line in lines:
    if(len(line)==0):
        a.append(b)
        b=0
    else:
      b=b+int(line)
a.append(b)

a.sort(reverse=True)

print(a[0])
print(a[0]+a[1]+a[2])
