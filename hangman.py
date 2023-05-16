import random
import string

def hangman():
    # Prompt user to create a username
    username = input("Enter username: ")
    # Set up target words
    words = ['python', 'programming', 'technology', 'hangman', 'game']
    # Randomly choose one of the target words
    word = random.choice(words).lower()
    # Created an empty list to keep track of guessed letters
    guessed_letters = []
    # Number of total attempts
    attempts = 6
   
    print("Welcome to Hangman" + ' ' + username + '!')
   
    while True:
        # Display current word with blanks for unguessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("\n" + display_word)

        # Print congrats message when word is guessed correctly
        if display_word == word:
            print("\nCongratulations! You guessed the word correctly.")
            break

        # Print game over message with solutuon after max numbers of attempts
        if attempts == 0:
            print("\nGame over! You ran out of attempts. The word was:", word)
            break
        
        # Prompt the user to enter a letter
        guess = input("\nEnter a letter: ").lower()
       
        # Error message when more than one letter is entered at once
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
       
        # Error message when guessing a letter that has been used already
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
       
        # Add guessed letters to list
        guessed_letters.append(guess)
       
        # display correct/incorrect message when letter is guessed
        if guess in word:
            print("Correct guess!")
        else:
            # when guessed incorrectly, the user loses an attempt
            attempts -= 1
            print("Wrong guess. Attempts remaining:", attempts)

hangman()
