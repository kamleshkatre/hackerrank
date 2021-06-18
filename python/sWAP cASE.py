def swap_case(s):
    alteredstring=""
    for x in s:
        if x.islower():
            alteredstring=alteredstring+x.upper()
        elif x.isupper:
            alteredstring=alteredstring+x.lower()
        else :
            alteredstring=alteredstring+x
    return alteredstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)