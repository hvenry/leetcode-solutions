import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)

        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_example2(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)

        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)

        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_root_is_none(self):
        root = None
        subRoot = TreeNode(1)

        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_subtree_at_leaf(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        subRoot = TreeNode(4)

        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_subtree_not_present(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        subRoot = TreeNode(5)

        self.assertFalse(self.solution.isSubtree(root, subRoot))


if __name__ == "__main__":
    unittest.main()
