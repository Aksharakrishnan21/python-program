string=input("Enter a string: ")
length=len(string)
if length>2:
    if string[-3:]=="ing":
        string=string+"ly"
    else:
        string=string+"ing"
    print("the string=>",string)
else:
    print("the string is too short")
