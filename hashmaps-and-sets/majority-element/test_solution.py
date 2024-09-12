import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        res = 2
        ans = self.solution.majorityElement(nums)
        self.assertEqual(ans, res)

if __name__ == "__main__":
    unittest.main()