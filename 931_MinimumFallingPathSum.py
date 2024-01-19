# 931. Minimum Falling Path Sum
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).



from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        # Iterate through each row starting from the second row
        for i in range(2, rows+1):
            for col in range(cols):
                # Calculate the values of the left, right, and center elements
                left = matrix[rows-i+1][col-1] if col else float('inf')
                right = matrix[rows-i+1][col+1] if col < cols - 1 else float('inf')
                center = matrix[rows-i+1][col]
                
                # Update the current element with the sum of the best next step and the current element
                matrix[rows-i][col] += min(left, center, right)
                # we reused the matrix to save space
        
        # Return the minimum sum from the first row
        return min(matrix[0])
