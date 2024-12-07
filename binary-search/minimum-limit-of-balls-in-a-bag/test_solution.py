import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [9]
        maxOperations = 2
        self.assertEqual(self.solution.minimumSize(nums, maxOperations), 3)

    def test_example2(self):
        nums = [2, 4, 8, 2]
        maxOperations = 4
        self.assertEqual(self.solution.minimumSize(nums, maxOperations), 2)

    def test_example3(self):
        nums = [7, 17]
        maxOperations = 2
        self.assertEqual(self.solution.minimumSize(nums, maxOperations), 7)

    def test_example4(self):
        nums = [1, 1, 1, 1]
        maxOperations = 0
        self.assertEqual(self.solution.minimumSize(nums, maxOperations), 1)

    def test_example5(self):
        nums = [100]
        maxOperations = 1
        self.assertEqual(self.solution.minimumSize(nums, maxOperations), 50)


if __name__ == "__main__":
    unittest.main()
