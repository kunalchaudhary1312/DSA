class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        sizes = [s, m, l]
        costs = [cs, cm, cl]
        
        limit = x + max(sizes)
        dp = [float('inf')] * (limit + 1)
        dp[0] = 0
        
        for i in range(1, limit + 1):
            for j in range(3):
                if i >= sizes[j]:
                    dp[i] = min(dp[i], dp[i - sizes[j]] + costs[j])
        
        return min(dp[x:])
