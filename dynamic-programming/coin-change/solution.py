"""
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be
made up by any combination of coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
coins = [1, 2, 5] amount = 11
Output: 3

This is because 11 = 5 + 5 + 1, which is a total of 3 coins.



First glance approach: Use Greedy Algorithm.
This is a good approach, but does not cover some of the edge cases.

Why we can't use the Greedy Approach:
Example:
coins = [1, 4, 5], amount = 12

in this scenario, greedy would return 5 + 5 + 1 + 1, or a total of 4 coins. This does not work, the best solution is 3 coins (4 + 4 + 4).



Dynamic Programming Solution:
- Make an array of lenght amount + 1 (ie 12 + 1)

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

The idea here is to build up this array from the bottom up.
- Each index should store the least amount of coins it takes to make that amount
- our base case at 0 is it takes 0 coins to get the value 0.

RECURRENCE RELATION:
For each position, we will start by using the smallest coin to see if we can make the amount, then use the previous values in the array
(which are the minimum values that it takes to get to the value at a given index) to find the amount of coins it take.

After finding this, we will try the next largest coin in the list, and follow the same above steps just now with a larger starting coin
to see if it is possible to make change. By doing this every time and seeing if we can use a larger coin, and the min coins it takes to
create an index value, we will be building up a solution that will give us the minimum value to make change for n amount.

Example:
coins = [1, 4, 5], amount = 12

Base case index 0:
[0, ... ]

Index 1:
[0, _, ... ]

We try the first coin value (1), it works, we then try the next coin (4), it does not work. Therfore the minimum value is 1.

[0, 1, ...]

Index 2:
[0, 1, _, ... ]

We try the first coin value (1), which gives us a remainder of 1 (2 - 1 = 1). We notice that 1 is in our previously seen index values,
and know already that the minimum amount of coins it takes to construct 1 is 1, so currently it takes a minimum of 2 coins to make index 2.

Finally, we try the next smallest coin, which is 4. This fails because 2 - 4 = -2, so we use the minimum value before which is 2.

Index 3:

[0, 1, 2, _, ...]

We can use the 1 coin to get 3 - 1 = 2.

We have previously found the minimum values it takes to get 2, so we use this value to get a total of 3 coins (1 + 2).

We then check if we can make it ANY BETTER (by checking the next smallest coin in the list). If we can, we do that instead.
    - We try 3 - 4 = -1, so we know that our current minimum is the best minimum amount of coins.

Index 4:

[0, 1, 2, 3, _, ...]

We can use a coin of 1, to get 4 - 1 = 3.

We know we can make 3 in 3 different ways, so we get a total of 4 coins.

We then check if there is a better coin to start off with. THERE IS!

We take the next coin (the value of 4) and use it. 4 - 4 = 0, so we can construct the value at index 4 with just 1 coin.

One final step is to try the next coin, which is 5, and we get 4 - 5 = -1, so we know that our previous minimum was the best minimum.

[0, 1, 2, 3, 1, ...]

Doing this will eventually give us:

[0, 1, 2, 3, 1, 1, 2, 3, 2, 2, 2, 3, 3]
 0  1  2  3  4  5  6  7  8  9  10 11 12

And we return the value at n - 1, which is 3.
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # Top down DP (memoization)
        # # Time: O(Coins * Amount)
        # # Space: O(Amount) <- recursion is starting at amount and trying to get  to 0
        # coins.sort()
        # memo = {0: 0}
        #
        # def min_coins(amt):
        #     # Base memoization: If we have seen index, return amount of coins
        #     if amt in memo:
        #         return memo[amt]
        #     # We use this to represent that it is currently not possible to make the amount
        #     min_val = float("inf")
        #
        #     for coin in coins:
        #         # try the first coin
        #         diff = amt - coin
        #
        #         # if our diff is a negative number, then our coin selected is not valid (it is too big)
        #         if diff < 0:
        #             break
        #
        #         # minimum of itself OR 1 (using a coin) + min_value of the minimum coins it takes to make the difference
        #         min_val = min(min_val, 1 + min_coins(diff))
        #
        #     # min is now the min amount of counts it takes to make amount
        #     memo[amt] = min_val
        #     return min_val
        #
        # result = min_coins(amount)
        #
        # if result < float("inf"):
        #     return result
        # else:
        #     return -1

        # Bottom up (tabulation) approach
        # Time: O(Coins * Amount) -> we have one for loop going over amount, we check each coin for each amount
        # Space: O(Amount)
        coins.sort()
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            curr_min = float("inf")

            for coin in coins:
                diff = i - coin

                if diff < 0:
                    break

                # dp[diff] gives us the minimum coins to make index diff
                curr_min = min(curr_min, dp[diff] + 1)

            dp[i] = curr_min

        if dp[amount] < float("inf"):
            return dp[amount]
        else:
            return -1
