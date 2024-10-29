"""
Given a string contaning digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letter.

1: _    2: abc  3: def
4: ghi  5: jkl  6: mno
7: pqrs 8: tuv  9: wxyz
        0: _

Example 1:
digits = "23"
returns: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

2: [a, b, c]
3: [d, e, f]

Solution
- create a hashmap
- use an index to look through the given string

'23'

                        [ ]
        [a]             [b]             [c]                 # consider index 0 (2: ['a', 'b', 'c'])
    [ad][ae][af]    [bd][bf][bc]    [cd][ce][cf]            # consider index 1 (3: ['d', 'e', 'f'])


Complexity:

Time: O(4^n) -> we branch off by 3 and at MAX 4 for each depth of n
Space: O(n) -> height of the tree

"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # base case
        if digits == "":
            return []

        # backtracking
        res, sol = [], []

        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        n = len(digits)

        # which digit we are looking at
        def backtrack(i):
            # base case
            if i == n:
                # make a str to append to result from chars in solution
                res.append("".join(sol))
                return

            # use lettermap to go through EACH letter for a given i
            for letter in letter_map[digits[i]]:
                # use the letter
                sol.append(letter)
                # call function to go forward with using the letter
                backtrack(i + 1)
                # undo the decision
                sol.pop()

        backtrack(0)
        return res
