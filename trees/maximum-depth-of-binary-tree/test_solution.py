import unittest
from solution import TreeNode, Solution


class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.maxDepth(root), 1)

    def test_two_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_three_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.maxDepth(root), 3)


if __name__ == "__main__":
    unittest.main()
