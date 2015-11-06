import unittest
from palindrome import checker

class TestPalindrome(unittest.TestCase):
    def test_even(self):
        self.assertTrue(checker("abccba"))
    def test_odd(self):
        self.assertTrue(checker("abcdcba"))

if '__main__' == __name__:
    unittest.main()
