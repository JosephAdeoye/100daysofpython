# BMI Calculator
# Write a program that calculates the BMI from a user's weight and height
# This is an improvement on the Day 2 version.

weight = input('enter your weight in kg: ')
intWeight = int(weight)
height = input('enter your height in m: ')
expHeight = float(height) ** 2
BMI = int((intWeight/expHeight))

if BMI < 18.5:
    print(f'Your BMI is {BMI}, and you are underweight.')
elif BMI <= 25:
    print(f'Your BMI is {BMI}, and you have a normal weight.')
elif BMI < 30:
    print(f'Your BMI is {BMI}, and you are overweight.')
elif BMI < 35:
    print(f'Your BMI is {BMI}, and you are obese.')
else:
    print(f'Your BMI is {BMI}, and you are critically obese.')

#   <18.5 = underweight
#   >18.5 == 25 = normal weight
#   >25 < 30 = overweight
#   >30 < 35 = obese
#   >35 = clinically obese

