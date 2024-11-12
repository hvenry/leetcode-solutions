"""
Given an interger array nums and an interger val, remove all occurrences of val in nums in place (operate directly on the
input data structure). The order of the elements may be change. Then return the number of elements in nums which are not
equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following
things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining
  elements of nums are not important as well as the size of nums.
- Return k.


Example:
nums = [3, 2, 2, 3], val = 3
Output: 2, nums = [2, 2, _, _]

Example 2:
nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
output: 5, nums = [0, 1, 4, 0, 3, _, _, _]
(5 becuase this is the number of elements to keep).

Solution:

Since the order does not matter of the elements that are not removed, we can do an approach that starts with a pointer at i (starting at 0)
and another at n-1.
- if the number at i is the number we need to remove, instead of just removing the number, we set it to be the number at n-1, and then shift n-1
  in by one.
- we do not move i over, because the number at the end of the list could be the one we want to remove
- while i does not equal the targer, we move it to the right of the array.
- when i and n-1 hit the same element, we have finished.


[2, 3, 1, 2, 3, 2, 4]
 i                 n-1

n = 7

set i to what is at n-1

[4, 3, 1, 2, 3, 2, 4]
 i              n-1

We can now move the i all the way over to index 3:

[4, 3, 1, 2, 3, 2, 4]
          i     n-1

We replace this with n-1, it does not change, so we try again after moving n-1 in.


[4, 3, 1, 2, 3, 2, 4]
          i  n-1

Trying again:


[4, 3, 1, 3, 3, 2, 4]
          i
          n-1

Complexity
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            # we are one something we want to remove
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            # we are on something we want to keep
            else:
                i += 1

        return n
