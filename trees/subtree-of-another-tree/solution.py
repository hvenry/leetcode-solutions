"""
Given the roots of two binary trees `root` and `subRoot`, return true
if there is a subtree of root with the same structure and node values
of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists ofa node in trees
and all of this node's descendants. The tree `tree` could also be
considered as subtree of itself.

Example 1:
root:
            3
    4               5
1       2

subRoot:
    4
1       2

returns True

Example 2:
root:
            3
    4               5
1       2

      0

subRoot:
        4
1               2

returns False


Solution:

"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            # these are the same
            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return same_tree(p.left, q.left) and same_tree(p.right, q.right)

        # scan through all the nodes in root, and see if we can find the same tree in subRoot
        # DFS Function (has subtree)

        def has_subtree(root):
            # we scanned all the way to the bottom
            if not root:
                return False

            # check if our root is the same as subroot
            if same_tree(root, subRoot):
                return True

            # check next node
            return has_subtree(root.left) or has_subtree(root.right)

        return has_subtree(root)
