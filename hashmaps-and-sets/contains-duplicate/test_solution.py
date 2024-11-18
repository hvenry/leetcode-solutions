import unittest
from solution import Solution


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))

    def test_example2(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(self.solution.containsDuplicate([]))

    def test_single_element(self):
        self.assertFalse(self.solution.containsDuplicate([1]))

    def test_all_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([2, 2, 2, 2]))

    def test_large_input(self):
        self.assertTrue(self.solution.containsDuplicate(list(range(10000)) + [9999]))

    def test_no_duplicates(self):
        self.assertFalse(self.solution.containsDuplicate(list(range(10000))))


if __name__ == "__main__":
    unittest.main()
