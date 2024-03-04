# control flow with if_else and conditional operators
print('Welcome to the Rollercoaster!')
height = int(input('What is your height in centimetres? '))

if height >= 120:
    print('You are allowed to ride the rollercoaster')
else:
    print('Sorry, you need to grow taller to ride the rollercoaster')
# the above shows conditional statements at it's basic form

# > greater than
# < less than
# >= greater than or equals to
# <= less than or equals to
# == equal to
# != not equal to
# % gives the remainder after a division

if height >= 120:
    print('You are allowed to ride the rollercoaster')
    age = int(input('How old are you? '))
    if age <= 18:
        print('Please pay $7.')
    else:
        print('Please pay $12.')
else:
    print('Sorry, you need to grow taller to ride the rollercoaster')

# # the above is an example of nesting one if else conditional in another

if height >= 120:
    print('You are allowed to ride the rollercoaster')
    age = int(input('How old are you? '))
    if age < 12:
        print('Please pay $5.')
    elif age <= 18:
        print('Please pay $7.')
    else:
        print('Please pay $12.')
else:
    print('Sorry, you need to grow taller to ride the rollercoaster')
# in the above we introduced the elif which is the else-if conditional. We can have as much elif between if-else.
