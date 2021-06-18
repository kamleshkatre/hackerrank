
if __name__ == '__main__':
    totalstu=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        totalstu.append([name,score])
    def giveVal(val):
        return val[1]
    totalstu.sort(key=giveVal)
    print(totalstu)
    min1=min(totalstu,key=giveVal)
    print(min1)
    #totalstu.pop(totalstu.index(min1))
    # count1=totalstu.count(min1[1])
    # print(count1)
    minimumlist=[]
    for x in totalstu:
        if min1[1]==x[1]:
            print(x)
        else:
            minimumlist.append(x)

    print(minimumlist)
    #totalstu.pop(totalstu.index(x))
    min2=min(minimumlist,key=giveVal)
    finalist=[x for x in minimumlist if x[1]==min2[1]]
    finalist.sort()
    for x in finalist:
        print(x[0])