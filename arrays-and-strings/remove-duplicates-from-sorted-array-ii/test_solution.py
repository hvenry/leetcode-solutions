import unittest
from solution import Solution


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 1, 2, 2, 3])

    def test_example_2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 7)
        self.assertEqual(nums[:k], [0, 0, 1, 1, 2, 3, 3])

    def test_example_3(self):
        nums = [1, 1, 1, 1, 1, 1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 1])

    def test_example_4(self):
        nums = [1, 2, 3, 4, 5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
