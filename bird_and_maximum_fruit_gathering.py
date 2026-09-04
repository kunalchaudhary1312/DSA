class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:
        n = len(arr)
        if m >= n:
            return sum(arr)

        curr_sum = sum(arr[:m])
        max_sum = curr_sum

        for i in range(1, n):
            curr_sum = curr_sum - arr[i - 1] + arr[(i + m - 1) % n]
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
