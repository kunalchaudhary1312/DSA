class Solution :
    def beautySum ( self , s : str ) -> int :
        res = 0
        n = len(s)
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                max_f = 0
                min_f = float('inf')
                for f in freq:
                    if f > 0:
                        if f > max_f:
                            max_f = f
                        if f < min_f:
                            min_f = f
                res += (max_f - min_f)
        return res
