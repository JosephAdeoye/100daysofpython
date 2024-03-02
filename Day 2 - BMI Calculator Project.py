# BMI Calculator
# Write a program that calculates the BMI from a user's weight and height
# The BMI is calculated by dividing a person's weight (in kg) by their height (in m)

weight = input('enter your weight in kg: ')
intWeight = int(weight)
# in the above, I converted the weight to an int from a str and stored it in intWeight
height = input('enter your height in m: ')
intHeight = float(height) ** 2
# in the above, I converted the height from a str to a float and stored it in intHeight
BMI = intWeight/intHeight
# the above is just the formula of getting the BMI weight/height ** 2
wholeBMI = int(BMI)
# in the above, I changed the data type of BMI to int to eliminate floats
print(wholeBMI)



