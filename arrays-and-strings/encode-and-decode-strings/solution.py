"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is
decoded back to the original list of strings (do not use serialze methods like eval).

Example 1:
dummy_input = ["Hello", "World!"]

returns: ["Hello", "World!"]
Solution:
- Insert the length of the current word infront of the string, then a delimiter beside it to form a combined string.
- Using these two values, we know how long the next string to encode is.


Visualization:
strs = ["Hello", "World!"]
encode(strs)

res = "5#Hello6#World!"

decode(res)
i = 0:
       j
      i
res = 5#Hello6#World!

length = res[i:j] = 5

i = j + 1
j = i + length

             j
        i
res = 5#Hello6#World!
res[i:] = Hello -> this is added to the decoded list

i = j -> moves to the start of the next number.


Complexity
Encode:
- Time: O(n)
- Space: O(1) -> (O(1) since the problem MUST return a string of O(n) space, because we use no auxilary space)

Decode:
- Time: O(n)
- Space: O(1) -> same as above
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Ecode a list of strings to a single string"""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings"""
        res = []
        i = 0

        while i < len(s):
            j = i

            # iterate until we hit a delimiter (this is useful for counter higher than 9)
            while s[j] != "#":
                j += 1

            # we stored our length variable between i and j, in the first run this should evaluate to 0
            length = int(s[i:j])
            # move i to the starting of the next word
            i = j + 1
            # set j to the end of the next word
            j = i + length
            # append the word (i -> j)
            res.append(s[i:j])
            # move i to the end of the word
            i = j

        return res
