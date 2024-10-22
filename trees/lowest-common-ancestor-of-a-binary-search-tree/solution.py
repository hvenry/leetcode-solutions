"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the deficition of LCA, "The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendents (where we allow a node to be a descendant of itself).

Example 1
root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8

                6
        2               8
    0      4         7     9
          3  5

output: 6

This is because the LCA of nodes 2 and 8 is 6.


Example 2
root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4

                6
        2               8
    0      4         7     9
          3  5

Ouptut: 2


This is because a node can be a descendant of itself.


Understanding:
- the root is the ancestor of EVERYTHING
- how can we find the lowest node that contains both p and q? C
    - check subtrees

How to limit the subtrees we check?
- Since it is a BST, we know that we should be traversing the side of the tree where:
  - LEFT when both p and q values are less then the current node
  - RIGHT when p and q both values are greater than the curent node

- We stop checking once the next nodes split the two values. we return the current node as the LCA.

Case when one node is higher than the other: Return the first node that is found as the LCA.

Time: O(h) -> close to log n if balanced (might not be true)
Space: O(h) -> recursive callstack
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # list so it is a global variable
        lca = root

        def search(root):
            nonlocal lca

            # we have found the best possible LCA
            if not root:
                return

            lca = root

            # case when one node is higher than the other
            if root is p or root is q:
                return
            # search for root
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return

        search(root)
        return lca
