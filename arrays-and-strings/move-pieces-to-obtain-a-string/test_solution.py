import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        start = "_L__R__R_"
        target = "L______RR"
        self.assertTrue(self.solution.canChange(start, target))

    def test_example2(self):
        start = "R_L_"
        target = "__RL"
        self.assertFalse(self.solution.canChange(start, target))

    def test_example3(self):
        start = "_R_"
        target = "__R"
        self.assertTrue(self.solution.canChange(start, target))

    def test_example4(self):
        start = "L__"
        target = "__L"
        self.assertFalse(self.solution.canChange(start, target))

    def test_example5(self):
        start = "R__L"
        target = "__RL"
        self.assertTrue(self.solution.canChange(start, target))

    def test_example6(self):
        start = "L_R_"
        target = "_L_R"
        self.assertFalse(self.solution.canChange(start, target))

    def test_example7(self):
        start = "L_R"
        target = "R_L"
        self.assertFalse(self.solution.canChange(start, target))


if __name__ == "__main__":
    unittest.main()
