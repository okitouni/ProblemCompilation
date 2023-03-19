# 211. Design Add and Search Words Data Structure
from string import ascii_lowercase
import unittest
from collections import defaultdict

class WordDictionary:

    def __init__(self):
        self.words = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.words[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        n = len(word)
        dot_count = word.count(".")
        if dot_count > 1:
            for w in self.words[n]:
                if all((word[i] in (w[i], '.') for i in range(n))):
                    return True
        elif dot_count > 0:
            for letter in ascii_lowercase:
                if word.replace(".", letter) in self.words[n]:
                    return True
        elif word in self.words[n]:
            return True
        return False
    

class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.wordDictionary = WordDictionary()

    def test_search(self):
        self.wordDictionary.addWord("bad")
        self.wordDictionary.addWord("dad")
        self.wordDictionary.addWord("mad")
        self.assertEqual(self.wordDictionary.search("pad"), False)
        self.assertEqual(self.wordDictionary.search("bad"), True)
        self.assertEqual(self.wordDictionary.search(".ad"), True)
        self.assertEqual(self.wordDictionary.search("b.."), True)

if __name__ == '__main__':
    unittest.main()