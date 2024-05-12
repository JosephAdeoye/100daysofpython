sum_even = 0
for even in range(0, 101, 2):
    sum_even = sum_even + even
print(f"The sum of all even numbers from 0 to 100 is {sum_even}")

# another way to implement this is

total = 0
for number in range(0, 101):
    if number % 2 == 0:
        total += number
print(f"The sum of all even numbers from 0 to 100 is {total}")
