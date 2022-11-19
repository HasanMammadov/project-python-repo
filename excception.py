x = input('Enter your number: ')
y = input('Enter another number: ')
if int(y) > 10:
    sum = int(x) + int(y)
    message = f'Sum is {sum}'
else:
    print('Nothing to do')
print(message)

food = {'fruit':'apple', 'protein':'hamburger'}
dairy_choice = food['dairy']
print(f'Your dairy choice is {dairy_choice}')




food = {'fruit':'apple', 'protein':'hamburger'}
if 'dairy' in food:
    dairy_choice = food['dairy']
else:
    dairy_choice = 'None'
print(f'Your dairy choice is {dairy_choice}')