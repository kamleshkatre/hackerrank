if __name__ == '__main__':
    s = input()
    isalnum1 = False
    isalpha1 = False
    isdigit1 = False
    islower1 = False
    isupper1 = False

    for x in s:
        if x.isalnum:
            isalnum1 = True
        if x.isalpha:
            isalpha1 = True
        if x.isdigit:
            isdigit1 = True
        if x.islower:
            islower1 = True
        if x.isupper:
            isupper1 = True

    print(isalnum1)
    print(isalpha1)
    print(isdigit1)
    print(islower1)
    print(isupper1)
# it did not work for all test cases use any(ch.isalnum for ch in s)