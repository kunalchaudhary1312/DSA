class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        n, m = len(s1), len(s2)
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                temp = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        lcs_len = dp[m]
        return (n - lcs_len) * costS1 + (m - lcs_len) * costS2
      
