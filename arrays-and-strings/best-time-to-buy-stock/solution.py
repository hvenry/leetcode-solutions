"""
You are given an array prices where prcies[i] is the price of a given stock on the ith day.

You want to maximuze your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
prices = [7, 1, 5, 3, 6, 4]
output = 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Solution:
- start with a min_price of (cost to buy stock) set to infinity to represent the min price we have seen so far
- keep track of max profit (default at 0)
- iterate over the prices of stock prices, check if current price is better (less than) than our min price
    - if it is, set it to min_price to price
- calculate the profit by subtracting price - min_price (THIS MEANS THAT THE VALUE NOW (PRICE) IS GREATER THAN MIN_PRICE (COST OF STOCK), THEREFORE PROFIT!
- if the profit value is better then our max profit we have calculated so far, TAKE IT!
return max profit

Complexity:
- Time: O(n)
- Space: O(1)
"""

from typing import List

# class Solution:
#     # brute force solution
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 profit = prices[j] - prices[i]

#                 if profit > 0:
#                     max_profit = max(max_profit, profit)

#         return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return int(max_profit)
