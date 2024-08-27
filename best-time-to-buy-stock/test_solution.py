import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test(self):
    prices = [7,1,5,3,6,4]

    res = self.solution.maxProfit(prices)
    self.assertEqual(res, 5)

if __name__ == "__main__":
  unittest.main()