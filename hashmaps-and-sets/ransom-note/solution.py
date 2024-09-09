from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)

        for char in ransomNote:
            if hashmap[char] > 0:
                hashmap[char] -= 1
            else:
                return False
        return True

        # time O(m + n) -> m is length of ransomNote, n is len magazine
        # space O(n) -> hashmap for n entries of chars in magazine
