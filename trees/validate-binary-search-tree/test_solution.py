import unittest
from solution import TreeNode, Solution


class TestValidateBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Example 1: root = [2, 1, 3]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(self.solution.isValidBST(root))

    def test_example_2(self):
        # Example 2: root = [5, 1, 4, None, None, 3, 6]
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(self.solution.isValidBST(root))

    def test_single_node(self):
        # Single node tree
        root = TreeNode(1)
        self.assertTrue(self.solution.isValidBST(root))

    def test_invalid_bst_with_equal_values(self):
        # Invalid BST with equal values: root = [2, 2, 2]
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        self.assertFalse(self.solution.isValidBST(root))

    def test_large_valid_bst(self):
        # Large valid BST
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(18)
        self.assertTrue(self.solution.isValidBST(root))

    def test_large_invalid_bst(self):
        # Large invalid BST
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(8)  # Invalid node
        self.assertFalse(self.solution.isValidBST(root))


if __name__ == "__main__":
    unittest.main()
