class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break  # Target must be in this row

        if not (top <= bottom):
            return False

        row = (top + bottom) // 2
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
# Time Complexity: O(log(m * n)) where m is the number of rows and n is the number of columns.
# Space Complexity: O(1) since we are using a constant amount of space.     

#the copde above is a solution to search for a target value in a 2D matrix that is sorted in ascending order both row-wise and column-wise.
# It uses binary search to first find the appropriate row and then searches within that row.    
# Example usage:
# matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
# target = 9                