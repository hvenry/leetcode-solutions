import unittest
from solution import Solution


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_character_strings(self):
        strs = ["a", "b", "c"]
        expected = [["a"], ["b"], ["c"]]
        result = self.solution.groupAnagrams(strs)
        self.assertCountEqual(result, expected)

    def test_multiple_anagrams(self):
        strs = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
        expected = [["abc", "bca", "cab"], ["xyz", "zyx", "yxz"]]
        result = self.solution.groupAnagrams(strs)
        self.assertCountEqual(result, expected)

    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        result = self.solution.groupAnagrams(strs)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
