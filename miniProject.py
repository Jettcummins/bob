print("Welcome to the To Do List!")
todoList = []
while True: 
	print("Enter a to add an item" )
	print("Enter r to remove an item")
	print("Enter p to print the list") 
	print("Enter q to quit")
	choice = input("Make your choice: ")

	if choice == "q": 
		break
	elif choice == "a":
		# add an item to the list 
		pass 
		a = input("What would you like to add?")
		todoList.append(a)
	elif choice == "r":
		# remove an item form the list
		r = input("what would you like to remove?")
		todoList.remove(r)
	elif choice == "p":
		# print the list 
		pass
		print(todoList) 
	else:
		print("This was not a choice try again")

	 

