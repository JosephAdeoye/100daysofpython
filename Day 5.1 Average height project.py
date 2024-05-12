student_heights = input('Input a list of student heights ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# below I initialized a variable to store the heights of students and set it to zero.
total_height = 0

# below every height entered into the students_heights variable, I added it the total_height above.
for height in student_heights:
    total_height += height
print(f'The sum of students height of {total_height}')

# below I initialized a variable to store the number of students whose heights were entered and set it to zero.
num_of_entries = 0

# below every entry entered into the students_heights variable is summed, so we can use it to calculate average height
for n in student_heights:
    num_of_entries += 1


# here calculated the average heights of students and rounded to the nearest whole number using the round()
average_height = round(total_height / num_of_entries)
print(f'The average height of students is {average_height}')
