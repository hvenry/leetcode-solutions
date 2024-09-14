import unittest
from solution import Solution

class testSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        operations = ["5", "2", "C", "D", "+"]
        ans = 30
        
        res = self.solution.calPoints(operations)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
