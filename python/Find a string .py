#iteration will number of char match +1
#count+1

import re
def count_substring(string, sub_string):
    count1=0
    position=0
    while True:
        if string[position:].count(sub_string)>0:
            if string[position:].find(sub_string)!=-1:
                position=position+string[position:].find(sub_string)+1
                count1=count1+1
        else:
            break

    return count1


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)