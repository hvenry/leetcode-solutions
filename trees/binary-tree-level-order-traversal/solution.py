"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(ie from left ro right, level by level)

Example 1:
Input:
        3
9               20
            15      7

Output:
[[3], [9, 20], [15, 7]]

Solution:

Traversal:
- Use a queue (BFS), start by queuing the root (if there is one)
- Then we dequeue and explore its neighbors (Dequeue works in O(1) time in python)
- if we store the values as results, then we will have our level-order-traversal

How to turn [3, 9, 20, 15, 7] to [[3], [9, 20], [15, 7]]:
- store level values, we use a for loop to iterate through all nodes in the queue (given a current level)
- we then store the values for a level, and then at the end of the for loop, we append the level list to our answer

Time Complexity:
- O(n)

Space:
- O(n) -> we could be storing all of the nodes in a queue while they are waiting to be processed
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)

        ans = []

        while queue:
            # this is the inner list
            level = []

            # n is the length of the upcomming level
            n = len(queue)

            # this iterates through 1 levels worth of nodes
            for i in range(n):
                # queue popping from the start of the list
                node = queue.popleft()
                level.append(node.val)

                # add our nodes to the queue (if they exist)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                ans.append(level)

        return ans
