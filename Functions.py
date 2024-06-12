#   function = a block of reusable code
#   place a () after the function name to invoke it

def happy_birthday(name, age):
    print(f'Happy Birthday to {name}!')
    print(f'You are {age} years old !')
    print('Happy Birthday to you!')
    print()

happy_birthday('Taiwo', 20)
happy_birthday('AY', 22)
happy_birthday('BEN', 31)

def display_invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount: .2f} is due on {due_date}')

display_invoice('Joseph', 100.768, '26/12')

# return = statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z



def divide(x, y):
    z = x / y
    return z


print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name('joseph', 'adeoye')
print(full_name)


