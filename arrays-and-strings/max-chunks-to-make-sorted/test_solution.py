import unittest
from solution import Solution


class TestMaxChunksToSorted(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr = [4, 3, 2, 1, 0]
        self.assertEqual(self.solution.maxChunksToSorted(arr), 1)

    def test_example_2(self):
        arr = [1, 0, 2, 3, 4]
        self.assertEqual(self.solution.maxChunksToSorted(arr), 4)

    def test_single_element(self):
        arr = [0]
        self.assertEqual(self.solution.maxChunksToSorted(arr), 1)

    def test_already_sorted(self):
        arr = [0, 1, 2, 3, 4]
        self.assertEqual(self.solution.maxChunksToSorted(arr), 5)

    def test_reverse_sorted(self):
        arr = [4, 3, 2, 1, 0]
        self.assertEqual(self.solution.maxChunksToSorted(arr), 1)

    def test_mixed(self):
        arr = [2, 0, 1, 3, 4]
        self.assertEqual(self.solution.maxChunksToSorted(arr), 3)

    def test_duplicates(self):
        arr = [1, 1, 0, 0, 2, 2]
        self.assertEqual(self.solution.maxChunksToSorted(arr), 1)


if __name__ == "__main__":
    unittest.main()
