num = input('Guess the num what I have in my mind: ')
while True:
    if int(num) < 39:
        print('A little higher')
        num = input('Guess the num what I have in my mind: ')
    elif int(num) > 39:
        print(“A little lower”)
        num = input('Guess the num what I have in my mind: ')
    else:
        print('you guessed it, it is 39')
    break