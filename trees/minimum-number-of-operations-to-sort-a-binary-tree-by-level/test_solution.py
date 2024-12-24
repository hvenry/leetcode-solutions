import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        root = TreeNode(1)
        root.left = TreeNode(4)
        root.right = TreeNode(3)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(6)
        root.right.left = TreeNode(8)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(9)
        root.right.right.right = TreeNode(10)
        self.assertEqual(self.solution.minimumOperations(root), 3)

    def test_already_sorted(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.minimumOperations(root), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.minimumOperations(root), 0)

    def test_two_levels(self):
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.right = TreeNode(1)
        self.assertEqual(self.solution.minimumOperations(root), 1)


if __name__ == "__main__":
    unittest.main()
