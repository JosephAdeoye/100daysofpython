# Review
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code. 

def greet():
    print('Hi, how are you?')
    print('Happy to see you today!')
    print('Have a great day!')

greet() 

def greet_with_name(name):
    print(f'Hi, how are you {name}?')
    print(f'Happy to see you today {name}!')
    print(f'Have a great day {name}!')

greet_with_name("Adeoye")

# # Explaining the f-string above
# # f-strings, or formatted string literals are prefixed with an 'f' and use curly braces {} to evaluate expressions inside a string. 
# # They support all kinds of expressions, including variables, operations, and even function calls.
# # EXAMPLE

name = 'Adeoye'
age = 23
greeting = f'My name is {name} and I am {age} years old!'
print(greeting)

# # f-strings can also be used to perform calculations directly in curly braces.
# # EXAMPLE

x = 10
y = 5
summation = f'{x} multiplied by {y} is equals to {x * y}'
print(summation) 

# # DIFFERENCE BETWEEN PARAMETERS AND ARGUMENTS 

# # A PARAMETER is a variable in the declaration of a function. 
# # They're like placeholders in the function definition that get their values when the function is called.

# # An ARGUMENT is the actual value that is passed to the function when it is called. 
# # ARGUMENTS are the real data passed to the parameters in the function.

# # Example

def greet(name): # Here name is the parameter
    print = f'Hello {name}'
greet('Adeoye') # Here ADEOYE is the argument that is being passed into the parameter name.

# # We can also have functions with more than one input

def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')
greet_with('Adeoye', 'Owerri')

# POSITIONAL ARGUMENTS AND KEYWORD ARGUMENTS

# POSITIONAL ARGUMENTS are passed to functions in the order they are defined. 
# The position of each argument in the function call must match the position of the corresponding parameter in the function definition.
# EXAMPLE
def print_book_details(title, author, year):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")
# Using POSITIONAL arguments, you have to pass the arguments in the exact order the parameters are defined:
print_book_details("1984", "George Orwell", 1949)

# # KEYWORD ARGUMENTS are passed to functions by explicitly stating the parameter name along with its value. 
# # This makes it clear which argument corresponds to which parameter, regardless of the order.
# # Using KEYWORD ARGUMENTS, you can specify the arguments in any order by naming them explicitly:
print_book_details(author="George Orwell", year="1949", title=1984)

# #You can also combine positional and keyword arguments, but positional arguments must come before keyword arguments
print_book_details("1984", year=1949, author="George Orwell")

def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')
greet_with(location='Owerri', name='Adeoye')