string=input("Enter a string: ")
d={}
for char in string:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1
print("Character frequencies:", d)