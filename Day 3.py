# control flow with if_else and conditional operators
print('Welcome to the Rollercoaster!')
height = int(input('What is your height in centimetres? '))

# if height >= 120:
#     print('You are allowed to ride the rollercoaster')
# else:
#     print('Sorry, you need to grow taller to ride the rollercoaster')
# # the above shows conditional statements at it's basic form
#
# # > greater than
# # < less than
# # >= greater than or equals to
# # <= less than or equals to
# # == equal to
# # != not equal to
# # % gives the remainder after a division
#
# if height >= 120:
#     print('You are allowed to ride the rollercoaster')
#     age = int(input('How old are you? '))
#     if age <= 18:
#         print('Please pay $7.')
#     else:
#         print('Please pay $12.')
# else:
#     print('Sorry, you need to grow taller to ride the rollercoaster')

# # the above is an example of nesting one if else conditional in another

bill = 0

if height >= 120:
    print('You are allowed to ride the rollercoaster')
    age = int(input('How old are you? '))
    if age < 12:
        bill = 5
        print('Please pay $5.')
    elif age <= 18:
        bill = 7
        print('Please pay $7.')
    elif age >= 45 and age <= 55:
        bill = 0
        print('You won a  free ride because of your mid-life crises')
    else:
        bill = 12
        print('Please pay $12.')

    wants_photo = input('Do you want a photo? Y or N.')
    if wants_photo == 'Y':
        bill += 3
        print(f'Your total bill is ${bill}.')
    else:
        print(f'Your total cost is ${bill}')
#   indentation really matters in python.
else:
    print('Sorry, you need to grow taller to ride the rollercoaster')
# in the above we introduced the elif which is the else-if conditional. We can have as much elif between if-else.

#   logical operators

# A and B AND here is a logical operator and stipulates that A and B must be true
# C or D  OR here is also a logical operator and, it stipulates that either C or D must be true
# not E   NOT here is also a logical operator and, it basically reverses the condition. If a condition is true,
# then it becomes false, and if it was false, it becomes true.



