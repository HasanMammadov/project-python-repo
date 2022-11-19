try:
    print(x)
    x = 2/0
except ZeroDivisionError:
    print('Attempt to divide by zero')
except Exception as e:
    print(f'Something else went wrong: {e}')