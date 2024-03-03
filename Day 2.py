print('Obaloluwa'[2])
# the [] indexing notation is used to access a specific character in a string. Indexing starts from 0.

print(456 + 654)
# this is a simple addition calculation possible with python

print(type(8/2))
# is a built-in Python function that returns the type of object. The type here would be a float.
# you can even get the type of data stored in a variable. See below for example

name = 'King'
print(type(name))
# the type of the object above would be string.

sentence = 'Python is an amazing programming language'
sentence.find('is')
indexz = sentence.find('is')

# the .find() method is a method used to find the index of the first occurrence of a substring within another string
# in the above sentence.find('is') would look for the first occurence of 'is' in the string in sentence
# and indexz would store the index that 'is' falls in which is 7
# if the char is not found, it would return -1


text = 'Hello World'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet.find(text[1])
index = alphabet.find(text[1])
print(index)

# what is happening in alphabet.find(text[1]) is that (text[1]) is taking note of the character at index 1 in text var.
# the alphabet.find is to look at the where the character in (text[1]) is in alphabet.
# the character (text[1]) is e. e in alphabet is at index 4.
# index stores what the output of alphabet.find(text[1]) which is 4.
# basically the interpretation of alphabet.find(text[1]) is that in var alphabet, find the char of text's 1 index.

letter = 'hello'
print(letter.upper())   # you can also do lower
# the above is just simple string manipulation

school = 'School'
moreschool = 'ashduywieoldndb'
schoolindex = moreschool.find(school[0])
print(schoolindex)
# the above would return -1 which means it could not find the char because S is different from s
# to solve this, we will use the string transform method

school = 'School'
moreschool = 'ashduywieoldndb'
schoolindex = moreschool.find(school.lower()[0])
print(schoolindex)
# now it returns 1 which is the second char in moreschool string.

num_char = (len(input("What is your name?\n")))

new_num_char = str(num_char)
# the above is how you change data type. The content in num_char is a int and I converted it to str.
print(type(new_num_char))

print('Your name has ' + new_num_char + ' characters')

# you can use the bracket notation to access the value stored in a var and store it in another var

studentsName = 'Joseph Oba Temitope Adeoye'
studentsName.find('Joseph')
firstName = studentsName.find('Joseph')
print(firstName)

# day 2 first challenge
# Instructions
# Write a program that adds the digits in a 2 digit number.
# e.g If the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input('Type a two digit number')

first_num = two_digit_number[0]
second_num = two_digit_number[1]
# in the above, i isolated the two digits from each other

first_number = int(first_num)
second_number = int(second_num)
# in the above, i changed the individually isolated numbers from str that they were by default to int
print(first_number + second_number)
# above i mathematically summed the two digits

# mathematical operators
# 5 + 2 # addition
# 6 - 2 # subtraction
# 8 / 2 # division
# 2 * 2 # multiplication
# 2 ** 2 # exponents (raise to the power)

# when numbers are on the same line, there is usually an order that python follows to execute the calculation: BODMAS

print(3 * 3 + 3 / 3 - 3)
# the output of this code would be 7.0. Python follows the BODMAS rule in making this kind of calculation.
# BODMAS = Brackets, Orders (exponents and roots), Division and Multiplication, Addition and Subtraction.
# step by step execution of the code would go thus:
# 3 * 3 = 9 (Multiplication) (from left to right)
# 3 / 3 = 1 (Division) (from left to right)
# 9 + 1 = 10 (Addition) (from left to right)
# 10 - 3 = 7 (Subtraction) (from left to right)

# print(3 * 3 + 3 / 3 - 3) # what can be changed in this line of code so the answer equals 3 and not 7?

print(3 * 3 + 9 / 3 - 9)    # this equals 3

# how do we round off in python

print(round(8 / 3))     # the round method takes away the float to the nearest whole number

print(round(8 / 3, 2))  # we can also specify how many decimal places we want. Here, it is two

print(8 // 3)   # the // is the floor method of also eliminating floats. The output here would also be an int

#   when we want to manipulate a variable that holds an existing number the below can come handy
score = 1
score += 1
score *= 2
print(score)

# F-strings let us put variables and expressions into strings with having to convert the data type
# let say we have variables with different data type like below

goal = 1    # int
height = 1.82   # float
isWinning = True    # boolean

#   with the F-string we can write the above into a string with having to change data type

print(f"Your goal is {goal}, your height is {height}, and you are winning is {isWinning}")













