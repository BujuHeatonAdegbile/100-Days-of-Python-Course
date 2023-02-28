#############
### DAY 7 ###
#############

# HANGMAN CHALLENGE 

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["building", "oven", "london", "table", "plant", "paper", "desktop", "coconut"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display += "_"

print(display)

end_of_game = False

while end_of_game == False:

    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])