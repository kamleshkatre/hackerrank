from itertools import combinations
word, num=input().split()
list_comb=list()
word = "".join(sorted(word))
# print(word)
for x in range(1,int(num)+1):
    comb=list(combinations(word,x))
    comb.sort()
    for y in comb:
        list_comb.append(y)

list_comb=["".join(x) for x in list_comb]
for i in list_comb:
    print(i)