import unittest
from solution import MinStack


class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.min_stack = MinStack()

    def test_operations(self):
        self.min_stack.push(-2)
        self.min_stack.push(0)
        self.min_stack.push(-3)
        self.assertEqual(self.min_stack.getMin(), -3)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 0)
        self.assertEqual(self.min_stack.getMin(), -2)

    def test_single_element(self):
        self.min_stack.push(1)
        self.assertEqual(self.min_stack.getMin(), 1)
        self.assertEqual(self.min_stack.top(), 1)
        self.min_stack.pop()
        with self.assertRaises(IndexError):
            self.min_stack.top()

    def test_increasing_elements(self):
        self.min_stack.push(1)
        self.min_stack.push(2)
        self.min_stack.push(3)
        self.assertEqual(self.min_stack.getMin(), 1)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 1)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 1)

    def test_decreasing_elements(self):
        self.min_stack.push(3)
        self.min_stack.push(2)
        self.min_stack.push(1)
        self.assertEqual(self.min_stack.getMin(), 1)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 2)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.getMin(), 3)


if __name__ == "__main__":
    unittest.main()
