import random


print("Welcome to the classic game of Hangman!")
print("Try to guess the below word")

word_list = ['hello', 'goodbye', 'random', 'jello', 'monster', 'camel']

# Randomly choose a word from the word list
word_to_guess = random.choice(word_list)

placeholder = ""

word_length = len(word_to_guess)

# Display underscores in replace of the letters in the word
for position in range(word_length):
    placeholder += "_"

print(placeholder, "\n")

game_over = False

correct_letters = []

lives = 6
print(f"Your starting lives are: {lives}")

while not game_over:
    
    # Let the user guess
    user_guess = input("What letter do you think is in the word?: ").strip().lower()
    
    
    word_to_display = ""
    
    # Replace the underscore with the correct letter if it's in the word
    for letter in word_to_guess:
        if letter == user_guess:
            word_to_display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            word_to_display += letter
        else:
           word_to_display += "_"
           
    print(word_to_display)
    

    # Handle decrementing the user's lives if they get the answer wrong
    if user_guess not in word_to_guess:
        print(f"'{user_guess}' is not in the word, try again.")
        lives -= 1
        print(f"\nLives left: {lives}")

        
        if lives == 0:
            print(word_to_display)
            print(f"The word to guess was: {word_to_guess}")
            print()
            print("GAME OVER. YOU RAN OUT OF LIVES!")
            game_over = True
    else:
        print(f"'{user_guess}' is in the word! Keep going!")
        print(f"\nLives left: {lives}")
        

    # Handle if the user wins the game
    if "_" not in word_to_display:
        print("YOU WIN! GREAT JOB!")
        game_over = True


    

    
    

