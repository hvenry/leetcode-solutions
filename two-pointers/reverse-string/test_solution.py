import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test(self):
        s = ["h", "e", "l", "l", "o"]
        ans = ["o", "l", "l", "e", "h"]

        self.solution.reverseString(s)
        self.assertEqual(s, ans)


if __name__ == "__main__":
    unittest.main()

