class Solution:
    def palindromicStrings(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        for L in range(1, n + 1):
            m = L // 2
            r = m if L % 2 == 0 else m + 1
            if r > k:
                continue
            ways = 1
            for i in range(r):
                ways = (ways * (k - i)) % MOD
            ans = (ans + ways) % MOD
        return ans
