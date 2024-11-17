"""
Given a positive integer n, write a function that returns the number of set bits in its binary
representation (also known as the Hamming weight).

Example 1:
n = 11
returns 3

The input binary string 1011, has a total of three set bits.

Example 2:
n = 128
returns 1

The input string 10000000 has a total of one set bit

Naive Approach:
- convert to binary string, count 1's, return amount of 1's
- not optimal, O(n) time complexity

Optimal Solution:
- use & method to remove 1 significant bit every single time by doing n & (n - 1)
- use a count to track every time you do this
- return count

Example:
for n = 11

11 in binary: 1011
10 in binary: 1010 &
              1010 = 10

 9 in binary: 0111
10 in binary: 1010 &
              0010 = 2

 2 in binary: 0010
 1 in binary: 0001 &
              0000 = 0

& was used 3 times to get to 0000, which means that there was previously 3 1's in the binary number.

Complexity
- Time: O(number of 1s)
- Space: O(1)

"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n != 0:
            ans += 1
            n = n & (n - 1)

        return ans
