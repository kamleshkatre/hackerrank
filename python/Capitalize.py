def solve(s):
    x=s.split(" ")
    y=[i.capitalize()for i in x]
    result=" ".join(y)
    return result
print(solve("ram shyam"))