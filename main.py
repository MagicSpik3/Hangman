import random
import csv

def get_words(filename = 'filename.csv'):

    words = []
    # Open the CSV file
    with open(filename) as f:
        lines = f.readlines()

    # Loop over each row in the CSV file
    for row in lines:
        # Append the row to the data list
        row = row.strip()
        words.append(row)
        #print(row)

# read in stop words and remove them

    return(words)

# Define a list of words to use in the game
#



# Define a function to print the current state of the game
def print_game_state():
    print(f"Word: {' '.join(hidden_word)}")
    print(f"Guessed letters: {' '.join(guessed_letters)}")
    print(f"Guesses remaining: {max_guesses - wrong_guesses}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # set up the game
    # get the word list:
    words = get_words(filename = '1-1000.txt')
#    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
    # Choose a word at random from the list
    word = random.choice(words)
    word = word.strip()
    #print(word)
    #print(len(word))
    #print(len(word.strip()))


    # Create a list of underscores to represent the hidden word
    hidden_word = ['_' for letter in word]

    # Define the number of guesses the player gets before they lose
    max_guesses = 10

    # Define a list to keep track of the letters the player has guessed
    guessed_letters = []
    wrong_guesses = 0

    # Start the game loop
    while max_guesses - (wrong_guesses) > 0:
        # Print the current state of the game
        print_game_state()

        # Prompt the player to guess a letter
        guess = input("Guess a letter: ")

        # If the player has already guessed the letter, tell them and skip to the next iteration of the loop
        if guess in guessed_letters:
            print(f"You already guessed {guess}. Try a different letter.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # If the guessed letter is in the word, update the hidden word to show the guessed letter(s)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = guess
        else:
            wrong_guesses += 1
            print("you guessed wrong. you have", wrong_guesses, "wrong guesses")

        # If the hidden word now matches the word, the player has won the game
        if ''.join(hidden_word) == word:
            print(f"Congratulations, you guessed the word '{word}'!")
            break

    # If the player has run out of guesses, they lose the game
    if max_guesses - (wrong_guesses) == 0:
        print(f"Sorry, you ran out of guesses. The word was '{word}'.")
    # This is a sample Python script.

    # Press Shift+F10 to execute it or replace it with your code.
    # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
