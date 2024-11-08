import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [2, 3, 1, 1, 4]
        self.assertTrue(self.solution.canJump(nums))

    def test_example2(self):
        nums = [3, 2, 1, 0, 4]
        self.assertFalse(self.solution.canJump(nums))

    def test_single_element(self):
        nums = [0]
        self.assertTrue(self.solution.canJump(nums))

    def test_two_elements_reachable(self):
        nums = [1, 0]
        self.assertTrue(self.solution.canJump(nums))

    def test_two_elements_unreachable(self):
        nums = [0, 1]
        self.assertFalse(self.solution.canJump(nums))

    def test_large_jump(self):
        nums = [10, 1, 1, 1, 1]
        self.assertTrue(self.solution.canJump(nums))

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        self.assertFalse(self.solution.canJump(nums))

    def test_alternating_zeros(self):
        nums = [1, 0, 1, 0, 1]
        self.assertFalse(self.solution.canJump(nums))

    def test_max_jump_each_step(self):
        nums = [1, 1, 1, 1, 1]
        self.assertTrue(self.solution.canJump(nums))


if __name__ == "__main__":
    unittest.main()
