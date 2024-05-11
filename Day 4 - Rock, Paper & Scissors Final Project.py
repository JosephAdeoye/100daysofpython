import random
rock = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
 _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
#   Rules ---
#   Rock beats scissors (rock crushes scissors)
#   Scissors beat paper (scissors cut paper)
#   Paper beats rock (paper covers rock)

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.' ))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

random_choice = random.randint(0, 2)
if random_choice == 0:
        print(f"Computer chose: \n {rock}")
elif random_choice == 1:
        print(f"Computer chose: \n {paper}")
elif random_choice == 2:
        print(f"Computer chose: \n {scissors}")
    # print(f"Computer chose \n {random_choice}")

# paper = 1
# scissors = 2




