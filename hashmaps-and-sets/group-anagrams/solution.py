from typing import List
from collections import defaultdict

"""
given an array of strings, strs, group the anagrams together.

return the answer in any order.

input strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

why:
no strings in strs that can be rearranged to "bat"
"nat" and "tan" can are both anagrams as they can be rearranged to each other
"ate", "eat", and "tea" are all anagrams of each other


Solution:
iterate through each str in strs

check if each str contains letters that are in a hashmap

if they are, add it to that index,

if they are not, create a new index

return all the keys of this hashmap


To sort all strings:
nat tan = aet, aet

This is a fine solution, but it is 
O(m * n log n)

where m is length of our strs and n is average length of individual str
NOT EFFICIENT 


Better solution:
count the number of chars per str and use a hashmap

the overall time complexity is O (m * n * 26)

m is strengths
n is average length of str
26 is length of count array.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            # a to 0
            count = [0] * 26

            for char in str:
                # take ascii value (a - a = 0, b - a = 1)
                count[ord(char) - ord("a")] += 1

            # lists can not be keys, so we change it to a tuple
            res[tuple(count)].append(str)

        return res.values()
