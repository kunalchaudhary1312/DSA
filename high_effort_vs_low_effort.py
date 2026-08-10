class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        n = len(h)
        if n == 0:
            return 0
        if n == 1:
            return max(h[0], l[0])
        
        dp = [0] * n
        dp[0] = max(h[0], l[0])
        dp[1] = max(l[1] + dp[0], h[1])
        
        for i in range(2, n):
            dp[i] = max(l[i] + dp[i-1], h[i] + dp[i-2])
            
        return dp[-1]
