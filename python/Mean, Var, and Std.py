import numpy as np

biglist = []
n, m = input().split(" ")
for i in range(int(n)):
    x = map(int,input().split())
    m = list(x)
    biglist.append(m)
arr=np.array(biglist)
print(arr)
print(biglist)