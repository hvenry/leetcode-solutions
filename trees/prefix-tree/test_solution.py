import unittest
from solution import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertTrue(self.trie.startsWith("app"))
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))

    def test_insert_and_search_multiple_words(self):
        words = ["apple", "app", "application", "bat", "batch", "batman"]
        for word in words:
            self.trie.insert(word)

        for word in words:
            self.assertTrue(self.trie.search(word))

        self.assertFalse(self.trie.search("batc"))
        self.assertFalse(self.trie.search("batmobile"))
        self.assertTrue(self.trie.startsWith("bat"))
        self.assertTrue(self.trie.startsWith("app"))
        self.assertFalse(self.trie.startsWith("cat"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.startsWith(""))

    def test_non_existent_word(self):
        self.trie.insert("hello")
        self.assertFalse(self.trie.search("hell"))
        self.assertFalse(self.trie.search("helloo"))
        self.assertTrue(self.trie.startsWith("hell"))
        self.assertFalse(self.trie.startsWith("helloo"))


if __name__ == "__main__":
    unittest.main()
