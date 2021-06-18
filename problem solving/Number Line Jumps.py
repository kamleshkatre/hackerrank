x=1
x1,v1,x2,v2=map(int,"21 6 47 3".split())
# x1=0
# v1=2
# x2=5
# v2=3
jump1=x1
jump2=x2
#know after which jump it will meet
while True:
    jump1=jump1+v1
    jump2=jump2+v2
    print("jump1 {} jump2 {}".format(jump1,jump2))
    if jump1==jump2:
        print("at this step {}".format(x))
        break
    x=x+1

#wether ethey will meet or not
if v1>v2:
    if (x2-x1)%(v2-v1)==0:
        print("YES")
    else:
        print ("NO")