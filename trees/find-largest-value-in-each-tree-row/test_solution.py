import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(9)
        self.assertEqual(self.solution.largestValues(root), [1, 3, 9])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.largestValues(root), [1])

    def test_all_left_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.largestValues(root), [1, 3])

    def test_empty_tree(self):
        self.assertEqual(self.solution.largestValues(None), [])


if __name__ == "__main__":
    unittest.main()
