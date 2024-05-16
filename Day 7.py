import random
word_list = ['aardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

#  Todo-1: - Create an empty list called display. For each letter in the chosen_word,
#   add a '_' to 'display'
#  So if the chosen word was 'apple', display should be ['_', '_', '_', '_', '_'] with 5 '_'
#  representing each letter to guess.

display = []
for letter in chosen_word:
    display.append('_')
print(display)
guess = input('Guess a letter\n').lower()

#   Todo-2: - Loop through each position in the chosen_word;
#   If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#   e.g. If the user guessed 'p' and the chosen word was 'apple', then display should be ['_', 'p', 'p', '_', '_',].

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] == guess
#
# for letter in chosen_word:
#     if letter == guess:
#         print('Yes')
#     else:
#         print('No')
#
# #   Todo-3: - Print 'display' and you should see the guessed letter in the correct position
# #   and every other letter replace with '_'.
#
#
#

