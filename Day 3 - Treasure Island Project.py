print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to Treasure Island!')
print('Your objective is to find the Treasure.')
direction = input('You are at a cross road. Where do you want to go? Type "left" or "right" \n')
what_direction = direction.lower()

if what_direction != 'left':
    print('You fell into a manhole, Game Over!')
# else:

swim_wait = input('You have come to a slow flowing river, What do you want to do? Type "swim" or "wait" \n')
swim_or_wait = swim_wait.lower()

if swim_or_wait != 'wait':
    print('You were attacked by a crocodile, Game Over')

door = input('You are faced with three doors. Which do you enter? Type "blue", "yellow", "red" \n')
which_door = door.lower()

if which_door == 'yellow':
    print('Congratulations, you have located the treasure, You Win!')
elif which_door == 'blue':
    print('You were eaten by beasts, Game Over')
elif which_door == 'red':
    print('You fell off a cliff, Game Over')
else:
    print('Game Over')

