age = input('What is your current age: ')

ageDifference = 90 - int(age)
# here I attempt to get the remaining years left by subtracting the user's age from 90
daysLeft = ageDifference * 365
# here I tried to get the days left by multiplying the user's left years by 365
weeksLeft = ageDifference * 52
# here I tried to get the weeks left by multiplying the user's left years by 52
monthsLeft = ageDifference * 12
# here I tried to get the months left by multiplying the user's left years by 12

message = f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left to live"
print(message)



