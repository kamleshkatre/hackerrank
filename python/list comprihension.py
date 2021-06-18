x = int(input())
y = int(input())
z = int(input())
n = int(input())
listall=[]
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a+b+c!=n:
                listall.append([a,b,c])

print(listall)

lis1=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n ]
print(lis1)