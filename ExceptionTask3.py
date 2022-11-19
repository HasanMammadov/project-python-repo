# fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
# while True:
# 	try:
# 		index = int(input("Pick an index number to choose your favorite fruit: "))
# 		print("My favorite fruit is", fruits[index])
# 		break
# 	except IndexError:
# 		print("There is no such an index. Try again!")
# 	except ValueError:
# 		print("You should enter integer. Try again!")


fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
count = 3
while count > 0:
	try:
		index = int(input("Pick an index number to choose your favorite fruit: "))
		print(f"My favorite fruit is: ", fruits[index])
	except IndexError:
		count -= 1
		print(f"There is no such an index. You have {count} right left. Try again!")
	except ValueError:
		print(f"You should enter integer. You have {count} right left. Try again!")
	else:
		print("Congrats! You've entered a valid input.")
		break
	finally:
		print("Our fruits are always fresh!")