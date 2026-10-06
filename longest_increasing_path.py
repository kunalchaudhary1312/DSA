import sys
sys.setrecursionlimit(10**6)

class Solution:
    def longIncPath(self, matrix, n, m):
        if not matrix or not matrix[0]:
            return 0

        dp = [[0] * m for _ in range(n)]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]

            max_path = 1
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(ni, nj))

            dp[i][j] = max_path
            return max_path

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))

        return ans
