class Solution:
    def zigzagSequence(self, mat):
        n = len(mat)
        if n == 0:
            return 0
        if n == 1:
            return mat[0][0]
            
        dp = [[0] * n for _ in range(n)]
        
        for j in range(n):
            dp[0][j] = mat[0][j]
            
        for i in range(1, n):
            for j in range(n):
                max_prev = 0
                for k in range(n):
                    if k != j:
                        max_prev = max(max_prev, dp[i-1][k])
                dp[i][j] = mat[i][j] + max_prev
                
        return max(dp[n-1])
