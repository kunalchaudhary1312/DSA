class Solution:
    def maxProduct(self, arr, k):
        n = len(arr)
        neg_inf = float('-inf')
        pos_inf = float('inf')

        dp_max = [neg_inf] * (k + 1)
        dp_min = [pos_inf] * (k + 1)

        dp_max[0] = 1
        dp_min[0] = 1

        for x in arr:
            for j in range(k, 0, -1):
                if dp_max[j - 1] != neg_inf and dp_min[j - 1] != pos_inf:
                    a = dp_max[j - 1] * x
                    b = dp_min[j - 1] * x

                    dp_max[j] = max(dp_max[j], a, b)
                    dp_min[j] = min(dp_min[j], a, b)

        return dp_max[k]
