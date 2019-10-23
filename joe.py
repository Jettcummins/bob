# Jett Cummins period 6 

# variable Declaeration and assignment 
myVariable = "Joe" # String variable 
myNumber = 12 # int variable 
myDecimal = 12.6 # float variable 

# Make a variable and assign it a string variable 
print("3 + 12 = " + str(3+ 12))

# while loops 
x = 1
while x <= 10:
	print(x)
	x += 1 
# challenge: make a loop that counts down from 100 to 1 
y = 100 
while y >= 1:
	print(y)
	y -= 1

# string concatenation 
# example

string1 = "Hello "
string2 = "World "
print(string1 + string2 + "!")

#challenge: make a variable with your favorit movie 

string1 = "My favorit movie is "
string2 = "A Silent Voice "
print(string1 + string2)

# input 
# Example 
yourName = input("What is your name") 
print("Hello" + yourName) 
#challenge"print your favorit song 
yourName = input("What is your favorite song?") 
print("I like" + yourName + " to" )


# casting change one type into another 
myNum = input("Enter a number") #myNum is a string type
myNum = int(myNum) + 10 # myNum is now an int 
print("The awnswer is " + str(myNum))

# ask two numbers add them then print the sum 
myNum1 = int(input("Enter a number"))
myNum2 = int(input("Enter another number"))
myNum3 = (myNum1) + (myNum2) 
print("The awnswer is " + str(myNum3))

# if and if/else 