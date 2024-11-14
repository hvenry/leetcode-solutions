import unittest
from solution import Solution


class TestHIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        citations = [3, 0, 6, 1, 5]
        self.assertEqual(self.solution.hIndex(citations), 3)

    def test_all_zero_citations(self):
        citations = [0, 0, 0, 0]
        self.assertEqual(self.solution.hIndex(citations), 0)

    def test_all_same_citations(self):
        citations = [4, 4, 4, 4]
        self.assertEqual(self.solution.hIndex(citations), 4)

    def test_increasing_citations(self):
        citations = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.hIndex(citations), 3)

    def test_decreasing_citations(self):
        citations = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.hIndex(citations), 3)

    def test_mixed_citations(self):
        citations = [10, 8, 5, 4, 3]
        self.assertEqual(self.solution.hIndex(citations), 4)

    def test_single_paper(self):
        citations = [10]
        self.assertEqual(self.solution.hIndex(citations), 1)

    def test_no_papers(self):
        citations = []
        self.assertEqual(self.solution.hIndex(citations), 0)


if __name__ == "__main__":
    unittest.main()
