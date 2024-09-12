import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        ans = [1,2,3,6,9,8,7,4,5]

        res = self.solution.spiralOrder(matrix)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()