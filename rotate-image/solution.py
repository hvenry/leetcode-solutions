from typing import List

# time: O(n^2)
# space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # transpose (flip across diagonal)
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # horizontal reflection
        # swap rows
        for row in range(n):
            # swap only one half of the matrix
            for col in range(n // 2):
                # j is left pointer going right and n - j - 1 is right pointer going left
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]

        # fancy reverse of rows in matrix

        # for i in range(n):
        #     matrix[i] = matrix[i][::-1]
