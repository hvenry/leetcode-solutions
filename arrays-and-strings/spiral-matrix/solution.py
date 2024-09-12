from typing import List

'''
given an n * m matrix, return all of the elements of the matrix in spiral order

i think:

print out first row (0 -> n)
print out last column (1 -> m)

print out last row? (n + 1 -> 0)
print out first column? (m + 1 -> 1)


example:

1, 2, 3,
4, 5, 6,
7, 8, 9

res:

1, 2, 3, 6, 9, 8, 7, 4, 5


solution:
repeat appending top row, right column, bottom row, left column
while adding -1 to each length, creating a spiral output of all
of the items in the matrix.
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        if not matrix or not matrix[0]:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # top row (left to right)
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # right column (top to bottom)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # bottom row (right to left)
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # left column (bottom to top)
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            
        return result
