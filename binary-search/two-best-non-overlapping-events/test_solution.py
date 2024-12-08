import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
        self.assertEqual(self.solution.maxTwoEvents(events), 4)

    def test_example2(self):
        events = [[1, 3, 2], [4, 5, 2], [1, 5, 5]]
        self.assertEqual(self.solution.maxTwoEvents(events), 5)

    def test_example3(self):
        events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
        self.assertEqual(self.solution.maxTwoEvents(events), 7)

    def test_single_event(self):
        events = [[1, 2, 5]]
        self.assertEqual(self.solution.maxTwoEvents(events), 5)

    def test_overlapping_events(self):
        events = [[1, 3, 4], [2, 5, 3], [4, 6, 5]]
        self.assertEqual(self.solution.maxTwoEvents(events), 9)

    def test_non_overlapping_events(self):
        events = [[1, 2, 4], [3, 4, 5], [5, 6, 6]]
        self.assertEqual(self.solution.maxTwoEvents(events), 11)


if __name__ == "__main__":
    unittest.main()
