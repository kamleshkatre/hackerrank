import re

x=int(input())

for n in range(x):
    str1=input()
    #pattern=("[-+]{0,1}[\d]*\.[0-9]{1,}")
    prog = re.compile(r"^[-+]{0,1}[\d]*\.[0-9]{1,}$")
                    #specify start character must be - snf + of max length1 and then digit
    result = prog.search(str1)# search and match both will work cause covering all length string length
    if result==None:
        print(False)
    else:
        print(True)
       # print(result)