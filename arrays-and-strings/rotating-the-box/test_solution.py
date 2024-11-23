import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        box = [["#", ".", "*", "."], ["#", "#", "*", "."]]
        expected = [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]
        self.assertEqual(self.solution.rotateTheBox(box), expected)

    def test_empty_box(self):
        box = [[".", ".", "."], [".", ".", "."]]
        expected = [[".", "."], [".", "."], [".", "."]]
        self.assertEqual(self.solution.rotateTheBox(box), expected)

    def test_all_stones(self):
        box = [["#", "#", "#"], ["#", "#", "#"]]
        expected = [["#", "#"], ["#", "#"], ["#", "#"]]
        self.assertEqual(self.solution.rotateTheBox(box), expected)

    def test_all_obstacles(self):
        box = [["*", "*", "*"], ["*", "*", "*"]]
        expected = [["*", "*"], ["*", "*"], ["*", "*"]]
        self.assertEqual(self.solution.rotateTheBox(box), expected)


if __name__ == "__main__":
    unittest.main()
