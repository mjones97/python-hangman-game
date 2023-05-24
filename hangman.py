import random

#Prompt a username from the user
username = input("Enter a username: ").capitalize()

def hangman():
    # opens file in read mode
    with open("words.txt") as file:
        # returns the entire file as a string and splits the string into a list of lines
        words = file.read().splitlines()
    # List of words to choose from
    words = ['apple', 'banana', 'orange', 'grape', 'watermelon']
    # Select a random word from the list
    word = random.choice(words)
    # List to store guessed letters
    guessed_letters = []
    # Number of attempts allowed
    attempts = 6
    # Print welcome message
    print("Welcome to my Python Hangman Game" + " " + username + "!")
    # Print initial representation of the word with underscores
    print("_ " * len(word))

    # Main game loop
    while attempts > 0:
        # Prompt the player to enter a letter guess
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
            
        # Check if the guessed letter is not in the word
        if guess not in word:
            # Decrement the number of attempts
            attempts -= 1
            print("Wrong guess. You have", attempts, "attempts left.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Construct the revealed word with guessed letters and underscores
        revealed_word = ""
        for letter in word:
            if letter in guessed_letters:
                revealed_word += letter + " "
            else:
                revealed_word += "_ "

        # Print the revealed word
        print(revealed_word)

        # Check if the word has been completely guessed
        if "_" not in revealed_word:
            # Display congratulations message
            print("Congrats! You guessed correctly.")
            # Prompt the player to play again
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                hangman()  # Restart the game by calling the hangman() function recursively
            else:
                print("Thank you for playing Hangman!")
                return

    # Game over, player ran out of attempts
    print("Game over! You've run out of attempts.")
    # Prompt the player to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        hangman()  # Restart the game by calling the hangman() function recursively
    else:
        print("Thank you for playing Hangman!")

# Call the hangman function to start the game
hangman()
