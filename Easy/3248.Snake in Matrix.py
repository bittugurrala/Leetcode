class Solution:
    def finalPositionOfSnake(self, n, commands):
        matrix = [[i*n + j for j in range(n)] for i in range(n)]

        i = 0
        j = 0
        for c in commands:
            if c == "DOWN":
                i = i + 1
            elif c == "UP":
                i = i - 1
            elif c == "RIGHT":
                j = j + 1
            else:
                j = j -1 

        return matrix[i][j]
            

            
if __name__ == "__main__":
    n = 4
    commands = ["DOWN", "RIGHT", "DOWN", "LEFT", "UP"]
    solution = Solution()
    print(solution.finalPositionOfSnake(n, commands))  # Output: 5
