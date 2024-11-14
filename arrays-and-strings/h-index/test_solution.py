import unittest
from solution import Solution


class TestHIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_all_zero_citations(self):
        citations = [0, 0, 0, 0, 0]
        expected = 0
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_all_same_citations(self):
        citations = [5, 5, 5, 5, 5]
        expected = 5
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_single_paper(self):
        citations = [10]
        expected = 1
        self.assertEqual(self.solution.hIndex(citations), expected)

    def test_no_papers(self):
        citations = []
        expected = 0
        self.assertEqual(self.solution.hIndex(citations), expected)


if __name__ == "__main__":
    unittest.main()
