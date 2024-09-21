import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.findMin([3, 4, 5, 1, 2]), 1)

    def test_sorted_array(self):
        self.assertEqual(self.solution.findMin([1, 2, 3, 4, 5]), 1)

    def test_single_element(self):
        self.assertEqual(self.solution.findMin([1]), 1)

    def test_two_elements(self):
        self.assertEqual(self.solution.findMin([2, 1]), 1)

    def test_large_rotation(self):
        self.assertEqual(self.solution.findMin([5, 6, 7, 8, 9, 1, 2, 3, 4]), 1)

    def test_no_rotation(self):
        self.assertEqual(self.solution.findMin([1, 2, 3, 4, 5, 6, 7]), 1)

    def test_rotation_at_end(self):
        self.assertEqual(self.solution.findMin([2, 3, 4, 5, 6, 7, 1]), 1)

    def test_rotation_at_start(self):
        self.assertEqual(self.solution.findMin([7, 1, 2, 3, 4, 5, 6]), 1)


if __name__ == "__main__":
    unittest.main()
