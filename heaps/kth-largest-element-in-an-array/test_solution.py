import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(self.solution.findKthLargest(nums, k), 5)

    def test_example2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(self.solution.findKthLargest(nums, k), 4)

    def test_single_element(self):
        nums = [1]
        k = 1
        self.assertEqual(self.solution.findKthLargest(nums, k), 1)

    def test_all_same_elements(self):
        nums = [2, 2, 2, 2, 2]
        k = 3
        self.assertEqual(self.solution.findKthLargest(nums, k), 2)

    def test_large_k(self):
        nums = [7, 10, 4, 3, 20, 15]
        k = 6
        self.assertEqual(self.solution.findKthLargest(nums, k), 3)


if __name__ == "__main__":
    unittest.main()
