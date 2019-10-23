# hangman game 
myWord = "Destiny"
# how to turn a string into a list 
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

# how to keep track of misses 
secret = "Destiny"
misses = 0
secret = list(secret)

hangList = [''' pic 1''' , '''pic 2''' , '''pic 3''', '''pic 4''', '''pic 5''', '''pic 6''', '''pic 7''' ]

while misses < 7:
	guess = input("Guess a letter") 
	if guess in secret: 
		# loop through secret and find all the matching letters 
		print("That letter is in the secret word")
	else:
		misses = misses + 1 
choice = input("Type a word")


if choice == myWord:
	print("Good job that's correct")

else: 
	print(" Sorry thats wrong")


# how to check to see if your word is right or not 
letter = input("Type a letter")
if letter in myWord: 
	print("Letter is in the word")
else: 
	print("Letter is not in the word")

count = 0 
for s in myWord: 
	if s == letter: 
		print(count) 
	count+= 1
 
