import random

class Hangman:
    def __init__(self, word):
        self.word = word.upper()
        self.guesses_left = 7
        self.guessed_letters = set()

    def display_word(self):
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def make_guess(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            return "You already guessed that letter."
        
        self.guessed_letters.add(letter)

        if letter not in self.word:
            self.guesses_left -= 1
            return "Incorrect guess. {} guesses left.".format(self.guesses_left)
        
        if set(self.word) == self.guessed_letters:
            return "Congratulations! You guessed the word: {}".format(self.word)
        
        return "Good guess! Current word: {}".format(self.display_word())

def choose_random_word():
    words = ["hangman", "python", "programming", "keyboard", "computer", "mouse"]
    return random.choice(words)

def main_menu():
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
    word_to_guess = choose_random_word()
    hangman_game = Hangman(word_to_guess)

    print("Try to guess the word.")

    while hangman_game.guesses_left > 0:
        print("\nWord: {}".format(hangman_game.display_word()))
        guess = input("Enter a letter: ")

        result = hangman_game.make_guess(guess)
        print(result)

        if '_' not in hangman_game.display_word():
            print("Congratulations! You guessed the word.")
            break

    if '_' in hangman_game.display_word():
        print("Sorry, you ran out of guesses. The word was: {}".format(word_to_guess))

if __name__ == "__main__":
    main_menu()
