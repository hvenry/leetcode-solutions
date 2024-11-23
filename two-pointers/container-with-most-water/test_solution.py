import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.solution.maxArea(height), 49)

    def test_single_element(self):
        height = [1]
        self.assertEqual(self.solution.maxArea(height), 0)

    def test_two_elements(self):
        height = [1, 2]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_decreasing_heights(self):
        height = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.maxArea(height), 6)

    def test_increasing_heights(self):
        height = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxArea(height), 6)

    def test_same_heights(self):
        height = [3, 3, 3, 3, 3]
        self.assertEqual(self.solution.maxArea(height), 12)

    def test_large_input(self):
        height = [i for i in range(1, 10001)]
        self.assertEqual(self.solution.maxArea(height), 25000000)


if __name__ == "__main__":
    unittest.main()
