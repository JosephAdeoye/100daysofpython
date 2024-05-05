import random

# split string method
names_string = input('Give me everybody\'s names, separated by a comma. \n')
names = names_string.split(', ')

names_index = random.randint(0, len(names) - 1)


who_pays = names[names_index]


print(f'{who_pays} is going to pay for the meal today.')