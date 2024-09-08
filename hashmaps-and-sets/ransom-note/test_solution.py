import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        ransomNote = "aa"
        magazine = "aab"

        ans = True

        res = self.solution.canConstruct(ransomNote, magazine)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
