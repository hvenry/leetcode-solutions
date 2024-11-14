import unittest
from solution import Solution


class TestSortColors(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [2, 0, 2, 1, 1, 0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_example2(self):
        nums = [2, 0, 1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_all_same_color(self):
        nums = [0, 0, 0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 0, 0])

        nums = [1, 1, 1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [1, 1, 1])

        nums = [2, 2, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [2, 2, 2])

    def test_already_sorted(self):
        nums = [0, 1, 2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_reverse_sorted(self):
        nums = [2, 1, 0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_empty(self):
        nums = []
        self.solution.sortColors(nums)
        self.assertEqual(nums, [])

    def test_single_element(self):
        nums = [0]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [0])

        nums = [1]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [1])

        nums = [2]
        self.solution.sortColors(nums)
        self.assertEqual(nums, [2])


if __name__ == "__main__":
    unittest.main()
