class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        memo = [0] * n
        for i in range(n):
            if memo[i] != 0:
                continue
            curr = []
            idx = i
            while 0 <= idx < n and memo[idx] == 0:
                memo[idx] = -1
                curr.append(idx)
                idx += arr[idx]

            if 0 <= idx < n and memo[idx] == 1:
                status = 1
            elif idx < 0 or idx >= n:
                status = 1
            else:
                status = -1

            if status == 1:
                for x in curr:
                    memo[x] = 1
            else:
                for x in curr:
                    memo[x] = -1
        return memo.count(1)
