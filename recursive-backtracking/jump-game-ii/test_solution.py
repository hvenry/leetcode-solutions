import unittest
from solution import Solution


class TestJumpGameII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 3, 1, 1, 4]
        self.assertEqual(self.solution.jump(nums), 2)

    def test_single_element(self):
        nums = [0]
        self.assertEqual(self.solution.jump(nums), 0)

    def test_two_elements(self):
        nums = [1, 2]
        self.assertEqual(self.solution.jump(nums), 1)

    def test_no_jump_needed(self):
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(self.solution.jump(nums), 4)

    def test_multiple_paths(self):
        nums = [2, 3, 0, 1, 4]
        self.assertEqual(self.solution.jump(nums), 2)


if __name__ == "__main__":
    unittest.main()
