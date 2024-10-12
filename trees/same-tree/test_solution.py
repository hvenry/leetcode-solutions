import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_same_tree(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_different_structure(self):
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_different_values(self):
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_both_empty(self):
        p = None
        q = None
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_one_empty(self):
        p = TreeNode(1)
        q = None
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_complex_tree(self):
        p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertTrue(self.solution.isSameTree(p, q))


if __name__ == "__main__":
    unittest.main()
