import random
import os 

print("Welcome to the classic game of Hangman!")
print("Try to guess the below word")

word_list = ['hello', 'goodbye', 'random', 'jello', 'monster', 'camel']

# Randomly choose a word from the word list
word_to_guess = random.choice(word_list)
placeholder = ""
word_to_display = ""
print(word_to_guess)

# Display underscores in replace of the letters in the word
for letter in word_to_guess:
    letter = "_"
    placeholder += letter

print(placeholder, "\n")

# Let the user guess
user_guess = input("What letter do you think is in the word?: ").strip().lower()

# Replace the underscore with the correct letter if it's in the word
for letter in word_to_guess:
    if user_guess != letter:
        letter = "_"
        word_to_display += letter
    else:
        letter = user_guess
        word_to_display += letter
print(word_to_display)