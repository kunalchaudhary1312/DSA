class Solution:
    def lexiString(self, s: str) -> str:
        n = len(s)
        s_concat = s + s
        i, j, k = 0, 1, 0

        while i < n and j < n and k < n:
            if s_concat[i + k] == s_concat[j + k]:
                k += 1
            elif s_concat[i + k] > s_concat[j + k]:
                i = i + k + 1
                if i <= j:
                    i = j + 1
                k = 0
            else:
                j = j + k + 1
                if j <= i:
                    j = i + 1
                k = 0

        idx = min(i, j)
        return s_concat[idx:idx + n]
