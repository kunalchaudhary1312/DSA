class Solution:
       def longestSubseq(self, arr):
           dp = {}
           max_len = 0

           for x in arr:
               dp[x] = max(dp.get(x - 1, 0), dp.get(x + 1, 0)) + 1
               if dp[x] > max_len:
                   max_len = dp[x]

           return max_len
