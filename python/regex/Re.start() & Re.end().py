# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string="aaadaa"
# string =input()
# patt=input()
patt="aa"
#m = re.search(patt,string)
#m =re.finditer(patt,string)
#print(m)
# for x in re.findall(patt,string):
#     print(tuple((x.start(),x.end())))

#import re
#text, pattern = input(), input()
text=string
pattern=patt
m= list(re.finditer("(?=(%s))"%pattern,text))
if not m:
    print((-1,-1))
for i in m:
    print((i.start(1),i.end(1)-1))