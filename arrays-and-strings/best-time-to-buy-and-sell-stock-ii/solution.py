"""
You are given an integer prices where prices[i] is the price ofa given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can acheive.

Example 1:
prices = [7, 1, 5, 3, 6, 4]
output: 7

by on day 2 ($1), sell on day 3 ($5) profit = $4
by on day 4 ($3), sell on day 5 ($6) profit = $3

Total profit is 4 + 3 = 7

Solution:
- keep track of low and high values (initialized at first value of array), and keep track of a total profit
- iterate through the until value goes up, when you are at the point before it goes up YOU ARE AT A LOW POINT (buy)
    - set lo to this point
- iterate now until the value stops going up, then YOU ARE AT A HIGH POINT (sell)
- add the value of high (buy) - low (sell) to max profit
- return max profit

Complexity:
- O(n)
- O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        buy = prices[0]
        sell = prices[0]
        profit = 0
        n = len(prices)

        while i < n - 1:
            # find buy, ignore until it starts going up
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1

            buy = prices[i]

            # find sell, ignore until it starts going down
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1

            sell = prices[i]
            profit += sell - buy

        return profit
