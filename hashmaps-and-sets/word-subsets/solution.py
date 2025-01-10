"""
You are given two strings arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including
multiplicity.

- For example, "wrr" is a subset of "warrior" but is not a subset of "world"

A string a from words1 is universal if for every string b in words2, b is a
subset of a.

Return an array of all the universal strings in words1. You may return the
answer in any order.

Example:
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]

returns: ["facebook", "google", "leetcode"]

Solution:
- Create a hashmap that contains the max count for each letter for all letters
  in words2.
- If any character count from word in words1 is less than the count of the same
  charcter in the hashmap, it cannot be added to res.

Complexity:
- Time: O(n * l + m * l2) -> l_x = lenght of word_x
- Space: O(n * l)
"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)

        # count all the letters in words2 for count_2
        for word in words2:
            count_word = Counter(word)
            for char, count in count_word.items():
                count_2[char] = max(count_2[char], count)

        res = []

        for word in words1:
            count_word = Counter(word)
            flag = True

            # check each count of count_2 to see if word has necessary chars
            for char, count in count_2.items():
                if count_word[char] < count:
                    flag = False
                    break

            if flag:
                res.append(word)

        return res
