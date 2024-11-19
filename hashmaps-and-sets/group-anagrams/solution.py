"""
Given an array of strings strs, group the anagrams together. You can return the answer
in any order.

Example::
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
returns: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

- No strings in strs that can be rearranged to "bat".
- "nat" and "tan" can are both anagrams as they can be rearranged to each other.
- "ate", "eat", and "tea" are all anagrams of each other

Solution:
- iterate through each str in strs
- check if each str contains letters that are in a hashmap
    - if they are, add it to that index,
    - if they are not, create a new index
- return all the keys of this hashmap

This is a fine solution, but it is O(m * n log n) -> Not optimal
- m is length of our strs
- n is average length of individual str


Optimal solution:
- count the number of chars per str
- use this count as they key of the hashmap, by doing this we can group all the strings that have the same letter frequencies, and
  thus grouping the anagrams.

Complexity
- Time: O(m * n)
- Space: O(m)
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for char in str:
                # take ascii value (a - a = 0, b - a = 1)
                count[ord(char) - ord("a")] += 1

            # lists can not be keys, so we change it to a tuple
            res[tuple(count)].append(str)

        return list(res.values())
