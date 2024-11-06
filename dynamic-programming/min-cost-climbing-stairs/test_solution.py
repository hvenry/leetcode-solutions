import unittest
from solution import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        cost = [10, 15, 20]
        self.assertEqual(self.solution.minCostClimbingStairs(cost), 15)

    def test_single_step(self):
        cost = [10]
        self.assertEqual(self.solution.minCostClimbingStairs(cost), 0)

    def test_two_steps(self):
        cost = [10, 15]
        self.assertEqual(self.solution.minCostClimbingStairs(cost), 10)

    def test_multiple_steps(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.assertEqual(self.solution.minCostClimbingStairs(cost), 6)

    def test_all_equal_steps(self):
        cost = [5, 5, 5, 5, 5, 5]
        self.assertEqual(self.solution.minCostClimbingStairs(cost), 15)

    def test_increasing_costs(self):
        cost = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.solution.minCostClimbingStairs(cost), 9)


if __name__ == "__main__":
    unittest.main()
