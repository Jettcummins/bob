# Make a list 
myClasses = ["Algerbra", "English", "World History"]
print(myClasses)

# add an item to the list 
# append or insert 
# appened will add to the back of the list 
myClasses.append("Coding")
print(myClasses)
favClass = input("What is your favorit class?")
myClasses.append(favClass)  
print(myClasses)
# insert 
myClasses.insert(3, "Art")
print(myClasses) 
# overwrite 
myClasses[4] = "Science" 
print(myClasses)

# remove list items 
# remove, pop 
# remove will remove a specific item 
myClasses.remove("Science")
# pop will remove specific item in the index 
print(myClasses) 
myClasses.pop()
print(myClasses)
myClasses.pop(1)
print(myClasses)
# len - it returns the length of a list 
print("myClasses is " + str(len(myClasses)+ " items long")) 

print(myClasses[len(myClasses) - 1 ])
 
# LOOP THROUGH THE LIST

count = 1 
for aClass in myClasses: 
	print("Item " + str(count) + " is " + aClass)

count = count + 1 
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
# challenge: loop through the list and ass numbers to print the sum 

total = 0 
for number in numbers: 
	total +- numbr 
if "cooking" in myClasses: 
	print("Have fun cooking")
else: 
	