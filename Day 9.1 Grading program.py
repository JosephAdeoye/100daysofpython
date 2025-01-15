student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# This is the scoring criteria
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# TODO-1 Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2 Write your code below to add the grades to student_grades.

student_grades = {}

for key, value in student_scores.items():
    if 91 <= value <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= value <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)