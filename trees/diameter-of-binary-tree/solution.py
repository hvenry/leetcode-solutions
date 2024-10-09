from typing import Optional

"""
Given the root of a binary tree, return the length of the diameter of the 
tree.

The diameter of the tree is the lenght of the longest path between any
two nodes n a tree. The path may or may not pass through the root.

The length of a path between two notes is represented by teh number of
edges between them.


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def maxDepth(root: TreeNode | None) -> int:
            nonlocal res

            if not root:
                return 0

            left = maxDepth(root.left)
            right = maxDepth(root.right)

            res = max(res, left + right)

            return 1 + max(left, right)

        maxDepth(root)
        return res
