import unittest
from solution import Solution


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fib_0(self):
        self.assertEqual(self.solution.fib(0), 0)

    def test_fib_1(self):
        self.assertEqual(self.solution.fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(self.solution.fib(2), 1)

    def test_fib_3(self):
        self.assertEqual(self.solution.fib(3), 2)

    def test_fib_4(self):
        self.assertEqual(self.solution.fib(4), 3)

    def test_fib_5(self):
        self.assertEqual(self.solution.fib(5), 5)

    def test_fib_10(self):
        self.assertEqual(self.solution.fib(10), 55)

    def test_fib_20(self):
        self.assertEqual(self.solution.fib(20), 6765)

    def test_fib_30(self):
        self.assertEqual(self.solution.fib(30), 832040)


if __name__ == "__main__":
    unittest.main()
