import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.levelOrder(root), [[1]])

    def test_empty_tree(self):
        self.assertEqual(self.solution.levelOrder(None), [])

    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.levelOrder(root), [[1], [2], [3], [4]])

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.solution.levelOrder(root), [[1], [2], [3], [4]])


if __name__ == "__main__":
    unittest.main()
