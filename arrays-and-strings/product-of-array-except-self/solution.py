"""
Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the divison operation.

Example:
nums = [1, 2, 3, 4]
returns: [24, 12, 8, 6]


Solution 1: Time: O(n), Space: O(n)
- find the product of the numbers from the left of nums[i]
- find the product of the numbers from the right of nums[i]
- then multiply these two numbers together to get the value of nums[i]

Visualization:
nums = [1, 2, 3, 4]

index 0: result[0] = left_products[0] * right_products[0] = 1 * 24 = 24
index 1: result[1] = left_products[1] * right_products[1] = 1 * 12 = 12
index 2: result[2] = left_products[2] * right_products[2] = 2 * 4 = 8
index 3: result[3] = left_products[3] * right_products[3] = 6 * 1 = 6

returns: [24, 12, 8, 6]

This is a good approach because it does not use division, but it uses O(n) space.

Optimal Solution:
- do 2 passes on our input array nums
- we use result because to store this as it does not count to O(n) time
    - start to end of nums: store prefix in i+1 which is made from the i, i-1 numbers.
        nums = [1, 2, 3, 4]
        prefix = [1 (no prefix, default 1),
                  1 (1*1),
                  2 (2*1),
                  6 (3*2)]

    - end to start of nums: store postfix in i-1
        result so far (prefix) = [1, 1, 2, 6]

        output = [24,   -> postfix is 24 (12*2), multiply this by the number at index (1) = 24
                  12,   -> postfix is 12 (4*3), multiply this by number at index (1) = 12
                  8,    -> postfix is 4 (4*1), multiply this by number at index (2) = 8
                  6     -> no postfix, default 1, multiply this by number at index (6) = 6

- This solution does forward and backward passes on nums and the resulting output, does not need
  to store the pre and post fixes in their own arrays. #optimal

Complexity:
- Time: O(n)
- Space: O(n)
"""

from typing import List

#         n = len(nums)
#         result = [1] * n

#         # Calculate left products and store in result
#         left_product = 1
#         for i in range(n):
#             result[i] = left_product
#             left_product *= nums[i]

#         # Calculate right products and multiply with the corresponding left product in result
#         right_product = 1
#         for i in range(n - 1, -1, -1):
#             result[i] *= right_product
#             right_product *= nums[i]

#         return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        # # storing pre and post fixes
        # n = len(nums)
        #
        # # initialize the left and right multipliers to 1
        # left_product = 1
        # right_product = 1
        #
        # # store left and right cumulative products
        # left_products = [0] * n
        # right_products = [0] * n
        #
        # # populate the left_products array
        # for i in range(n):
        #     left_products[i] = left_product
        #
        #     # update left_product by multiplying it with current element
        #     left_product *= nums[i]
        #
        #     # find index from the end of the array
        #     j = -i - 1
        #
        #     # od the same for right
        #     right_products[j] = right_product
        #     right_product *= nums[j]
        #
        # result = []
        #
        # # loop to calculate product of left and right cumulative products for each index
        # for i in range(n):
        #     # multiply the corresponding values form left_products and right_products
        #     result.append(left_products[i] * right_products[i])
        #
        # return result
