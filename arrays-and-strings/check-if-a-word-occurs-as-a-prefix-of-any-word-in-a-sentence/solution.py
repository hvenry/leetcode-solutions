"""
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is
a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a
prefix of more than one word, return the ndex of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

Example:
sentence = "i love eating burger"
searchWord = "burg"
returns: 4

- "burg" is prefix of "burger" which is the 4th word in the sentence.

Solution:
- iterate through each word, checking
- check if the word is the same lenght of searchword
- comepare search word to the start of word to searchword
- return count if true, else keep going

Complexity:
- Time: O(n)
- Space: O(n) -> the split method storing words
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        count = 1

        for word in words:
            if len(word) < len(searchWord):
                pass
            if searchWord == word[: len(searchWord)]:
                return count

            count += 1

        return -1
