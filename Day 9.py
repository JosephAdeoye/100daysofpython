# Dictionaries in python work similarly to dictionaires in real life. 

#  {key: value}

programming_dictionary = {
    "bug": "An error in a program that prevents the program from running as expected.",
    "function": "A piece of code that you can easily call over and over again.",
    "loop": "The action of doing something over and over again."
}

# retrieving an item from a dictionary
print(programming_dictionary["bug"])

# adding a new item to a dictionary

programming_dictionary["recursion"] = "A function that calls itself."

# creating an empty dictionary

empty_dictionary = {}

# wiping an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# editing an item in a dictionary

programming_dictionary["bug"] = "A moth in your computer."
print(programming_dictionary)

# looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])