import re
string=input()
#string="rabcdeefgyYhFjkIoomnpOeorteeeeet"
pattern=re.compile(r"(?<=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])([aeiouAEIOU]{2,})(?=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])")
match=pattern.findall(string)
#print(match)
if len(match)!=0:
    for mat in match:
        print(mat)
else:
    print("-1")
