class Solution:
    def countWays(self, n, sum):
        if sum < 1 or sum > 9 * n:
            return -1
            
        dp = [[-1] * (sum + 1) for _ in range(n + 1)]
        
        def countRec(digits, target):
            if target < 0:
                return 0
            if digits == 0:
                return 1 if target == 0 else 0
                
            if dp[digits][target] != -1:
                return dp[digits][target]
                
            res = 0
            for i in range(10):
                if target - i >= 0:
                    res += countRec(digits - 1, target - i)
                    
            dp[digits][target] = res
            return res
            
        ans = 0
        for i in range(1, 10):
            if sum - i >= 0:
                ans += countRec(n - 1, sum - i)
                
        return ans if ans > 0 else -1