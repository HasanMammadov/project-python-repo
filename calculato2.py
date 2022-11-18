def calculator(x,y, operator):
    if operator == '+':
        result = x+y
    elif operator == '-':
        result = x-y
    elif operator == '*':
        result = x*y
    else: 
        result = x/y
    
    return result

print(calculator(10,2,'*'))