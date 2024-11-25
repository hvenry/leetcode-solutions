import unittest
from solution import Solution


class TestSlidingPuzzle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [[1, 2, 3], [4, 0, 5]]
        self.assertEqual(self.solution.slidingPuzzle(board), 1)

    def test_example2(self):
        board = [[1, 2, 3], [5, 4, 0]]
        self.assertEqual(self.solution.slidingPuzzle(board), -1)

    def test_solved_board(self):
        board = [[1, 2, 3], [4, 5, 0]]
        self.assertEqual(self.solution.slidingPuzzle(board), 0)

    def test_one_move_away(self):
        board = [[1, 2, 3], [4, 0, 5]]
        self.assertEqual(self.solution.slidingPuzzle(board), 1)

    def test_two_moves_away(self):
        board = [[1, 2, 3], [0, 4, 5]]
        self.assertEqual(self.solution.slidingPuzzle(board), 2)


if __name__ == "__main__":
    unittest.main()
