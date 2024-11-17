"""
Given an integer num, return a string of its base 7 representation.

Example 1:
num = 100
output: "202"

100 is written in base 10, meaning that from left to right is the ones, tens, hundreds column.

We can represent this number as:
100 = (1 * 10^2) + (0 * 10^1) + (0 * 10^0)
    = 100 + 0 + 0
    = 100


Solution:
We convert to base 7 by dividing by 7 until we get to 0.

100 / 7 = 14 % 2 <- remainder of 2
14 / 7 = 2 % 0 <- remainder of 0
2 / 7 = 0 % 2 <- remainder of 2

Notice how the remainders 2, 0, 2 when concatinated together is the value of 100 in base 7.

To prove that 202_{7} in base 7 is 100:
100 = (2 * 7^2) + (0 * 7^1) + (2 * 7^0)
    = (2 * 49) + (0 * 7) + (2 * 1)
    = 98 + 0 + 2
    = 100

Complexity:
- Time: O(log_7 n)
- Space: O(log_7 n)
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        original_num = num
        num = abs(num)

        remainders = []
        while num > 0:
            remainder = num % 7
            remainders.append(str(remainder))
            # integer division
            num = num // 7

        # for negative numbers, we just check if it was negative and if it was append -
        if original_num < 0:
            remainders.append("-")

        remainders.reverse()
        return "".join(remainders)
