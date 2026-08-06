class Solution:
    def countMinOperations(self, arr):
        if max(arr) == 0:
            return 0
        return sum(bin(x).count('1') for x in arr) + len(bin(max(arr))) - 3
