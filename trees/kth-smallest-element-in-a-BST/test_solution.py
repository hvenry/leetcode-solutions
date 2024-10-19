import unittest
from solution import TreeNode, Solution


class TestKthSmallestElementInBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        k = 1
        self.assertEqual(self.solution.kthSmallest(root, k), 1)

    def test_example_2(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        k = 3
        self.assertEqual(self.solution.kthSmallest(root, k), 3)

    def test_example_3(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        k = 2
        self.assertEqual(self.solution.kthSmallest(root, k), 2)

    def test_example_4(self):
        root = TreeNode(1)
        k = 1
        self.assertEqual(self.solution.kthSmallest(root, k), 1)

    def test_example_5(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        k = 4
        self.assertEqual(self.solution.kthSmallest(root, k), 4)


if __name__ == "__main__":
    unittest.main()
