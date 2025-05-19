import random
import os 

print("Welcome to the classic game of Hangman!")
print("Try to guess the below word")

word_list = ['hello', 'goodbye', 'random', 'jello', 'monster', 'camel']

# Randomly choose a word from the word list
word_to_guess = random.choice(word_list)

placeholder = ""

word_length = len(word_to_guess)

lives = 6

print(word_to_guess)

# Display underscores in replace of the letters in the word
for position in range(word_length):
    placeholder += "_"

print(placeholder, "\n")

game_over = False

while not game_over:
    # Let the user guess
    user_guess = input("What letter do you think is in the word?: ").strip().lower()

    word_to_display = ""

    # Replace the underscore with the correct letter if it's in the word
    for letter in word_to_guess:
        if letter == user_guess:
            word_to_display += letter
        else:
           word_to_display += "_"

    print(word_to_display)
           
    if "_" not in word_to_display:
        print("YOU WIN!")
        game_over = True

