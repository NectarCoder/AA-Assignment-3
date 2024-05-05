import sys
import unittest
from main import *


class Tests(unittest.TestCase):

    # TEST RANDOM STRINGS

    def test_1(self):
        word1 = "someone"
        word2 = "sometwo"
        self.assertEqual(levenshtein_distance(word1, word2), 3)

    def test_2(self):
        word1 = "hi there"
        word2 = "hi where"
        self.assertEqual(levenshtein_distance(word1, word2), 1)

    def test_3(self):
        word1 = "programming"
        word2 = "program"
        self.assertEqual(levenshtein_distance(word1, word2), 4)

    def test_4(self):
        word1 = "intelligent"
        word2 = "intelligence"
        self.assertEqual(levenshtein_distance(word1, word2), 2)

    def test_5(self):
        word1 = "exemplification"
        word2 = "example"
        self.assertEqual(levenshtein_distance(word1, word2), 10)

    def test_6(self):
        word1 = "encyclopedia"
        word2 = "wikipedia"
        self.assertEqual(levenshtein_distance(word1, word2), 7)

    def test_7(self):
        word1 = "unprecedented"
        word2 = "extraordinary"
        self.assertEqual(levenshtein_distance(word1, word2), 10)

    def test_8(self):
        word1 = "catastrophe"
        word2 = "apocalypse"
        self.assertEqual(levenshtein_distance(word1, word2), 8)

    def test_9(self):
        word1 = "electroencephalograph"
        word2 = "magnetoencephalography"
        self.assertEqual(levenshtein_distance(word1, word2), 7)

    def test_10(self):
        word1 = "OptimusPrime"
        word2 = "NemesisPrime"
        self.assertEqual(levenshtein_distance(word1, word2), 6)

    # TEST STRINGS FROM INPUT FILE

    def test_11(self):
        word1 = "word_11"
        word2 = "word_12"
        self.assertEqual(levenshtein_distance(word1, word2), 1)

    def test_12(self):
        word1 = "word_21"
        word2 = "word_22"
        self.assertEqual(levenshtein_distance(word1, word2), 1)

    def test_13(self):
        word1 = "kitten"
        word2 = "sitting"
        self.assertEqual(levenshtein_distance(word1, word2), 3)

    def test_14(self):
        word1 = "book"
        word2 = "back"
        self.assertEqual(levenshtein_distance(word1, word2), 2)

    def test_15(self):
        word1 = "algorithm"
        word2 = "logarithm"
        self.assertEqual(levenshtein_distance(word1, word2), 3)

    def test_16(self):
        word1 = "hell0"
        word2 = "hell0"
        self.assertEqual(levenshtein_distance(word1, word2), 0)

    def test_17(self):
        word1 = "apple"
        word2 = "snapple"
        self.assertEqual(levenshtein_distance(word1, word2), 2)

    def test_18(self):
        word1 = "houses"
        word2 = "mouse"
        self.assertEqual(levenshtein_distance(word1, word2), 2)

    def test_19(self):
        word1 = "sun"
        word2 = "moon"
        self.assertEqual(levenshtein_distance(word1, word2), 3)

    def test_20(self):
        word1 = "asdf4321"
        word2 = "xyzs4321"
        self.assertEqual(levenshtein_distance(word1, word2), 4)

    def test_21(self):
        word1 = "sameword"
        word2 = "sameword"
        self.assertEqual(levenshtein_distance(word1, word2), 0)
