import unittest
from algorithms.map import (
    is_anagram
)
from algorithms.strings import *

class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        text = "golden retriever puppies"
        this_is_an_anagram = "etrpepsi uprvieer nedlog"
        this_is_not_an_anagram = "border collie puppies"
        self.assertTrue(is_anagram(text, this_is_an_anagram))
        self.assertFalse(is_anagram(text , this_is_not_an_anagram))

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        palindrome = "murder for a jar of red rum"
        not_palindrome = "this is not a palindrome :("
        self.assertFalse(is_palindrome(not_palindrome))
        self.assertTrue(is_palindrome(remove_punctuation(palindrome)))


if __name__ == "__main__":
    unittest.main()