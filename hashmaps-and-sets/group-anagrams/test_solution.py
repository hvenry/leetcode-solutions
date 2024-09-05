import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        ans = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

        res = self.solution.groupAnagrams(strs)
        res = [sorted(x) for x in res]
        ans = [sorted(x) for x in ans]
        self.assertListEqual(sorted(res), sorted(ans))


if __name__ == "__main__":
    unittest.main()
