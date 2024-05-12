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

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if user_choice == 0:
    print(f"You chose: \n {rock}")
elif user_choice == 1:
    print(f"You chose: \n {paper}")
elif user_choice == 2:
    print(f"You chose: \n {scissors}")

computer_choice = random.randint(0, 2)
if user_choice > 2:
    print('You lose')
elif computer_choice == 0:
    print(f"Computer chose: \n {rock}")
elif computer_choice == 1:
    print(f"Computer chose: \n {paper}")
elif computer_choice == 2:
    print(f"Computer chose: \n {scissors}")

#   Rules ---
#   Rock beats scissors (rock crushes scissors)
#   Scissors beat paper (scissors cut paper)
#   Paper beats rock (paper covers rock)

# 0 for Rock, 1 for Paper or 2 for Scissors.

if computer_choice == 0 and user_choice == 2:
    print('You lost, computer wins')
elif user_choice == 0 and computer_choice == 2:
    print('You won, computer lost')

if computer_choice == 2 and user_choice == 1:
    print('You lost, computer wins')
elif user_choice == 2 and computer_choice == 1:
    print('You won, computer lost')

if computer_choice == 1 and user_choice == 0:
    print('You lost, computer wins')
elif user_choice == 1 and computer_choice == 0:
    print('You won, computer lost')

if user_choice == 0 and computer_choice == 0:
    print('It is a draw. Play Again!')
if user_choice == 1 and computer_choice == 1:
    print('It is a draw. Play Again!')
if user_choice == 2 and computer_choice == 2:
    print('It is a draw. Play Again!')