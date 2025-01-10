import math
# Instructions
# You are painting a wall. The instructions on the paint says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you will need to buy.
# NUMBER OF CANS = (wall height X wall width) / coverage per can
# e.g Height = 2, Width = 4, Coverage = 5
# NUMBER OF CANS = (2 X 4) / 5
# = 1.6

# But because you can't buy 0.6 can of paint, your answer must be rounded up to 2 cans.

# Write your code below this line

def paint_calc(height, width, cover):
    area = height * width
    apprx_number_of_cans = area / 5
    number_of_cans = math.ceil(apprx_number_of_cans)
    print(f"You will need {number_of_cans} cans of paint!")


# Write your code above this line

# Don't change the code below this line
test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
