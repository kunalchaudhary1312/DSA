class Solution:
    def compress(self, s):
        n = len(s)

        z = [0] * n
        l = r = 0

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])

            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1

            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]

            if i > 0 and 2 * i <= n and z[i] >= i:
                dp[i] = min(dp[i], 1 + dp[2 * i])

        ans = []
        i = 0

        while i < n:
            if i > 0 and 2 * i <= n and z[i] >= i and 1 + dp[2 * i] == dp[i]:
                ans.append('*')
                i *= 2
            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)
