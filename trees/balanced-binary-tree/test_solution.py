import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_balanced_tree(self):
        # Balanced tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertTrue(self.solution.isBalanced(root))

    def test_unbalanced_tree(self):
        # Unbalanced tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertFalse(self.solution.isBalanced(root))

    def test_empty_tree(self):
        # Empty tree
        root = None
        self.assertTrue(self.solution.isBalanced(root))

    def test_single_node_tree(self):
        # Single node tree
        root = TreeNode(1)
        self.assertTrue(self.solution.isBalanced(root))

    def test_balanced_tree_with_subtree_unbalanced(self):
        # Balanced tree with an unbalanced subtree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.left.left = TreeNode(6)
        self.assertFalse(self.solution.isBalanced(root))


if __name__ == "__main__":
    unittest.main()
