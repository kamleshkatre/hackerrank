import re


#string =input()
string="..12345678910111213141516171820212223"

#pattern=re.compile(r"([a-zA-Z0-9])\1+")
pattern=re.compile(r"([a-zA-Z0-9])")

m=pattern.search(string)
print(m)
print(m.group(1) if m else -1)
