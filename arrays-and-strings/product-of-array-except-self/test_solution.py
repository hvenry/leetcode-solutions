import unittest
from solution import Solution


class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_single_element(self):
        self.assertEqual(self.solution.productExceptSelf([1]), [1])

    def test_two_elements(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2]), [2, 1])

    def test_all_ones(self):
        self.assertEqual(self.solution.productExceptSelf([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_with_zero(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 0, 4]), [0, 0, 8, 0])

    def test_negative_numbers(self):
        self.assertEqual(
            self.solution.productExceptSelf([-1, -2, -3, -4]), [-24, -12, -8, -6]
        )

    def test_mixed_numbers(self):
        self.assertEqual(
            self.solution.productExceptSelf([-1, 2, -3, 4]), [-24, 12, -8, 6]
        )


if __name__ == "__main__":
    unittest.main()
