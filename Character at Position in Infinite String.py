class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        n = len(s)
        lengths = [n]
        step = 0

        while lengths[-1] < pos:
            step += 1
            next_len = 2 * lengths[-1] + step
            lengths.append(next_len)

        for i in range(step, 0, -1):
            prev_len = lengths[i - 1]
            curr_len = lengths[i]
            rev_start = curr_len - prev_len + 1

            if pos >= rev_start:
                pos = curr_len - pos + 1
            elif pos > prev_len:
                return "$"

        return s[pos - 1]
