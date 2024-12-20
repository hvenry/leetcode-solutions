import unittest
from collections import deque
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def tree_to_list(self, root):
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    def list_to_tree(self, lst):
        if not lst:
            return None
        root = TreeNode(lst[0])
        q = deque([root])
        i = 1
        while q and i < len(lst):
            node = q.popleft()
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                q.append(node.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                q.append(node.right)
            i += 1
        return root

    def test_reverse_odd_levels(self):
        sol = Solution()

        # Test case 1
        root = self.list_to_tree([7, 13, 11])
        expected = [7, 11, 13]
        self.assertEqual(self.tree_to_list(sol.reverseOddLevels(root)), expected)

        # Test case 2
        root = self.list_to_tree([1, 2, 3, 4, 5, 6, 7])
        expected = [1, 3, 2, 4, 5, 6, 7]
        self.assertEqual(self.tree_to_list(sol.reverseOddLevels(root)), expected)

        # Test case 3
        root = self.list_to_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        expected = [1, 3, 2, 4, 5, 6, 7, 15, 14, 13, 12, 11, 10, 9, 8]
        self.assertEqual(self.tree_to_list(sol.reverseOddLevels(root)), expected)

        # Test case 4
        root = self.list_to_tree([1])
        expected = [1]
        self.assertEqual(self.tree_to_list(sol.reverseOddLevels(root)), expected)

        # Test case 5
        root = self.list_to_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = [1, 3, 2, 4, 5, 6, 7, 9, 8]
        self.assertEqual(self.tree_to_list(sol.reverseOddLevels(root)), expected)


if __name__ == "__main__":
    unittest.main()
