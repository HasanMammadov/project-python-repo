# x = input('Enter your number: ')
# y = input('Enter another number: ')
# if int(y) > 10:
#     sum = int(x) + int(y)
#     message = f'Sum is {sum}'
# else:
#     print('Nothing to do')
# print(message)

# food = {'fruit':'apple', 'protein':'hamburger'}
# dairy_choice = food['dairy']
# print(f'Your dairy choice is {dairy_choice}')




# food = {'fruit':'apple', 'protein':'hamburger'}
# if 'dairy' in food:
#     dairy_choice = food['dairy']
# else:
#     dairy_choice = 'None'
# print(f'Your dairy choice is {dairy_choice}')



# denomenators = [5, 1, 0, 3, 4]
# numerators = [1, 2, 3, 4, 5]
# for d in denomenators:
#     for n in numerators:
#         try:
#             result = n / d
#             print(f'Result of {n} divided by {d} is {result}')
#         except: 
#             print('Unknown error ocurred')




# denomenators = [5, 1, 0, 3, 4]
# numerators = [1, 2, 3, 4, 5]
# try:
#     for d in denomenators:
#          for n in numerators:
    
#             result = n / d
#             print(f'Result of {n} divided by {d} is {result}')
    
# except:
#     print('Unknown error ocurred')



# while True:
#     no_one = int(input("The first number please : "))
#     no_two = int(input("The second number please : "))
#     try:
#         division = no_one / no_two
#         print("The result of the division is : ", division)
#         #break
#     except:
#         print("Something went wrong...Try again.")


# while True:
#     no_one = int(input("The first number please : "))
#     no_two = int(input("The second number please : "))
#     try:
#         division = no_one / no_two
#         print("The result of the division is : ", division)
#     except ZeroDivisionError:
#         print("You can't divide by 0.  Try again")


try:
    file = open('my_file.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print('No such file or directory')

