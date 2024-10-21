"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
    2
1       3

root = [2, 1, 3]
returns True

Example 2:
    5
1       4
      3   6

root = [5, 1, 4, null, null, 3, 6]
returns False

Solution:
- if we traverse left, we need to make sure all nodes to the left are less than the current node
- if we traverse right, we need to make sure all nodes to the right are greater than the current node
- if this is true, then it is a valid bst
- we can verify this by adjusting the max and min values while we traverse left and right subtrees of root
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, min_val, max_val):
            # base case
            if not node:
                return True

            # violation of BST
            if node.val <= min_val or node.val >= max_val:
                return False

            # set new max and min
            # we set the new min_val to the value of the current node to validate upcomming left nodes
            # we set the new max_val to the value of the current node to validate upcomming right nodes
            return isValid(node.left, min_val, node.val) and isValid(
                node.right, node.val, max_val
            )

        return isValid(root, float("-inf"), float("inf"))
