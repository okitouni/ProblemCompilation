# 208. Implement Trie (Prefix Tree)
import unittest


class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        node = self.head
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = None

    def search(self, word: str) -> bool:
        node = self.startsWith_(word)
        return "#" in node if node else False

    def startsWith_(self, prefix: str) -> bool:
        node = self.head
        for char in prefix:
            if char not in node:
                return None
            node = node[char]
        return node

    def startsWith(self, prefix: str) -> bool:
        return self.startsWith_(prefix) is not None

class Test(unittest.TestCase):
    def test1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(trie.search("apple"), True)
        self.assertEqual(trie.search("app"), False)
        self.assertEqual(trie.startsWith("app"), True)
        trie.insert("app")
        self.assertEqual(trie.search("app"), True)
    

if __name__ == "__main__":
    unittest.main()