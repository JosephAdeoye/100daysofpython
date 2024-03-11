print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

combined_name = name1 + name2

lower_string_name = combined_name.lower()

t = lower_string_name.count('t')
r = lower_string_name.count('r')
u = lower_string_name.count('u')
e = lower_string_name.count('e')

true = t + r + u + e

l = lower_string_name.count('l')
o = lower_string_name.count('o')
v = lower_string_name.count('v')
e = lower_string_name.count('e')

love = l + o + v + e

love_score = str(true) + str(love)







