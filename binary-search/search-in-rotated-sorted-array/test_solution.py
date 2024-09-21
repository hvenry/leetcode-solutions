import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4
        self.assertEqual(self.solution.search(nums, target), expected)

    def test_target_not_in_array(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1
        self.assertEqual(self.solution.search(nums, target), expected)

    def test_single_element_found(self):
        nums = [1]
        target = 1
        expected = 0
        self.assertEqual(self.solution.search(nums, target), expected)

    def test_single_element_not_found(self):
        nums = [1]
        target = 0
        expected = -1
        self.assertEqual(self.solution.search(nums, target), expected)

    def test_no_rotation(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        target = 5
        expected = 4
        self.assertEqual(self.solution.search(nums, target), expected)

    def test_large_rotation(self):
        nums = [6, 7, 1, 2, 3, 4, 5]
        target = 3
        expected = 4
        self.assertEqual(self.solution.search(nums, target), expected)

    def test_target_at_start(self):
        nums = [6, 7, 1, 2, 3, 4, 5]
        target = 6
        expected = 0
        self.assertEqual(self.solution.search(nums, target), expected)

    def test_target_at_end(self):
        nums = [6, 7, 1, 2, 3, 4, 5]
        target = 5
        expected = 6
        self.assertEqual(self.solution.search(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
