import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test(self):
    nums = [1, 2, 3, 4]
    answer = [24, 12, 8, 6]

    res = self.solution.productExceptSelf(nums)
    self.assertEqual(res, answer)

if __name__ == "__main__":
  unittest.main()