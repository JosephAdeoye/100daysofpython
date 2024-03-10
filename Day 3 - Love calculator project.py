print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

# Count the total occurrences of 'true love' characters in the name
total_occurrences_name1 = lower_case_name1.count('t') + lower_case_name1.count('r') + lower_case_name1.count('u') + \
                            lower_case_name1.count('e') + lower_case_name1.count('l') + lower_case_name1.count('o') + \
                            lower_case_name1.count('v') + lower_case_name1.count('e')

total_occurrences_name2 = lower_case_name2.count('t') + lower_case_name2.count('r') + lower_case_name2.count('u') + \
                            lower_case_name2.count('e') + lower_case_name2.count('l') + lower_case_name2.count('o') + \
                            lower_case_name2.count('v') + lower_case_name2.count('e')

final_occurrence_name1 = str(total_occurrences_name1)
final_occurrence_name2 = str(total_occurrences_name2)

love_level = int(final_occurrence_name1) + int(final_occurrence_name2)
print(love_level)

# if love_level >= 40:
#     print('lol')
# else:
#









