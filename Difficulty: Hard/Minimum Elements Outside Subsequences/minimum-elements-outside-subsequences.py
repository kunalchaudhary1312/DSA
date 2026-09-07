class Solution:
    def minCount(self, arr):
        dp = {(0, float('inf')): 0}

        for x in arr:
            new_dp = dp.copy()
            for (inc, dec), count in dp.items():
                if x > inc:
                    s1 = (x, dec)
                    if count + 1 > new_dp.get(s1, -1):
                        new_dp[s1] = count + 1
                if x < dec:
                    s2 = (inc, x)
                    if count + 1 > new_dp.get(s2, -1):
                        new_dp[s2] = count + 1
            dp = new_dp

        return len(arr) - max(dp.values())