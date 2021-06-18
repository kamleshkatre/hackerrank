# You are given a string .
#  contains alphanumeric characters only.
#  Your task is to sort the string  in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Sample Input
#
# Sorting1234
# Sample Output
#
# ginortS1324


string1=input()
list1 = [i for i in string1]
listdigiteven=[]
listdigitodd=[]
listupper=[]
listslower=[]
for ch in string1:
    if ch.isdigit():
        if int(ch)%2==0:
            listdigiteven.append(ch)
        else :
            listdigitodd.append(ch)
    elif ch.isupper():
        listupper.append(ch)
    elif ch.islower():
        listslower.append(ch)
    else :
        pass

listslower.sort()
listupper.sort()
listdigitodd.sort()
listdigiteven.sort()
final ="".join(listslower)+"".join(listupper)+"".join(listdigitodd)+"".join(listdigiteven)
print(final)