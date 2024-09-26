import unittest
from solution import TreeNode, Solution


class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.diameterOfBinaryTree(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)

    def test_two_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 1)

    def test_three_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 2)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 4)


if __name__ == "__main__":
    unittest.main()
