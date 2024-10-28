import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combine_n4_k2(self):
        n, k = 4, 2
        expected_output = [[2, 1], [3, 1], [3, 2], [4, 1], [4, 2], [4, 3]]
        result = self.solution.combine(n, k)
        self.assertEqual(sorted(result), sorted(expected_output))

    def test_combine_n5_k3(self):
        n, k = 5, 3
        expected_output = [
            [3, 2, 1],
            [4, 2, 1],
            [4, 3, 1],
            [4, 3, 2],
            [5, 2, 1],
            [5, 3, 1],
            [5, 3, 2],
            [5, 4, 1],
            [5, 4, 2],
            [5, 4, 3],
        ]
        result = self.solution.combine(n, k)
        self.assertEqual(sorted(result), sorted(expected_output))

    def test_combine_n3_k1(self):
        n, k = 3, 1
        expected_output = [[1], [2], [3]]
        result = self.solution.combine(n, k)
        self.assertEqual(sorted(result), sorted(expected_output))

    def test_combine_n1_k1(self):
        n, k = 1, 1
        expected_output = [[1]]
        result = self.solution.combine(n, k)
        self.assertEqual(result, expected_output)

    def test_combine_n4_k4(self):
        n, k = 4, 4
        expected_output = [[4, 3, 2, 1]]
        result = self.solution.combine(n, k)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
