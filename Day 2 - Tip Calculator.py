# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12

print('Welcome to my Tip Calculator')
totalCost = float(input('What is the total bill: $'))
Percent = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
numPeople = int(input('How many people to split the bill? '))
#   the above is simply straight forward and below is the arithemetic

tipAmount = totalCost * Percent/100
billAndTip = totalCost + tipAmount
tip = round(billAndTip/numPeople, 2)

print(f'Each person should pay: $ {tip}')



