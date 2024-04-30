import unittest
from unittest.mock import patch
from hangman import Hangman 

class TestHangman(unittest.TestCase):
    def setUp(self):
        self.hangman = Hangman("TEST")

    

    def test_display_word(self):
        self.assertEqual(self.hangman.display_word(), "____")

        self.hangman.make_guess("T")
        self.assertEqual(self.hangman.display_word(), "T__T")

        self.hangman.make_guess("E")
        self.assertEqual(self.hangman.display_word(), "TE_T")

    def test_make_guess(self):
        self.assertEqual(self.hangman.make_guess("T"), "Good guess! Current word: T__T")
        self.assertEqual(self.hangman.guesses_left, 7)
        self.assertEqual(self.hangman.guessed_letters, {"T"})

        self.assertEqual(self.hangman.make_guess("E"), "Good guess! Current word: TE_T")
        self.assertEqual(self.hangman.guesses_left, 7)
        self.assertEqual(self.hangman.guessed_letters, {"T", "E"})

        self.assertEqual(self.hangman.make_guess("Z"), "Incorrect guess. 6 guesses left.")
        self.assertEqual(self.hangman.guesses_left, 6)
        self.assertEqual(self.hangman.guessed_letters, {"T", "E", "Z"})

        with patch('builtins.input', side_effect=["Z"]):
            self.assertEqual(self.hangman.make_guess("Z"), "You already guessed that letter.")
            self.assertEqual(self.hangman.guesses_left, 6)
            self.assertEqual(self.hangman.guessed_letters, {"T", "E", "Z"})

    def test_display_word_initial(self):
        # Test the initial display of the word (should be all underscores)
        expected = "____"  # Corresponding to the word 'TEST'
        self.assertEqual(self.hangman.display_word(), expected)

    def test_make_guess_correct(self):
        # Test guessing a correct letter
        guess = 'T'
        result = self.hangman.make_guess(guess)
        expected_display = "T__T"  # Corresponding to the word 'TEST' with guessed letter 'T'
        self.assertEqual(result, f"Good guess! Current word: {expected_display}")
        self.assertIn(guess, self.hangman.guessed_letters)
        self.assertEqual(self.hangman.guesses_left, 7)

    def test_make_guess_incorrect(self):
        # Test guessing an incorrect letter
        guess = 'Z'
        result = self.hangman.make_guess(guess)
        self.assertEqual(result, "Incorrect guess. 6 guesses left.")
        self.assertIn(guess, self.hangman.guessed_letters)
        self.assertEqual(self.hangman.guesses_left, 6)

    def test_make_guess_repeated(self):
        # Test guessing a letter that was already guessed
        guess = 'T'
        self.hangman.make_guess(guess)  # Guess once
        result = self.hangman.make_guess(guess)  # Guess again
        self.assertEqual(result, "You already guessed that letter.")
        self.assertEqual(self.hangman.guesses_left, 7)  # Guesses left should not change



if __name__ == "__main__":
    unittest.main()
