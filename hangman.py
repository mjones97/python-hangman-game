import random

def hangman():
    with open("words.txt") as file:
        words = file.read().splitlines()

    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6
    username = input("Enter a username: ").capitalize()

    print("Welcome to my Python Hangman Game, " + username + "!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess not in word:
            attempts -= 1
            print("Wrong guess. You have", attempts, "attempts left.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        revealed_word = ""
        for letter in word:
            if letter in guessed_letters:
                revealed_word += letter + " "
            else:
                revealed_word += "_ "

        print(revealed_word)

        if "_" not in revealed_word:
            print("Congrats! You guessed correctly.")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == "y":
                hangman()
            else:
                print("Thank you for playing Hangman!")
                return

    print("Game over! You've run out of attempts.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        hangman()
    else:
        print("Thank you for playing Hangman!")

hangman()
