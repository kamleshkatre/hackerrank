if __name__ == '__main__':
    list1=[]
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
