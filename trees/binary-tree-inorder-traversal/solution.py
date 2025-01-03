"""
Inorder Traversal:

Tree:
    10
20      30
      40  50


Understanding of recursive callstack for inorder traversal:

inorder(10)
- inorder(20) <- 10.left
    - inorder(None) <- 20.left
    - append(20) <- 20.val
    - inorder(None) <- 20.right
- append(10) <- 10.val
    - inorder(30) 10.right
        - inorder(40) <- 30.left
            - inorder(None) <- 40.left
            - append(30) <- 30.val
            - inorder(None) <- 40.right
        - append(40) <- 40.val
        - inorder(50) <- 30.left
            - inorder(None) <- 50.left
            - append(50) <- 50.val
            - inorder(None) <- 50.right
"""

from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    # iterative approach to this solution
    # we can simulate the recursive callstack with a stack
    def itarativeInorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        # start with current being the root
        while cur or stack:
            # traverse left as far as possible
            while cur:
                stack.append(cur)
                cur = cur.left
            # once we are as far left, pop the top value of the stack
            cur = stack.pop()
            # add the value of this node
            res.append(cur.val)
            # go to the right node
            cur = cur.right

        return res
