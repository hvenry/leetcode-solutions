"""
given text, use characters of text to form as many instances of the word
"balloon" as possible

you can use characters in text at most once

solution: use a dict (in java a hash map) to store
occurrences of each char in balloon.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {
            "b": 0,
            "a": 0,
            "l": 0,  # needs 2
            "o": 0,  # needs 2
            "n": 0,
        }

        for char in text:
            if char in counter:
                counter[char] += 1

        if any(counter[char] == 0 for char in "balloon"):
            return 0
        else:
            return min(
                counter["b"],
                counter["a"],
                counter["l"] // 2,
                counter["o"] // 2,
                counter["n"],
            )
