import unittest
from palindrome import checker

class TestPalindrome(unittest.TestCase):
    def test_even_true(self):
        self.assertTrue(checker("abccba"))
    def test_odd_true(self):
        self.assertTrue(checker("abcdcba"))
    def test_even_false(self):
        self.assertFalse(checker("abcd"))
    def test_odd_false(self):
        self.assertFalse(checker("abcde"))
    def test_case_true(self):
        self.assertTrue(checker("Abcba"))

if '__main__' == __name__:
    unittest.main()
