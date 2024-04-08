"""
A simple implementation of the Hangman game.
"""

import random

class Hangman:
    """A class representing the Hangman game."""
    def __init__(self, word):
        """ Initialize Hangman object.
        Parameters:
        - word (str): The word to guess.
        """
        self.word = word.upper()
        self.guesses_left = 7
        self.guessed_letters = set()

    def display_word(self):
        """ Display the current state of the word.
        Returns:
        - str: The word with guessed letters revealed and the rest hidden.
        """
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def make_guess(self, letter):
        """ Process a player's guess and return feedback messages.
        Parameters:
        - letter (str): The letter guessed by the player.
        Returns:
        - str: Feedback message based on the correctness of the guess.
        """
        letter = letter.upper()
        if letter in self.guessed_letters:
            return "You already guessed that letter."
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.guesses_left -= 1
            return f"Incorrect guess. {self.guesses_left} guesses left."
        if set(self.word) == self.guessed_letters:
            return f"Congratulations! You guessed the word: {self.word}"
        return f"Good guess! Current word: {self.display_word()}"

def choose_random_word():
    """Choose a random word from a predefined list."""
    words = ["hangman", "python", "programming", "keyboard", "computer", "mouse"]
    return random.choice(words)

def main_menu():
    """Display the main menu and handle user input to start the game mode."""
    print("Welcome to Hangman!")
    print("Choose a game mode:")
    print("1. Regular Words")
    print("2. Custom Words (Coming Soon)")
    print("3. Multiplayer (Coming Soon)")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        regular_mode()
    elif choice == "2":
        print("Custom Words mode is not available yet.")
    elif choice == "3":
        print("Multiplayer mode is not available yet.")
    else:
        print("Invalid choice. Please enter a valid number.")

def regular_mode():
    """Start a regular Hangman game with a randomly chosen word."""
    word_to_guess = choose_random_word()
    hangman_game = Hangman(word_to_guess)
    print("Try to guess the word.")
    while hangman_game.guesses_left > 0:
        print(f"\nWord: {hangman_game.display_word()}")
        guess = input("Enter a letter: ")
        result = hangman_game.make_guess(guess)
        print(result)
        if '_' not in hangman_game.display_word():
            print("Congratulations! You guessed the word.")
            break
    if '_' in hangman_game.display_word():
        print(f"Sorry, you ran out of guesses. The word was: {word_to_guess}")

if __name__ == "__main__":
    main_menu()