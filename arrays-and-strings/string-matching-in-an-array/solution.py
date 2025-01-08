"""
Given an array of string words, return all strings in words that is a substring of another word. You can return the
answer in any order.

A substring is a contiguous sequence of characters within a string.

Example:
words = ["mass", "as", "hero", "superhero"]
returns: ["as", "hero"]

- "as" is a substring of "mass", and "hero" is a substring of "superhero".

Brute Force Solution:
- Nested for loop to compare every word to each other (excluding itself)
- If the word is inside the other word, we add the current word to our result

Optimal Solution
- See Knuth-Morris-Pratt Algorithm

Complexity:
- Time: O(n^2 * m * k) -> m is the average length of words in the list, k is the average length of the words being compared
- Space: (n * m)
"""

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if words[i] in words[j]:
                    res.append(words[i])
                    break

        return res
