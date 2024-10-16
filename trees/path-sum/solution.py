"""
Given the root of a binary tree and an integer targetSum, return
true if the tree has a root-to-leaf path such that adding up all
the vaues along the path equals targetSum

example:
root = [5, 4, 6, 11, null, 13, 4, 7, 2, null, null, null, 1]
targetSum = 22

                    5
            4               8
        11              13      4
    7       2                       1

Target sum = 22:
Returns true

The path 5-4-11-2 equals 22.

Solution:
- Use DFS and current sum
- traverse down tree to the first leaf node, keep track of the curernt sum adding value from each leaf
- if we reach the leaf node, and the sum is the same as target, we return true
- if not, we continue the DFS, subtracking the value of the node we are leaving, adding values to new nodes
  we come across, and then check at the next leaf node if current sum is equal to target, return true if yes, keep
  doing the dfs if not.

- if we traverse the whole tree with dfs, and current sum never equaled the target value, we return false

Time complexity:
O(n)
Space: O(h) -> recursive callstack of height of tree
"""

from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # helper function
        def has_sum(root, cur_sum):
            # we went too far
            if not root:
                return False

            # keep track of cur_sum
            cur_sum += root.val

            # leaf node definition, check if cur_sum equals targetSum
            if not root.left and not root.right:
                # if they do, return true
                return cur_sum == targetSum

            # see if we can find path on left or right side
            return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)

        return has_sum(root, 0)
