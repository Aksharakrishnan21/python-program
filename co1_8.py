word=input("enter a string:")
first_word=word[0]
result=first_word+word[1:].replace(first_word,"$")
print(result)
