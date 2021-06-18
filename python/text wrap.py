import textwrap

def wrap(string, max_width):
    count1=int(len(string)/max_width)
    count2=len(string)%max_width
    i=0
    j=max_width
    l1=[]
    for x in range(count1):
        l1.append(string[i:j])
        i=i+max_width
        j=j+max_width
    last_chunk =string[-count2:]
    l1.append(last_chunk)
    result1="\n".join(l1)
    return result1

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)