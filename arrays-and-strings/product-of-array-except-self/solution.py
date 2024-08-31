from typing import List

"""
solution:

find the product of the numbers from the left of nums[i]
and find the product of the numbers from the right of nums[i]

then multiply these two numbers together to get the value of nums[i]

example: [1, 2, 3, 4]
left_products: [1, 1, 2, 6]
right_products: [24, 12, 4, 1]

For index 0: result[0] = left_products[0] * right_products[0] = 1 * 24 = 24
For index 1: result[1] = left_products[1] * right_products[1] = 1 * 12 = 12
For index 2: result[2] = left_products[2] * right_products[2] = 2 * 4 = 8
For index 3: result[3] = left_products[3] * right_products[3] = 6 * 1 = 6

result = [24, 12, 8, 6]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize the left anr right multipliers to 1
        left_product = 1
        right_product = 1

        n = len(nums)

        # store left and right cumulative products
        left_products = [0] * n
        right_products = [0] * n

        # populate the left_products array
        for i in range(n):
            left_products[i] = left_product
            # update left_product by multiplying it with current element
            left_product *= nums[i]

            # find index from the end of the array
            j = -i - 1

            # od the same for right
            right_products[j] = right_product
            right_product *= nums[j]

        result = []

        # loop to calculate product of left and right cumulative products for each index
        for i in range(n):
            # multiply the corresponding values form left_products and right_products
            result.append(left_products[i] * right_products[i])

        return result
