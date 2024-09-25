"""
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which
the depth of the two subtrees of every node never differs
by more than one.

solution:
If left and right trees of root node are balanced (heights
that don't differ more than 1), it does not mean they are balanced!

naive approach:
- go through every node in the tree and see if their trees are balanced
- O(n^2) time complexity

optimized approach:
- check if it is from balanced from the bottom up
- visit each node once O(n)


start at leaf node (balanced)
- calculate height and go up
find the max height of each node by taking 1 + max(left height, right height)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def dfs(root):
        #     # base case
        #     if not root:
        #         return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)

        #     # this balanced does not only mean balanced at root
        #     # it checks for all subtrees -> because left or right [0] would evaluate to false
        #     balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        #     return [balanced, 1 + max(left[1], right[1])]

        # # return bool if balanced or naw
        # return dfs(root)[0]

        # def height_and_balance(root):
        #     if not root:
        #         return 0, True

        #     left_height, left_balanced = height_and_balance(root.left)

        #     if not left_balanced:
        #         return 0, False

        #     right_height, right_balanced = height_and_balance(root.right)

        #     if not right_balanced:
        #         return 0, False

        #     balanced = abs(left_height - right_height) <= 1
        #     height = 1 + max(left_height, right_height)

        #     return height, balanced

        # _, is_balanced = height_and_balance(root)

        # return is_balanced

        # i personally really like this solution:
        def check(Node):
            if Node is None:
                return 0

            lh = check(Node.left)
            rh = check(Node.right)

            if lh == -1 or rh == -1:
                return -1

            if abs(lh - rh) > 1:
                return -1

            # return the height (max height of subtrees)
            return max(lh, rh) + 1

        if check(root) == -1:
            return False

        return True
