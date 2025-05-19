import random

print('Welcome to the classic game of Hangman!')

word_list = ['hello', 'goodbye', 'random', 'jello', 'monster', 'camel']

# Randomly choose a word from the word list
word_to_guess = random.choice(word_list)

# Let the user guess
user_guess = input("Try to guess a letter in the word!: ").strip().lower()

if user_guess in word_to_guess:
    print("Right!")
else:
    print("Wrong")

