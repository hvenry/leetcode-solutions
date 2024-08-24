import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        word1 = "abc"
        word2 = "pqrs"

        res = self.solution.mergeAlternately(word1, word2)
        self.assertEqual(res, "apbqcrs")

if __name__ == "__main__":
    unittest.main()
