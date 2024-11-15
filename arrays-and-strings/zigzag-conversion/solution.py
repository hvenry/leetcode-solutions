"""
The string "PAYPALISHIRING" written in zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R


Wirte the coe that will take a string and make this conversion given a number of rows.

Example 1:
s = "PAYPALISHIRING", numRows = 3
returns: "PAHNAPLSIIGYIR"

Example 2:
s = "PAYPALISHIRING, numRows = 4
returns: "PINALSIGYAHRPI"
Explanation:
P     I     N
A   L S   I
Y A   H R
P     I

Solution:
create a matrix with n number of rows (for example, 3):
m = [[], [], []]

keep track of i, which shows what list in the matrix wer are at, and also keep track of d, which is the direction.

start at i=0, move down and place 1 element into matrix rows until there are none lesft, then we swtich d.

now we go backwards, and add elements to the matrix rows

then we print out matrix rows to get our resulting string.

Compmlexity:
- Time: O(R * N) -> string concatination R times we are concatinating N elemnts from the list.
- Space: O(N + R) -> you store R lists, and N elements among them
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        i = 0
        # 1 for down, -1 going back up
        direction = 1

        # num rows number of empty list
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)

            if i == 0:
                direction = 1
            # when we hit bottom, swtich direction to up
            elif i == numRows - 1:
                direction = -1

            # this controls the direction of i (go down then up, repeating for all chars in string)
            i += direction

        ret = ""

        # concatinate row values
        for i in range(numRows):
            ret += "".join(rows[i])

        return ret
