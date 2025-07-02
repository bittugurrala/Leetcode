class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            matrix.append([0]*n)

        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        c = 1
        while left <= right and top <= bottom:      #my mistake - putting c variable in line 13 that resets everytime the loops runs
            for i in range(left, right+1):
                matrix[top][i] = c
                c = c + 1
            top = top + 1

            for i in range(top, bottom+1): #mandatory check done for edge cases like single row, single col
                matrix[i][right] = c
                c = c + 1
            right = right -1 

            if top <= bottom:  #mandatory check done for edge cases like single row, single col
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = c
                    c = c + 1
                bottom = bottom - 1
            if left <= right : #mandatory check done for edge cases like single row, single col
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = c 
                    c= c + 1
                left = left + 1


        return matrix


"""
the above logic becomes easy if we know the way to traverse the Matrix in spiral, 
just we repalce the existing element in matrix with the path number


"""

            

        