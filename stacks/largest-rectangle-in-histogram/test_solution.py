import unittest
from solution import Solution


class TestLargestRectangleArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        heights = [2, 1, 5, 6, 2, 3]
        self.assertEqual(self.solution.largestRectangleArea(heights), 10)

    def test_single_bar(self):
        heights = [5]
        self.assertEqual(self.solution.largestRectangleArea(heights), 5)

    def test_two_bars(self):
        heights = [2, 4]
        self.assertEqual(self.solution.largestRectangleArea(heights), 4)

    def test_decreasing_heights(self):
        heights = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.largestRectangleArea(heights), 9)

    def test_increasing_heights(self):
        heights = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.largestRectangleArea(heights), 9)

    def test_all_same_height(self):
        heights = [3, 3, 3, 3, 3]
        self.assertEqual(self.solution.largestRectangleArea(heights), 15)

    def test_empty_heights(self):
        heights = []
        self.assertEqual(self.solution.largestRectangleArea(heights), 0)

    def test_mixed_heights(self):
        heights = [2, 1, 2]
        self.assertEqual(self.solution.largestRectangleArea(heights), 3)


if __name__ == "__main__":
    unittest.main()
