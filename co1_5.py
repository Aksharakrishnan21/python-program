number=input("enter the number:").split()
result=[]
for x in number:
  x=int(x)
  if x>100:
    result.append ("over")
  else:
    result.append ("x")
print(result)
