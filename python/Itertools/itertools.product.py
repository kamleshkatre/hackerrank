# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

l1=map(int,input().split())
l2=map(int,input().split())
cart=list(product(l1,l2))
for x in cart :
    print(x, end=" ")