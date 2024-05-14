import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the Password Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like to have in your password?\n'))
nr_numbers = int(input('How many numbers would you like to have in your password?\n'))

for_letters = ''.join(random.sample(letters, nr_letters))
for_symbols = ''.join(random.sample(symbols, nr_symbols))
for_numbers = ''.join(random.sample(numbers, nr_numbers))

pass_word = for_letters + for_symbols + for_numbers




print(f'Your password is  {pass_word}')


