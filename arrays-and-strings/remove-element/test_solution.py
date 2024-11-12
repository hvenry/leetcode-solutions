import unittest
from solution import Solution


class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_length = 2
        expected_nums = [2, 2]
        result_length = self.solution.removeElement(nums, val)
        self.assertEqual(result_length, expected_length)
        self.assertEqual(sorted(nums[:result_length]), sorted(expected_nums))

    def test_example_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_length = 5
        expected_nums = [0, 1, 3, 0, 4]
        result_length = self.solution.removeElement(nums, val)
        self.assertEqual(result_length, expected_length)
        self.assertEqual(sorted(nums[:result_length]), sorted(expected_nums))

    def test_no_removal(self):
        nums = [1, 2, 3, 4, 5]
        val = 6
        expected_length = 5
        expected_nums = [1, 2, 3, 4, 5]
        result_length = self.solution.removeElement(nums, val)
        self.assertEqual(result_length, expected_length)
        self.assertEqual(sorted(nums[:result_length]), sorted(expected_nums))

    def test_all_elements_removed(self):
        nums = [1, 1, 1, 1]
        val = 1
        expected_length = 0
        expected_nums = []
        result_length = self.solution.removeElement(nums, val)
        self.assertEqual(result_length, expected_length)
        self.assertEqual(nums[:result_length], expected_nums)

    def test_mixed_elements(self):
        nums = [4, 1, 2, 1, 3, 1, 4]
        val = 1
        expected_length = 4
        expected_nums = [4, 2, 3, 4]
        result_length = self.solution.removeElement(nums, val)
        self.assertEqual(result_length, expected_length)
        self.assertEqual(sorted(nums[:result_length]), sorted(expected_nums))


if __name__ == "__main__":
    unittest.main()
