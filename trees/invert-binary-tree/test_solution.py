import unittest
from solution import TreeNode, Solution


class TestInvertBinaryTree(unittest.TestCase):
    def tree_to_list(self, root):
        """Helper function to convert tree to list (level-order)"""
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result

    def list_to_tree(self, lst):
        """Helper function to convert list (level-order) to tree"""
        if not lst:
            return None
        root = TreeNode(lst[0])
        queue = [root]
        i = 1
        while queue and i < len(lst):
            node = queue.pop(0)
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1
        return root

    def test_invert_tree(self):
        sol = Solution()

        # Test case 1: Empty tree
        self.assertIsNone(sol.invertTree(None))

        # Test case 2: Single node tree
        root = TreeNode(1)
        inverted = sol.invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [1])

        # Test case 3: Tree with two nodes
        root = self.list_to_tree([1, 2])
        inverted = sol.invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [1, None, 2])

        # Test case 4: Tree with three nodes
        root = self.list_to_tree([1, 2, 3])
        inverted = sol.invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [1, 3, 2])

        # Test case 5: Larger tree
        root = self.list_to_tree([4, 2, 7, 1, 3, 6, 9])
        inverted = sol.invertTree(root)
        self.assertEqual(self.tree_to_list(inverted), [4, 7, 2, 9, 6, 3, 1])


if __name__ == "__main__":
    unittest.main()
