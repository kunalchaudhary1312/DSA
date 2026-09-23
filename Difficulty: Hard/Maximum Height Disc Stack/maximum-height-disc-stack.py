class Solution:
    def maxStackHeight(self, r, h):
        discs = sorted(zip(r, h), key=lambda x: (x[0], -x[1]))
        max_h = max(h)
        bit = [0] * (max_h + 2)

        for _, ht in discs:
            idx = ht - 1
            res = 0
            while idx > 0:
                if bit[idx] > res:
                    res = bit[idx]
                idx -= idx & -idx

            val = res + ht
            idx = ht
            while idx < len(bit):
                if val > bit[idx]:
                    bit[idx] = val
                idx += idx & -idx

        ans = 0
        idx = max_h
        while idx > 0:
            if bit[idx] > ans:
                ans = bit[idx]
            idx -= idx & -idx

        return ans