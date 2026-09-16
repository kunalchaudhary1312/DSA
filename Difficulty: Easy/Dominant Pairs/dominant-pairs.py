class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr)
        left = sorted(arr[:n//2])
        right = sorted(arr[n//2:])

        count = 0
        j = 0

        for i in range(n//2):
            while j < n//2 and left[i] >= 5 * right[j]:
                j += 1
            count += j

        return count