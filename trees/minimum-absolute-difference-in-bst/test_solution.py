import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Tree: [4, 2, 6, 1, 3]
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(self.solution.getMinimumDifference(root), 1)

    def test_example2(self):
        # Tree: [1, 0, 48, None, None, 12, 49]
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(48)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(49)
        self.assertEqual(self.solution.getMinimumDifference(root), 1)

    def test_two_nodes(self):
        # Tree: [1, None, 3]
        root = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.getMinimumDifference(root), 2)

    def test_large_tree(self):
        # Tree: [10, 5, 15, 3, 7, None, 18]
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.right = TreeNode(18)
        self.assertEqual(self.solution.getMinimumDifference(root), 2)


if __name__ == "__main__":
    unittest.main()
