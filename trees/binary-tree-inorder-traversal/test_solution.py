import unittest
from solution import TreeNode, Solution


class TestInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.inorderTraversal(None), [])

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.inorderTraversal(root), [1])

    def test_tree_with_only_left_children(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.solution.inorderTraversal(root), [3, 2, 1])

    def test_tree_with_only_right_children(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.solution.inorderTraversal(root), [1, 2, 3])

    def test_full_tree(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(self.solution.inorderTraversal(root), [2, 1, 3])

    def test_complex_tree(self):
        root = TreeNode(10, TreeNode(20), TreeNode(30, TreeNode(40), TreeNode(50)))
        self.assertEqual(self.solution.inorderTraversal(root), [20, 10, 40, 30, 50])


if __name__ == "__main__":
    unittest.main()
