"""
Given a position integer num, return 'true' if 'num' is a perfect square
or 'false' otherwise.

A perfect square is an integer that is the square of an integer. In other
words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

example:
input: num = 16
output: true

input: num = 14
output: false

solution: use binary search (this is better than O(sqrt n) solution)
- do binary search from 1 to n
- check middle squared and see if it is bigger
- if it is, return, True, if less then check right side, if greater check left side
- return True if value is found, False otherwise


"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # # O (sqrt (n))
        # for i in range(1, num + 1):
        #     if i * i == num:
        #         return True
        #     if i * i > nums:
        #         return False

        # O (log n)
        left = 1
        right = num

        while left <= right:
            middle = (left + right) // 2

            # look for smaller numbers,
            if middle * middle > num:
                right = middle - 1
            # look for larger numbers
            elif middle * middle < num:
                left = middle + 1
            else:
                return True
        return False
