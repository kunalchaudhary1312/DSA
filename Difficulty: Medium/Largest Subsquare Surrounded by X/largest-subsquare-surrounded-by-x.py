class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)
        top = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if mat[i][j] == 'X':
                    top[i][j] = top[i-1][j] + 1 if i > 0 else 1
                    left[i][j] = left[i][j-1] + 1 if j > 0 else 1

        max_len = 0

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                side = min(top[i][j], left[i][j])
                while side > max_len:
                    if top[i][j - side + 1] >= side and left[i - side + 1][j] >= side:
                        max_len = side
                    side -= 1

        return max_len