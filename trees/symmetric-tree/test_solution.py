import unittest
from solution import TreeNode, Solution


class TestSymmetricTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_symmetric_tree(self):
        # Example 1: Symmetric tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_asymmetric_tree(self):
        # Example 2: Asymmetric tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)
        self.assertFalse(self.solution.isSymmetric(root))

    def test_empty_tree(self):
        # Edge case: Empty tree
        root = None
        self.assertTrue(self.solution.isSymmetric(root))

    def test_single_node_tree(self):
        # Edge case: Single node tree
        root = TreeNode(1)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_two_level_symmetric_tree(self):
        # Two level symmetric tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_two_level_asymmetric_tree(self):
        # Two level asymmetric tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(self.solution.isSymmetric(root))


if __name__ == "__main__":
    unittest.main()
