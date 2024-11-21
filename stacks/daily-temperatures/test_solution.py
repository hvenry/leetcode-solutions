import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_all_same_temperatures(self):
        temperatures = [70, 70, 70, 70]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_decreasing_temperatures(self):
        temperatures = [80, 79, 78, 77]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_increasing_temperatures(self):
        temperatures = [60, 61, 62, 63]
        expected = [1, 1, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_single_temperature(self):
        temperatures = [50]
        expected = [0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)

    def test_alternating_temperatures(self):
        temperatures = [70, 75, 70, 75, 70, 75]
        expected = [1, 0, 1, 0, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(temperatures), expected)


if __name__ == "__main__":
    unittest.main()
