import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word))

    def test_example2(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))

    def test_example3(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))

    def test_single_letter_true(self):
        board = [["A"]]
        word = "A"
        self.assertTrue(self.solution.exist(board, word))

    def test_single_letter_false(self):
        board = [["A"]]
        word = "B"
        self.assertFalse(self.solution.exist(board, word))

    def test_large_board(self):
        board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
        word = "ABCESEEEFS"
        self.assertTrue(self.solution.exist(board, word))

    def test_no_match(self):
        board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
        word = "XYZ"
        self.assertFalse(self.solution.exist(board, word))


if __name__ == "__main__":
    unittest.main()
