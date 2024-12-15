import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        classes = [[1, 2], [3, 5], [2, 2]]
        extraStudents = 2
        result = self.solution.maxAverageRatio(classes, extraStudents)
        print(result)
        self.assertAlmostEqual(result, 0.78333, places=5)

    def test_all_pass(self):
        classes = [[5, 5], [3, 3], [2, 2]]
        extraStudents = 3
        result = self.solution.maxAverageRatio(classes, extraStudents)
        self.assertAlmostEqual(result, 1.0, places=5)


if __name__ == "__main__":
    unittest.main()
