import unittest
from solution import Solution


class TestThreeSumClosest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_example2(self):
        self.assertEqual(self.solution.threeSumClosest([0, 0, 0], 1), 0)

    def test_case1(self):
        self.assertEqual(self.solution.threeSumClosest([1, 1, 1, 1], 3), 3)

    def test_case2(self):
        self.assertEqual(self.solution.threeSumClosest([-1, 0, 1, 1], 1), 1)

    def test_case3(self):
        self.assertEqual(self.solution.threeSumClosest([1, 2, 3, 4], 6), 6)

    def test_case4(self):
        self.assertEqual(self.solution.threeSumClosest([-1, 2, 1, -4, 5, 6], 3), 3)

    def test_case5(self):
        self.assertEqual(self.solution.threeSumClosest([1, 1, -1, -1, 3], -1), -1)


if __name__ == "__main__":
    unittest.main()
