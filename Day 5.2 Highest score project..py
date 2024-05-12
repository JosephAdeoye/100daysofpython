student_scores = input('Input a list of student scores here ').split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_scores = student_scores[0]

for score in student_scores:
    if score > highest_scores:
        highest_scores = score
print(f'The highest score among students is {highest_scores}')