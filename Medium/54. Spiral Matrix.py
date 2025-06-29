class Solution:
    def spiralOrder(self, matrix) :
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        res = []

        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top = top + 1

            for i in range(top, bottom+ 1):
                res.append(matrix[i][right])
            right = right - 1

            if top <= bottom:                       #condt to handle single, odd number of rows and cols
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom = bottom - 1

            if left <= right:                        #condt to handle single, odd number of rows and cols
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left = left + 1

        return res
            
if __name__ == "__main__":
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    sol = Solution()
    print(sol.spiralOrder(matrix))  # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]          
        