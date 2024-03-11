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

L = lower_string_name.count('l')
o = lower_string_name.count('o')
v = lower_string_name.count('v')
e = lower_string_name.count('e')

love = L + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f'Your love score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50:
    print(f'Your love score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}')






