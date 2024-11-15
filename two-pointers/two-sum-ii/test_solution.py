import unittest
from solution import Solution


class TestTwoSumII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_example2(self):
        numbers = [2, 3, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 3])

    def test_example3(self):
        numbers = [-1, 0]
        target = -1
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_example4(self):
        numbers = [1, 2, 3, 4, 4, 9, 56, 90]
        target = 8
        self.assertEqual(self.solution.twoSum(numbers, target), [4, 5])

    def test_example5(self):
        numbers = [5, 25, 75]
        target = 100
        self.assertEqual(self.solution.twoSum(numbers, target), [2, 3])


if __name__ == "__main__":
    unittest.main()
