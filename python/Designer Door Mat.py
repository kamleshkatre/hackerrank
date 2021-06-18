# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME -------
# ---.|..|..|..|..|.---
# ------.|..|..|.------rege
# ---------.|.---------
#7*21



m,n=input().split(" ")
m=int(m)
n=int(n)
for j in range(1,m,2):
    print((".|."*j).center(n, '-'))
print("WELCOME".center(n,"-"))

for k in range(m-2,0,-2):
    print((".|."*k).center(n, '-'))
