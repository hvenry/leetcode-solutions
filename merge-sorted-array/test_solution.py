import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_case1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        self.solution.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_merge_case2(self):
        nums1 = [1]
        nums2 = []
        self.solution.merge(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

if __name__ == "__main__":
    unittest.main()
