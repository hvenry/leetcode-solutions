"""
given the root of a binary tree, return its maximum depth

a binary tree's max depth is the number of nodes along the longes
path from the root node down to the farthest leaf node.

solution:
recursively calculate the height of the left and the right
subtrees of a node and assign height to the node as max of the
heights of the two children + 1.

example:
consider the following binary tree:
    1
   / \
  2   3
 /
4

- For node 4, both left and right children are None, so left_depth and right_depth are 0. The depth of node 4 is 1 + max(0, 0) = 1.
- For node 2, the left child has depth 1 (node 4), and the right child is None with depth 0. The depth of node 2 is 1 + max(1, 0) = 2.
- For node 3, both children are None, so its depth is 1 + max(0, 0) = 1.
- For the root node 1, the left child has depth 2 (node 2), and the right child has depth 1 (node 3). The depth of the root node is 1 + max(2, 1) = 3.

Therefore, the +1 ensures that each node's depth includes itself in the count.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0

        # recursively check left and right
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
