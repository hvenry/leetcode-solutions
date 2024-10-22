import unittest
from solution import TreeNode, Solution


class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        # Create the tree for the tests
        self.root = TreeNode(6)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(8)
        self.root.left.left = TreeNode(0)
        self.root.left.right = TreeNode(4)
        self.root.right.left = TreeNode(7)
        self.root.right.right = TreeNode(9)
        self.root.left.right.left = TreeNode(3)
        self.root.left.right.right = TreeNode(5)
        self.solution = Solution()

    def test_lca_case1(self):
        p = self.root.left  # Node with value 2
        q = self.root.right  # Node with value 8
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 6)

    def test_lca_case2(self):
        p = self.root.left  # Node with value 2
        q = self.root.left.right  # Node with value 4
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 2)

    def test_lca_case3(self):
        p = self.root.left.left  # Node with value 0
        q = self.root.left.right.right  # Node with value 5
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 2)

    def test_lca_case4(self):
        p = self.root.right.left  # Node with value 7
        q = self.root.right.right  # Node with value 9
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 8)

    def test_lca_case5(self):
        p = self.root.left.right.left  # Node with value 3
        q = self.root.left.right.right  # Node with value 5
        lca = self.solution.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(lca.val, 4)


if __name__ == "__main__":
    unittest.main()
