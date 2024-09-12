from typing import List

'''
given an array nums of size n, return the majority element.

the majority element is the element that appears more than [n/2] times
- assume it always exists in a given array

example:
nums = [2, 2, 1, 1, 1, 2, 2]
result: 2

solution:
use a dict as a counter
for each number, if it does not exist, add it to dict, and increment the counter
if the number already exists, just increment the counter.
'''

'''
solution 1:

time O(n)
space O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            # increment counter
            counter[num] += 1
        
        return max(counter)
'''

'''
solution 2:

time O(n)
space O(1)

uses Boyer-Moore Voting algorithm, which finds majority element
by maintaining a candidate and a count of how many times that candidate appears.

steps:
initialize candidate: (store potential majority element), count: (store count of specific candidate)
traverse through list
- if count is 0, set candidate to current number and set count to 1
- if the current number is same as candidate, increment count
- if current number is less than candidate, decrement count
'''    

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
            