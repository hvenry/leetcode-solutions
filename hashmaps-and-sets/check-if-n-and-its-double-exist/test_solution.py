import unittest
from solution import Solution


class TestCheckIfExist(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        arr = [10, 2, 5, 3]
        self.assertTrue(self.solution.checkIfExist(arr))

    def test_example2(self):
        arr = [3, 1, 7, 11]
        self.assertFalse(self.solution.checkIfExist(arr))

    def test_empty_array(self):
        arr = []
        self.assertFalse(self.solution.checkIfExist(arr))

    def test_single_element(self):
        arr = [1]
        self.assertFalse(self.solution.checkIfExist(arr))

    def test_no_double_exists(self):
        arr = [1, 3, 5, 7]
        self.assertFalse(self.solution.checkIfExist(arr))

    def test_double_exists(self):
        arr = [1, 3, 6, 12]
        self.assertTrue(self.solution.checkIfExist(arr))

    def test_mixed_numbers(self):
        arr = [7, 1, 14, 11]
        self.assertTrue(self.solution.checkIfExist(arr))


if __name__ == "__main__":
    unittest.main()
