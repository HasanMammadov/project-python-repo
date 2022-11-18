def order_food(name, main_course, drink=None, desert = None):
    print(f'Here is order for {name}')
    print(f'Main course is {main_course}')
    if(drink!=None):
        print(f'Drink is {drink}')
    if(desert!=None):
        print(f'Desert is {desert}')

order_food('Messi','Beef')
order_food('Ronaldo','Per Peri Chicken','Water')
order_food('Saka', 'fish&chicps','Coke','Pie')