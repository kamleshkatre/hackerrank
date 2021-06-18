import  re
#s = input()
s="BANANA"
vowels = 'AEIOU'


# kevsc = 0
# stusc = 0
# for i in range(len(s)):
#     print(i)
#     print(s[i])
#     if s[i] in vowels:
#         kevsc += (len(s)-i)
#     else:
#         stusc += (len(s)-i)
#
# if kevsc > stusc:
#     print("Kevin", kevsc)
# elif kevsc < stusc:
#     print("Stuart", stusc)
# else:
#     print("Draw")
# stuartlist=[]
# kevinlist=[]
total=[]
stscr=0
kvscr=0
# stuartlist=[]
# kevinlist=[]
#Get all the pattern available
for i in range(0,len(s)):
    for j in range(i,len(s)):
        #print(s[i:j+1])
        total.append(s[i:j+1])
#get the marks
total=set(total)
for x in total:
    #means the strings are for stuart
    if re.match("[AEIOU]",x)==None:
        #stscr=stscr+s.count(x)
        stscr=stscr+len(re.findall('(?=({}))'.format(x),s))
        #stuartlist.append(x)
    #kevin sub set of strings
    else:
        #kvscr=kvscr+s.count(x)
        kvscr=kvscr+len(re.findall('(?=({}))'.format(x),s))
        #kevinlist.append(x)


# print(stscr)
# print(kvscr)
# print(stuartlist)
# print(kevinlist)

if stscr>kvscr:
    print("Stuart {}".format(stscr))
elif kvscr>stscr:
    print("Kevin {}".format(kvscr))
else:
    print("Draw")
