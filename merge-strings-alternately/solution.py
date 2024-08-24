from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize two pointers
        i = 0
        j = 0

        # Initialize the merged string
        merged = ""

        # Iterate through the two words
        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1

        # Append the remaining characters
        if i < len(word1):
            merged += word1[i:]
        elif j < len(word2):
            merged += word2[j:]

        return merged
