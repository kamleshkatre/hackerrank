def merge_the_tools(string, k):
    # your code goes here
    split_len = k
    chunk= len(string)/k
    list1=[]
    # for x in range(1,k+1):# note considering case when 1 is given as k
    #     #temp=""
    #     list1.append(string[(x-1)*k:x*k])
    #     #st=string[(x-1)*k:x*k]
    for i in range(0, len(string), k):
        list1.append(string[i: (i + k)])
    for l in list1:
        tempstr=""
        for ele in l:
            if ele not in tempstr:
                tempstr=tempstr+ele
        print(tempstr)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)