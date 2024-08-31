import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = "anagram"
        t = "nagaram"
        ans = True

        res = self.solution.isAnagram(s, t)
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
