import random

random_number = random.randint(1, 9)

print(random_number)

random_float = random.uniform(0.0, 5.0)

print(random_float)

# Python lists
# lists can contain any type of data
# it is also important to note that lists have orders and the other is not lost when the list is stored in a variable

fruits = ['apple', 'orange', 'pawpaw', 'cucumber', 'date', 'coconut']

print(fruits[0])

# you can have positive or negative index

fruits[1] = 'oranjen'

# you can also select an item in the list and change it

fruits.append('cashew')

# using the append function, we can add an item to the end of our list.

# if you have more than one item, you can use the extend function. See below

fruits.extend(['mango', 'pineapple'])

