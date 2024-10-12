"""
Given the roots of two binary trees, p and q, write a function to check if they are the same or not.

Two binary binary trees are considered the same if they are structurally identical, and the nodes have
the same value.

example:
p = [1, 2, 3]
q = [1, 2, 3]
output: true

example 2:
p = [1, 2]
q = [1, null, 2]
output: false
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def balanced(p, q):
            # if nothing, they match
            if not p and not q:
                return True
            # check if one exists and the other does not
            if (p and not q) or (q and not p):
                return False
            # If they both exist, see if the values are the same
            if p.val != q.val:
                return False

            # see if left side is balanced, see if right side is balanced
            return balanced(p.left, q.left) and balanced(p.right, q.right)

        # return True or False based on if recursive balanced exits with True or False
        return balanced(p, q)
