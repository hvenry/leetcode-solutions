"""
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith them, then you will recieve a discount equivalent to
prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not recieev any
discount at all.

Return an integer array answer where answer[i] is the final price youwill you pay for the ith item of the shop, considering
the special discount.

Example:
prices = [8, 4, 6, 2, 3]
returns: [4, 2, 4, 2, 3]

- For item 0, with price [0]=8, you will recieve a discount equivalent to prices[1]=4.
- For item 1, with price [1]=4, you will recieve a discount equivalent to prices[3]=2
- For item 2, with price [2]=6, you will recieve a discount equivalent to prices[3]=2
- For items 3, and 4, you do not get a discount.

Solution:
- Use a monotonic stack to maintain a decreasing order of prices to efficiently find the next smaller price for each item.
- Push index of prices into the stack to allow modification of the res list when discount is applied to price

Complexity:
Time: O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[::]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]

            stack.append(i)

        return res
