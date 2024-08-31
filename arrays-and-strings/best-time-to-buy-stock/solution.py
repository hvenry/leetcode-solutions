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
    # time O(n)
    # space O(1)
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
