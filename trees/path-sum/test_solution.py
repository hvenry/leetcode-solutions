import unittest
from solution import TreeNode, Solution


class TestPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        targetSum = 22
        self.assertTrue(self.solution.hasPathSum(root, targetSum))

    def test_single_node_true(self):
        root = TreeNode(5)
        targetSum = 5
        self.assertTrue(self.solution.hasPathSum(root, targetSum))

    def test_single_node_false(self):
        root = TreeNode(5)
        targetSum = 10
        self.assertFalse(self.solution.hasPathSum(root, targetSum))

    def test_no_path(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        targetSum = 5
        self.assertFalse(self.solution.hasPathSum(root, targetSum))

    def test_multiple_paths(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        targetSum = 7
        self.assertTrue(self.solution.hasPathSum(root, targetSum))

    def test_empty_tree(self):
        root = None
        targetSum = 0
        self.assertFalse(self.solution.hasPathSum(root, targetSum))


if __name__ == "__main__":
    unittest.main()
