import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.averageOfLevels(root), [3.0, 14.5, 11.0])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.averageOfLevels(root), [1.0])

    def test_two_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.averageOfLevels(root), [1.0, 2.5])

    def test_three_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(self.solution.averageOfLevels(root), [1.0, 2.5, 5.0])

    def test_null_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = None
        root.left.right = TreeNode(4)
        root.right.left = None
        root.right.right = TreeNode(5)
        self.assertEqual(self.solution.averageOfLevels(root), [1.0, 2.5, 4.5])


if __name__ == "__main__":
    unittest.main()
