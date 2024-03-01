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

print(3 * 3 + 3 / 3 - 3)
# the output of this code would be 7.0. Python follows the BODMAS rule in making this kind of calculation.
# BODMAS = Brackets, Orders (exponents and roots), Division and Multiplication, Addition and Subtraction.
# step by step execution of the code would go thus:
# 3 * 3 = 9 (Multiplication) (from left to right)
# 3 / 3 = 1 (Division) (from left to right)
# 9 + 1 = 10 (Addition) (from left to right)
# 10 - 3 = 7 (Subtraction) (from left to right)

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
print(letter.upper()) # you can also do lower
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









