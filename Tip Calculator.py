# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12

print('Welcome to my Tip Calculator')
totalCost = int(input('What is the total bill: $'))
tipPercent = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
numPeople = int(input('How many people to split the bill? '))

tip = (totalCost / numPeople) * tipPercent

print(f'Each person should pay: ${tip}')

