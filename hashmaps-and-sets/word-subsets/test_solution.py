import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case_1(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["e", "o"]
        expected = ["facebook", "google", "leetcode"]
        self.assertEqual(self.solution.wordSubsets(words1, words2), expected)

    def test_example_case_2(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["l", "e"]
        expected = ["apple", "google", "leetcode"]
        self.assertEqual(self.solution.wordSubsets(words1, words2), expected)

    def test_example_case_4(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["lo", "eo"]
        expected = ["google", "leetcode"]
        self.assertEqual(self.solution.wordSubsets(words1, words2), expected)

    def test_example_case_5(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["ec", "oc", "ceo"]
        expected = ["facebook", "leetcode"]
        self.assertEqual(self.solution.wordSubsets(words1, words2), expected)


if __name__ == "__main__":
    unittest.main()
