import unittest
from solution import Solution


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_unique_paths_3x7(self):
        self.assertEqual(self.solution.uniquePaths(3, 7), 28)

    def test_unique_paths_3x2(self):
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)

    def test_unique_paths_7x3(self):
        self.assertEqual(self.solution.uniquePaths(7, 3), 28)

    def test_unique_paths_3x3(self):
        self.assertEqual(self.solution.uniquePaths(3, 3), 6)

    def test_unique_paths_1x1(self):
        self.assertEqual(self.solution.uniquePaths(1, 1), 1)

    def test_unique_paths_1x10(self):
        self.assertEqual(self.solution.uniquePaths(1, 10), 1)

    def test_unique_paths_10x1(self):
        self.assertEqual(self.solution.uniquePaths(10, 1), 1)

    def test_unique_paths_10x10(self):
        self.assertEqual(self.solution.uniquePaths(10, 10), 48620)


if __name__ == "__main__":
    unittest.main()
