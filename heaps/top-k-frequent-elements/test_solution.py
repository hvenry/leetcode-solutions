import unittest
from solution import Solution


class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, [1, 2])

    def test_example2(self):
        nums = [1]
        k = 1
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, [1])

    def test_all_same(self):
        nums = [1, 1, 1, 1, 1]
        k = 1
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, [1])

    def test_large_k(self):
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        k = 5
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, [1, 2, 3, 4, 5])

    def test_zero_k(self):
        nums = [1, 1, 2, 2, 3, 3]
        k = 0
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, [])


if __name__ == "__main__":
    unittest.main()
