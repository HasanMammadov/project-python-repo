fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
while True:
	try:
		index = int(input("Pick an index number to choose your favorite fruit"))
		print("My favorite fruit is", fruits[index])
		break
	except IndexError:
		print("There is no such an index. Try again!")
	except ValueError:
		print("You should enter integer. Try again!")