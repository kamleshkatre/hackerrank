from itertools import permutations

str1,n=input().strip().split(" ")

perm=list(permutations(str1,int(n)))
perm.sort()
for x in perm:
    print("".join(x))