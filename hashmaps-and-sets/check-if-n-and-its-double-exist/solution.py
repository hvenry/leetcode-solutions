"""
Given an array arr of integers, check if there exist two indicies i and j such that:
1. i != j
2. 0 <= i, j < arr.length
3. arr[i] == 2 * arr[j]

Example 1:
arr = [10, 2, 5, 3]
returns: True

- For i = 0 and j = 2, arr[i] == 10, arr[j] == 5, 10 == 5 * 2

Example 2:
arr = [3, 1, 7, 11]
returns: False

- There is no i and j that satisfy the conditions.

Solution:
- Use a hashmap to store values as key and index
- Iterate through every index, value in arr, and check if
    - A given value * 2 is in our hashmap -> this is our case 3 from question statement
    - and if hash_map[value] does not store our current index -> this is case 1 from question statement
- Return True if condition is met, false otherwise outside the loop

Complexity:
- Time: O(n) -> iterating through all elements in arr
- Space: O(n) -> storing elements in hashmap
"""

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_map = {value: index for index, value in enumerate(arr)}

        for index, value in enumerate(arr):
            if (value * 2 in hash_map) and (hash_map[value * 2] != index):
                return True

        return False
