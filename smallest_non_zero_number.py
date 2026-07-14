class Solution:
    def find(self, arr):
        x = 0
        for num in reversed(arr):
            x = (x + num + 1) // 2
        return x
