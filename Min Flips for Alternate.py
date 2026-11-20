class Solution:
    def minFlips(self, s):
        flips_start_0 = 0
        flips_start_1 = 0
        for i, ch in enumerate(s):
            exp_0 = '0' if i % 2 == 0 else '1'
            exp_1 = '1' if i % 2 == 0 else '0'
            if ch != exp_0:
                flips_start_0 += 1
            if ch != exp_1:
                flips_start_1 += 1
        return min(flips_start_0, flips_start_1)
