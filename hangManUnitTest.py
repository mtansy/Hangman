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

if __name__ == "__main__":
    unittest.main()