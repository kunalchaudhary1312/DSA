class Solution:
    def findPerimeter(self, mat: list[list[int]]) -> int:
        perimeter = 0
        n, m = len(mat), len(mat[0])

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    perimeter += 4
                    if i > 0 and mat[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and mat[i][j-1] == 1:
                        perimeter -= 2

        return perimeter
