import random
#test

class Hangman:
    def __init__(self, word):
        # Initialize Hangman object with the given word in uppercase, set initial guesses, and an empty set for guessed letters.
        self.word = word.upper()
        self.guesses_left = 7
        self.guessed_letters = set()

    def display_word(self):
        # Display the current state of the word, revealing guessed letters and hiding the rest.
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def make_guess(self, letter):
        # Process a player's guess and return feedback messages.

        # Convert the guess to uppercase for case-insensitivity.
        letter = letter.upper()

        # Check if the letter has already been guessed.
        if letter in self.guessed_letters:
            return "You already guessed that letter."
        
        # Add the guessed letter to the set of guessed letters.
        self.guessed_letters.add(letter)

        # Check if the guessed letter is not in the word, decrement guesses if incorrect.
        if letter not in self.word:
            self.guesses_left -= 1
            return "Incorrect guess. {} guesses left.".format(self.guesses_left)
        
        # Check if all letters in the word have been guessed.
        if set(self.word) == self.guessed_letters:
            return "Congratulations! You guessed the word: {}".format(self.word)
        
        # If the guessed letter is correct, return feedback and the current state of the word.
        return "Good guess! Current word: {}".format(self.display_word())

def choose_random_word():
    # Choose a random word from a predefined list.
    words = ["hangman", "python", "programming", "keyboard", "computer", "mouse"]
    return random.choice(words)

def main_menu():
    # Display the main menu and handle user input to start the game mode.
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
    # Start a regular Hangman game with a randomly chosen word.
    word_to_guess = choose_random_word()
    hangman_game = Hangman(word_to_guess)

    print("Try to guess the word.")

    # Main game loop where the player makes guesses until they win or run out of guesses.
    while hangman_game.guesses_left > 0:
        print("\nWord: {}".format(hangman_game.display_word()))
        guess = input("Enter a letter: ")

        result = hangman_game.make_guess(guess)
        print(result)

        # Check if all letters have been guessed, and congratulate the player.
        if '_' not in hangman_game.display_word():
            print("Congratulations! You guessed the word.")
            break

    # If the loop ends and there are still hidden letters, reveal the word.
    if '_' in hangman_game.display_word():
        print("Sorry, you ran out of guesses. The word was: {}".format(word_to_guess))

if __name__ == "__main__":
    main_menu()
