"""
You are given the root of a binary tree with unique values.

In one operation, you can chose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.

Example:
root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]

        1
    4       3
  7   6   8   5
          9   10

returns: 3
- Swap 4 and 3 in level 2, now it is [3, 4]
- Swap 7 and 5 in level 3, now it is [5, 6, 8, 7]
- Swap 8 and 7 in level 3, now it is [5, 6, 7, 8]
    - Since 3 operations were used, we return 3.

Solution:
- Use a bfs to process each level
- For each level we need to count the amount of operations it takes to sort
    - We do this by comparing the level to a sorted version of it
    - We can use an index map to locate the value that we are swapping for a better time complexity.
- We then increment the result by the amount of operations per level and return it.

Complexity:
- Time: O(n log n) -> sorting swaps
- Space: O(n) -> BFS queue
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count_operations(nums):
            operations = 0
            sorted_nums = sorted(nums)
            # hashmap for indicies
            index_map = {num: index for index, num in enumerate(nums)}

            for i in range(len(nums)):
                if nums[i] != sorted_nums[i]:
                    operations += 1
                    # swap using index map
                    j = index_map[sorted_nums[i]]
                    nums[i], nums[j] = nums[j], nums[i]
                    index_map[nums[i]] = i
                    index_map[nums[j]] = j

            return operations

        q = deque([root])
        res = 0

        # bfs
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res += count_operations(level)
        return res
