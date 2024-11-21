import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        m = 4
        n = 6
        guards = [[0, 0], [1, 1], [2, 3]]
        walls = [[0, 1], [2, 2], [1, 4]]
        self.assertEqual(self.solution.countUnguarded(m, n, guards, walls), 7)

    def test_no_guards_or_walls(self):
        m = 3
        n = 3
        guards = []
        walls = []
        self.assertEqual(self.solution.countUnguarded(m, n, guards, walls), 9)

    def test_all_guards(self):
        m = 2
        n = 2
        guards = [[0, 0], [0, 1], [1, 0], [1, 1]]
        walls = []
        self.assertEqual(self.solution.countUnguarded(m, n, guards, walls), 0)

    def test_all_walls(self):
        m = 2
        n = 2
        guards = []
        walls = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.assertEqual(self.solution.countUnguarded(m, n, guards, walls), 0)


if __name__ == "__main__":
    unittest.main()
