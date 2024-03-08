print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M, L ')
add_pepperoni = input('Do you want pepperoni? Y or N ')
extra_cheese = input('Do you want extra cheese? Y or N ')

#   small pizza: $15
#   medium pizza: $20
#   large pizza: $25
#   pepperoni for small pizza: +$2
#   pepperoni for medium or large pizza: +3
#   extra cheese for any size pizza: + $1

price = 0

if size == 'S':
    price = 15
    if add_pepperoni == 'Y':
        price += 2
    if extra_cheese == 'Y':
        price += 1
elif size == 'M':
    price = 20
    if add_pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
elif size == 'L':
    price = 25
    if add_pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
print(f'Your final bill is ${price}')

