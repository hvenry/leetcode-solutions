import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPrefixOfWord(self):
        self.assertEqual(
            self.solution.isPrefixOfWord("i love eating burger", "burg"), 4
        )
        self.assertEqual(
            self.solution.isPrefixOfWord("this is a simple test", "sim"), 4
        )
        self.assertEqual(self.solution.isPrefixOfWord("hello world", "wor"), 2)
        self.assertEqual(self.solution.isPrefixOfWord("hello world", "hello"), 1)
        self.assertEqual(self.solution.isPrefixOfWord("hello world", "world"), 2)
        self.assertEqual(self.solution.isPrefixOfWord("hello world", "test"), -1)
        self.assertEqual(
            self.solution.isPrefixOfWord(
                "a quick brown fox jumps over the lazy dog", "qui"
            ),
            2,
        )
        self.assertEqual(
            self.solution.isPrefixOfWord(
                "a quick brown fox jumps over the lazy dog", "cat"
            ),
            -1,
        )


if __name__ == "__main__":
    unittest.main()
