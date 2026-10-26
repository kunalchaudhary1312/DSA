class Solution:

    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        if k == n:
            return 0
        pref_max = [0] * n
        pref_min = [0] * n
        suff_max = [0] * n
        suff_min = [0] * n

        pref_max[0] = arr[0]
        pref_min[0] = arr[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], arr[i])
            pref_min[i] = min(pref_min[i - 1], arr[i])

        suff_max[n - 1] = arr[n - 1]
        suff_min[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suff_max[i] = max(suff_max[i + 1], arr[i])
            suff_min[i] = min(suff_min[i + 1], arr[i])

        ans = float("inf")

        for i in range(n - k + 1):
            j = i + k - 1
            cur_max = -float("inf")
            cur_min = float("inf")
            if i > 0:
                cur_max = max(cur_max, pref_max[i - 1])
                cur_min = min(cur_min, pref_min[i - 1])
            if j < n - 1:
                cur_max = max(cur_max, suff_max[j + 1])
                cur_min = min(cur_min, suff_min[j + 1])
            ans = min(ans, cur_max - cur_min)

        return ans
