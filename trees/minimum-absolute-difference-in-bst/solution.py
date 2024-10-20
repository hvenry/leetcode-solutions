"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values
of any two different nodes in the tree.

Example 1:
root = [4, 2, 5, 1, 3]
        4
    2       6
  1   3

output: 1
the minimum difference is 1

Example 2:
root = [1, 0, 48, null, null, 12, 49]

        1
    0       48
          12  49

output: 1

Solution:
- do an in-order traversal (to get ordered list since it is a binary tree)
- keep track of min difference
- compare current - previous values of traversal to the min difference, take the min of either
- return min difference after traversing all nodes
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        prev_val = None

        # helper function to perform in-order traversal
        def inorder(node):
            # refrence the prev_val, min_diff outside the enclosing functions scope
            nonlocal prev_val, min_diff

            # reached end, return
            if not node:
                return

            # traverse left subtree
            inorder(node.left)

            # process current node
            if prev_val is not None:
                min_diff = min(min_diff, node.val - prev_val)

            # update previous node's value to current node's values
            prev_val = node.val

            # Traverse the right subtree
            inorder(node.right)

        # start inorder traversal from the root
        inorder(root)

        return int(min_diff)
