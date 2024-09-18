import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_exists(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 5), 4)

    def test_target_does_not_exist(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 0), -1)

    def test_empty_array(self):
        self.assertEqual(self.solution.search([], 1), -1)

    def test_single_element_array(self):
        self.assertEqual(self.solution.search([1], 1), 0)
        self.assertEqual(self.solution.search([1], 2), -1)

    def test_large_numbers(self):
        self.assertEqual(self.solution.search([10**5, 10**6, 10**7], 10**6), 1)
        self.assertEqual(self.solution.search([10**5, 10**6, 10**7], 10**8), -1)


if __name__ == "__main__":
    unittest.main()
