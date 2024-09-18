import unittest
from solution import Solution


class TestSearchInsertPosition(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_found(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)

    def test_target_not_found_insert_position(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(self.solution.searchInsert([1], 0), 0)
        self.assertEqual(self.solution.searchInsert([1], 2), 1)

    def test_empty_array(self):
        self.assertEqual(self.solution.searchInsert([], 1), 0)

    def test_large_numbers(self):
        self.assertEqual(self.solution.searchInsert([10, 20, 30, 40, 50], 35), 3)
        self.assertEqual(self.solution.searchInsert([10, 20, 30, 40, 50], 10), 0)
        self.assertEqual(self.solution.searchInsert([10, 20, 30, 40, 50], 55), 5)


if __name__ == "__main__":
    unittest.main()
