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
direction = input('You are at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if direction == 'left':
    swim_or_wait = input('Do you want to swim or wait? \n').lower()
    if swim_or_wait != 'swim':
        which_door = input('You  saw a boat and it ferried you across. You are now faced with three doors, which do you want to enter? "red", "yellow" or "blue" \n').lower()
        if which_door != 'blue':
            print('You entered a room filled with venomous snakes, Game Over!')
        else:
            print('You found the trophy. You Win!')
    else:
        print('You were attacked by a croc, Game Over!')
else:
    print('You fell into a manhole, Game Over!')
