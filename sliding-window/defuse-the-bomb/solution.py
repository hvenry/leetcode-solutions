"""
You have a bomb to defuse, and your time is running out! Your informer will provide you
with a circular array code of length n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced smultaneously.
- if k > 0, replace the ith number the the sum of the next k numbers.
- if k < 0, replace the ith number with the sum of the previous k numbers.
- if k == 0, replace the ith number with 0.

As the code is circular, the next element of coe[n - 1] is code[0], and the previous element of code[0]
is code [n-1].

Given the circular array code and the integer key k, return the decrypted code to defuse the bomb!

Example:
code = [5, 7, 1, 4]
k = 3
returns: [12, 10, 16, 13]

index 0 = 7 + 1 + 4 = 12
index 1 = 1 + 4 + 5 = 10
index 2 = 4 + 5 + 7 = 16
index 3 = 5 + 7 + 1 = 13

Naive Approach:
- iterate through each number
- if k > 0, iterate for j in range i + k, and sum each k lenght array to each res[i].
    - calculate index of circular array by doing [j % n] -> ie index 4 of above array would be 4 % 4 = 0, which is the first index (wrapping around)
- do the same for k < 0, only go backwards

Optimal Solution:
- Use a sliding window of length k
- we use left and right, left starting at 0 and right starting at 0 going to n + k
- this makes time complexity go from O(n * k) to O(n) because you are not re-iterating for each i k times.
- when we fully construct a window of lenght k, we assign the cur_sum to either
    - left - 1 % n -> if we are moving right (k > 0)
    - right + 1 % n -> if we are moving left (k < 0)

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # sliding window approach:
        n = len(code)
        res = [0] * n

        left = 0
        cur_sum = 0

        for right in range(n + abs(k)):
            cur_sum += code[right % n]

            # window too big, shift left pointer over
            if right - left + 1 > abs(k):
                cur_sum -= code[left % n]
                left = (left + 1) % n

            # correct window size, the sum belongs to the previous element
            # if k > 0, window is moving right
            # if k < 0, window is moving left
            if right - left + 1 == abs(k):
                if k > 0:
                    res[(left - 1) % n] = cur_sum
                elif k < 0:
                    res[(right + 1) % n] = cur_sum

        return res

        # # brute force solution
        # n = len(code)
        # res = [0] * n

        # if k == 0:
        #     return res

        # for i in range(n):
        #     if k > 0:
        #         for j in range(i + 1, i + 1 + k):
        #             res[i] += code[j % n]
        #     elif k < 0:
        #         for j in range(i - 1, i - 1 - abs(k), -1):
        #             res[i] += code[j % n]

        # return res
