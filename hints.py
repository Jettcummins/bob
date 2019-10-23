# how to turn a string inot a list 
myString = "Hello" 
myList = list(myString)
print(myList)
secret = []
# how to create a list with _ in place of letters 
for a in myList:   
	secret.append("_")

print(secret)

# how to replace an _ with a letter 

secret[2] = "1"
print(secret)