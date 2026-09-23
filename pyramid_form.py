class Solution:
    def formPyramid(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        l = [0] * n
        r = [0] * n

        l[0] = min(arr[0], 1)
        for i in range(1, n):
            l[i] = min(arr[i], l[i - 1] + 1)

        r[-1] = min(arr[-1], 1)
        for i in range(n - 2, -1, -1):
            r[i] = min(arr[i], r[i + 1] + 1)

        max_h = max(min(a, b) for a, b in zip(l, r))

        return sum(arr) - max_h * max_h
