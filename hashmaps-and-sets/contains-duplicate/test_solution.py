import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()
  
  def test(self):
    nums = [1, 2, 3, 1]
    ans = True

    res = self.solution.containsDuplicate(nums)
    self.assertEqual(res, ans)

if __name__ == "__main__":
  unittest.main()
