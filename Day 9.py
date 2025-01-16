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

# Nesting 
capitals = {
    "Nigeria": "Abuja",
    "United Kingdom": "London",
    "Germany": "Berlin", 
    "United States": "Washington DC"
}

# Nesting a list in a dictionary

travels_log = [
    {
        "Country": "Germany", 
        "cities_visited": ["Frankfurt", "Berlin", "Munich", "Dortmund"], 
        "total_visits": 17
    },
    {
        "Country": "Nigeria",
        "cities_visited": ["Abuja", "Lagos", "Oyo", "Osun", "Ondo", "Imo"], 
        "total_visits": 47}
]

print(travels_log)

# In lists, items are accessed by using their index
# In Dictionaries however, items are accessed by using their keys 