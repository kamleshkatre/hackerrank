#https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
#get some idea from here


if __name__ == '__main__':
    n = int(input())
    #arr = map(int, input().split())
    arr = [*map(int,input().split())]#unpacking map object to syntax list[*mapobject]
    # l1=list(arr)
    # l1.sort(reverse=False)
    # s1=set()
    # s1.update(l1)
    # l2=list(s1)
    # #print(l2)
    # print(l2[-2])
    # # get some test case failed this way
    # max=arr[0]
    # for a in arr:
    #     if max< a:
    #         max=a
    # print(max)
    # secmax=arr[0]
    # for a in arr:
    #     if max >a and secmax< a:
    #             secmax=a
    #
    # print(secmax)
    # this one also  failed in some test cases
    max1=max(arr)
    #print(max1)
    for x in range(arr.count(max1)):
        arr.remove(max1)
    #print(arr)
    secmac=max(arr)
    print(secmac)